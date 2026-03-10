"""
Stopword removal preprocessor.

Removes common words that don't contribute to search relevance.

Uses the shared stopwords from deepsearch.utils.stopwords for consistency
across all modules.
"""

from typing import Any, Dict, List, Optional, Set

from .base import Preprocessor

# Re-export from shared module for backward compatibility
from deepsearch.utils.stopwords import (
    load_stopwords,
    ENGLISH_STOPWORDS,
    GERMAN_STOPWORDS,
)


class StopwordRemover(Preprocessor):
    """
    Remove stopwords from query.

    Preserves word order and handles punctuation gracefully.
    Returns original query if all words would be removed.
    """

    def __init__(
        self,
        languages: Optional[List[str]] = None,
        preserve_quoted: bool = True,
        min_word_length: int = 1,
        custom_stopwords: Optional[Set[str]] = None,
    ):
        """
        Initialize stopword remover.

        Args:
            languages: List of languages to load stopwords for
            preserve_quoted: Preserve words in quotes
            min_word_length: Minimum word length to keep
            custom_stopwords: Additional stopwords to remove
        """
        self._languages = languages or ["english", "german"]
        self._preserve_quoted = preserve_quoted
        self._min_word_length = min_word_length

        self._stopwords = load_stopwords(self._languages)
        if custom_stopwords:
            self._stopwords.update(custom_stopwords)

    @property
    def name(self) -> str:
        langs = "_".join(sorted(self._languages))
        return f"stopwords_{langs}"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "languages": self._languages,
            "preserve_quoted": self._preserve_quoted,
            "min_word_length": self._min_word_length,
            "stopword_count": len(self._stopwords),
        }

    def process(self, query: str) -> str:
        """Remove stopwords from query."""
        if not query or not query.strip():
            return query

        # Handle quoted phrases
        if self._preserve_quoted and '"' in query:
            return self._process_with_quotes(query)

        words = query.lower().split()
        filtered = [
            w for w in words
            if w not in self._stopwords and len(w) >= self._min_word_length
        ]

        # Never return empty query
        if not filtered:
            return query

        return " ".join(filtered)

    def _process_with_quotes(self, query: str) -> str:
        """Process query while preserving quoted phrases."""
        import re

        # Extract quoted phrases
        quoted = re.findall(r'"([^"]*)"', query)

        # Remove quoted phrases temporarily
        temp = re.sub(r'"[^"]*"', ' __QUOTED__ ', query)

        # Process non-quoted parts
        words = temp.lower().split()
        filtered = []
        quoted_idx = 0

        for w in words:
            if w == "__quoted__":
                if quoted_idx < len(quoted):
                    filtered.append(f'"{quoted[quoted_idx]}"')
                    quoted_idx += 1
            elif w not in self._stopwords and len(w) >= self._min_word_length:
                filtered.append(w)

        if not filtered:
            return query

        return " ".join(filtered)
