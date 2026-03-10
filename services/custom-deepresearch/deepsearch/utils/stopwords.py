"""
Unified stopword loading for all DeepSearch modules.

This module consolidates stopword handling for:
- deepsearch.processors.query_reformulator (async, LLM-capable)
- deepsearch.retrievers.preprocessors.stopwords (sync, non-LLM)

Both modules now import from here for consistency.
"""

from typing import List, Optional, Set

from deepsearch.observability import get_logger

logger = get_logger(__name__)


# Comprehensive English stopwords
ENGLISH_STOPWORDS: Set[str] = {
    # Articles
    "a", "an", "the",
    # Prepositions
    "in", "on", "at", "to", "for", "of", "with", "by", "from", "up", "about",
    "into", "over", "after", "through", "during", "before", "between", "under",
    "above", "below", "out", "off", "down", "away", "across", "behind", "beyond",
    # Conjunctions
    "and", "or", "but", "nor", "so", "yet", "both", "either", "neither",
    # Auxiliary verbs
    "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "do", "does", "did", "will", "would", "could", "should", "may", "might",
    "must", "shall", "can", "need", "dare", "ought", "used",
    # Pronouns
    "i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "us", "them",
    "my", "your", "his", "its", "our", "their", "mine", "yours", "hers", "ours", "theirs",
    "myself", "yourself", "himself", "herself", "itself", "ourselves", "themselves",
    # Demonstratives
    "this", "that", "these", "those",
    # Interrogatives
    "what", "which", "who", "whom", "whose", "when", "where", "why", "how",
    # Quantifiers
    "all", "each", "every", "both", "few", "more", "most", "other", "some",
    "such", "no", "any", "many", "much", "several", "enough",
    # Adverbs
    "not", "only", "own", "same", "so", "than", "too", "very", "just", "also",
    "now", "here", "there", "then", "once", "always", "never", "often", "still",
    "already", "even", "ever", "again", "further",
    # Subordinating conjunctions
    "if", "because", "as", "until", "while", "although", "though", "unless",
    "since", "whether", "whereas",
    # Common verbs (often noise in search)
    "get", "got", "getting", "make", "made", "let", "lets", "like", "know",
    "think", "want", "see", "look", "use", "find", "give", "tell", "say",
    "said", "come", "came", "go", "went", "take", "took", "put", "try",
}

# Comprehensive German stopwords
GERMAN_STOPWORDS: Set[str] = {
    # Articles
    "der", "die", "das", "den", "dem", "des", "ein", "eine", "einer", "einem",
    "einen", "eines",
    # Conjunctions
    "und", "oder", "aber", "doch", "wenn", "weil", "dass", "ob", "als", "wie",
    "sondern", "denn", "bevor", "nachdem", "obwohl", "während", "falls", "damit",
    # Prepositions
    "in", "im", "an", "am", "auf", "aus", "bei", "mit", "nach", "über",
    "unter", "vor", "zwischen", "durch", "für", "gegen", "ohne", "um",
    "bis", "seit", "von", "zu", "zum", "zur",
    # Pronouns
    "ich", "du", "er", "sie", "es", "wir", "ihr", "mein", "dein", "sein",
    "unser", "euer", "dieser", "diese", "dieses", "jener", "jene",
    "welcher", "welche", "welches", "was", "wer", "wie", "wo", "wann",
    "warum", "mich", "dich", "sich", "uns", "euch",
    # Auxiliary verbs
    "ist", "sind", "war", "waren", "bin", "bist", "hat", "haben",
    "hatte", "hatten", "wird", "werden", "wurde", "wurden", "kann", "können",
    "konnte", "konnten", "muss", "müssen", "musste", "mussten", "soll",
    "sollen", "sollte", "sollten", "will", "wollen", "wollte", "wollten",
    "darf", "dürfen", "durfte", "durften", "mag", "mögen", "mochte", "mochten",
    "wäre", "wären", "hätte", "hätten", "würde", "würden",
    # Negation
    "nicht", "kein", "keine", "keiner", "keinem", "keinen", "keines", "nie", "niemals",
    # Adverbs
    "auch", "nur", "noch", "schon", "immer", "wieder", "hier", "dort",
    "heute", "gestern", "morgen", "jetzt", "dann", "so", "sehr", "zu",
    "ja", "nein", "vielleicht", "etwa", "denn", "also", "nun", "eben",
    "ganz", "fast", "wohl", "jedoch", "bereits", "gleich",
    # Common verbs
    "sein", "haben", "werden", "machen", "gehen", "kommen", "sehen",
    "geben", "nehmen", "finden", "wissen", "sagen", "lassen",
}


def load_stopwords(languages: Optional[List[str]] = None) -> Set[str]:
    """
    Load stopwords for specified languages.

    Uses built-in comprehensive sets for English and German.
    Falls back to NLTK for other languages.

    Args:
        languages: List of language codes ("english", "german", "en", "de")
                   Defaults to ["english", "german"]

    Returns:
        Set of stopwords for the specified languages
    """
    languages = languages or ["english", "german"]
    stopwords: Set[str] = set()

    for lang in languages:
        lang_lower = lang.lower()

        # Built-in comprehensive sets
        if lang_lower in ("english", "en"):
            stopwords.update(ENGLISH_STOPWORDS)
        elif lang_lower in ("german", "de", "deutsch"):
            stopwords.update(GERMAN_STOPWORDS)
        else:
            # Try NLTK as fallback for other languages
            try:
                from nltk.corpus import stopwords as nltk_stopwords
                try:
                    stopwords.update(nltk_stopwords.words(lang_lower))
                    logger.debug(
                        "stopwords_loaded_nltk",
                        language=lang_lower,
                    )
                except OSError:
                    # Try downloading
                    try:
                        import nltk
                        nltk.download("stopwords", quiet=True)
                        stopwords.update(nltk_stopwords.words(lang_lower))
                    except Exception:
                        logger.warning(
                            "stopwords_not_found",
                            language=lang_lower,
                        )
            except ImportError:
                logger.warning(
                    "nltk_not_available",
                    language=lang_lower,
                    message="Install nltk for additional language support",
                )

    logger.debug(
        "stopwords_loaded",
        languages=languages,
        count=len(stopwords),
    )
    return stopwords
