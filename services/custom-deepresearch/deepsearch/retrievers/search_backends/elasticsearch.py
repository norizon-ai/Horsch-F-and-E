"""
Elasticsearch Search Backend

Implements the SearchBackend interface for Elasticsearch.
Configuration is per-instance, not global.
"""

import asyncio
from typing import Any, Dict, List, Optional

import httpx
from pydantic import Field

from deepsearch.models import SearchResult, SearchResponse
from deepsearch.observability import get_logger
from .base import SearchBackend, SearchBackendConfig

logger = get_logger(__name__)


class ElasticsearchConfig(SearchBackendConfig):
    """Configuration for Elasticsearch backend."""

    url: str = Field(..., description="Elasticsearch URL")
    index: str = Field(..., description="Index name to search")
    username: Optional[str] = Field(default=None, description="Basic auth username")
    password: Optional[str] = Field(default=None, description="Basic auth password")
    source_type: Optional[str] = Field(
        default=None,
        description="Source type for UI mapping (e.g., 'confluence', 'sharepoint'). Defaults to index name if not set."
    )

    # Search configuration
    search_fields: List[str] = Field(
        default=["title^3", "content"],
        description="Fields to search with optional boosting",
    )
    source_fields: List[str] = Field(
        default=["id", "title", "content", "url"],
        description="Fields to return in results",
    )
    highlight_fields: Dict[str, Dict[str, Any]] = Field(
        default_factory=lambda: {
            "content": {"fragment_size": 150, "number_of_fragments": 2}
        },
        description="Fields to highlight in results",
    )

    # Result mapping - how to extract fields from ES response
    id_field: str = Field(default="id", description="Field containing document ID")
    title_field: str = Field(default="title", description="Field containing title")
    content_field: str = Field(
        default="content", description="Field containing content"
    )
    url_field: str = Field(default="url", description="Field containing URL")

    # Hybrid search configuration (per-agent)
    hybrid_enabled: bool = Field(
        default=False, description="Enable hybrid BM25+vector search"
    )
    vector_field: str = Field(
        default="vector", description="Field containing document embeddings"
    )
    vector_weight: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Weight for vector similarity score"
    )
    bm25_weight: float = Field(
        default=0.5, ge=0.0, le=1.0, description="Weight for BM25 keyword score"
    )
    embedding_model: str = Field(
        default="sentence-transformers/all-MiniLM-L6-v2",
        description="Sentence transformer model for query embeddings",
    )


class ElasticsearchBackend(SearchBackend):
    """
    Elasticsearch search backend implementation.

    Each retriever can have its own ElasticsearchBackend instance
    with its own configuration (index, fields, etc.).

    Supports hybrid search (BM25 + vector KNN) when hybrid_enabled=True.
    Each backend instance has its own embedding model for query vectorization.
    """

    def __init__(self, config: ElasticsearchConfig):
        """
        Initialize Elasticsearch backend.

        Args:
            config: Elasticsearch configuration
        """
        super().__init__(config)
        self.es_config = config
        self._client: Optional[httpx.AsyncClient] = None
        self._embedding_model = None  # Lazy-loaded

    @property
    def embedding_model(self):
        """
        Lazy-load embedding model only when hybrid search is enabled.

        Returns:
            SentenceTransformer model or None if hybrid disabled
        """
        if self._embedding_model is None and self.es_config.hybrid_enabled:
            try:
                from sentence_transformers import SentenceTransformer

                logger.info(
                    "loading_embedding_model",
                    model=self.es_config.embedding_model,
                    index=self.es_config.index,
                )
                self._embedding_model = SentenceTransformer(
                    self.es_config.embedding_model
                )
            except ImportError:
                logger.error(
                    "sentence_transformers_not_installed",
                    message="Install with: pip install sentence-transformers",
                )
            except Exception as e:
                logger.error("embedding_model_load_failed", error=str(e))
        return self._embedding_model

    def embed_query(self, query: str) -> Optional[List[float]]:
        """
        Generate embedding for query using this backend's configured model.

        Args:
            query: Search query text

        Returns:
            List of floats (embedding vector) or None if hybrid disabled/failed
        """
        if not self.embedding_model:
            return None
        try:
            embedding = self.embedding_model.encode(query, normalize_embeddings=True)
            return embedding.tolist()
        except Exception as e:
            logger.error("embed_query_failed", error=str(e), query=query[:100])
            return None

    @property
    def backend_name(self) -> str:
        return "elasticsearch"

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create HTTP client."""
        if self._client is None:
            auth = None
            if self.es_config.username and self.es_config.password:
                auth = httpx.BasicAuth(self.es_config.username, self.es_config.password)

            self._client = httpx.AsyncClient(
                base_url=self.es_config.url,
                auth=auth,
                timeout=httpx.Timeout(self.config.timeout),
            )
        return self._client

    async def close(self) -> None:
        """Close HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> SearchResponse:
        """
        Execute search against Elasticsearch.

        Args:
            query: Search query
            max_results: Maximum results
            filters: Optional ES filters
            **kwargs: Additional options

        Returns:
            SearchResponse with results
        """
        import time

        start_time = time.time()

        # Build ES query (includes KNN if hybrid enabled)
        es_query = self._build_query(query, max_results=max_results, filters=filters)
        es_query["size"] = max_results
        es_query["_source"] = self.es_config.source_fields

        # Add highlighting
        if self.es_config.highlight_fields:
            es_query["highlight"] = {
                "fields": self.es_config.highlight_fields,
                "pre_tags": ["<em>"],
                "post_tags": ["</em>"],
            }

        # Execute with retry
        try:
            response_data = await self._execute_with_retry(es_query)
            results = self._parse_response(response_data)
            total = response_data.get("hits", {}).get("total", {})
            total_found = total.get("value", 0) if isinstance(total, dict) else total

            search_time = (time.time() - start_time) * 1000

            logger.debug(
                "elasticsearch_search",
                index=self.es_config.index,
                query=query[:100],
                result_count=len(results),
                total_found=total_found,
                search_time_ms=search_time,
            )

            return SearchResponse(
                results=results,
                total_found=total_found,
                query=query,
                search_time_ms=search_time,
            )

        except Exception as e:
            logger.error(
                "elasticsearch_search_error",
                index=self.es_config.index,
                error=str(e),
            )
            return SearchResponse(
                results=[],
                total_found=0,
                query=query,
                error=str(e),
            )

    def _build_query(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Build Elasticsearch query body.

        Supports hybrid search (BM25 + KNN) when hybrid_enabled=True.
        Falls back to BM25-only if embedding generation fails.

        Args:
            query: Search query text
            max_results: Maximum results to return
            filters: Optional term filters

        Returns:
            Elasticsearch query body dict
        """
        # BM25 component
        bm25_clause = {
            "multi_match": {
                "query": query,
                "fields": self.es_config.search_fields,
                "type": "best_fields",
                "fuzziness": "AUTO",
            }
        }

        # Add boost if hybrid enabled (scores will be combined)
        if self.es_config.hybrid_enabled:
            bm25_clause["multi_match"]["boost"] = self.es_config.bm25_weight

        # Build filter clause if provided
        filter_clause = (
            [{"term": {k: v}} for k, v in filters.items()] if filters else None
        )

        # BM25-only query (default or hybrid disabled)
        if not self.es_config.hybrid_enabled:
            if filter_clause:
                return {
                    "query": {
                        "bool": {
                            "must": bm25_clause,
                            "filter": filter_clause,
                        }
                    }
                }
            return {"query": bm25_clause}

        # Hybrid search: Generate query embedding
        query_vector = self.embed_query(query)

        # Fallback to BM25 if embedding fails
        if query_vector is None:
            logger.warning(
                "hybrid_fallback_to_bm25",
                reason="embedding_failed",
                index=self.es_config.index,
            )
            if filter_clause:
                return {
                    "query": {
                        "bool": {
                            "must": bm25_clause,
                            "filter": filter_clause,
                        }
                    }
                }
            return {"query": bm25_clause}

        # Build hybrid query (BM25 + KNN)
        es_query = {
            "query": {
                "bool": {
                    "should": [bm25_clause],
                }
            },
            "knn": {
                "field": self.es_config.vector_field,
                "query_vector": query_vector,
                "k": max_results,
                "num_candidates": max_results * 5,
                "boost": self.es_config.vector_weight,
            },
        }

        # Add filters to bool clause
        if filter_clause:
            es_query["query"]["bool"]["filter"] = filter_clause

        logger.debug(
            "hybrid_query_built",
            index=self.es_config.index,
            bm25_weight=self.es_config.bm25_weight,
            vector_weight=self.es_config.vector_weight,
            vector_dims=len(query_vector),
        )

        return es_query

    async def _execute_with_retry(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Execute query with retry logic."""
        client = await self._get_client()
        last_error = None

        for attempt in range(self.config.max_retries):
            try:
                response = await client.post(
                    f"/{self.es_config.index}/_search",
                    json=query,
                )
                response.raise_for_status()
                return response.json()

            except httpx.HTTPStatusError as e:
                last_error = e
                logger.warning(
                    "elasticsearch_retry",
                    attempt=attempt + 1,
                    status=e.response.status_code,
                )

            except Exception as e:
                last_error = e
                logger.warning(
                    "elasticsearch_retry",
                    attempt=attempt + 1,
                    error=str(e),
                )

            if attempt < self.config.max_retries - 1:
                await asyncio.sleep(self.config.retry_delay * (2**attempt))

        raise last_error or Exception("Search failed after retries")

    def _parse_response(self, response: Dict[str, Any]) -> List[SearchResult]:
        """Parse Elasticsearch response into SearchResult objects."""
        results = []
        hits = response.get("hits", {}).get("hits", [])

        for hit in hits:
            source = hit.get("_source", {})
            highlight = hit.get("highlight", {})

            # Get highlight text if available
            highlight_text = None
            for field in self.es_config.highlight_fields.keys():
                if field in highlight:
                    highlight_text = " ... ".join(highlight[field])
                    break

            results.append(
                SearchResult(
                    id=source.get(self.es_config.id_field, hit.get("_id", "")),
                    title=source.get(self.es_config.title_field, ""),
                    content=source.get(self.es_config.content_field, ""),
                    score=hit.get("_score", 0.0),
                    source_type=self.es_config.source_type or self.es_config.index,
                    url=source.get(self.es_config.url_field),
                    highlight=highlight_text,
                    metadata={
                        k: v
                        for k, v in source.items()
                        if k
                        not in [
                            self.es_config.id_field,
                            self.es_config.title_field,
                            self.es_config.content_field,
                            self.es_config.url_field,
                        ]
                    },
                )
            )

        return results

    async def health_check(self) -> bool:
        """Check Elasticsearch connectivity."""
        try:
            client = await self._get_client()
            response = await client.get("/_cluster/health")
            return response.status_code == 200
        except Exception as e:
            logger.warning("elasticsearch_health_check_failed", error=str(e))
            return False
