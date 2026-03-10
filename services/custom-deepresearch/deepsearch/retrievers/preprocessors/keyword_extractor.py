"""
Keyword extraction preprocessor.

Extracts key terms from queries for focused search.
"""

import re
from typing import Any, Dict, List, Optional, Set

from .base import Preprocessor
from .stopwords import load_stopwords


class KeywordExtractor(Preprocessor):
    """
    Extract key terms from query.

    Focuses on nouns, technical terms, and important words
    while filtering out common words and filler.
    """

    def __init__(
        self,
        max_terms: int = 8,
        min_term_length: int = 3,
        preserve_patterns: Optional[List[str]] = None,
        languages: Optional[List[str]] = None,
        preserve_numbers: bool = True,
        preserve_quoted: bool = True,
    ):
        """
        Initialize keyword extractor.

        Args:
            max_terms: Maximum keywords to extract
            min_term_length: Minimum word length to consider
            preserve_patterns: Regex patterns to always preserve (e.g., product codes)
            languages: Languages for stopword filtering
            preserve_numbers: Keep numeric terms
            preserve_quoted: Preserve quoted phrases
        """
        self._max_terms = max_terms
        self._min_length = min_term_length
        self._patterns = preserve_patterns or []
        self._preserve_numbers = preserve_numbers
        self._preserve_quoted = preserve_quoted
        self._stopwords = load_stopwords(languages or ["english", "german"])

    @property
    def name(self) -> str:
        return f"keywords_{self._max_terms}"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "max_terms": self._max_terms,
            "min_term_length": self._min_length,
            "patterns": self._patterns,
            "preserve_numbers": self._preserve_numbers,
            "preserve_quoted": self._preserve_quoted,
        }

    def process(self, query: str) -> str:
        """Extract keywords from query."""
        if not query or not query.strip():
            return query

        preserved: List[str] = []
        working_query = query

        # 1. Extract and preserve quoted phrases
        if self._preserve_quoted:
            quoted = re.findall(r'"([^"]+)"', query)
            preserved.extend(f'"{q}"' for q in quoted)
            working_query = re.sub(r'"[^"]+"', ' ', working_query)

        # 2. Extract and preserve pattern matches (e.g., product codes)
        for pattern in self._patterns:
            try:
                matches = re.findall(pattern, working_query, re.IGNORECASE)
                preserved.extend(matches)
                working_query = re.sub(pattern, ' ', working_query, flags=re.IGNORECASE)
            except re.error:
                continue

        # 3. Extract words
        words = re.findall(r'\b[\w-]+\b', working_query.lower())

        # 4. Filter words
        filtered: List[str] = []
        seen: Set[str] = set()

        for word in words:
            # Skip if already seen
            if word in seen:
                continue

            # Skip stopwords
            if word in self._stopwords:
                continue

            # Skip too-short words
            if len(word) < self._min_length:
                continue

            # Handle numbers
            if word.isdigit():
                if self._preserve_numbers:
                    filtered.append(word)
                    seen.add(word)
                continue

            # Keep the word
            filtered.append(word)
            seen.add(word)

        # 5. Combine preserved + filtered, limit count
        # Preserved items come first
        result = list(dict.fromkeys(preserved + filtered))  # Dedupe while preserving order
        result = result[:self._max_terms]

        # Never return empty
        if not result:
            return query

        return " ".join(result)


class TechnicalTermExtractor(KeywordExtractor):
    """
    Keyword extractor optimized for technical documentation.

    Includes patterns for common technical identifiers like:
    - Product codes (RC-3000, CNC-X500)
    - Version numbers (v2.1, 3.0.1)
    - Error codes (ERR-404, E1001)
    - Model numbers (MX-2000, T-800)
    """

    DEFAULT_PATTERNS = [
        r'\b[A-Z]{2,4}-?\d{3,5}\b',        # Product codes: RC-3000, CNC500
        r'\b[A-Z]\d{3,4}\b',                # Short codes: E1001, M200
        r'\bv?\d+\.\d+(?:\.\d+)?\b',        # Versions: v2.1, 3.0.1
        r'\b[A-Z]{2,}[_-][A-Z0-9]+\b',      # Tech identifiers: API_KEY, MAX_VALUE
        r'\b\d{6,}\b',                       # Long numbers (order IDs, etc.)
    ]

    def __init__(
        self,
        max_terms: int = 8,
        min_term_length: int = 3,
        additional_patterns: Optional[List[str]] = None,
        languages: Optional[List[str]] = None,
    ):
        """
        Initialize technical term extractor.

        Args:
            max_terms: Maximum keywords to extract
            min_term_length: Minimum word length
            additional_patterns: Additional regex patterns to preserve
            languages: Languages for stopword filtering
        """
        patterns = self.DEFAULT_PATTERNS.copy()
        if additional_patterns:
            patterns.extend(additional_patterns)

        super().__init__(
            max_terms=max_terms,
            min_term_length=min_term_length,
            preserve_patterns=patterns,
            languages=languages,
            preserve_numbers=True,
            preserve_quoted=True,
        )

    @property
    def name(self) -> str:
        return f"tech_keywords_{self._max_terms}"


class QueryFocuser(Preprocessor):
    """
    Focus query on most important terms using simple heuristics.

    Unlike KeywordExtractor, this preserves word order and
    tries to identify the core question/intent.
    """

    # Question words that should be removed
    QUESTION_WORDS = {
        "what", "how", "why", "when", "where", "who", "which",
        "was", "wie", "warum", "wann", "wo", "wer", "welche",
    }

    # Filler phrases to remove
    FILLER_PHRASES = [
        r'\bhow (?:do|can|to)\b',
        r'\bwhat (?:is|are|does)\b',
        r'\bcan you\b',
        r'\bi want to\b',
        r'\bi need to\b',
        r'\bplease\b',
        r'\bhelp me\b',
        r'\btell me\b',
        r'\bwie kann ich\b',
        r'\bwas ist\b',
        r'\bkannst du\b',
    ]

    def __init__(
        self,
        remove_question_words: bool = True,
        remove_filler: bool = True,
        max_words: int = 10,
    ):
        """
        Initialize query focuser.

        Args:
            remove_question_words: Remove question words
            remove_filler: Remove filler phrases
            max_words: Maximum words to keep
        """
        self._remove_question_words = remove_question_words
        self._remove_filler = remove_filler
        self._max_words = max_words

    @property
    def name(self) -> str:
        return f"focus_{self._max_words}"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "remove_question_words": self._remove_question_words,
            "remove_filler": self._remove_filler,
            "max_words": self._max_words,
        }

    def process(self, query: str) -> str:
        """Focus query on core terms."""
        if not query or not query.strip():
            return query

        result = query.lower().strip()

        # Remove filler phrases
        if self._remove_filler:
            for pattern in self.FILLER_PHRASES:
                result = re.sub(pattern, ' ', result, flags=re.IGNORECASE)

        # Clean up whitespace
        result = ' '.join(result.split())

        # Remove leading question words
        if self._remove_question_words:
            words = result.split()
            while words and words[0] in self.QUESTION_WORDS:
                words = words[1:]
            result = ' '.join(words)

        # Limit word count
        words = result.split()
        if len(words) > self._max_words:
            result = ' '.join(words[:self._max_words])

        # Never return empty
        if not result.strip():
            return query

        return result.strip()
