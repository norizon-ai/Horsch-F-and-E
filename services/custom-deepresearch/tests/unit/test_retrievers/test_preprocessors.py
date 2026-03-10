"""
Unit tests for query preprocessors.

Tests the non-LLM preprocessors: StopwordRemover, Stemmer, KeywordExtractor, PreprocessorChain.
"""

import pytest

from deepsearch.retrievers.preprocessors import (
    Preprocessor,
    StopwordRemover,
    Stemmer,
    KeywordExtractor,
    PreprocessorChain,
)
from deepsearch.retrievers.preprocessors.keyword_extractor import (
    TechnicalTermExtractor,
    QueryFocuser,
)
from deepsearch.retrievers.preprocessors.chain import chain


class TestStopwordRemover:
    """Tests for StopwordRemover preprocessor."""

    def test_basic_stopword_removal(self):
        """Test basic English stopword removal."""
        preprocessor = StopwordRemover(languages=["english"])
        result = preprocessor.process("what is the error code")
        # "what", "is", "the" are stopwords
        assert "what" not in result.split()
        assert "is" not in result.split()
        assert "the" not in result.split()
        assert "error" in result
        assert "code" in result

    def test_german_stopword_removal(self):
        """Test German stopword removal."""
        preprocessor = StopwordRemover(languages=["german"])
        result = preprocessor.process("was ist der fehler")
        # "was", "ist", "der" are stopwords
        assert "fehler" in result

    def test_combined_languages(self):
        """Test English + German stopword removal."""
        preprocessor = StopwordRemover(languages=["english", "german"])
        result = preprocessor.process("what is the error was ist der fehler")
        assert "error" in result
        assert "fehler" in result

    def test_empty_query(self):
        """Test handling of empty query."""
        preprocessor = StopwordRemover()
        assert preprocessor.process("") == ""
        assert preprocessor.process("   ") == "   "

    def test_all_stopwords_returns_original(self):
        """Test that if all words are stopwords, original is returned."""
        preprocessor = StopwordRemover(languages=["english"])
        result = preprocessor.process("the is a an")
        assert result == "the is a an"

    def test_preserve_quoted_phrases(self):
        """Test that quoted phrases are preserved."""
        preprocessor = StopwordRemover(languages=["english"], preserve_quoted=True)
        result = preprocessor.process('what is "the error code"')
        assert '"the error code"' in result

    def test_name_property(self):
        """Test name property reflects languages."""
        preprocessor = StopwordRemover(languages=["english", "german"])
        assert "english" in preprocessor.name
        assert "german" in preprocessor.name

    def test_get_config(self):
        """Test configuration retrieval."""
        preprocessor = StopwordRemover(languages=["english"], min_word_length=2)
        config = preprocessor.get_config()
        assert config["languages"] == ["english"]
        assert config["min_word_length"] == 2


class TestStemmer:
    """Tests for Stemmer preprocessor."""

    def test_english_stemming(self):
        """Test English word stemming."""
        preprocessor = Stemmer(language="english")
        result = preprocessor.process("running searches searching")
        # "running" -> "run", "searches" -> "search"
        assert "run" in result or "search" in result

    def test_german_stemming(self):
        """Test German word stemming."""
        preprocessor = Stemmer(language="german")
        result = preprocessor.process("technische dokumentation")
        # Should stem German words
        assert len(result) > 0

    def test_short_words_preserved(self):
        """Test that short words are not stemmed."""
        preprocessor = Stemmer(language="english", min_word_length=4)
        result = preprocessor.process("the cat sat")
        # "the", "cat", "sat" are all < 4 chars
        assert "the" in result
        assert "cat" in result
        assert "sat" in result

    def test_punctuation_preserved(self):
        """Test that punctuation around words is preserved."""
        preprocessor = Stemmer(language="english")
        result = preprocessor.process("what's running?")
        assert "?" in result

    def test_language_mapping(self):
        """Test language code mapping."""
        # "de" should map to "german"
        preprocessor = Stemmer(language="de")
        assert preprocessor._language == "german"

    def test_name_property(self):
        """Test name property reflects language."""
        preprocessor = Stemmer(language="english")
        assert preprocessor.name == "stem_english"

    def test_invalid_language_graceful_fallback(self):
        """Test graceful handling of unsupported language."""
        preprocessor = Stemmer(language="klingon")
        # Should not crash, just return original
        result = preprocessor.process("test query")
        assert result == "test query"


class TestKeywordExtractor:
    """Tests for KeywordExtractor preprocessor."""

    def test_basic_extraction(self):
        """Test basic keyword extraction."""
        preprocessor = KeywordExtractor(max_terms=5)
        result = preprocessor.process("what is the RC-3000 error code in the system")
        words = result.split()
        assert len(words) <= 5
        # Should prioritize content words
        assert "error" in result or "code" in result or "system" in result

    def test_stopword_filtering(self):
        """Test that stopwords are filtered."""
        preprocessor = KeywordExtractor(max_terms=10, languages=["english"])
        result = preprocessor.process("what is the error code")
        assert "what" not in result.split()
        assert "is" not in result.split()
        assert "the" not in result.split()

    def test_max_terms_limit(self):
        """Test that max_terms is respected."""
        preprocessor = KeywordExtractor(max_terms=3)
        result = preprocessor.process("error code system documentation troubleshooting")
        words = result.split()
        assert len(words) <= 3

    def test_preserve_quoted_phrases(self):
        """Test preservation of quoted phrases."""
        preprocessor = KeywordExtractor(max_terms=5, preserve_quoted=True)
        result = preprocessor.process('search for "error code" in docs')
        assert '"error code"' in result

    def test_min_term_length(self):
        """Test minimum term length filtering."""
        preprocessor = KeywordExtractor(min_term_length=4)
        result = preprocessor.process("cat dog error")
        # "cat", "dog" are < 4 chars
        assert "error" in result

    def test_empty_query(self):
        """Test handling of empty query."""
        preprocessor = KeywordExtractor()
        assert preprocessor.process("") == ""

    def test_name_property(self):
        """Test name property."""
        preprocessor = KeywordExtractor(max_terms=8)
        assert preprocessor.name == "keywords_8"


class TestTechnicalTermExtractor:
    """Tests for TechnicalTermExtractor preprocessor."""

    def test_product_code_extraction(self):
        """Test extraction of product codes."""
        preprocessor = TechnicalTermExtractor()
        result = preprocessor.process("what is wrong with RC-3000")
        assert "RC-3000" in result

    def test_version_number_extraction(self):
        """Test extraction of version numbers."""
        preprocessor = TechnicalTermExtractor()
        result = preprocessor.process("bug in version 2.0.1")
        assert "2.0.1" in result

    def test_error_code_extraction(self):
        """Test extraction of error codes."""
        preprocessor = TechnicalTermExtractor()
        result = preprocessor.process("getting E1001 error")
        assert "E1001" in result

    def test_combined_technical_terms(self):
        """Test extraction of multiple technical terms."""
        preprocessor = TechnicalTermExtractor(max_terms=10)
        result = preprocessor.process("RC-3000 showing E1001 in version 3.0.1")
        assert "RC-3000" in result
        assert "E1001" in result
        assert "3.0.1" in result


class TestQueryFocuser:
    """Tests for QueryFocuser preprocessor."""

    def test_question_word_removal(self):
        """Test removal of leading question words."""
        preprocessor = QueryFocuser()
        result = preprocessor.process("what is the error code")
        assert not result.startswith("what")

    def test_filler_phrase_removal(self):
        """Test removal of filler phrases."""
        preprocessor = QueryFocuser()
        result = preprocessor.process("can you help me find the error")
        assert "can you" not in result
        assert "help me" not in result

    def test_max_words_limit(self):
        """Test max words limiting."""
        preprocessor = QueryFocuser(max_words=3)
        result = preprocessor.process("find the error code in the documentation")
        words = result.split()
        assert len(words) <= 3

    def test_empty_result_returns_original(self):
        """Test that empty result returns original query."""
        preprocessor = QueryFocuser()
        result = preprocessor.process("what is")
        # If all words are removed, should return original
        assert len(result) > 0


class TestPreprocessorChain:
    """Tests for PreprocessorChain."""

    def test_chain_creation(self):
        """Test creating a preprocessor chain."""
        chain = PreprocessorChain([
            StopwordRemover(),
            KeywordExtractor(max_terms=5),
        ])
        assert len(chain) == 2

    def test_chain_empty_raises(self):
        """Test that empty chain raises error."""
        with pytest.raises(ValueError):
            PreprocessorChain([])

    def test_chain_processing(self):
        """Test that chain applies preprocessors in order."""
        chain = PreprocessorChain([
            StopwordRemover(languages=["english"]),
            KeywordExtractor(max_terms=3),
        ])
        result = chain.process("what is the error code in the system")
        words = result.split()
        assert len(words) <= 3
        assert "what" not in words
        assert "is" not in words
        assert "the" not in words

    def test_chain_name_combined(self):
        """Test that chain name combines preprocessor names."""
        chain = PreprocessorChain([
            StopwordRemover(languages=["english"]),
            KeywordExtractor(max_terms=5),
        ])
        assert "stopwords" in chain.name
        assert "keywords" in chain.name
        assert "+" in chain.name

    def test_chain_get_config(self):
        """Test configuration retrieval."""
        chain = PreprocessorChain([
            StopwordRemover(),
            Stemmer(),
        ])
        config = chain.get_config()
        assert "chain" in config
        assert len(config["chain"]) == 2

    def test_chain_iteration(self):
        """Test iterating over chain."""
        preprocessors = [StopwordRemover(), KeywordExtractor()]
        chain = PreprocessorChain(preprocessors)
        assert list(chain) == preprocessors

    def test_chain_indexing(self):
        """Test indexing chain."""
        preprocessors = [StopwordRemover(), KeywordExtractor()]
        chain = PreprocessorChain(preprocessors)
        assert chain[0] == preprocessors[0]
        assert chain[1] == preprocessors[1]


class TestChainConvenienceFunction:
    """Tests for the chain() convenience function."""

    def test_chain_function(self):
        """Test chain() function creates PreprocessorChain."""
        result = chain(
            StopwordRemover(),
            KeywordExtractor(),
        )
        assert isinstance(result, PreprocessorChain)
        assert len(result) == 2

    def test_chain_function_single(self):
        """Test chain() with single preprocessor."""
        result = chain(StopwordRemover())
        assert len(result) == 1
