"""
Vector similarity search method.

Uses Elasticsearch's KNN search for pure semantic retrieval.
"""

import asyncio
from typing import Any, Dict, List, Optional, TYPE_CHECKING

import httpx

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger
from .base import SearchMethod

if TYPE_CHECKING:
    from sentence_transformers import SentenceTransformer

logger = get_logger(__name__)


class VectorSearch(SearchMethod):
    """
    Pure vector similarity search using Elasticsearch KNN.

    Uses sentence transformers to embed the query and finds similar
    documents based on cosine similarity of embeddings.
    """

    def __init__(
        self,
        es_client: httpx.AsyncClient,
        index: str,
        vector_field: str,
        embedding_model: "SentenceTransformer",
        source_fields: Optional[List[str]] = None,
        highlight_fields: Optional[Dict[str, Dict]] = None,
        num_candidates_multiplier: int = 5,
        id_field: str = "id",
        title_field: str = "title",
        content_field: str = "content",
        url_field: str = "url",
        source_type: Optional[str] = None,
        max_retries: int = 3,
        retry_delay: float = 0.5,
    ):
        """
        Initialize vector search method.

        Args:
            es_client: Async HTTP client configured for Elasticsearch
            index: Index name to search
            vector_field: Field containing document embeddings
            embedding_model: SentenceTransformer model for query embedding
            source_fields: Fields to return in results
            highlight_fields: Fields to highlight with configuration
            num_candidates_multiplier: Multiplier for num_candidates (k * multiplier)
            id_field: Field containing document ID
            title_field: Field containing title
            content_field: Field containing content
            url_field: Field containing URL
            source_type: Source type identifier for results
            max_retries: Maximum retry attempts
            retry_delay: Base delay between retries
        """
        self._client = es_client
        self._index = index
        self._vector_field = vector_field
        self._model = embedding_model
        self._source_fields = source_fields or ["id", "title", "content", "url"]
        self._highlight_fields = highlight_fields or {
            "content": {"fragment_size": 150, "number_of_fragments": 2}
        }
        self._num_candidates_multiplier = num_candidates_multiplier
        self._id_field = id_field
        self._title_field = title_field
        self._content_field = content_field
        self._url_field = url_field
        self._source_type = source_type or index
        self._max_retries = max_retries
        self._retry_delay = retry_delay

    @property
    def name(self) -> str:
        return "vector"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "index": self._index,
            "vector_field": self._vector_field,
            "model": getattr(self._model, "model_card_data", {}).get("model_id", "unknown"),
            "num_candidates_multiplier": self._num_candidates_multiplier,
        }

    def _embed_query(self, query: str) -> Optional[List[float]]:
        """Generate embedding for query."""
        try:
            embedding = self._model.encode(query, normalize_embeddings=True)
            return embedding.tolist()
        except Exception as e:
            logger.error("vector_embed_query_failed", error=str(e), query=query[:100])
            return None

    async def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> List[SearchResult]:
        """Execute vector similarity search."""
        query_vector = self._embed_query(query)
        if query_vector is None:
            logger.warning("vector_search_skipped", reason="embedding_failed")
            return []

        es_query = self._build_query(query_vector, max_results, filters)

        try:
            response = await self._execute_with_retry(es_query)
            return self._parse_response(response)
        except Exception as e:
            logger.error(
                "vector_search_error",
                index=self._index,
                query=query[:100],
                error=str(e),
            )
            return []

    def _build_query(
        self,
        query_vector: List[float],
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Build Elasticsearch KNN query body."""
        query_body = {
            "size": max_results,
            "_source": self._source_fields,
            "knn": {
                "field": self._vector_field,
                "query_vector": query_vector,
                "k": max_results,
                "num_candidates": max_results * self._num_candidates_multiplier,
            },
        }

        if filters:
            query_body["knn"]["filter"] = {
                "bool": {
                    "must": [{"term": {k: v}} for k, v in filters.items()]
                }
            }

        if self._highlight_fields:
            query_body["highlight"] = {
                "fields": self._highlight_fields,
                "pre_tags": ["<em>"],
                "post_tags": ["</em>"],
            }

        return query_body

    async def _execute_with_retry(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Execute query with retry logic."""
        last_error = None

        for attempt in range(self._max_retries):
            try:
                response = await self._client.post(
                    f"/{self._index}/_search",
                    json=query,
                )
                response.raise_for_status()
                return response.json()

            except httpx.HTTPStatusError as e:
                last_error = e
                logger.warning(
                    "vector_search_retry",
                    attempt=attempt + 1,
                    status=e.response.status_code,
                )

            except Exception as e:
                last_error = e
                logger.warning(
                    "vector_search_retry",
                    attempt=attempt + 1,
                    error=str(e),
                )

            if attempt < self._max_retries - 1:
                await asyncio.sleep(self._retry_delay * (2**attempt))

        raise last_error or Exception("Vector search failed after retries")

    def _parse_response(self, response: Dict[str, Any]) -> List[SearchResult]:
        """Parse Elasticsearch response into SearchResult objects."""
        results = []
        hits = response.get("hits", {}).get("hits", [])

        for hit in hits:
            source = hit.get("_source", {})
            highlight = hit.get("highlight", {})

            highlight_text = None
            for field in self._highlight_fields.keys():
                if field in highlight:
                    highlight_text = " ... ".join(highlight[field])
                    break

            results.append(
                SearchResult(
                    id=source.get(self._id_field, hit.get("_id", "")),
                    title=source.get(self._title_field, ""),
                    content=source.get(self._content_field, ""),
                    score=hit.get("_score", 0.0),
                    source_type=self._source_type,
                    url=source.get(self._url_field),
                    highlight=highlight_text,
                    metadata={
                        k: v
                        for k, v in source.items()
                        if k not in [
                            self._id_field,
                            self._title_field,
                            self._content_field,
                            self._url_field,
                        ]
                    },
                )
            )

        return results
