"""
Hallucination Detector for Nora Search (DeepSearch) QA Evaluation.

Detects claims in generated answers that are not grounded in the provided sources.
This module helps identify when the LLM generates information not present in
the retrieved documents.
"""

import json
import re
from dataclasses import dataclass, field
from typing import Any, Optional

from deepsearch.llm.base import LLMMessage, LLMProvider


# Prompt for extracting claims from an answer
CLAIM_EXTRACTION_PROMPT = """Extrahiere alle faktischen Behauptungen aus dem folgenden Text.
Eine Behauptung ist eine Aussage, die wahr oder falsch sein kann.

## Text
{text}

## Anweisungen
- Extrahiere jede einzelne faktische Behauptung
- Ignoriere Fragen, Meinungen und Aufforderungen
- Jede Behauptung sollte eigenständig verständlich sein
- Fokussiere auf technische Fakten, Zahlen, Namen, Prozesse

## Antwortformat
Antworte NUR mit einem JSON-Array:
```json
["Behauptung 1", "Behauptung 2", "Behauptung 3"]
```"""


# Prompt for verifying a claim against sources
CLAIM_VERIFICATION_PROMPT = """Prüfe, ob die folgende Behauptung durch die gegebenen Quellen belegt ist.

## Behauptung
{claim}

## Quellen
{sources}

## Anweisungen
Bewerte, ob die Behauptung:
- SUPPORTED: Vollständig durch mindestens eine Quelle belegt
- PARTIALLY_SUPPORTED: Teilweise belegt, aber mit Abweichungen
- NOT_SUPPORTED: Nicht in den Quellen enthalten
- CONTRADICTED: Widerspricht den Quellen

## Antwortformat
Antworte NUR mit einem JSON-Objekt:
```json
{{
  "verdict": "SUPPORTED|PARTIALLY_SUPPORTED|NOT_SUPPORTED|CONTRADICTED",
  "evidence": "<Relevanter Text aus Quelle, falls vorhanden>",
  "reasoning": "<Kurze Begründung>"
}}
```"""


# Entity extraction prompt for hallucination detection
ENTITY_EXTRACTION_PROMPT = """Extrahiere alle benannten Entitäten aus dem folgenden Text.

## Text
{text}

## Entitätstypen zu extrahieren
- Produktnamen (z.B. RC-3000, VS-Pro 3.0)
- Projektnummern (z.B. PRJ-2025-018)
- Firmennamen (z.B. AutoTech AG, MediPack Solutions)
- Personennamen
- Dokumentnummern (z.B. AWA-001, 8D-2024-089)
- Normen und Standards (z.B. ISO 12100, IEC 61508)
- Technische Werte (z.B. 150 kg Tragfähigkeit, ±0.02mm Toleranz)
- Datumsangaben

## Antwortformat
Antworte NUR mit einem JSON-Objekt:
```json
{{
  "products": ["..."],
  "projects": ["..."],
  "companies": ["..."],
  "persons": ["..."],
  "documents": ["..."],
  "standards": ["..."],
  "values": ["..."],
  "dates": ["..."]
}}
```"""


@dataclass
class HallucinatedClaim:
    """A claim detected as potentially hallucinated."""

    claim: str
    verdict: str  # NOT_SUPPORTED, CONTRADICTED
    reasoning: str
    evidence: str = ""


@dataclass
class EntityHallucination:
    """An entity that appears fabricated."""

    entity: str
    entity_type: str
    reasoning: str


@dataclass
class HallucinationReport:
    """Full report of hallucination detection."""

    answer: str
    sources: list[str]
    total_claims: int
    supported_claims: int
    partially_supported_claims: int
    unsupported_claims: int
    contradicted_claims: int
    hallucinated_claims: list[HallucinatedClaim]
    entity_hallucinations: list[EntityHallucination]

    @property
    def hallucination_rate(self) -> float:
        """Proportion of claims that are unsupported or contradicted."""
        if self.total_claims == 0:
            return 0.0
        return (self.unsupported_claims + self.contradicted_claims) / self.total_claims

    @property
    def grounding_rate(self) -> float:
        """Proportion of claims that are supported."""
        if self.total_claims == 0:
            return 1.0
        return (self.supported_claims + self.partially_supported_claims) / self.total_claims

    @property
    def has_hallucinations(self) -> bool:
        """Check if any hallucinations were detected."""
        return len(self.hallucinated_claims) > 0 or len(self.entity_hallucinations) > 0


class HallucinationDetector:
    """Detect hallucinations in generated answers."""

    def __init__(
        self,
        llm_provider: LLMProvider,
        temperature: float = 0.0,
    ) -> None:
        """
        Initialize the detector.

        Args:
            llm_provider: LLM provider for analysis.
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

    async def extract_claims(self, text: str) -> list[str]:
        """
        Extract factual claims from text.

        Args:
            text: Text to extract claims from.

        Returns:
            List of claims.
        """
        prompt = CLAIM_EXTRACTION_PROMPT.format(text=text)
        messages = [LLMMessage.user(prompt)]

        response = await self.llm.complete(
            messages=messages,
            temperature=self.temperature,
            max_tokens=2000,
        )

        try:
            claims = self._parse_json_response(response.content)
            return claims if isinstance(claims, list) else []
        except json.JSONDecodeError:
            return []

    async def verify_claim(
        self, claim: str, sources: list[str]
    ) -> tuple[str, str, str]:
        """
        Verify a single claim against sources.

        Args:
            claim: The claim to verify.
            sources: List of source texts.

        Returns:
            Tuple of (verdict, evidence, reasoning).
        """
        sources_text = "\n\n---\n\n".join(
            f"Quelle {i+1}:\n{src}" for i, src in enumerate(sources)
        )

        prompt = CLAIM_VERIFICATION_PROMPT.format(
            claim=claim,
            sources=sources_text,
        )
        messages = [LLMMessage.user(prompt)]

        response = await self.llm.complete(
            messages=messages,
            temperature=self.temperature,
            max_tokens=500,
        )

        try:
            result = self._parse_json_response(response.content)
            return (
                result.get("verdict", "NOT_SUPPORTED"),
                result.get("evidence", ""),
                result.get("reasoning", ""),
            )
        except json.JSONDecodeError:
            return "NOT_SUPPORTED", "", "Failed to parse verification response"

    async def detect_unsupported_claims(
        self, answer: str, sources: list[str]
    ) -> list[HallucinatedClaim]:
        """
        Detect claims in answer not supported by sources.

        Args:
            answer: The generated answer.
            sources: List of source texts.

        Returns:
            List of potentially hallucinated claims.
        """
        # Extract claims
        claims = await self.extract_claims(answer)

        hallucinated = []
        for claim in claims:
            verdict, evidence, reasoning = await self.verify_claim(claim, sources)

            if verdict in ("NOT_SUPPORTED", "CONTRADICTED"):
                hallucinated.append(
                    HallucinatedClaim(
                        claim=claim,
                        verdict=verdict,
                        reasoning=reasoning,
                        evidence=evidence,
                    )
                )

        return hallucinated

    async def extract_entities(self, text: str) -> dict[str, list[str]]:
        """
        Extract named entities from text.

        Args:
            text: Text to extract entities from.

        Returns:
            Dict mapping entity types to lists of entities.
        """
        prompt = ENTITY_EXTRACTION_PROMPT.format(text=text)
        messages = [LLMMessage.user(prompt)]

        response = await self.llm.complete(
            messages=messages,
            temperature=self.temperature,
            max_tokens=1000,
        )

        try:
            entities = self._parse_json_response(response.content)
            return entities if isinstance(entities, dict) else {}
        except json.JSONDecodeError:
            return {}

    async def detect_entity_hallucinations(
        self, answer: str, known_entities: set[str]
    ) -> list[EntityHallucination]:
        """
        Detect fabricated entities not in the knowledge base.

        Args:
            answer: The generated answer.
            known_entities: Set of known entity strings from knowledge base.

        Returns:
            List of potentially hallucinated entities.
        """
        entities = await self.extract_entities(answer)

        hallucinated = []
        for entity_type, entity_list in entities.items():
            for entity in entity_list:
                # Check if entity is known
                # Use fuzzy matching for variations
                entity_lower = entity.lower()
                is_known = any(
                    known.lower() in entity_lower or entity_lower in known.lower()
                    for known in known_entities
                )

                if not is_known:
                    hallucinated.append(
                        EntityHallucination(
                            entity=entity,
                            entity_type=entity_type,
                            reasoning=f"Entity not found in knowledge base",
                        )
                    )

        return hallucinated

    async def full_analysis(
        self,
        answer: str,
        sources: list[str],
        known_entities: Optional[set[str]] = None,
    ) -> HallucinationReport:
        """
        Perform full hallucination analysis.

        Args:
            answer: The generated answer.
            sources: List of source texts.
            known_entities: Optional set of known entities.

        Returns:
            HallucinationReport with full analysis.
        """
        # Extract and verify claims
        claims = await self.extract_claims(answer)

        supported = 0
        partially_supported = 0
        unsupported = 0
        contradicted = 0
        hallucinated_claims = []

        for claim in claims:
            verdict, evidence, reasoning = await self.verify_claim(claim, sources)

            if verdict == "SUPPORTED":
                supported += 1
            elif verdict == "PARTIALLY_SUPPORTED":
                partially_supported += 1
            elif verdict == "NOT_SUPPORTED":
                unsupported += 1
                hallucinated_claims.append(
                    HallucinatedClaim(
                        claim=claim,
                        verdict=verdict,
                        reasoning=reasoning,
                        evidence=evidence,
                    )
                )
            elif verdict == "CONTRADICTED":
                contradicted += 1
                hallucinated_claims.append(
                    HallucinatedClaim(
                        claim=claim,
                        verdict=verdict,
                        reasoning=reasoning,
                        evidence=evidence,
                    )
                )

        # Check entity hallucinations if known entities provided
        entity_hallucinations = []
        if known_entities:
            entity_hallucinations = await self.detect_entity_hallucinations(
                answer, known_entities
            )

        return HallucinationReport(
            answer=answer,
            sources=sources,
            total_claims=len(claims),
            supported_claims=supported,
            partially_supported_claims=partially_supported,
            unsupported_claims=unsupported,
            contradicted_claims=contradicted,
            hallucinated_claims=hallucinated_claims,
            entity_hallucinations=entity_hallucinations,
        )

    def format_report(self, report: HallucinationReport) -> str:
        """
        Format hallucination report as readable text.

        Args:
            report: HallucinationReport to format.

        Returns:
            Formatted string report.
        """
        lines = ["=" * 60]
        lines.append("HALLUCINATION DETECTION REPORT")
        lines.append("=" * 60)
        lines.append("")

        lines.append(f"Total claims analyzed: {report.total_claims}")
        lines.append(f"  - Supported: {report.supported_claims}")
        lines.append(f"  - Partially supported: {report.partially_supported_claims}")
        lines.append(f"  - Unsupported: {report.unsupported_claims}")
        lines.append(f"  - Contradicted: {report.contradicted_claims}")
        lines.append("")

        lines.append(f"Grounding rate: {report.grounding_rate*100:.1f}%")
        lines.append(f"Hallucination rate: {report.hallucination_rate*100:.1f}%")
        lines.append("")

        if report.hallucinated_claims:
            lines.append("Hallucinated Claims:")
            for i, h in enumerate(report.hallucinated_claims, 1):
                lines.append(f"  {i}. [{h.verdict}] {h.claim}")
                lines.append(f"     Reason: {h.reasoning}")
            lines.append("")

        if report.entity_hallucinations:
            lines.append("Potentially Fabricated Entities:")
            for h in report.entity_hallucinations:
                lines.append(f"  - {h.entity} ({h.entity_type})")
            lines.append("")

        lines.append("=" * 60)

        return "\n".join(lines)
