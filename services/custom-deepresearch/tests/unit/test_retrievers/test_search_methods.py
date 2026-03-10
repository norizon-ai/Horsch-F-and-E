"""
Unit tests for search methods.

Tests BM25Search, VectorSearch, and HybridSearch with mocked Elasticsearch.
"""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
import json

import httpx

from deepsearch.models import SearchResult
from deepsearch.retrievers.search_methods import BM25Search, VectorSearch, HybridSearch


def create_mock_es_response(hits: list, total: int = 10) -> dict:
    """Create a mock Elasticsearch response."""
    return {
        "hits": {
            "total": {"value": total},
            "hits": hits,
        }
    }


def create_mock_hit(doc_id: str, score: float, title: str, content: str) -> dict:
    """Create a mock Elasticsearch hit."""
    return {
        "_id": doc_id,
        "_score": score,
        "_source": {
            "id": doc_id,
            "title": title,
            "content": content,
            "url": f"https://example.com/{doc_id}",
        },
        "highlight": {
            "content": [f"...{content[:50]}..."],
        },
    }


class MockAsyncClient:
    """Mock httpx.AsyncClient for testing."""

    def __init__(self, response_data: dict = None):
        self._response_data = response_data or create_mock_es_response([])
        self.post = AsyncMock(return_value=self._create_response())

    def _create_response(self):
        response = MagicMock()
        response.json.return_value = self._response_data
        response.raise_for_status = MagicMock()
        return response

    def set_response(self, data: dict):
        self._response_data = data
        self.post.return_value = self._create_response()


class TestBM25Search:
    """Tests for BM25Search method."""

    @pytest.mark.asyncio
    async def test_basic_search(self):
        """Test basic BM25 search."""
        hits = [
            create_mock_hit("doc1", 10.0, "Title 1", "Content 1"),
            create_mock_hit("doc2", 8.0, "Title 2", "Content 2"),
        ]
        client = MockAsyncClient(create_mock_es_response(hits, total=2))

        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["title^3", "content"],
        )

        results = await search.search("test query", max_results=10)

        assert len(results) == 2
        assert results[0].id == "doc1"
        assert results[0].score == 10.0
        assert results[1].id == "doc2"

    @pytest.mark.asyncio
    async def test_search_with_filters(self):
        """Test BM25 search with filters."""
        client = MockAsyncClient(create_mock_es_response([]))

        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["title", "content"],
        )

        await search.search("test query", max_results=10, filters={"category": "docs"})

        # Verify filter was included in query
        call_args = client.post.call_args
        query_body = call_args[1]["json"]
        assert "query" in query_body
        assert "bool" in query_body["query"]
        assert "filter" in query_body["query"]["bool"]

    @pytest.mark.asyncio
    async def test_search_fields_boosting(self):
        """Test that field boosting is included in query."""
        client = MockAsyncClient(create_mock_es_response([]))

        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["title^3", "content"],
        )

        await search.search("test query", max_results=10)

        call_args = client.post.call_args
        query_body = call_args[1]["json"]
        multi_match = query_body["query"]["multi_match"]
        assert "title^3" in multi_match["fields"]
        assert "content" in multi_match["fields"]

    @pytest.mark.asyncio
    async def test_fuzziness_setting(self):
        """Test fuzziness is included in query."""
        client = MockAsyncClient(create_mock_es_response([]))

        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["content"],
            fuzziness="AUTO",
        )

        await search.search("test query", max_results=10)

        call_args = client.post.call_args
        query_body = call_args[1]["json"]
        assert query_body["query"]["multi_match"]["fuzziness"] == "AUTO"

    def test_name_property(self):
        """Test name property."""
        client = MockAsyncClient()
        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["content"],
        )
        assert search.name == "bm25"

    def test_get_config(self):
        """Test configuration retrieval."""
        client = MockAsyncClient()
        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["title^3", "content"],
            fuzziness="AUTO",
        )

        config = search.get_config()
        assert config["name"] == "bm25"
        assert config["index"] == "test_index"
        assert config["search_fields"] == ["title^3", "content"]
        assert config["fuzziness"] == "AUTO"


class TestVectorSearch:
    """Tests for VectorSearch method."""

    @pytest.fixture
    def mock_embedding_model(self):
        """Create mock embedding model."""
        model = MagicMock()
        model.encode.return_value = MagicMock(
            tolist=MagicMock(return_value=[0.1] * 384)
        )
        return model

    @pytest.mark.asyncio
    async def test_basic_search(self, mock_embedding_model):
        """Test basic vector search."""
        hits = [
            create_mock_hit("doc1", 0.95, "Title 1", "Content 1"),
            create_mock_hit("doc2", 0.85, "Title 2", "Content 2"),
        ]
        client = MockAsyncClient(create_mock_es_response(hits, total=2))

        search = VectorSearch(
            es_client=client,
            index="test_index",
            vector_field="vector",
            embedding_model=mock_embedding_model,
        )

        results = await search.search("test query", max_results=10)

        assert len(results) == 2
        mock_embedding_model.encode.assert_called_once()

    @pytest.mark.asyncio
    async def test_knn_query_structure(self, mock_embedding_model):
        """Test that KNN query is properly structured."""
        client = MockAsyncClient(create_mock_es_response([]))

        search = VectorSearch(
            es_client=client,
            index="test_index",
            vector_field="embedding",
            embedding_model=mock_embedding_model,
            num_candidates_multiplier=5,
        )

        await search.search("test query", max_results=10)

        call_args = client.post.call_args
        query_body = call_args[1]["json"]

        assert "knn" in query_body
        assert query_body["knn"]["field"] == "embedding"
        assert query_body["knn"]["k"] == 10
        assert query_body["knn"]["num_candidates"] == 50  # 10 * 5

    @pytest.mark.asyncio
    async def test_embedding_failure_returns_empty(self, mock_embedding_model):
        """Test that embedding failure returns empty results."""
        mock_embedding_model.encode.side_effect = Exception("Embedding failed")
        client = MockAsyncClient()

        search = VectorSearch(
            es_client=client,
            index="test_index",
            vector_field="vector",
            embedding_model=mock_embedding_model,
        )

        results = await search.search("test query", max_results=10)

        assert results == []
        client.post.assert_not_called()

    def test_name_property(self, mock_embedding_model):
        """Test name property."""
        client = MockAsyncClient()
        search = VectorSearch(
            es_client=client,
            index="test_index",
            vector_field="vector",
            embedding_model=mock_embedding_model,
        )
        assert search.name == "vector"


class TestHybridSearch:
    """Tests for HybridSearch method."""

    @pytest.fixture
    def mock_embedding_model(self):
        """Create mock embedding model."""
        model = MagicMock()
        model.encode.return_value = MagicMock(
            tolist=MagicMock(return_value=[0.1] * 384)
        )
        return model

    @pytest.mark.asyncio
    async def test_basic_search(self, mock_embedding_model):
        """Test basic hybrid search."""
        hits = [
            create_mock_hit("doc1", 15.0, "Title 1", "Content 1"),
            create_mock_hit("doc2", 12.0, "Title 2", "Content 2"),
        ]
        client = MockAsyncClient(create_mock_es_response(hits, total=2))

        search = HybridSearch(
            es_client=client,
            index="test_index",
            search_fields=["title^3", "content"],
            vector_field="vector",
            embedding_model=mock_embedding_model,
            bm25_weight=0.6,
            vector_weight=0.4,
        )

        results = await search.search("test query", max_results=10)

        assert len(results) == 2
        mock_embedding_model.encode.assert_called_once()

    @pytest.mark.asyncio
    async def test_hybrid_query_structure(self, mock_embedding_model):
        """Test that hybrid query has both BM25 and KNN components."""
        client = MockAsyncClient(create_mock_es_response([]))

        search = HybridSearch(
            es_client=client,
            index="test_index",
            search_fields=["title", "content"],
            vector_field="vector",
            embedding_model=mock_embedding_model,
            bm25_weight=0.6,
            vector_weight=0.4,
        )

        await search.search("test query", max_results=10)

        call_args = client.post.call_args
        query_body = call_args[1]["json"]

        # Should have both query (BM25) and knn components
        assert "query" in query_body
        assert "knn" in query_body
        assert "bool" in query_body["query"]
        assert query_body["query"]["bool"]["should"][0]["multi_match"]["boost"] == 0.6
        assert query_body["knn"]["boost"] == 0.4

    @pytest.mark.asyncio
    async def test_fallback_to_bm25_on_embedding_failure(self, mock_embedding_model):
        """Test fallback to BM25 when embedding fails."""
        mock_embedding_model.encode.side_effect = Exception("Embedding failed")
        hits = [create_mock_hit("doc1", 10.0, "Title 1", "Content 1")]
        client = MockAsyncClient(create_mock_es_response(hits, total=1))

        search = HybridSearch(
            es_client=client,
            index="test_index",
            search_fields=["content"],
            vector_field="vector",
            embedding_model=mock_embedding_model,
            fallback_to_bm25=True,
        )

        results = await search.search("test query", max_results=10)

        # Should still return results via BM25 fallback
        assert len(results) == 1
        client.post.assert_called_once()

        # Verify query is BM25-only (no knn)
        call_args = client.post.call_args
        query_body = call_args[1]["json"]
        assert "knn" not in query_body

    @pytest.mark.asyncio
    async def test_no_fallback_option(self, mock_embedding_model):
        """Test no fallback when disabled."""
        mock_embedding_model.encode.side_effect = Exception("Embedding failed")
        client = MockAsyncClient()

        search = HybridSearch(
            es_client=client,
            index="test_index",
            search_fields=["content"],
            vector_field="vector",
            embedding_model=mock_embedding_model,
            fallback_to_bm25=False,
        )

        results = await search.search("test query", max_results=10)

        assert results == []
        client.post.assert_not_called()

    def test_name_property_with_weights(self, mock_embedding_model):
        """Test name property includes weights."""
        client = MockAsyncClient()
        search = HybridSearch(
            es_client=client,
            index="test_index",
            search_fields=["content"],
            vector_field="vector",
            embedding_model=mock_embedding_model,
            bm25_weight=0.6,
            vector_weight=0.4,
        )
        assert search.name == "hybrid_60_40"

    def test_get_config(self, mock_embedding_model):
        """Test configuration retrieval."""
        client = MockAsyncClient()
        search = HybridSearch(
            es_client=client,
            index="test_index",
            search_fields=["title^3", "content"],
            vector_field="vector",
            embedding_model=mock_embedding_model,
            bm25_weight=0.6,
            vector_weight=0.4,
        )

        config = search.get_config()
        assert config["bm25_weight"] == 0.6
        assert config["vector_weight"] == 0.4
        assert config["vector_field"] == "vector"


class TestSearchMethodRetry:
    """Tests for retry logic in search methods."""

    @pytest.mark.asyncio
    async def test_retry_on_failure(self):
        """Test that search methods retry on failure."""
        client = MockAsyncClient()

        # First call fails, second succeeds
        client.post = AsyncMock(side_effect=[
            httpx.HTTPStatusError("Error", request=MagicMock(), response=MagicMock(status_code=500)),
            client._create_response(),
        ])

        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["content"],
            max_retries=2,
            retry_delay=0.01,
        )

        results = await search.search("test query", max_results=10)

        assert client.post.call_count == 2

    @pytest.mark.asyncio
    async def test_max_retries_exceeded(self):
        """Test that max retries is respected."""
        client = MockAsyncClient()
        client.post = AsyncMock(
            side_effect=httpx.HTTPStatusError("Error", request=MagicMock(), response=MagicMock(status_code=500))
        )

        search = BM25Search(
            es_client=client,
            index="test_index",
            search_fields=["content"],
            max_retries=3,
            retry_delay=0.01,
        )

        results = await search.search("test query", max_results=10)

        assert results == []
        assert client.post.call_count == 3
