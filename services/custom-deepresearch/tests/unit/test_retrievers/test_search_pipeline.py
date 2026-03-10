"""
Unit tests for SearchPipeline.

Tests the SearchPipeline class with mocked search methods and postprocessors.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock

from deepsearch.models import SearchResult
from deepsearch.retrievers import SearchPipeline, SearchPipelineBuilder
from deepsearch.retrievers.preprocessors import (
    StopwordRemover,
    KeywordExtractor,
    ResultTransform,
)


class MockSearchMethod:
    """Mock search method for testing."""

    def __init__(self, name: str = "mock", results: list = None):
        self._name = name
        self._results = results or []
        self.search = AsyncMock(return_value=self._results)

    @property
    def name(self) -> str:
        return self._name

    def get_config(self) -> dict:
        return {"name": self._name, "type": "mock"}


def create_mock_results(count: int = 5) -> list:
    """Create mock SearchResult objects."""
    return [
        SearchResult(
            id=f"doc_{i}",
            title=f"Document {i}",
            content=f"Content for document {i}",
            score=10.0 - i,
            source_type="test",
        )
        for i in range(count)
    ]


class TestSearchPipeline:
    """Tests for SearchPipeline class."""

    @pytest.mark.asyncio
    async def test_basic_search(self):
        """Test basic search without preprocessors."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        pipeline = SearchPipeline(search_method=method)
        search_results = await pipeline.search("test query", max_results=10)

        method.search.assert_called_once_with("test query", max_results=10, filters=None)
        assert search_results == results

    @pytest.mark.asyncio
    async def test_search_with_preprocessors(self):
        """Test search with preprocessors applied."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[StopwordRemover(languages=["english"])],
        )

        await pipeline.search("what is the error", max_results=10)

        # Verify the preprocessed query was passed to search method
        call_args = method.search.call_args
        query = call_args[0][0]  # First positional argument
        assert "what" not in query.split()
        assert "is" not in query.split()
        assert "the" not in query.split()
        assert "error" in query

    @pytest.mark.asyncio
    async def test_search_with_multiple_preprocessors(self):
        """Test search with chained preprocessors."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[
                StopwordRemover(languages=["english"]),
                KeywordExtractor(max_terms=3),
            ],
        )

        await pipeline.search(
            "what is the error code in the system documentation",
            max_results=10,
        )

        call_args = method.search.call_args
        query = call_args[0][0]
        words = query.split()
        assert len(words) <= 3

    @pytest.mark.asyncio
    async def test_search_with_filters(self):
        """Test search with filters passed through."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        pipeline = SearchPipeline(search_method=method)
        await pipeline.search(
            "test query",
            max_results=10,
            filters={"category": "docs"},
        )

        method.search.assert_called_once_with(
            "test query",
            max_results=10,
            filters={"category": "docs"},
        )

    @pytest.mark.asyncio
    async def test_search_with_response(self):
        """Test search_with_response returns SearchResponse."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        pipeline = SearchPipeline(search_method=method)
        response = await pipeline.search_with_response("test query", max_results=10)

        assert response.results == results
        assert response.query == "test query"
        assert response.success
        assert response.search_time_ms >= 0

    def test_preprocess_single(self):
        """Test preprocess with single preprocessor."""
        method = MockSearchMethod()
        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[StopwordRemover(languages=["english"])],
        )

        result = pipeline.preprocess("what is the error")
        assert "error" in result
        assert "what" not in result.split()

    def test_preprocess_empty(self):
        """Test preprocess with no preprocessors."""
        method = MockSearchMethod()
        pipeline = SearchPipeline(search_method=method)

        result = pipeline.preprocess("what is the error")
        assert result == "what is the error"

    def test_name_property(self):
        """Test pipeline name property."""
        method = MockSearchMethod(name="bm25")
        pipeline = SearchPipeline(search_method=method)
        assert pipeline.name == "bm25"

        pipeline_with_prep = SearchPipeline(
            search_method=method,
            preprocessors=[StopwordRemover()],
        )
        assert "bm25" in pipeline_with_prep.name
        assert "stopwords" in pipeline_with_prep.name

    def test_get_config(self):
        """Test pipeline configuration retrieval."""
        method = MockSearchMethod(name="bm25")
        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[StopwordRemover()],
        )

        config = pipeline.get_config()
        assert config["name"] == pipeline.name
        assert "search_method" in config
        assert "preprocessors" in config
        assert len(config["preprocessors"]) == 1


class TestSearchPipelineBuilder:
    """Tests for SearchPipelineBuilder class."""

    def test_builder_with_search_method(self):
        """Test builder with search method."""
        method = MockSearchMethod(name="bm25")

        pipeline = (
            SearchPipelineBuilder()
            .with_search_method(method)
            .build()
        )

        assert pipeline.search_method == method

    def test_builder_with_preprocessors(self):
        """Test builder with preprocessors."""
        method = MockSearchMethod()

        pipeline = (
            SearchPipelineBuilder()
            .with_search_method(method)
            .with_stopwords(["english"])
            .with_keywords(max_terms=5)
            .build()
        )

        assert len(pipeline.preprocessors) == 2

    def test_builder_without_method_raises(self):
        """Test builder without search method raises error."""
        with pytest.raises(ValueError, match="Search method is required"):
            SearchPipelineBuilder().build()

    def test_builder_with_preprocessor_list(self):
        """Test builder with preprocessor list."""
        method = MockSearchMethod()
        preprocessors = [StopwordRemover(), KeywordExtractor()]

        pipeline = (
            SearchPipelineBuilder()
            .with_search_method(method)
            .with_preprocessors(preprocessors)
            .build()
        )

        assert pipeline.preprocessors == preprocessors

    def test_builder_with_stemmer(self):
        """Test builder with stemmer."""
        method = MockSearchMethod()

        pipeline = (
            SearchPipelineBuilder()
            .with_search_method(method)
            .with_stemmer("english")
            .build()
        )

        assert len(pipeline.preprocessors) == 1
        assert "stem" in pipeline.preprocessors[0].name


class TestSearchPipelineEdgeCases:
    """Edge case tests for SearchPipeline."""

    @pytest.mark.asyncio
    async def test_empty_query(self):
        """Test handling of empty query."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[StopwordRemover()],
        )

        await pipeline.search("", max_results=10)
        method.search.assert_called_once()

    @pytest.mark.asyncio
    async def test_all_stopwords_query(self):
        """Test query where all words are stopwords."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[StopwordRemover(languages=["english"])],
        )

        await pipeline.search("the is a an", max_results=10)
        # Should pass original query if preprocessing would return empty
        call_args = method.search.call_args
        query = call_args[0][0]
        assert len(query) > 0

    @pytest.mark.asyncio
    async def test_preprocessor_exception_handled(self):
        """Test that preprocessor exceptions are handled gracefully."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        class FailingPreprocessor:
            @property
            def name(self):
                return "failing"

            def process(self, query):
                raise Exception("Preprocessor failed")

        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[FailingPreprocessor()],
        )

        # Should not raise, should continue with original query
        search_results = await pipeline.search("test query", max_results=10)
        assert search_results == results

    @pytest.mark.asyncio
    async def test_search_method_exception(self):
        """Test handling of search method exception."""
        method = MockSearchMethod()
        method.search = AsyncMock(side_effect=Exception("Search failed"))

        pipeline = SearchPipeline(search_method=method)

        response = await pipeline.search_with_response("test query", max_results=10)
        assert not response.success
        assert "Search failed" in response.error


class MockResultTransform(ResultTransform):
    """Mock result transform for testing."""

    def __init__(self, name: str = "mock_transform"):
        self._name = name
        self._called_with = None

    @property
    def name(self) -> str:
        return self._name

    async def process(self, results, query):
        self._called_with = (results, query)
        # Reverse order and halve scores as a visible transformation
        return [
            SearchResult(
                id=r.id,
                title=r.title,
                content=r.content,
                score=r.score / 2,
                source_type=r.source_type,
            )
            for r in reversed(results)
        ]


class TestSearchPipelinePostprocessors:
    """Tests for SearchPipeline postprocessor functionality."""

    @pytest.mark.asyncio
    async def test_search_with_postprocessor(self):
        """Test search with a postprocessor."""
        results = create_mock_results(5)
        method = MockSearchMethod(results=results)
        transform = MockResultTransform()

        pipeline = SearchPipeline(
            search_method=method,
            postprocessors=[transform],
        )

        search_results = await pipeline.search("test query", max_results=5)

        # Verify postprocessor was called
        assert transform._called_with is not None
        assert transform._called_with[1] == "test query"

        # Verify results were transformed (reversed order)
        assert search_results[0].id == "doc_4"
        assert search_results[-1].id == "doc_0"

        # Verify scores were halved
        assert search_results[0].score == 3.0  # Was 6.0

    @pytest.mark.asyncio
    async def test_search_with_multiple_postprocessors(self):
        """Test search with chained postprocessors."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        transform1 = MockResultTransform("transform1")
        transform2 = MockResultTransform("transform2")

        pipeline = SearchPipeline(
            search_method=method,
            postprocessors=[transform1, transform2],
        )

        await pipeline.search("test query", max_results=3)

        # Both transforms should have been called
        assert transform1._called_with is not None
        assert transform2._called_with is not None

    @pytest.mark.asyncio
    async def test_postprocessor_receives_original_query(self):
        """Test that postprocessor receives original query, not preprocessed."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)
        transform = MockResultTransform()

        pipeline = SearchPipeline(
            search_method=method,
            preprocessors=[StopwordRemover(languages=["english"])],
            postprocessors=[transform],
        )

        await pipeline.search("what is the error", max_results=3)

        # Postprocessor should receive original query
        assert transform._called_with[1] == "what is the error"

    @pytest.mark.asyncio
    async def test_pipeline_name_includes_postprocessors(self):
        """Test that pipeline name includes postprocessor names."""
        method = MockSearchMethod(name="bm25")
        transform = MockResultTransform("reranker")

        pipeline = SearchPipeline(
            search_method=method,
            postprocessors=[transform],
        )

        assert "reranker" in pipeline.name

    def test_get_config_includes_postprocessors(self):
        """Test that get_config includes postprocessor configs."""
        method = MockSearchMethod(name="bm25")
        transform = MockResultTransform("reranker")

        pipeline = SearchPipeline(
            search_method=method,
            postprocessors=[transform],
        )

        config = pipeline.get_config()
        assert "postprocessors" in config
        assert len(config["postprocessors"]) == 1
        assert config["postprocessors"][0]["name"] == "reranker"

    @pytest.mark.asyncio
    async def test_postprocessor_exception_handled(self):
        """Test that postprocessor exceptions are handled gracefully."""
        results = create_mock_results(3)
        method = MockSearchMethod(results=results)

        class FailingTransform(ResultTransform):
            @property
            def name(self):
                return "failing"

            async def process(self, results, query):
                raise Exception("Transform failed")

        pipeline = SearchPipeline(
            search_method=method,
            postprocessors=[FailingTransform()],
        )

        # Should not raise, should return original results
        search_results = await pipeline.search("test query", max_results=3)
        assert len(search_results) == 3

    @pytest.mark.asyncio
    async def test_postprocessor_fetches_more_results(self):
        """Test that pipeline fetches more results when postprocessors present."""
        # Create 30 results with positive scores
        results = [
            SearchResult(
                id=f"doc_{i}",
                title=f"Document {i}",
                content=f"Content for document {i}",
                score=100.0 - i,  # Large enough to stay positive
                source_type="test",
            )
            for i in range(30)
        ]
        method = MockSearchMethod(results=results)
        transform = MockResultTransform()

        pipeline = SearchPipeline(
            search_method=method,
            postprocessors=[transform],
        )

        await pipeline.search("test query", max_results=10)

        # Should fetch more than 10 for reranking
        call_args = method.search.call_args
        fetched_count = call_args.kwargs.get("max_results") or call_args[1].get("max_results")
        assert fetched_count >= 30  # 3x requested


class TestSearchPipelineBuilderPostprocessors:
    """Tests for SearchPipelineBuilder postprocessor support."""

    def test_builder_with_postprocessor(self):
        """Test builder with postprocessor."""
        method = MockSearchMethod()
        transform = MockResultTransform()

        pipeline = (
            SearchPipelineBuilder()
            .with_search_method(method)
            .with_postprocessor(transform)
            .build()
        )

        assert len(pipeline.postprocessors) == 1
        assert pipeline.postprocessors[0] == transform

    def test_builder_with_multiple_postprocessors(self):
        """Test builder with multiple postprocessors."""
        method = MockSearchMethod()
        transforms = [MockResultTransform("t1"), MockResultTransform("t2")]

        pipeline = (
            SearchPipelineBuilder()
            .with_search_method(method)
            .with_postprocessors(transforms)
            .build()
        )

        assert len(pipeline.postprocessors) == 2

    def test_builder_full_pipeline(self):
        """Test builder with preprocessors and postprocessors."""
        method = MockSearchMethod()
        transform = MockResultTransform()

        pipeline = (
            SearchPipelineBuilder()
            .with_search_method(method)
            .with_stopwords(["english"])
            .with_keywords(max_terms=5)
            .with_postprocessor(transform)
            .build()
        )

        assert len(pipeline.preprocessors) == 2
        assert len(pipeline.postprocessors) == 1
