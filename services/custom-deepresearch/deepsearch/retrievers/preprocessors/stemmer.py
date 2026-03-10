"""
Stemming preprocessor.

Reduces words to their root form for better matching.
"""

from typing import Any, Dict, Optional

from deepsearch.observability import get_logger
from .base import Preprocessor

logger = get_logger(__name__)


class Stemmer(Preprocessor):
    """
    Apply stemming to query terms.

    Uses NLTK's Snowball stemmer which supports multiple languages
    including English and German.
    """

    # Supported languages by NLTK Snowball stemmer
    SUPPORTED_LANGUAGES = {
        "english", "en",
        "german", "de", "deutsch",
        "french", "fr",
        "spanish", "es",
        "italian", "it",
        "dutch", "nl",
        "portuguese", "pt",
        "swedish", "sv",
        "norwegian", "no",
        "danish", "da",
        "finnish", "fi",
        "russian", "ru",
    }

    # Language code mapping to NLTK language names
    LANGUAGE_MAP = {
        "en": "english",
        "de": "german",
        "deutsch": "german",
        "fr": "french",
        "es": "spanish",
        "it": "italian",
        "nl": "dutch",
        "pt": "portuguese",
        "sv": "swedish",
        "no": "norwegian",
        "da": "danish",
        "fi": "finnish",
        "ru": "russian",
    }

    def __init__(
        self,
        language: str = "english",
        preserve_case: bool = False,
        min_word_length: int = 3,
    ):
        """
        Initialize stemmer.

        Args:
            language: Language for stemming (e.g., "english", "german", "de")
            preserve_case: Preserve original case (default: lowercase)
            min_word_length: Minimum word length to stem (shorter words pass through)
        """
        # Normalize language name
        self._language = self.LANGUAGE_MAP.get(language.lower(), language.lower())
        self._preserve_case = preserve_case
        self._min_word_length = min_word_length
        self._stemmer = None  # Lazy-loaded

    @property
    def name(self) -> str:
        return f"stem_{self._language}"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "language": self._language,
            "preserve_case": self._preserve_case,
            "min_word_length": self._min_word_length,
        }

    def _get_stemmer(self):
        """Lazy-load NLTK stemmer."""
        if self._stemmer is None:
            try:
                from nltk.stem import SnowballStemmer
                self._stemmer = SnowballStemmer(self._language)
            except ImportError:
                logger.warning(
                    "nltk_not_installed",
                    message="Install with: pip install nltk",
                )
            except ValueError as e:
                logger.warning(
                    "stemmer_language_not_supported",
                    language=self._language,
                    error=str(e),
                )
        return self._stemmer

    def process(self, query: str) -> str:
        """Apply stemming to query terms."""
        if not query or not query.strip():
            return query

        stemmer = self._get_stemmer()
        if stemmer is None:
            return query

        words = query.split()
        stemmed = []

        for word in words:
            # Preserve short words
            if len(word) < self._min_word_length:
                stemmed.append(word)
                continue

            # Extract and preserve punctuation
            prefix = ""
            suffix = ""
            clean_word = word

            while clean_word and not clean_word[0].isalnum():
                prefix += clean_word[0]
                clean_word = clean_word[1:]
            while clean_word and not clean_word[-1].isalnum():
                suffix = clean_word[-1] + suffix
                clean_word = clean_word[:-1]

            if not clean_word:
                stemmed.append(word)
                continue

            # Stem the word
            try:
                if self._preserve_case:
                    was_upper = clean_word[0].isupper()
                    was_all_upper = clean_word.isupper()
                    stem = stemmer.stem(clean_word.lower())
                    if was_all_upper:
                        stem = stem.upper()
                    elif was_upper:
                        stem = stem.capitalize()
                else:
                    stem = stemmer.stem(clean_word.lower())

                stemmed.append(f"{prefix}{stem}{suffix}")
            except Exception:
                stemmed.append(word)

        return " ".join(stemmed)


class MultiLanguageStemmer(Preprocessor):
    """
    Stemmer that tries multiple languages.

    Useful when the query language is unknown.
    """

    def __init__(
        self,
        languages: Optional[list] = None,
        min_word_length: int = 3,
    ):
        """
        Initialize multi-language stemmer.

        Args:
            languages: Languages to try (default: ["english", "german"])
            min_word_length: Minimum word length to stem
        """
        self._languages = languages or ["english", "german"]
        self._min_word_length = min_word_length
        self._stemmers: Dict[str, Stemmer] = {}

        for lang in self._languages:
            self._stemmers[lang] = Stemmer(
                language=lang,
                min_word_length=min_word_length,
            )

    @property
    def name(self) -> str:
        langs = "_".join(sorted(self._languages))
        return f"stem_multi_{langs}"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "languages": self._languages,
            "min_word_length": self._min_word_length,
        }

    def process(self, query: str) -> str:
        """
        Apply stemming using the first available language.

        Note: This is a simple implementation. For better results,
        use language detection to pick the right stemmer.
        """
        # Use first language as primary
        primary = self._languages[0]
        return self._stemmers[primary].process(query)
