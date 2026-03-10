"""
Search method protocol.

Defines the interface that all search methods (BM25, vector, hybrid) must implement.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from deepsearch.models import SearchResult


class SearchMethod(ABC):
    """
    Protocol for search methods (BM25, vector, hybrid).

    Search methods encapsulate the query-building and result-parsing logic
    for different retrieval strategies. They are stateless and can be
    reused across multiple searches.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Method identifier for logging/benchmarking.

        Examples: "bm25", "vector", "hybrid_60_40"
        """
        ...

    @abstractmethod
    async def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> List[SearchResult]:
        """
        Execute search and return ranked results.

        Args:
            query: Preprocessed query string
            max_results: Maximum results to return
            filters: Optional field filters (e.g., {"category": "docs"})
            **kwargs: Additional method-specific parameters

        Returns:
            List of SearchResult ordered by score (descending)
        """
        ...

    def get_config(self) -> Dict[str, Any]:
        """
        Return configuration for logging/reproducibility.

        Override this to expose method-specific settings.
        """
        return {"name": self.name}
