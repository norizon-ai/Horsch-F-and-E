"""
Assumption Checker Processor

Extracts and validates user assumptions from queries.
Models are co-located with the processor for separation of concerns.
All prompts are loaded from external YAML files.
"""

from enum import Enum
from typing import List, Optional, TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger
from .base import BaseProcessor

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

logger = get_logger(__name__)


# --------------------------------------------------------------------------- #
# Models
# --------------------------------------------------------------------------- #


class AssumptionValidation(str, Enum):
    """Assumption validation status."""

    VALID = "valid"
    INVALID = "invalid"
    UNKNOWN = "unknown"


class UserAssumption(BaseModel):
    """
    A user assumption extracted from their query.

    Assumptions are implicit beliefs in user queries that may or may not be correct.
    """

    assumption: str = Field(..., description="The assumption text")
    validation_status: AssumptionValidation = Field(
        default=AssumptionValidation.UNKNOWN, description="Validation result"
    )
    evidence: Optional[str] = Field(
        default=None, description="Evidence supporting the validation"
    )
    confidence: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Confidence in the validation"
    )
    source_reference: Optional[str] = Field(
        default=None, description="Reference to source that provided evidence"
    )

    model_config = ConfigDict(frozen=True)

    @property
    def is_valid(self) -> bool:
        """Whether this assumption is validated as correct."""
        return self.validation_status == AssumptionValidation.VALID


class AssumptionCheckResult(BaseModel):
    """Result of checking assumptions in a query."""

    query: str = Field(..., description="Original query")
    assumptions: List[UserAssumption] = Field(
        default_factory=list, description="Extracted and validated assumptions"
    )

    @property
    def num_valid(self) -> int:
        """Number of valid assumptions."""
        return sum(
            1
            for a in self.assumptions
            if a.validation_status == AssumptionValidation.VALID
        )

    @property
    def num_invalid(self) -> int:
        """Number of invalid assumptions."""
        return sum(
            1
            for a in self.assumptions
            if a.validation_status == AssumptionValidation.INVALID
        )

    @property
    def num_unknown(self) -> int:
        """Number of unknown assumptions."""
        return sum(
            1
            for a in self.assumptions
            if a.validation_status == AssumptionValidation.UNKNOWN
        )

    @property
    def has_invalid_assumptions(self) -> bool:
        """Whether any assumptions were found to be invalid."""
        return self.num_invalid > 0


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #


class AssumptionCheckerConfig(BaseModel):
    """Configuration for AssumptionChecker."""

    max_assumptions: int = Field(
        default=5, description="Maximum number of assumptions to extract"
    )
    validate_assumptions: bool = Field(
        default=True, description="Whether to validate extracted assumptions"
    )
    extract_prompt_name: str = Field(
        default="extract_assumptions", description="Prompt name for extraction"
    )
    validate_prompt_name: str = Field(
        default="validate_assumption", description="Prompt name for validation"
    )

    model_config = ConfigDict(frozen=True)


# --------------------------------------------------------------------------- #
# Processor
# --------------------------------------------------------------------------- #


class AssumptionChecker(BaseProcessor):
    """
    Extracts and validates user assumptions from queries.

    This processor can:
    1. Extract implicit assumptions from user queries
    2. Validate those assumptions against search results

    All prompts are loaded from external YAML files via PromptManager.
    """

    def __init__(
        self,
        llm: "LLMProvider",
        prompts: "PromptManager",
        config: Optional[AssumptionCheckerConfig] = None,
    ):
        """
        Initialize the assumption checker.

        Args:
            llm: LLM provider for extraction and validation.
            prompts: Prompt manager for loading prompt templates.
            config: Optional configuration overrides.
        """
        self.llm = llm
        self.prompts = prompts
        self.config = config or AssumptionCheckerConfig()

        logger.info(
            "assumption_checker_init",
            max_assumptions=self.config.max_assumptions,
            validate=self.config.validate_assumptions,
        )

    async def post_process(
        self,
        results: List[SearchResult],
        original_query: str,
        context: Optional[dict] = None,
    ) -> List[SearchResult]:
        """
        Post-process results by checking assumptions.

        Extracts assumptions from the original query and validates them
        against the search results. The check result is stored in the
        context dictionary.

        Args:
            results: Search results to use for validation.
            original_query: The original user query.
            context: Context dict where results will be stored.

        Returns:
            The original results (unmodified).
        """
        if context is None:
            context = {}

        assumption_result = await self.check_assumptions(
            original_query, results
        )

        context["assumption_check_result"] = assumption_result

        logger.info(
            "assumptions_checked",
            total=len(assumption_result.assumptions),
            valid=assumption_result.num_valid,
            invalid=assumption_result.num_invalid,
            unknown=assumption_result.num_unknown,
        )

        return results

    async def check_assumptions(
        self,
        query: str,
        sources: Optional[List[SearchResult]] = None,
    ) -> AssumptionCheckResult:
        """
        Extract and optionally validate assumptions from a query.

        Args:
            query: The user query to analyze.
            sources: Optional search results for validation.

        Returns:
            AssumptionCheckResult with extracted (and possibly validated)
            assumptions.
        """
        assumptions = await self._extract_assumptions(query)

        if self.config.validate_assumptions and sources:
            assumptions = await self._validate_assumptions(assumptions, sources)

        return AssumptionCheckResult(query=query, assumptions=assumptions)

    async def _extract_assumptions(
        self, query: str
    ) -> List[UserAssumption]:
        """Extract assumptions from a query using the LLM."""
        from deepsearch.llm import LLMMessage

        try:
            prompt = self.prompts.get_prompt(
                "assumption_checker",
                self.config.extract_prompt_name,
                query=query,
                max_assumptions=self.config.max_assumptions,
            )

            response = await self.llm.complete(
                messages=[LLMMessage.user(prompt)],
                temperature=0.2,
                max_tokens=500,
            )

            assumptions = self._parse_assumptions(response.content)

            logger.debug(
                "assumptions_extracted",
                query=query[:100],
                count=len(assumptions),
            )

            return assumptions

        except Exception as e:
            logger.error("assumption_extraction_failed", error=str(e))
            return []

    def _parse_assumptions(self, text: str) -> List[UserAssumption]:
        """Parse assumption text into UserAssumption objects."""
        assumptions = []

        if not text or "NONE" in text.upper():
            return assumptions

        import re

        lines = re.findall(r"(?:^|\n)\s*(?:-|\d+\.?)\s*(.+)", text)

        for line in lines:
            line = line.strip()
            if not line or not len(line) > 5:
                continue
            assumptions.append(
                UserAssumption(
                    assumption=line,
                    validation_status=AssumptionValidation.UNKNOWN,
                )
            )

        return assumptions[: self.config.max_assumptions]

    async def _validate_assumptions(
        self,
        assumptions: List[UserAssumption],
        sources: List[SearchResult],
    ) -> List[UserAssumption]:
        """Validate assumptions against search results."""
        from deepsearch.llm import LLMMessage

        validated = []

        sources_text = "\n\n".join(
            f"[{i + 1}] {s.title}\n{s.content[:500]}"
            for i, s in enumerate(sources[:5])
        )

        for assumption in assumptions:
            try:
                prompt = self.prompts.get_prompt(
                    "assumption_checker",
                    self.config.validate_prompt_name,
                    assumption=assumption.assumption,
                    sources=sources_text,
                )

                response = await self.llm.complete(
                    messages=[LLMMessage.user(prompt)],
                    temperature=0.1,
                    max_tokens=200,
                )

                status, evidence, confidence = self._parse_validation(
                    response.content
                )

                validated.append(
                    UserAssumption(
                        assumption=assumption.assumption,
                        validation_status=status,
                        evidence=evidence,
                        confidence=confidence,
                    )
                )

            except Exception as e:
                logger.warning(
                    "assumption_validation_failed",
                    assumption=assumption.assumption[:50],
                    error=str(e),
                )
                validated.append(assumption)

        return validated

    def _parse_validation(
        self, text: str
    ) -> tuple[AssumptionValidation, Optional[str], float]:
        """Parse validation response into status, evidence, and confidence."""
        text_upper = text.upper()

        # Determine status
        if "VALID" in text_upper and "INVALID" not in text_upper:
            status = AssumptionValidation.VALID
            confidence = 0.8
        elif "INVALID" in text_upper or "FALSE" in text_upper:
            status = AssumptionValidation.INVALID
            confidence = 0.8
        else:
            status = AssumptionValidation.UNKNOWN
            confidence = 0.5

        # Extract evidence
        evidence = None
        for keyword in ("EVIDENCE:", "REASON:", "EXPLANATION:"):
            if keyword in text.upper():
                idx = text.upper().find(keyword)
                evidence = text[idx + len(keyword) :].strip()
                break

        if not evidence and len(text) > 20:
            evidence = text.strip()

        return status, evidence, confidence
