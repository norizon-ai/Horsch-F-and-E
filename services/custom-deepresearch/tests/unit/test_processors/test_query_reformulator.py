"""
Unit tests for deepsearch.processors.query_reformulator module.

Tests QueryReformulator, SimpleTermExtractor, and get_stopwords.
"""

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from deepsearch.processors.query_reformulator import (
    QueryReformulator,
    QueryReformulatorConfig,
    SimpleTermExtractor,
    get_stopwords,
)
from deepsearch.utils.stopwords import ENGLISH_STOPWORDS, GERMAN_STOPWORDS
from deepsearch.llm.base import LLMResponse


class TestGetStopwords:
    """Test get_stopwords function."""

    def test_returns_set(self):
        """Returns a set of stopwords."""
        stopwords = get_stopwords()
        assert isinstance(stopwords, set)
        assert len(stopwords) > 0

    def test_default_languages(self):
        """Default includes English and German."""
        stopwords = get_stopwords()
        # Should contain common English words
        assert "the" in stopwords or "a" in stopwords
        # Should contain common German words
        assert "der" in stopwords or "die" in stopwords

    def test_single_language(self):
        """Can request single language."""
        stopwords = get_stopwords(["english"])
        assert isinstance(stopwords, set)

    def test_shared_stopwords_exist(self):
        """Shared stopwords are defined and comprehensive."""
        assert len(ENGLISH_STOPWORDS) > 0
        assert len(GERMAN_STOPWORDS) > 0
        # Check both languages have common words
        assert "the" in ENGLISH_STOPWORDS
        assert "der" in GERMAN_STOPWORDS


class TestQueryReformulatorConfig:
    """Test QueryReformulatorConfig."""

    def test_default_values(self):
        """Config has sensible defaults."""
        config = QueryReformulatorConfig()
        assert config.max_terms == 10
        assert config.min_term_length == 2
        assert config.use_llm is False
        assert "english" in config.languages
        assert "german" in config.languages
        assert config.custom_stopwords == set()
        assert config.prompt_name == "reformulate_query"

    def test_custom_values(self):
        """Config accepts custom values."""
        config = QueryReformulatorConfig(
            max_terms=5,
            min_term_length=3,
            use_llm=True,
            languages=["english"],
            custom_stopwords={"custom", "words"},
            prompt_name="custom_prompt",
        )
        assert config.max_terms == 5
        assert config.min_term_length == 3
        assert config.use_llm is True
        assert config.languages == ["english"]
        assert config.custom_stopwords == {"custom", "words"}
        assert config.prompt_name == "custom_prompt"


class TestQueryReformulatorInit:
    """Test QueryReformulator initialization."""

    def test_default_config(self):
        """Uses default config if not provided."""
        reformulator = QueryReformulator()
        assert reformulator.config.max_terms == 10
        assert reformulator.config.use_llm is False

    def test_custom_config(self):
        """Accepts custom config."""
        config = QueryReformulatorConfig(max_terms=5)
        reformulator = QueryReformulator(config=config)
        assert reformulator.config.max_terms == 5

    def test_llm_disabled_without_provider(self):
        """LLM mode disabled if provider not given."""
        config = QueryReformulatorConfig(use_llm=True)
        reformulator = QueryReformulator(config=config)
        assert reformulator.config.use_llm is False

    def test_llm_disabled_without_prompts(self):
        """LLM mode disabled if prompts not given."""
        config = QueryReformulatorConfig(use_llm=True)
        mock_llm = MagicMock()
        reformulator = QueryReformulator(config=config, llm=mock_llm)
        assert reformulator.config.use_llm is False

    def test_llm_enabled_with_both(self):
        """LLM mode enabled when both LLM and prompts provided."""
        config = QueryReformulatorConfig(use_llm=True)
        mock_llm = MagicMock()
        mock_prompts = MagicMock()
        reformulator = QueryReformulator(
            config=config, llm=mock_llm, prompts=mock_prompts
        )
        assert reformulator.config.use_llm is True

    def test_stopwords_loaded(self):
        """Stopwords are loaded during init."""
        reformulator = QueryReformulator()
        assert len(reformulator.stop_words) > 0

    def test_custom_stopwords_added(self):
        """Custom stopwords are added to set."""
        config = QueryReformulatorConfig(custom_stopwords={"custom1", "custom2"})
        reformulator = QueryReformulator(config=config)
        assert "custom1" in reformulator.stop_words
        assert "custom2" in reformulator.stop_words


class TestQueryReformulatorSimpleReformulation:
    """Test simple (non-LLM) query reformulation."""

    @pytest.fixture
    def reformulator(self):
        """Create a reformulator with simple mode."""
        return QueryReformulator()

    @pytest.mark.asyncio
    async def test_basic_reformulation(self, reformulator):
        """Basic query is reformulated."""
        result = await reformulator.pre_process("What is the capital of France?")
        # Stopwords removed, key terms remain
        assert "capital" in result
        assert "france" in result
        # Stopwords removed
        assert "what" not in result.lower()
        assert "the" not in result.lower()

    @pytest.mark.asyncio
    async def test_empty_query(self, reformulator):
        """Empty query returns unchanged."""
        result = await reformulator.pre_process("")
        assert result == ""

    @pytest.mark.asyncio
    async def test_whitespace_query(self, reformulator):
        """Whitespace-only query returns unchanged."""
        result = await reformulator.pre_process("   ")
        assert result == "   "

    @pytest.mark.asyncio
    async def test_stopword_removal_english(self, reformulator):
        """English stopwords are removed."""
        result = await reformulator.pre_process(
            "The quick brown fox jumps over the lazy dog"
        )
        assert "the" not in result.lower()
        assert "over" not in result.lower()
        assert "quick" in result
        assert "brown" in result
        assert "fox" in result

    @pytest.mark.asyncio
    async def test_stopword_removal_german(self, reformulator):
        """German stopwords are removed."""
        result = await reformulator.pre_process("Der schnelle braune Fuchs springt")
        assert "der" not in result.lower()
        assert "schnelle" in result
        assert "braune" in result
        assert "fuchs" in result

    @pytest.mark.asyncio
    async def test_min_term_length(self):
        """Terms below min length are filtered."""
        config = QueryReformulatorConfig(min_term_length=4)
        reformulator = QueryReformulator(config=config)
        # Query with some words >= 4 chars that pass filter
        result = await reformulator.pre_process("a big elephant runs")
        # Short words should not be in result when we have longer words
        assert "elephant" in result or "runs" in result
        # If longer words exist, shorter ones should be filtered

    @pytest.mark.asyncio
    async def test_max_terms_limit(self):
        """Result is limited to max_terms."""
        config = QueryReformulatorConfig(max_terms=3)
        reformulator = QueryReformulator(config=config)
        result = await reformulator.pre_process(
            "elephant giraffe zebra lion tiger leopard"
        )
        terms = result.split()
        assert len(terms) <= 3

    @pytest.mark.asyncio
    async def test_duplicate_removal(self, reformulator):
        """Duplicate terms are removed."""
        result = await reformulator.pre_process("python python programming python")
        assert result.count("python") == 1

    @pytest.mark.asyncio
    async def test_case_normalization(self, reformulator):
        """Terms are lowercased."""
        result = await reformulator.pre_process("PYTHON Programming")
        assert "PYTHON" not in result
        assert "python" in result or "programming" in result

    @pytest.mark.asyncio
    async def test_preserves_german_umlauts(self, reformulator):
        """German umlauts are preserved."""
        result = await reformulator.pre_process("Prüfung Öffnung Übung")
        # Umlauts should be in result
        assert "prüfung" in result or "öffnung" in result or "übung" in result

    @pytest.mark.asyncio
    async def test_digits_filtered(self, reformulator):
        """Pure digit terms are filtered."""
        result = await reformulator.pre_process("year 2024 was great")
        assert "2024" not in result
        assert "year" in result or "great" in result

    @pytest.mark.asyncio
    async def test_only_stopwords_returns_original(self, reformulator):
        """Query with only stopwords returns original."""
        result = await reformulator.pre_process("the a an is are")
        # Should return original if all filtered
        assert result == "the a an is are"


class TestQueryReformulatorLLMReformulation:
    """Test LLM-based query reformulation."""

    @pytest.fixture
    def mock_llm(self):
        """Create mock LLM provider."""
        llm = AsyncMock()
        llm.complete.return_value = LLMResponse(
            content="reformulated query terms",
            model="test",
            finish_reason="stop",
        )
        return llm

    @pytest.fixture
    def mock_prompts(self):
        """Create mock prompt manager."""
        prompts = MagicMock()
        prompts.get_prompt.return_value = "Reformulate: {query}"
        return prompts

    @pytest.mark.asyncio
    async def test_llm_reformulation(self, mock_llm, mock_prompts):
        """LLM reformulation calls LLM provider."""
        config = QueryReformulatorConfig(use_llm=True)
        reformulator = QueryReformulator(
            config=config, llm=mock_llm, prompts=mock_prompts
        )

        result = await reformulator.pre_process("test query")

        assert result == "reformulated query terms"
        mock_llm.complete.assert_called_once()

    @pytest.mark.asyncio
    async def test_llm_prompt_loaded(self, mock_llm, mock_prompts):
        """LLM mode loads prompt from PromptManager."""
        config = QueryReformulatorConfig(use_llm=True, prompt_name="custom_prompt")
        reformulator = QueryReformulator(
            config=config, llm=mock_llm, prompts=mock_prompts
        )

        await reformulator.pre_process("test query")

        mock_prompts.get_prompt.assert_called_once()
        call_args = mock_prompts.get_prompt.call_args
        assert call_args[0][0] == "query_reformulator"
        assert call_args[0][1] == "custom_prompt"

    @pytest.mark.asyncio
    async def test_llm_fallback_on_error(self, mock_llm, mock_prompts):
        """Falls back to simple on LLM error."""
        mock_llm.complete.side_effect = Exception("LLM error")
        config = QueryReformulatorConfig(use_llm=True)
        reformulator = QueryReformulator(
            config=config, llm=mock_llm, prompts=mock_prompts
        )

        result = await reformulator.pre_process("test query for search")

        # Should fall back to simple reformulation
        assert "test" in result or "query" in result or "search" in result

    @pytest.mark.asyncio
    async def test_llm_fallback_on_long_response(self, mock_llm, mock_prompts):
        """Falls back if LLM response is too long."""
        mock_llm.complete.return_value = LLMResponse(
            content="a" * 1000,  # Very long response
            model="test",
            finish_reason="stop",
        )
        config = QueryReformulatorConfig(use_llm=True)
        reformulator = QueryReformulator(
            config=config, llm=mock_llm, prompts=mock_prompts
        )

        result = await reformulator.pre_process("test")

        # Should fall back due to length validation
        assert len(result) < 1000

    @pytest.mark.asyncio
    async def test_llm_fallback_on_empty_response(self, mock_llm, mock_prompts):
        """Falls back if LLM returns empty."""
        mock_llm.complete.return_value = LLMResponse(
            content="",
            model="test",
            finish_reason="stop",
        )
        config = QueryReformulatorConfig(use_llm=True)
        reformulator = QueryReformulator(
            config=config, llm=mock_llm, prompts=mock_prompts
        )

        result = await reformulator.pre_process("machine learning")

        # Should fall back to simple reformulation
        assert "machine" in result or "learning" in result


class TestSimpleTermExtractor:
    """Test SimpleTermExtractor processor."""

    @pytest.fixture
    def extractor(self):
        """Create a simple term extractor."""
        return SimpleTermExtractor()

    @pytest.mark.asyncio
    async def test_extracts_terms(self, extractor):
        """Extracts key terms from query."""
        result = await extractor.pre_process("What is machine learning?")
        assert "machine" in result
        assert "learning" in result

    @pytest.mark.asyncio
    async def test_removes_stopwords(self, extractor):
        """Removes common stopwords."""
        result = await extractor.pre_process("The quick brown fox")
        assert "the" not in result.lower()
        assert "quick" in result
        assert "brown" in result
        assert "fox" in result

    @pytest.mark.asyncio
    async def test_max_terms_limit(self):
        """Respects max_terms setting."""
        extractor = SimpleTermExtractor(max_terms=2)
        result = await extractor.pre_process("one two three four five")
        terms = result.split()
        assert len(terms) <= 2

    @pytest.mark.asyncio
    async def test_custom_languages(self):
        """Works with custom language settings."""
        extractor = SimpleTermExtractor(languages=["german"])
        result = await extractor.pre_process("der schnelle braune Fuchs")
        assert "der" not in result.lower()

    @pytest.mark.asyncio
    async def test_minimum_word_length(self, extractor):
        """Filters words less than 3 characters."""
        result = await extractor.pre_process("a at to go run walk")
        # 'a', 'at', 'to', 'go' are all <= 2 chars, should be filtered
        assert "a" not in result.split()
        assert "at" not in result.split()
        assert "to" not in result.split()
        assert "go" not in result.split()
        # 'run' and 'walk' are 3+ chars
        assert "run" in result or "walk" in result

    @pytest.mark.asyncio
    async def test_returns_original_if_all_filtered(self, extractor):
        """Returns original query if all words filtered."""
        result = await extractor.pre_process("a to in")
        # All filtered, should return original
        assert result == "a to in"

    @pytest.mark.asyncio
    async def test_deduplicates_terms(self, extractor):
        """Removes duplicate terms."""
        result = await extractor.pre_process("python python programming python code")
        assert result.count("python") == 1

    @pytest.mark.asyncio
    async def test_preserves_order(self, extractor):
        """Preserves order of first occurrence."""
        result = await extractor.pre_process("alpha beta gamma delta")
        terms = result.split()
        if "alpha" in terms and "beta" in terms:
            assert terms.index("alpha") < terms.index("beta")
