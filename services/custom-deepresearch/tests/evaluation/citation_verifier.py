"""
Citation Verifier for Nora Search (DeepSearch) QA Evaluation.

Verifies that inline citations in generated answers correctly reference
and accurately represent the source content.
"""

import json
import re
from dataclasses import dataclass, field
from typing import Any, Optional

from deepsearch.llm.base import LLMMessage, LLMProvider


# Prompt for extracting citations from an answer
CITATION_EXTRACTION_PROMPT = """Extrahiere alle Zitate und Quellenverweise aus dem folgenden Text.

## Text
{text}

## Anweisungen
Suche nach:
- Explizite Quellenangaben in Klammern (z.B. "(Quelle: XYZ)", "[1]")
- Verweise auf Dokumente (z.B. "laut AWA-001", "gemäß ISO 12100")
- Verweise auf Seiten oder Artikel (z.B. "im Artikel X", "auf Seite Y")
- Implizite Verweise (z.B. "Das Handbuch beschreibt...")

Für jeden Fund extrahiere:
- Den zitierten Text (was behauptet wird)
- Die angegebene Quelle (worauf verwiesen wird)

## Antwortformat
Antworte NUR mit einem JSON-Array:
```json
[
  {{"cited_text": "...", "source_reference": "..."}},
  ...
]
```"""


# Prompt for verifying a citation
CITATION_VERIFICATION_PROMPT = """Prüfe, ob das folgende Zitat die angegebene Quelle korrekt wiedergibt.

## Zitat im Text
"{cited_text}"

## Angegebene Quelle
{source_reference}

## Tatsächlicher Quellinhalt
{source_content}

## Anweisungen
Bewerte:
- CORRECT: Zitat gibt die Quelle korrekt und vollständig wieder
- MOSTLY_CORRECT: Inhaltlich korrekt, aber leicht vereinfacht oder paraphrasiert
- PARTIALLY_CORRECT: Teilweise korrekt, aber wichtige Details fehlen oder sind ungenau
- INCORRECT: Falsche oder irreführende Darstellung der Quelle
- SOURCE_NOT_FOUND: Die angegebene Quelle wurde nicht gefunden

## Antwortformat
Antworte NUR mit einem JSON-Objekt:
```json
{{
  "verdict": "CORRECT|MOSTLY_CORRECT|PARTIALLY_CORRECT|INCORRECT|SOURCE_NOT_FOUND",
  "accuracy_score": <0.0-1.0>,
  "issues": ["<Probleme falls vorhanden>"],
  "reasoning": "<Kurze Begründung>"
}}
```"""


# Prompt for finding missing citations
MISSING_CITATION_PROMPT = """Analysiere den folgenden Text und identifiziere Aussagen, die eine Quellenangabe benötigen, aber keine haben.

## Text
{text}

## Verfügbare Quellen
{sources}

## Anweisungen
Eine Quellenangabe ist erforderlich für:
- Spezifische Fakten und Zahlen
- Technische Spezifikationen
- Verfahrensanweisungen
- Behauptungen die nicht allgemein bekannt sind

Ignoriere:
- Allgemeinwissen
- Logische Schlussfolgerungen
- Einleitungen und Überleitungen

## Antwortformat
Antworte NUR mit einem JSON-Array:
```json
[
  {{"uncited_statement": "...", "suggested_source": "...", "importance": "high|medium|low"}}
]
```"""


@dataclass
class Citation:
    """A citation extracted from the answer."""

    cited_text: str
    source_reference: str


@dataclass
class CitationVerification:
    """Result of verifying a single citation."""

    citation: Citation
    verdict: str
    accuracy_score: float
    issues: list[str] = field(default_factory=list)
    reasoning: str = ""


@dataclass
class MissingCitation:
    """A statement that should be cited but isn't."""

    statement: str
    suggested_source: str
    importance: str  # high, medium, low


@dataclass
class CitationReport:
    """Full citation verification report."""

    answer: str
    sources: list[str]
    total_citations: int
    correct_citations: int
    mostly_correct_citations: int
    partially_correct_citations: int
    incorrect_citations: int
    source_not_found: int
    verifications: list[CitationVerification]
    missing_citations: list[MissingCitation]

    @property
    def citation_accuracy(self) -> float:
        """Average accuracy of all citations."""
        if not self.verifications:
            return 1.0
        return sum(v.accuracy_score for v in self.verifications) / len(self.verifications)

    @property
    def correct_rate(self) -> float:
        """Proportion of citations that are correct or mostly correct."""
        if self.total_citations == 0:
            return 1.0
        return (self.correct_citations + self.mostly_correct_citations) / self.total_citations

    @property
    def has_issues(self) -> bool:
        """Check if there are citation issues."""
        return (
            self.incorrect_citations > 0
            or self.source_not_found > 0
            or len(self.missing_citations) > 0
        )


class CitationVerifier:
    """Verify citation accuracy in generated answers."""

    def __init__(
        self,
        llm_provider: LLMProvider,
        temperature: float = 0.0,
    ) -> None:
        """
        Initialize the verifier.

        Args:
            llm_provider: LLM provider for verification.
            temperature: LLM temperature (0.0 for deterministic).
        """
        self.llm = llm_provider
        self.temperature = temperature

    def _parse_json_response(self, response_text: str) -> Any:
        """Parse JSON from LLM response."""
        text = response_text.strip()
        if text.startswith("```"):
            first_newline = text.find("\n")
            if first_newline != -1:
                text = text[first_newline + 1 :]
            if text.endswith("```"):
                text = text[:-3]
            text = text.strip()

        json_match = re.search(r"[\[\{].*[\]\}]", text, re.DOTALL)
        if json_match:
            text = json_match.group()

        return json.loads(text)

    async def extract_citations(self, answer: str) -> list[Citation]:
        """
        Extract citations from answer text.

        Args:
            answer: The answer text to analyze.

        Returns:
            List of extracted citations.
        """
        prompt = CITATION_EXTRACTION_PROMPT.format(text=answer)
        messages = [LLMMessage.user(prompt)]

        response = await self.llm.complete(
            messages=messages,
            temperature=self.temperature,
            max_tokens=2000,
        )

        try:
            citations_data = self._parse_json_response(response.content)
            return [
                Citation(
                    cited_text=c.get("cited_text", ""),
                    source_reference=c.get("source_reference", ""),
                )
                for c in citations_data
                if isinstance(c, dict)
            ]
        except json.JSONDecodeError:
            return []

    def _find_source_content(
        self, source_reference: str, sources: list[dict]
    ) -> Optional[str]:
        """
        Find the content of a referenced source.

        Args:
            source_reference: Reference to look up (e.g., page title).
            sources: List of source dicts with title and content.

        Returns:
            Source content if found, None otherwise.
        """
        ref_lower = source_reference.lower()
        for source in sources:
            title = source.get("title", "").lower()
            # Match if reference contains title or title contains reference
            if ref_lower in title or title in ref_lower:
                return source.get("content", "")
        return None

    async def verify_citation(
        self,
        citation: Citation,
        sources: list[dict],
    ) -> CitationVerification:
        """
        Verify a single citation against sources.

        Args:
            citation: The citation to verify.
            sources: List of source dicts with title and content.

        Returns:
            CitationVerification result.
        """
        # Find the source content
        source_content = self._find_source_content(citation.source_reference, sources)

        if source_content is None:
            return CitationVerification(
                citation=citation,
                verdict="SOURCE_NOT_FOUND",
                accuracy_score=0.0,
                issues=["Referenced source not found in provided sources"],
                reasoning="Could not locate the cited source",
            )

        # Verify the citation
        prompt = CITATION_VERIFICATION_PROMPT.format(
            cited_text=citation.cited_text,
            source_reference=citation.source_reference,
            source_content=source_content[:3000],  # Limit source length
        )
        messages = [LLMMessage.user(prompt)]

        response = await self.llm.complete(
            messages=messages,
            temperature=self.temperature,
            max_tokens=500,
        )

        try:
            result = self._parse_json_response(response.content)
            return CitationVerification(
                citation=citation,
                verdict=result.get("verdict", "INCORRECT"),
                accuracy_score=float(result.get("accuracy_score", 0.0)),
                issues=result.get("issues", []),
                reasoning=result.get("reasoning", ""),
            )
        except json.JSONDecodeError:
            return CitationVerification(
                citation=citation,
                verdict="INCORRECT",
                accuracy_score=0.0,
                issues=["Failed to parse verification response"],
                reasoning="",
            )

    async def find_missing_citations(
        self, answer: str, sources: list[dict]
    ) -> list[MissingCitation]:
        """
        Find statements that should be cited but aren't.

        Args:
            answer: The answer text.
            sources: List of source dicts.

        Returns:
            List of missing citations.
        """
        sources_summary = "\n".join(
            f"- {s.get('title', 'Unknown')}" for s in sources[:20]
        )

        prompt = MISSING_CITATION_PROMPT.format(
            text=answer,
            sources=sources_summary,
        )
        messages = [LLMMessage.user(prompt)]

        response = await self.llm.complete(
            messages=messages,
            temperature=self.temperature,
            max_tokens=1500,
        )

        try:
            missing_data = self._parse_json_response(response.content)
            return [
                MissingCitation(
                    statement=m.get("uncited_statement", ""),
                    suggested_source=m.get("suggested_source", ""),
                    importance=m.get("importance", "medium"),
                )
                for m in missing_data
                if isinstance(m, dict)
            ]
        except json.JSONDecodeError:
            return []

    async def verify_all_citations(
        self,
        answer: str,
        sources: list[dict],
    ) -> CitationReport:
        """
        Perform full citation verification.

        Args:
            answer: The answer text.
            sources: List of source dicts with title and content.

        Returns:
            CitationReport with full analysis.
        """
        # Extract citations
        citations = await self.extract_citations(answer)

        # Verify each citation
        verifications = []
        correct = 0
        mostly_correct = 0
        partially_correct = 0
        incorrect = 0
        not_found = 0

        for citation in citations:
            verification = await self.verify_citation(citation, sources)
            verifications.append(verification)

            if verification.verdict == "CORRECT":
                correct += 1
            elif verification.verdict == "MOSTLY_CORRECT":
                mostly_correct += 1
            elif verification.verdict == "PARTIALLY_CORRECT":
                partially_correct += 1
            elif verification.verdict == "INCORRECT":
                incorrect += 1
            elif verification.verdict == "SOURCE_NOT_FOUND":
                not_found += 1

        # Find missing citations
        missing = await self.find_missing_citations(answer, sources)

        return CitationReport(
            answer=answer,
            sources=[s.get("title", "") for s in sources],
            total_citations=len(citations),
            correct_citations=correct,
            mostly_correct_citations=mostly_correct,
            partially_correct_citations=partially_correct,
            incorrect_citations=incorrect,
            source_not_found=not_found,
            verifications=verifications,
            missing_citations=missing,
        )

    def format_report(self, report: CitationReport) -> str:
        """
        Format citation report as readable text.

        Args:
            report: CitationReport to format.

        Returns:
            Formatted string report.
        """
        lines = ["=" * 60]
        lines.append("CITATION VERIFICATION REPORT")
        lines.append("=" * 60)
        lines.append("")

        lines.append(f"Total citations found: {report.total_citations}")
        lines.append(f"  - Correct: {report.correct_citations}")
        lines.append(f"  - Mostly correct: {report.mostly_correct_citations}")
        lines.append(f"  - Partially correct: {report.partially_correct_citations}")
        lines.append(f"  - Incorrect: {report.incorrect_citations}")
        lines.append(f"  - Source not found: {report.source_not_found}")
        lines.append("")

        lines.append(f"Citation accuracy: {report.citation_accuracy*100:.1f}%")
        lines.append(f"Correct rate: {report.correct_rate*100:.1f}%")
        lines.append("")

        if report.incorrect_citations > 0 or report.source_not_found > 0:
            lines.append("Citation Issues:")
            for v in report.verifications:
                if v.verdict in ("INCORRECT", "SOURCE_NOT_FOUND"):
                    lines.append(f"  - [{v.verdict}] '{v.citation.cited_text[:50]}...'")
                    lines.append(f"    Source: {v.citation.source_reference}")
                    if v.issues:
                        lines.append(f"    Issues: {', '.join(v.issues)}")
            lines.append("")

        if report.missing_citations:
            lines.append(f"Missing Citations ({len(report.missing_citations)}):")
            for m in report.missing_citations:
                if m.importance == "high":
                    lines.append(f"  [HIGH] '{m.statement[:60]}...'")
                    lines.append(f"         Suggested: {m.suggested_source}")
            lines.append("")

        lines.append("=" * 60)

        return "\n".join(lines)
