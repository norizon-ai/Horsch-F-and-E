"""
Query Reformulator Processor

Reformulates queries for better search results by extracting key terms
and optimizing query structure for the search backend.

Supports multiple languages including English and German.
All prompts are configurable via the PromptManager.
"""

import re
from typing import List, Optional, Set, TYPE_CHECKING

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger
from deepsearch.utils.stopwords import load_stopwords
from .base import BaseProcessor

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

logger = get_logger(__name__)


def get_stopwords(languages: List[str] = None) -> Set[str]:
    """
    Get stopwords for specified languages.

    Uses the shared stopwords from deepsearch.utils.stopwords.

    Args:
        languages: List of language codes (e.g., ["english", "german"])
                   Defaults to ["english", "german"]

    Returns:
        Set of stopwords
    """
    return load_stopwords(languages)


class QueryReformulatorConfig:
    """Configuration for QueryReformulator."""

    def __init__(
        self,
        max_terms: int = 10,
        min_term_length: int = 2,
        use_llm: bool = False,
        languages: Optional[List[str]] = None,
        custom_stopwords: Optional[Set[str]] = None,
        prompt_name: str = "reformulate_query",
    ):
        self.max_terms = max_terms
        self.min_term_length = min_term_length
        self.use_llm = use_llm
        self.languages = languages or ["english", "german"]
        self.custom_stopwords = custom_stopwords or set()
        self.prompt_name = prompt_name


class QueryReformulator(BaseProcessor):
    """
    Reformulates queries for better search results.

    Supports multiple languages (default: English and German).
    Can use either simple term extraction or LLM-based reformulation.
    All prompts are loaded from the PromptManager for configurability.
    """

    def __init__(
        self,
        config: Optional[QueryReformulatorConfig] = None,
        llm: Optional["LLMProvider"] = None,
        prompts: Optional["PromptManager"] = None,
    ):
        """
        Initialize the reformulator.

        Args:
            config: Configuration object (or uses defaults)
            llm: LLM provider for advanced reformulation (optional)
            prompts: PromptManager for loading prompts (required if use_llm=True)
        """
        self.config = config or QueryReformulatorConfig()
        self.llm = llm
        self.prompts = prompts

        # Validate: if use_llm, we need both llm and prompts
        if self.config.use_llm and (not llm or not prompts):
            logger.warning(
                "llm_reformulation_disabled",
                reason="LLM or PromptManager not provided, falling back to simple reformulation",
            )
            self.config.use_llm = False

        # Load stopwords
        self.stop_words = get_stopwords(self.config.languages)
        if self.config.custom_stopwords:
            self.stop_words.update(self.config.custom_stopwords)

        logger.info(
            "query_reformulator_init",
            languages=self.config.languages,
            stopword_count=len(self.stop_words),
            use_llm=self.config.use_llm,
        )

    async def pre_process(
        self,
        query: str,
        context: Optional[dict] = None,
    ) -> str:
        """
        Reformulate the query for better search results.

        Args:
            query: Original query
            context: Optional context (may contain "index_type" hint)

        Returns:
            Reformulated query
        """
        if not query or not query.strip():
            return query

        if self.config.use_llm:
            return await self._llm_reformulate(query, context)
        else:
            return self._simple_reformulate(query)

    def _simple_reformulate(self, query: str) -> str:
        """
        Simple term extraction reformulation.

        Extracts key terms, removes stop words, and limits term count.
        Works with both English and German text.
        """
        # Extract words (including German umlauts and special chars)
        words = re.findall(
            r"\b[\w\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc-]+\b", query.lower()
        )

        # Filter
        filtered = [
            word
            for word in words
            if (
                word not in self.stop_words
                and len(word) >= self.config.min_term_length
                and not word.isdigit()
            )
        ]

        # Deduplicate while preserving order
        seen = set()
        unique = []
        for word in filtered:
            if word not in seen:
                seen.add(word)
                unique.append(word)

        # Limit terms
        terms = unique[: self.config.max_terms]

        if not terms:
            return query

        reformulated = " ".join(terms)

        logger.debug(
            "query_reformulated_simple",
            original=query[:100],
            reformulated=reformulated,
            original_word_count=len(words),
            term_count=len(terms),
        )

        return reformulated

    async def _llm_reformulate(
        self,
        query: str,
        context: Optional[dict] = None,
    ) -> str:
        """
        LLM-based query reformulation using configurable prompts.
        """
        from deepsearch.llm import LLMMessage

        try:
            # Load prompt from PromptManager
            prompt = self.prompts.get_prompt(
                "query_reformulator",
                self.config.prompt_name,
                query=query,
                max_terms=self.config.max_terms,
            )

            response = await self.llm.complete(
                messages=[LLMMessage.user(prompt)],
                temperature=0.0,
                max_tokens=100,
            )

            reformulated = response.content.strip()

            # Validate
            if reformulated and len(reformulated) < len(query) * 3:
                logger.debug(
                    "query_reformulated_llm",
                    original=query[:100],
                    reformulated=reformulated,
                )
                return reformulated

        except Exception as e:
            logger.warning("llm_reformulation_failed", error=str(e))

        # Fallback to simple reformulation
        return self._simple_reformulate(query)


class SimpleTermExtractor(BaseProcessor):
    """
    Simple processor that just extracts key terms without LLM.

    Lightweight alternative to full QueryReformulator.
    """

    def __init__(
        self,
        max_terms: int = 8,
        languages: Optional[List[str]] = None,
    ):
        self.max_terms = max_terms
        self.stop_words = get_stopwords(languages or ["english", "german"])

    async def pre_process(
        self,
        query: str,
        context: Optional[dict] = None,
    ) -> str:
        """Extract key terms from query."""
        words = re.findall(
            r"\b[\w\u00e4\u00f6\u00fc\u00df\u00c4\u00d6\u00dc]{3,}\b", query.lower()
        )
        unique = list(dict.fromkeys(words))
        filtered = [w for w in unique if w not in self.stop_words]
        return " ".join(filtered[: self.max_terms]) or query
