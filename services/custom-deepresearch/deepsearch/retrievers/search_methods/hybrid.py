"""
Hybrid search method combining BM25 and vector similarity.

Supports two fusion strategies:
1. Score Normalization (default): Runs BM25 and KNN separately, normalizes scores
   to 0-1 range, then combines with weights. More accurate weighting.
2. RRF (Reciprocal Rank Fusion): Uses rank-based fusion (ES 8.10+).

The old boost-based approach is deprecated as it doesn't properly balance
BM25 scores (5-20+) with KNN scores (0-1).
"""

import asyncio
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING

import httpx

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger
from .base import SearchMethod

if TYPE_CHECKING:
    from sentence_transformers import SentenceTransformer

logger = get_logger(__name__)


class HybridSearch(SearchMethod):
    """
    Combined BM25 + vector search with configurable weights.

    Combines the precision of keyword matching with the semantic
    understanding of vector similarity for improved recall.
    """

    def __init__(
        self,
        es_client: httpx.AsyncClient,
        index: str,
        search_fields: List[str],
        vector_field: str,
        embedding_model: "SentenceTransformer",
        bm25_weight: float = 0.6,
        vector_weight: float = 0.4,
        source_fields: Optional[List[str]] = None,
        highlight_fields: Optional[Dict[str, Dict]] = None,
        fuzziness: str = "AUTO",
        num_candidates_multiplier: int = 5,
        id_field: str = "id",
        title_field: str = "title",
        content_field: str = "content",
        url_field: str = "url",
        source_type: Optional[str] = None,
        max_retries: int = 3,
        retry_delay: float = 0.5,
        fallback_to_bm25: bool = True,
        fusion_strategy: str = "score_normalization",
    ):
        """
        Initialize hybrid search method.

        Args:
            es_client: Async HTTP client configured for Elasticsearch
            index: Index name to search
            search_fields: Fields to search with optional boosting
            vector_field: Field containing document embeddings
            embedding_model: SentenceTransformer model for query embedding
            bm25_weight: Weight for BM25 keyword score (0.0 to 1.0)
            vector_weight: Weight for vector similarity score (0.0 to 1.0)
            source_fields: Fields to return in results
            highlight_fields: Fields to highlight
            fuzziness: Elasticsearch fuzziness setting
            num_candidates_multiplier: Multiplier for KNN num_candidates
            id_field: Field containing document ID
            title_field: Field containing title
            content_field: Field containing content
            url_field: Field containing URL
            source_type: Source type identifier for results
            max_retries: Maximum retry attempts
            retry_delay: Base delay between retries
            fallback_to_bm25: Fall back to BM25-only if embedding fails
            fusion_strategy: How to combine BM25 and vector scores:
                - "score_normalization" (default): Normalize scores to 0-1, then combine
                - "rrf": Reciprocal Rank Fusion (rank-based, ES 8.10+)
                - "boost": Legacy boost-based (not recommended, BM25 dominates)
        """
        self._client = es_client
        self._index = index
        self._search_fields = search_fields
        self._vector_field = vector_field
        self._model = embedding_model
        self._bm25_weight = bm25_weight
        self._vector_weight = vector_weight
        self._source_fields = source_fields or ["id", "title", "content", "url"]
        self._highlight_fields = highlight_fields or {
            "content": {"fragment_size": 150, "number_of_fragments": 2}
        }
        self._fuzziness = fuzziness
        self._num_candidates_multiplier = num_candidates_multiplier
        self._id_field = id_field
        self._title_field = title_field
        self._content_field = content_field
        self._url_field = url_field
        self._source_type = source_type or index
        self._max_retries = max_retries
        self._retry_delay = retry_delay
        self._fallback_to_bm25 = fallback_to_bm25
        self._fusion_strategy = fusion_strategy

    @property
    def name(self) -> str:
        bm25_pct = int(self._bm25_weight * 100)
        vector_pct = int(self._vector_weight * 100)
        return f"hybrid_{bm25_pct}_{vector_pct}"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "index": self._index,
            "search_fields": self._search_fields,
            "vector_field": self._vector_field,
            "bm25_weight": self._bm25_weight,
            "vector_weight": self._vector_weight,
            "fuzziness": self._fuzziness,
            "fusion_strategy": self._fusion_strategy,
        }

    def _embed_query(self, query: str) -> Optional[List[float]]:
        """Generate embedding for query."""
        try:
            embedding = self._model.encode(query, normalize_embeddings=True)
            return embedding.tolist()
        except Exception as e:
            logger.error("hybrid_embed_query_failed", error=str(e), query=query[:100])
            return None

    async def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> List[SearchResult]:
        """Execute hybrid BM25 + vector search."""
        query_vector = self._embed_query(query)

        if query_vector is None:
            if self._fallback_to_bm25:
                logger.warning("hybrid_fallback_to_bm25", reason="embedding_failed")
                return await self._search_bm25_only(query, max_results, filters)
            else:
                logger.warning("hybrid_search_skipped", reason="embedding_failed")
                return []

        # Use appropriate fusion strategy
        if self._fusion_strategy == "score_normalization":
            return await self._search_with_score_normalization(
                query, query_vector, max_results, filters
            )
        elif self._fusion_strategy == "rrf":
            return await self._search_with_rrf(
                query, query_vector, max_results, filters
            )
        else:
            # Legacy boost-based approach (not recommended)
            return await self._search_with_boost(
                query, query_vector, max_results, filters
            )

    async def _search_with_score_normalization(
        self,
        query: str,
        query_vector: List[float],
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[SearchResult]:
        """
        Hybrid search with proper score normalization.

        Runs BM25 and KNN separately, normalizes scores to 0-1,
        then combines with configured weights.
        """
        # Fetch more candidates for better fusion
        fetch_count = max(max_results * 3, 30)

        # Run BM25 and KNN searches in parallel
        bm25_task = self._run_bm25_search(query, fetch_count, filters)
        knn_task = self._run_knn_search(query_vector, fetch_count, filters)

        try:
            bm25_response, knn_response = await asyncio.gather(bm25_task, knn_task)
        except Exception as e:
            logger.error("hybrid_parallel_search_failed", error=str(e))
            # Fall back to BM25 only
            return await self._search_bm25_only(query, max_results, filters)

        # Extract scores by doc ID
        bm25_scores: Dict[str, Tuple[float, Dict]] = {}  # doc_id -> (score, hit_data)
        knn_scores: Dict[str, Tuple[float, Dict]] = {}

        for hit in bm25_response.get("hits", {}).get("hits", []):
            doc_id = hit.get("_id")
            bm25_scores[doc_id] = (hit.get("_score", 0.0), hit)

        for hit in knn_response.get("hits", {}).get("hits", []):
            doc_id = hit.get("_id")
            knn_scores[doc_id] = (hit.get("_score", 0.0), hit)

        # Normalize scores to 0-1 range
        bm25_normalized = self._normalize_scores(
            {doc_id: score for doc_id, (score, _) in bm25_scores.items()}
        )
        knn_normalized = self._normalize_scores(
            {doc_id: score for doc_id, (score, _) in knn_scores.items()}
        )

        # Combine scores with weights
        all_doc_ids = set(bm25_scores.keys()) | set(knn_scores.keys())
        combined_scores: Dict[str, Tuple[float, Dict]] = {}

        for doc_id in all_doc_ids:
            bm25_norm = bm25_normalized.get(doc_id, 0.0)
            knn_norm = knn_normalized.get(doc_id, 0.0)

            combined = (
                self._bm25_weight * bm25_norm +
                self._vector_weight * knn_norm
            )

            # Get hit data from whichever search found it
            hit_data = bm25_scores.get(doc_id, (0, None))[1]
            if hit_data is None:
                hit_data = knn_scores.get(doc_id, (0, {}))[1]

            combined_scores[doc_id] = (combined, hit_data)

        # Sort by combined score and take top results
        sorted_results = sorted(
            combined_scores.items(),
            key=lambda x: x[1][0],
            reverse=True
        )[:max_results]

        logger.debug(
            "hybrid_score_normalization_complete",
            bm25_candidates=len(bm25_scores),
            knn_candidates=len(knn_scores),
            combined_candidates=len(all_doc_ids),
            bm25_weight=self._bm25_weight,
            vector_weight=self._vector_weight,
        )

        # Convert to SearchResult objects
        return self._hits_to_results([
            (doc_id, score, hit)
            for doc_id, (score, hit) in sorted_results
        ])

    def _normalize_scores(self, scores: Dict[str, float]) -> Dict[str, float]:
        """Normalize scores to 0-1 range using min-max normalization."""
        if not scores:
            return {}

        values = list(scores.values())
        min_score = min(values)
        max_score = max(values)

        # Avoid division by zero
        score_range = max_score - min_score
        if score_range == 0:
            return {doc_id: 1.0 for doc_id in scores}

        return {
            doc_id: (score - min_score) / score_range
            for doc_id, score in scores.items()
        }

    async def _run_bm25_search(
        self,
        query: str,
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Run BM25-only search."""
        query_body = {
            "size": max_results,
            "_source": self._source_fields,
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": self._search_fields,
                    "type": "best_fields",
                    "fuzziness": self._fuzziness,
                }
            },
        }

        if filters:
            query_body["query"] = {
                "bool": {
                    "must": query_body["query"],
                    "filter": [{"term": {k: v}} for k, v in filters.items()],
                }
            }

        return await self._execute_with_retry(query_body)

    async def _run_knn_search(
        self,
        query_vector: List[float],
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Run KNN-only search."""
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
                    "filter": [{"term": {k: v}} for k, v in filters.items()]
                }
            }

        return await self._execute_with_retry(query_body)

    async def _search_with_rrf(
        self,
        query: str,
        query_vector: List[float],
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[SearchResult]:
        """
        Hybrid search using Reciprocal Rank Fusion (ES 8.10+).

        RRF combines results based on rank position, not raw scores.
        Formula: RRF(d) = sum(1 / (k + rank(d))) for each retriever
        """
        # RRF rank constant (higher = more weight to lower ranks)
        rank_constant = 60

        query_body = {
            "size": max_results,
            "_source": self._source_fields,
            "retriever": {
                "rrf": {
                    "retrievers": [
                        {
                            "standard": {
                                "query": {
                                    "multi_match": {
                                        "query": query,
                                        "fields": self._search_fields,
                                        "type": "best_fields",
                                        "fuzziness": self._fuzziness,
                                    }
                                }
                            }
                        },
                        {
                            "knn": {
                                "field": self._vector_field,
                                "query_vector": query_vector,
                                "k": max_results * 2,
                                "num_candidates": max_results * self._num_candidates_multiplier,
                            }
                        }
                    ],
                    "rank_constant": rank_constant,
                    "rank_window_size": max_results * 3,
                }
            },
        }

        if filters:
            # Add filter to both retrievers
            for retriever in query_body["retriever"]["rrf"]["retrievers"]:
                if "standard" in retriever:
                    retriever["standard"]["query"] = {
                        "bool": {
                            "must": retriever["standard"]["query"],
                            "filter": [{"term": {k: v}} for k, v in filters.items()],
                        }
                    }
                elif "knn" in retriever:
                    retriever["knn"]["filter"] = {
                        "bool": {
                            "filter": [{"term": {k: v}} for k, v in filters.items()]
                        }
                    }

        try:
            response = await self._execute_with_retry(query_body)
            return self._parse_response(response)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 400:
                logger.warning(
                    "rrf_not_supported",
                    message="RRF requires Elasticsearch 8.10+, falling back to score normalization",
                )
                return await self._search_with_score_normalization(
                    query, query_vector, max_results, filters
                )
            raise

    async def _search_with_boost(
        self,
        query: str,
        query_vector: List[float],
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[SearchResult]:
        """
        Legacy boost-based hybrid search (not recommended).

        Warning: BM25 scores (5-20+) will dominate KNN scores (0-1)
        regardless of configured weights.
        """
        logger.warning(
            "using_legacy_boost_fusion",
            message="Boost-based fusion is deprecated, use score_normalization instead",
        )

        es_query = self._build_boost_query(query, query_vector, max_results, filters)

        try:
            response = await self._execute_with_retry(es_query)
            return self._parse_response(response)
        except Exception as e:
            logger.error("hybrid_boost_search_error", error=str(e))
            return []

    def _build_boost_query(
        self,
        query: str,
        query_vector: List[float],
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Build legacy boost-based hybrid query (deprecated)."""
        bm25_clause = {
            "multi_match": {
                "query": query,
                "fields": self._search_fields,
                "type": "best_fields",
                "fuzziness": self._fuzziness,
                "boost": self._bm25_weight,
            }
        }

        query_body = {
            "size": max_results,
            "_source": self._source_fields,
            "query": {
                "bool": {
                    "should": [bm25_clause],
                }
            },
            "knn": {
                "field": self._vector_field,
                "query_vector": query_vector,
                "k": max_results,
                "num_candidates": max_results * self._num_candidates_multiplier,
                "boost": self._vector_weight,
            },
        }

        if filters:
            query_body["query"]["bool"]["filter"] = [
                {"term": {k: v}} for k, v in filters.items()
            ]

        if self._highlight_fields:
            query_body["highlight"] = {
                "fields": self._highlight_fields,
                "pre_tags": ["<em>"],
                "post_tags": ["</em>"],
            }

        return query_body

    async def _search_bm25_only(
        self,
        query: str,
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[SearchResult]:
        """Execute BM25-only search as fallback."""
        es_query = self._build_bm25_only_query(query, max_results, filters)
        try:
            response = await self._execute_with_retry(es_query)
            return self._parse_response(response)
        except Exception as e:
            logger.error("bm25_fallback_search_error", error=str(e))
            return []

    def _hits_to_results(
        self,
        hits: List[Tuple[str, float, Dict]],
    ) -> List[SearchResult]:
        """Convert hit tuples to SearchResult objects."""
        results = []
        for doc_id, score, hit in hits:
            if hit is None:
                continue

            source = hit.get("_source", {})
            highlight = hit.get("highlight", {})

            highlight_text = None
            for field in self._highlight_fields.keys():
                if field in highlight:
                    highlight_text = " ... ".join(highlight[field])
                    break

            results.append(
                SearchResult(
                    id=source.get(self._id_field, doc_id),
                    title=source.get(self._title_field, ""),
                    content=source.get(self._content_field, ""),
                    score=score,
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

    def _build_bm25_only_query(
        self,
        query: str,
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Build BM25-only fallback query."""
        bm25_clause = {
            "multi_match": {
                "query": query,
                "fields": self._search_fields,
                "type": "best_fields",
                "fuzziness": self._fuzziness,
            }
        }

        if filters:
            query_body = {
                "query": {
                    "bool": {
                        "must": bm25_clause,
                        "filter": [{"term": {k: v}} for k, v in filters.items()],
                    }
                }
            }
        else:
            query_body = {"query": bm25_clause}

        query_body["size"] = max_results
        query_body["_source"] = self._source_fields

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
                    "hybrid_search_retry",
                    attempt=attempt + 1,
                    status=e.response.status_code,
                )

            except Exception as e:
                last_error = e
                logger.warning(
                    "hybrid_search_retry",
                    attempt=attempt + 1,
                    error=str(e),
                )

            if attempt < self._max_retries - 1:
                await asyncio.sleep(self._retry_delay * (2**attempt))

        raise last_error or Exception("Hybrid search failed after retries")

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
