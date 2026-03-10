"""
Rigorous LLM-as-Judge Evaluator for Nora Search (DeepSearch).

This evaluator implements a user-centric evaluation framework based on 2024-2025
LLM-as-judge best practices:

Key Features:
1. Hard fail conditions (language match, direct resolution)
2. 3-point scale (FAIL/PARTIAL/PASS) instead of 1-5
3. User-centric dimensions focusing on actionability
4. Low temperature (0.1) for consistency

Dimensions:
- language_match (binary, hard fail): Answer language matches query language
- direct_resolution (binary, hard fail): Contains actual info, not just references
- factual_grounding (3-point): Claims supported by retrieved context
- answer_completeness (3-point): All aspects of question addressed
- user_actionability (binary): User can proceed with their task

Usage:
    from deepsearch.llm import create_llm_provider
    from tests.evaluation import RigorousEvaluator

    # Create LLM provider for judge (gpt-4o-mini recommended for cost)
    judge_llm = create_llm_provider(
        provider_type="openai",
        base_url="https://api.openai.com/v1",
        api_key="sk-...",
        model="gpt-4o-mini",
    )

    evaluator = RigorousEvaluator(judge_llm)
    report = await evaluator.evaluate(
        question_id="PS-001",
        question="Was sind die Lastberechnungen für die RC-5000?",
        answer="...",
        context="...",
    )

    print(f"Overall pass: {report.overall_pass}")
    print(f"Overall score: {report.overall_score}")
"""

import asyncio
import json
import re
import time
from dataclasses import dataclass, asdict, field
from enum import Enum
from typing import Any, Optional

from deepsearch.llm.base import LLMMessage, LLMProvider, LLMResponse


# =============================================================================
# DATA STRUCTURES
# =============================================================================


class Verdict(Enum):
    """3-point verdict scale aligned with user perception."""
    PASS = "pass"
    PARTIAL = "partial"
    FAIL = "fail"

    @property
    def score(self) -> float:
        """Numeric score for the verdict."""
        return {"pass": 1.0, "partial": 0.5, "fail": 0.0}[self.value]


@dataclass
class DimensionResult:
    """Result for a single evaluation dimension."""
    dimension: str
    verdict: Verdict
    score: float
    reasoning: str
    evidence: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "dimension": self.dimension,
            "verdict": self.verdict.value,
            "score": self.score,
            "reasoning": self.reasoning,
            "evidence": self.evidence,
        }


@dataclass
class RigorousEvaluationReport:
    """Complete evaluation report with all dimensions."""
    question_id: str
    overall_pass: bool
    overall_score: float
    failure_reasons: list[str]
    dimensions: dict[str, DimensionResult]
    latency_ms: float

    def to_dict(self) -> dict[str, Any]:
        return {
            "question_id": self.question_id,
            "overall_pass": self.overall_pass,
            "overall_score": self.overall_score,
            "failure_reasons": self.failure_reasons,
            "dimensions": {k: v.to_dict() for k, v in self.dimensions.items()},
            "latency_ms": self.latency_ms,
        }


# =============================================================================
# EVALUATION PROMPTS (German)
# =============================================================================

JUDGE_PROMPTS = {
    "language_match": """Bewerte, ob die Antwortsprache zur Fragesprache passt.

FRAGE:
{question}

ANTWORT:
{answer}

BEWERTUNG:
- Erkenne die Sprache der Frage
- Erkenne die Sprache der Antwort
- Technische Fachbegriffe oder Code in anderer Sprache sind akzeptabel
- Englische Überschriften in einer deutschen Antwort sind NICHT akzeptabel

Antworte NUR mit diesem JSON:
{{"fragesprache": "...", "antwortsprache": "...", "reasoning": "...", "verdict": "pass" oder "fail"}}""",

    "direct_resolution": """Bewerte, ob die Antwort die Frage DIREKT beantwortet oder nur auf Quellen verweist.

KRITISCHE UNTERSCHEIDUNG:
- DIREKTE ANTWORT = Enthält die angeforderte Information (Zahlen, Fakten, Schritte)
- KEINE DIREKTE ANTWORT = Sagt "siehe Dokument X" / "konnte nicht abgerufen werden" / "Sie sollten Y konsultieren" / "leider keine Information verfügbar"

FRAGE:
{question}

ANTWORT:
{answer}

Eine gute Antwort ENTHÄLT die substantielle Information.
Eine schlechte Antwort VERWEIST nur darauf, wo die Information sein könnte.

Antworte NUR mit diesem JSON:
{{"user_braucht": "...", "antwort_enthaelt_info": true/false, "reasoning": "...", "verdict": "pass" oder "fail"}}""",

    "factual_grounding": """Bewerte, ob die Antwort auf dem abgerufenen Kontext basiert (Faithfulness).

KONTEXT:
{context}

ANTWORT:
{answer}

BEWERTUNG:
- pass: Alle Behauptungen werden vom Kontext gestützt
- partial: Die meisten Behauptungen werden gestützt, einige sind generisch oder extrapoliert
- fail: Antwort enthält halluzinierte Information, widerspricht dem Kontext, oder ignoriert den Kontext komplett

Antworte NUR mit diesem JSON:
{{"behauptungen": ["..."], "gestuetzt": ["..."], "nicht_gestuetzt": ["..."], "reasoning": "...", "verdict": "pass", "partial" oder "fail"}}""",

    "answer_completeness": """Bewerte, ob die Antwort alle Aspekte der Frage vollständig adressiert.

FRAGE:
{question}

ANTWORT:
{answer}

BEWERTUNG:
- pass: Alle Aspekte der Frage werden mit ausreichender Tiefe adressiert
- partial: Hauptfrage beantwortet, aber einige Teilaspekte fehlen
- fail: Wesentliche Teile der Frage werden nicht adressiert

Antworte NUR mit diesem JSON:
{{"informationsbedarfe": ["..."], "adressiert": ["..."], "fehlend": ["..."], "reasoning": "...", "verdict": "pass", "partial" oder "fail"}}""",

    "user_actionability": """Bewerte, ob der Nutzer basierend auf dieser Antwort handeln kann.

FRAGE:
{question}

ANTWORT:
{answer}

BEWERTUNG:
- pass: Antwort liefert handlungsrelevante Information - Nutzer kann mit seiner Aufgabe fortfahren
- fail: Nutzer bleibt ohne klaren Weg vorwärts - müsste woanders suchen

Antworte NUR mit diesem JSON:
{{"nutzer_kann_fortfahren": true/false, "was_nutzer_tun_kann": "...", "was_noch_fehlt": "...", "reasoning": "...", "verdict": "pass" oder "fail"}}""",
}


# =============================================================================
# RIGOROUS EVALUATOR
# =============================================================================


class RigorousEvaluator:
    """
    Rigorous LLM-as-Judge evaluator for answer quality.

    Uses hard fail conditions and user-centric dimensions to provide
    realistic quality assessment that correlates with user satisfaction.
    """

    def __init__(
        self,
        llm_provider: LLMProvider,
        temperature: float = 0.1,
    ) -> None:
        """
        Initialize the rigorous evaluator.

        Args:
            llm_provider: LLM provider for evaluation (recommend gpt-4o-mini).
            temperature: Sampling temperature (0.1 for consistency).
        """
        self.llm = llm_provider
        self.temperature = temperature

        # Hard requirements - any fail = overall fail
        self.hard_requirements = ["language_match", "direct_resolution"]

        # Weighted dimensions for composite score
        self.dimension_weights = {
            "factual_grounding": 0.35,
            "answer_completeness": 0.35,
            "user_actionability": 0.30,
        }

    def _parse_json_response(self, response_text: str) -> dict[str, Any]:
        """Parse JSON from LLM response, handling markdown code blocks."""
        text = response_text.strip()

        # Remove markdown code blocks if present
        if "```json" in text:
            text = text.split("```json")[1].split("```")[0]
        elif "```" in text:
            parts = text.split("```")
            if len(parts) >= 2:
                text = parts[1]

        # Try to find JSON object
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            text = json_match.group()

        return json.loads(text.strip())

    async def evaluate_dimension(
        self,
        dimension: str,
        question: str,
        answer: str,
        context: Optional[str] = None,
    ) -> DimensionResult:
        """
        Evaluate a single dimension using LLM judge.

        Args:
            dimension: Dimension name (e.g., "language_match").
            question: The user's question.
            answer: The system's answer.
            context: Retrieved context (for factual_grounding).

        Returns:
            DimensionResult with verdict, score, and reasoning.
        """
        prompt_template = JUDGE_PROMPTS[dimension]
        prompt = prompt_template.format(
            question=question,
            answer=answer,
            context=context or "Kein Kontext verfügbar",
        )

        try:
            messages = [LLMMessage.user(prompt)]

            response = await self.llm.complete(
                messages=messages,
                temperature=self.temperature,
                max_tokens=1000,
            )

            result = self._parse_json_response(response.content)

            verdict_str = result.get("verdict", "fail").lower()
            verdict = Verdict(verdict_str)

            # Extract evidence (everything except reasoning and verdict)
            evidence_data = {
                k: v for k, v in result.items()
                if k not in ["reasoning", "verdict"]
            }

            return DimensionResult(
                dimension=dimension,
                verdict=verdict,
                score=verdict.score,
                reasoning=result.get("reasoning", ""),
                evidence=json.dumps(evidence_data, ensure_ascii=False) if evidence_data else None,
            )

        except Exception as e:
            # On error, fail conservatively
            return DimensionResult(
                dimension=dimension,
                verdict=Verdict.FAIL,
                score=0.0,
                reasoning=f"Evaluation error: {str(e)}",
                evidence=None,
            )

    async def evaluate(
        self,
        question_id: str,
        question: str,
        answer: str,
        context: str,
        expected_sources: Optional[list[str]] = None,
    ) -> RigorousEvaluationReport:
        """
        Run complete evaluation across all dimensions.

        Args:
            question_id: Unique identifier for the question.
            question: The user's question.
            answer: The system's answer.
            context: Retrieved context used for the answer.
            expected_sources: Optional list of expected source documents.

        Returns:
            RigorousEvaluationReport with:
            - overall_pass: True if all hard requirements pass AND composite >= 0.7
            - overall_score: Weighted composite of quality dimensions
            - failure_reasons: List of why evaluation failed
            - dimensions: Detailed results per dimension
        """
        start_time = time.time()

        dimensions_to_evaluate = list(self.hard_requirements) + list(self.dimension_weights.keys())

        # Evaluate all dimensions concurrently
        tasks = [
            self.evaluate_dimension(dim, question, answer, context)
            for dim in dimensions_to_evaluate
        ]

        results = await asyncio.gather(*tasks)
        dimension_results = {r.dimension: r for r in results}

        # Check hard requirements
        failure_reasons = []
        hard_fail = False

        for dim in self.hard_requirements:
            if dimension_results[dim].verdict == Verdict.FAIL:
                hard_fail = True
                failure_reasons.append(
                    f"HARD FAIL [{dim}]: {dimension_results[dim].reasoning}"
                )

        # Calculate weighted composite score
        if hard_fail:
            overall_score = 0.0
        else:
            weighted_sum = 0.0
            total_weight = 0.0

            for dim, weight in self.dimension_weights.items():
                if dim in dimension_results:
                    weighted_sum += dimension_results[dim].score * weight
                    total_weight += weight

            overall_score = weighted_sum / total_weight if total_weight > 0 else 0.0

        # Determine overall pass
        overall_pass = not hard_fail and overall_score >= 0.7

        if not hard_fail and overall_score < 0.7:
            failure_reasons.append(
                f"Composite score {overall_score:.2f} below threshold 0.7"
            )

        latency_ms = (time.time() - start_time) * 1000

        return RigorousEvaluationReport(
            question_id=question_id,
            overall_pass=overall_pass,
            overall_score=round(overall_score, 3),
            failure_reasons=failure_reasons,
            dimensions=dimension_results,
            latency_ms=round(latency_ms, 2),
        )

    async def evaluate_batch(
        self,
        test_cases: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """
        Evaluate a batch of test cases and compute aggregate metrics.

        Args:
            test_cases: List of dicts with keys:
                - question_id: str
                - question: str
                - answer: str
                - context: str (optional)
                - expected_sources: list[str] (optional)

        Returns:
            Aggregate metrics including pass rate and per-dimension stats.
        """
        results = []
        for case in test_cases:
            result = await self.evaluate(
                question_id=case["question_id"],
                question=case["question"],
                answer=case["answer"],
                context=case.get("context", ""),
                expected_sources=case.get("expected_sources"),
            )
            results.append(result)

        # Compute aggregate metrics
        total = len(results)
        passed = sum(1 for r in results if r.overall_pass)

        # Per-dimension aggregates
        dimension_stats = {}
        for dim in list(JUDGE_PROMPTS.keys()):
            scores = [
                r.dimensions[dim].score
                for r in results
                if dim in r.dimensions
            ]
            if scores:
                dimension_stats[dim] = {
                    "mean": round(sum(scores) / len(scores), 3),
                    "pass_rate": round(
                        sum(1 for s in scores if s >= 0.5) / len(scores), 3
                    ),
                }

        return {
            "total_cases": total,
            "passed": passed,
            "pass_rate": round(passed / total, 3) if total > 0 else 0,
            "mean_score": round(
                sum(r.overall_score for r in results) / total, 3
            ) if total > 0 else 0,
            "dimension_stats": dimension_stats,
            "detailed_results": [r.to_dict() for r in results],
        }

    def format_report(
        self,
        results: list[RigorousEvaluationReport],
        aggregated: Optional[dict[str, Any]] = None,
    ) -> str:
        """
        Format evaluation results as a readable report.

        Args:
            results: List of evaluation reports.
            aggregated: Pre-computed aggregated metrics (optional).

        Returns:
            Formatted string report.
        """
        if aggregated is None:
            aggregated = {
                "total_cases": len(results),
                "passed": sum(1 for r in results if r.overall_pass),
                "pass_rate": sum(1 for r in results if r.overall_pass) / len(results) if results else 0,
                "mean_score": sum(r.overall_score for r in results) / len(results) if results else 0,
            }

        lines = ["=" * 70]
        lines.append("RIGOROUS ANSWER QUALITY EVALUATION REPORT")
        lines.append("=" * 70)
        lines.append("")

        lines.append(f"Total evaluations: {aggregated['total_cases']}")
        lines.append(f"Passed: {aggregated['passed']} ({aggregated['pass_rate']*100:.1f}%)")
        lines.append(f"Mean score: {aggregated['mean_score']:.3f}")
        lines.append("")

        lines.append("-" * 70)
        lines.append("HARD REQUIREMENTS (must pass):")
        lines.append("-" * 70)
        for dim in self.hard_requirements:
            if "dimension_stats" in aggregated and dim in aggregated["dimension_stats"]:
                stats = aggregated["dimension_stats"][dim]
                lines.append(f"  {dim}: {stats['pass_rate']*100:.1f}% pass rate")
        lines.append("")

        lines.append("-" * 70)
        lines.append("QUALITY DIMENSIONS (weighted):")
        lines.append("-" * 70)
        for dim, weight in self.dimension_weights.items():
            if "dimension_stats" in aggregated and dim in aggregated["dimension_stats"]:
                stats = aggregated["dimension_stats"][dim]
                lines.append(
                    f"  {dim} ({int(weight*100)}%): "
                    f"mean={stats['mean']:.2f}, pass_rate={stats['pass_rate']*100:.1f}%"
                )
        lines.append("")

        # Show failure breakdown
        if results:
            hard_fails = {dim: 0 for dim in self.hard_requirements}
            for r in results:
                for dim in self.hard_requirements:
                    if dim in r.dimensions and r.dimensions[dim].verdict == Verdict.FAIL:
                        hard_fails[dim] += 1

            if any(v > 0 for v in hard_fails.values()):
                lines.append("-" * 70)
                lines.append("HARD FAILURE BREAKDOWN:")
                lines.append("-" * 70)
                for dim, count in hard_fails.items():
                    if count > 0:
                        lines.append(f"  {dim}: {count} failures ({count/len(results)*100:.1f}%)")
                lines.append("")

        lines.append("=" * 70)

        return "\n".join(lines)
