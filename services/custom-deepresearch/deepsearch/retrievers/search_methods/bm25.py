"""
BM25 keyword search method.

Uses Elasticsearch's multi_match query with BM25 scoring.
"""

import asyncio
from typing import Any, Dict, List, Optional

import httpx

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger
from .base import SearchMethod

logger = get_logger(__name__)


class BM25Search(SearchMethod):
    """
    BM25 keyword search using Elasticsearch.

    Uses multi_match query across configurable fields with optional
    field boosting and fuzziness.
    """

    def __init__(
        self,
        es_client: httpx.AsyncClient,
        index: str,
        search_fields: List[str],
        source_fields: Optional[List[str]] = None,
        highlight_fields: Optional[Dict[str, Dict]] = None,
        fuzziness: str = "AUTO",
        id_field: str = "id",
        title_field: str = "title",
        content_field: str = "content",
        url_field: str = "url",
        source_type: Optional[str] = None,
        max_retries: int = 3,
        retry_delay: float = 0.5,
    ):
        """
        Initialize BM25 search method.

        Args:
            es_client: Async HTTP client configured for Elasticsearch
            index: Index name to search
            search_fields: Fields to search with optional boosting (e.g., ["title^3", "content"])
            source_fields: Fields to return in results
            highlight_fields: Fields to highlight with configuration
            fuzziness: Elasticsearch fuzziness setting ("AUTO", "0", "1", "2")
            id_field: Field containing document ID
            title_field: Field containing title
            content_field: Field containing content
            url_field: Field containing URL
            source_type: Source type identifier for results
            max_retries: Maximum retry attempts
            retry_delay: Base delay between retries (exponential backoff)
        """
        self._client = es_client
        self._index = index
        self._search_fields = search_fields
        self._source_fields = source_fields or ["id", "title", "content", "url"]
        self._highlight_fields = highlight_fields or {
            "content": {"fragment_size": 150, "number_of_fragments": 2}
        }
        self._fuzziness = fuzziness
        self._id_field = id_field
        self._title_field = title_field
        self._content_field = content_field
        self._url_field = url_field
        self._source_type = source_type or index
        self._max_retries = max_retries
        self._retry_delay = retry_delay

    @property
    def name(self) -> str:
        return "bm25"

    def get_config(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "index": self._index,
            "search_fields": self._search_fields,
            "fuzziness": self._fuzziness,
        }

    async def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> List[SearchResult]:
        """Execute BM25 search."""
        es_query = self._build_query(query, max_results, filters)

        try:
            response = await self._execute_with_retry(es_query)
            return self._parse_response(response)
        except Exception as e:
            logger.error(
                "bm25_search_error",
                index=self._index,
                query=query[:100],
                error=str(e),
            )
            return []

    def _build_query(
        self,
        query: str,
        max_results: int,
        filters: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Build Elasticsearch query body with document code boosting."""
        import re

        # Extract document codes for exact matching (German technical docs)
        doc_code_patterns = [
            r'\b(AWA-?\d{3})\b',           # Work instructions: AWA-201
            r'\b(PRJ-?\d{3,4})\b',          # Project codes: PRJ-001
            r'\b(QMH-?\d{3})\b',            # Quality management: QMH-001
            r'\b(ISO\s?\d{4,5}(?:-\d+)?)\b', # Standards: ISO 12100, ISO 13849-1
            r'\b(DIN\s?(?:EN\s?)?\d{4,5})\b', # DIN standards: DIN 15018, DIN EN 60204
            r'\b(EN\s?\d{4,5})\b',          # EN standards: EN 60204
        ]

        doc_codes = []
        for pattern in doc_code_patterns:
            matches = re.findall(pattern, query, re.IGNORECASE)
            doc_codes.extend(matches)

        bm25_clause = {
            "multi_match": {
                "query": query,
                "fields": self._search_fields,
                "type": "best_fields",
                "fuzziness": self._fuzziness,
            }
        }

        filter_clause = (
            [{"term": {k: v}} for k, v in filters.items()] if filters else None
        )

        # Build query with optional document code boosting
        if doc_codes:
            # Add should clauses for exact doc code matches
            should_clauses = []
            for code in doc_codes:
                should_clauses.extend([
                    {"match_phrase": {self._title_field: {"query": code, "boost": 5.0}}},
                    {"match_phrase": {self._content_field: {"query": code, "boost": 3.0}}},
                ])

            if filter_clause:
                query_body = {
                    "query": {
                        "bool": {
                            "must": bm25_clause,
                            "should": should_clauses,
                            "minimum_should_match": 0,
                            "filter": filter_clause,
                        }
                    }
                }
            else:
                query_body = {
                    "query": {
                        "bool": {
                            "must": bm25_clause,
                            "should": should_clauses,
                            "minimum_should_match": 0,
                        }
                    }
                }

            logger.debug(
                "bm25_doc_code_boost",
                codes=doc_codes,
                query=query[:50],
            )
        elif filter_clause:
            query_body = {
                "query": {
                    "bool": {
                        "must": bm25_clause,
                        "filter": filter_clause,
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
                    "bm25_search_retry",
                    attempt=attempt + 1,
                    status=e.response.status_code,
                )

            except Exception as e:
                last_error = e
                logger.warning(
                    "bm25_search_retry",
                    attempt=attempt + 1,
                    error=str(e),
                )

            if attempt < self._max_retries - 1:
                await asyncio.sleep(self._retry_delay * (2**attempt))

        raise last_error or Exception("BM25 search failed after retries")

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
