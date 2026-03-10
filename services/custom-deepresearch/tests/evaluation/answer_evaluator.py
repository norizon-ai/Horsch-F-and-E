"""
LLM-as-Judge Answer Evaluator for Nora Search (DeepSearch) QA Evaluation.

This module provides answer quality evaluation using an LLM as judge.
Metrics evaluated:
- Factual accuracy (Faktische Korrektheit)
- Completeness (Vollständigkeit)
- Relevance (Relevanz)
- Source grounding (Quellenverankerung)
- Clarity (Klarheit)
"""

import json
import re
from dataclasses import dataclass, field
from typing import Any, Optional

from deepsearch.llm.base import LLMMessage, LLMProvider, LLMResponse


# German evaluation prompt for TechMech Solutions domain
EVALUATION_PROMPT_DE = """Du bist ein Experte für die Bewertung von RAG-System-Antworten.
Bewerte die folgende Antwort eines Wissenssuchsystems.

## Kontext
Das System durchsucht die interne Wissensdatenbank von TechMech Solutions GmbH,
einem deutschen Automatisierungsunternehmen (Roboterzellen, Fördertechnik, Qualitätsprüfsysteme).

## Frage
{question}

## Systemantwort
{answer}

## Verwendete Quellen
{sources}

## Bewertungskriterien
Bewerte auf einer Skala von 1-5 (1=sehr schlecht, 5=exzellent):

1. **FAKTISCHE_KORREKTHEIT**: Enthält die Antwort nur korrekte Fakten aus den Quellen?
   - 5: Alle Fakten sind korrekt und durch Quellen belegt
   - 3: Einige kleinere Ungenauigkeiten
   - 1: Enthält falsche oder erfundene Informationen

2. **VOLLSTÄNDIGKEIT**: Werden alle relevanten Aspekte der Frage abgedeckt?
   - 5: Alle Aspekte vollständig beantwortet
   - 3: Hauptaspekte beantwortet, einige Details fehlen
   - 1: Frage nur oberflächlich oder gar nicht beantwortet

3. **RELEVANZ**: Beantwortet die Antwort die Frage direkt?
   - 5: Direkt und präzise auf die Frage bezogen
   - 3: Überwiegend relevant, einige Abschweifungen
   - 1: Geht nicht auf die Frage ein

4. **QUELLENVERANKERUNG**: Ist jede Behauptung durch eine Quelle belegt?
   - 5: Alle Behauptungen sind klar den Quellen zugeordnet
   - 3: Die meisten Behauptungen sind belegt
   - 1: Keine oder falsche Quellenangaben

5. **KLARHEIT**: Ist die Antwort klar und professionell formuliert?
   - 5: Sehr klar, gut strukturiert, professionelle Sprache
   - 3: Verständlich, aber könnte besser strukturiert sein
   - 1: Verwirrend oder unprofessionell

## Antwortformat
Antworte NUR mit einem JSON-Objekt in diesem Format:
```json
{{
  "scores": {{
    "faktische_korrektheit": <1-5>,
    "vollständigkeit": <1-5>,
    "relevanz": <1-5>,
    "quellenverankerung": <1-5>,
    "klarheit": <1-5>
  }},
  "reasoning": "<Kurze Begründung der Bewertung auf Deutsch>",
  "hallucinations": ["<Liste von Behauptungen die nicht durch Quellen belegt sind>"],
  "missing_aspects": ["<Liste von fehlenden Aspekten>"],
  "overall_quality": "<sehr_gut|gut|akzeptabel|mangelhaft|ungenügend>"
}}
```"""


# English evaluation prompt as alternative
EVALUATION_PROMPT_EN = """You are an expert evaluator for RAG system answers.
Evaluate the following answer from a knowledge search system.

## Context
The system searches the internal knowledge base of TechMech Solutions GmbH,
a German automation company (robot cells, conveyor systems, quality testing systems).

## Question
{question}

## System Answer
{answer}

## Sources Used
{sources}

## Evaluation Criteria
Rate on a scale of 1-5 (1=very poor, 5=excellent):

1. **FACTUAL_ACCURACY**: Does the answer contain only correct facts from sources?
   - 5: All facts are correct and backed by sources
   - 3: Some minor inaccuracies
   - 1: Contains false or fabricated information

2. **COMPLETENESS**: Are all relevant aspects of the question covered?
   - 5: All aspects fully answered
   - 3: Main aspects covered, some details missing
   - 1: Question only superficially or not answered

3. **RELEVANCE**: Does the answer directly address the question?
   - 5: Directly and precisely related to the question
   - 3: Mostly relevant, some digressions
   - 1: Does not address the question

4. **SOURCE_GROUNDING**: Is every claim backed by a source?
   - 5: All claims are clearly attributed to sources
   - 3: Most claims are backed
   - 1: No or incorrect source attributions

5. **CLARITY**: Is the answer clear and professionally written?
   - 5: Very clear, well-structured, professional language
   - 3: Understandable, but could be better structured
   - 1: Confusing or unprofessional

## Response Format
Respond ONLY with a JSON object in this format:
```json
{{
  "scores": {{
    "factual_accuracy": <1-5>,
    "completeness": <1-5>,
    "relevance": <1-5>,
    "source_grounding": <1-5>,
    "clarity": <1-5>
  }},
  "reasoning": "<Brief justification of the evaluation>",
  "hallucinations": ["<List of claims not backed by sources>"],
  "missing_aspects": ["<List of missing aspects>"],
  "overall_quality": "<excellent|good|acceptable|poor|unacceptable>"
}}
```"""


@dataclass
class EvaluationScores:
    """Scores from the evaluation."""

    factual_accuracy: float
    completeness: float
    relevance: float
    source_grounding: float
    clarity: float

    @property
    def average(self) -> float:
        """Calculate average score."""
        return (
            self.factual_accuracy
            + self.completeness
            + self.relevance
            + self.source_grounding
            + self.clarity
        ) / 5

    @property
    def weighted_average(self) -> float:
        """Calculate weighted average (factual accuracy and source grounding weighted higher)."""
        weights = {
            "factual_accuracy": 0.25,
            "completeness": 0.15,
            "relevance": 0.20,
            "source_grounding": 0.25,
            "clarity": 0.15,
        }
        return (
            self.factual_accuracy * weights["factual_accuracy"]
            + self.completeness * weights["completeness"]
            + self.relevance * weights["relevance"]
            + self.source_grounding * weights["source_grounding"]
            + self.clarity * weights["clarity"]
        )

    def to_dict(self) -> dict[str, float]:
        """Convert to dictionary."""
        return {
            "factual_accuracy": self.factual_accuracy,
            "completeness": self.completeness,
            "relevance": self.relevance,
            "source_grounding": self.source_grounding,
            "clarity": self.clarity,
            "average": self.average,
            "weighted_average": self.weighted_average,
        }


@dataclass
class EvaluationResult:
    """Full evaluation result from LLM-as-judge."""

    question: str
    answer: str
    sources: list[str]
    scores: EvaluationScores
    reasoning: str = ""
    hallucinations: list[str] = field(default_factory=list)
    missing_aspects: list[str] = field(default_factory=list)
    overall_quality: str = ""
    raw_response: Optional[dict] = None

    @property
    def is_acceptable(self) -> bool:
        """Check if answer quality is acceptable (average >= 3)."""
        return self.scores.average >= 3.0

    @property
    def is_good(self) -> bool:
        """Check if answer quality is good (average >= 4)."""
        return self.scores.average >= 4.0

    @property
    def has_hallucinations(self) -> bool:
        """Check if any hallucinations were detected."""
        return len(self.hallucinations) > 0


class AnswerEvaluator:
    """Evaluate answer quality using LLM-as-judge."""

    def __init__(
        self,
        llm_provider: LLMProvider,
        language: str = "de",
        temperature: float = 0.0,
    ) -> None:
        """
        Initialize the evaluator.

        Args:
            llm_provider: LLM provider for evaluation.
            language: Evaluation language ("de" or "en").
            temperature: LLM temperature (0.0 for deterministic).
        """
        self.llm = llm_provider
        self.language = language
        self.temperature = temperature
        self.prompt_template = (
            EVALUATION_PROMPT_DE if language == "de" else EVALUATION_PROMPT_EN
        )

    def _format_sources(self, sources: list[str]) -> str:
        """Format sources list for prompt."""
        if not sources:
            return "Keine Quellen angegeben"
        return "\n".join(f"- {src}" for src in sources)

    def _parse_json_response(self, response_text: str) -> dict[str, Any]:
        """Parse JSON from LLM response, handling markdown code blocks."""
        # Remove markdown code blocks if present
        text = response_text.strip()
        if text.startswith("```"):
            # Find the end of the first line (language specifier)
            first_newline = text.find("\n")
            if first_newline != -1:
                text = text[first_newline + 1 :]
            # Remove trailing ```
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

        # Try to find JSON object
        json_match = re.search(r"\{.*\}", text, re.DOTALL)
        if json_match:
            text = json_match.group()

        return json.loads(text)

    def _normalize_scores(self, raw_scores: dict[str, Any]) -> EvaluationScores:
        """Normalize scores from different response formats."""
        # Handle German key names
        key_mapping = {
            "faktische_korrektheit": "factual_accuracy",
            "vollständigkeit": "completeness",
            "relevanz": "relevance",
            "quellenverankerung": "source_grounding",
            "klarheit": "clarity",
        }

        normalized = {}
        for de_key, en_key in key_mapping.items():
            value = raw_scores.get(de_key) or raw_scores.get(en_key) or 3.0
            normalized[en_key] = float(value)

        return EvaluationScores(**normalized)

    async def evaluate(
        self,
        question: str,
        answer: str,
        sources: list[str],
    ) -> EvaluationResult:
        """
        Evaluate a single answer using LLM-as-judge.

        Args:
            question: The original question.
            answer: The system's answer.
            sources: List of sources used.

        Returns:
            EvaluationResult with scores and analysis.
        """
        prompt = self.prompt_template.format(
            question=question,
            answer=answer,
            sources=self._format_sources(sources),
        )

        messages = [LLMMessage.user(prompt)]

        response = await self.llm.complete(
            messages=messages,
            temperature=self.temperature,
            max_tokens=1500,
        )

        try:
            parsed = self._parse_json_response(response.content)
            scores = self._normalize_scores(parsed.get("scores", {}))

            return EvaluationResult(
                question=question,
                answer=answer,
                sources=sources,
                scores=scores,
                reasoning=parsed.get("reasoning", ""),
                hallucinations=parsed.get("hallucinations", []),
                missing_aspects=parsed.get("missing_aspects", []),
                overall_quality=parsed.get("overall_quality", ""),
                raw_response=parsed,
            )
        except (json.JSONDecodeError, KeyError) as e:
            # Return default scores if parsing fails
            return EvaluationResult(
                question=question,
                answer=answer,
                sources=sources,
                scores=EvaluationScores(
                    factual_accuracy=0,
                    completeness=0,
                    relevance=0,
                    source_grounding=0,
                    clarity=0,
                ),
                reasoning=f"Failed to parse evaluation response: {e}",
                raw_response={"raw_content": response.content, "error": str(e)},
            )

    async def evaluate_batch(
        self,
        evaluations: list[tuple[str, str, list[str]]],
    ) -> list[EvaluationResult]:
        """
        Evaluate a batch of answers.

        Args:
            evaluations: List of (question, answer, sources) tuples.

        Returns:
            List of EvaluationResults.
        """
        results = []
        for question, answer, sources in evaluations:
            result = await self.evaluate(question, answer, sources)
            results.append(result)
        return results

    def aggregate_results(
        self, results: list[EvaluationResult]
    ) -> dict[str, float]:
        """
        Aggregate evaluation results.

        Args:
            results: List of EvaluationResults.

        Returns:
            Dict with aggregated metrics.
        """
        if not results:
            return {}

        n = len(results)

        aggregated = {
            "factual_accuracy": sum(r.scores.factual_accuracy for r in results) / n,
            "completeness": sum(r.scores.completeness for r in results) / n,
            "relevance": sum(r.scores.relevance for r in results) / n,
            "source_grounding": sum(r.scores.source_grounding for r in results) / n,
            "clarity": sum(r.scores.clarity for r in results) / n,
            "average": sum(r.scores.average for r in results) / n,
            "weighted_average": sum(r.scores.weighted_average for r in results) / n,
            "acceptable_rate": sum(1 for r in results if r.is_acceptable) / n,
            "good_rate": sum(1 for r in results if r.is_good) / n,
            "hallucination_rate": sum(1 for r in results if r.has_hallucinations) / n,
            "total_hallucinations": sum(len(r.hallucinations) for r in results),
        }

        return aggregated

    def format_report(
        self,
        results: list[EvaluationResult],
        aggregated: Optional[dict[str, float]] = None,
    ) -> str:
        """
        Format evaluation results as a readable report.

        Args:
            results: List of EvaluationResults.
            aggregated: Pre-computed aggregated metrics (optional).

        Returns:
            Formatted string report.
        """
        if aggregated is None:
            aggregated = self.aggregate_results(results)

        lines = ["=" * 60]
        lines.append("ANSWER QUALITY EVALUATION REPORT")
        lines.append("=" * 60)
        lines.append("")

        lines.append(f"Total evaluations: {len(results)}")
        lines.append("")

        lines.append("Quality Metrics (1-5 scale):")
        lines.append(f"  Factual Accuracy:  {aggregated.get('factual_accuracy', 0):.2f}")
        lines.append(f"  Completeness:      {aggregated.get('completeness', 0):.2f}")
        lines.append(f"  Relevance:         {aggregated.get('relevance', 0):.2f}")
        lines.append(f"  Source Grounding:  {aggregated.get('source_grounding', 0):.2f}")
        lines.append(f"  Clarity:           {aggregated.get('clarity', 0):.2f}")
        lines.append("")

        lines.append("Overall Scores:")
        lines.append(f"  Average Score:     {aggregated.get('average', 0):.2f}")
        lines.append(f"  Weighted Average:  {aggregated.get('weighted_average', 0):.2f}")
        lines.append("")

        lines.append("Quality Rates:")
        lines.append(f"  Acceptable (>=3):  {aggregated.get('acceptable_rate', 0)*100:.1f}%")
        lines.append(f"  Good (>=4):        {aggregated.get('good_rate', 0)*100:.1f}%")
        lines.append(f"  Hallucination:     {aggregated.get('hallucination_rate', 0)*100:.1f}%")
        lines.append(f"  Total Hallucinations: {int(aggregated.get('total_hallucinations', 0))}")
        lines.append("")

        lines.append("=" * 60)

        return "\n".join(lines)
