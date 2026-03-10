"""
Preprocessor and ResultTransform protocols.

Defines interfaces for:
- Preprocessor: Synchronous query transformations (non-LLM)
- ResultTransform: Async result post-processing (can use LLM/models)
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from deepsearch.models import SearchResult


class Preprocessor(ABC):
    """
    Protocol for query preprocessors (non-LLM).

    Preprocessors are simple, synchronous transformations applied
    to queries before search. They must not make API calls or
    use LLMs - for that, use deepsearch.processors.

    Design principles:
    - Synchronous (no async/await)
    - Deterministic (same input = same output)
    - Fast (no I/O or heavy computation)
    - Composable (can be chained)
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Preprocessor identifier for logging/benchmarking.

        Examples: "stopwords", "stem_english", "keywords_8"
        """
        ...

    @abstractmethod
    def process(self, query: str) -> str:
        """
        Transform query. Must be synchronous (no LLM calls).

        Args:
            query: Input query string

        Returns:
            Processed query string (never empty - return original if processing fails)
        """
        ...

    def get_config(self) -> Dict[str, Any]:
        """
        Return configuration for logging/reproducibility.

        Override this to expose preprocessor-specific settings.
        """
        return {"name": self.name}


class ResultTransform(ABC):
    """
    Protocol for result post-processors (reranking, filtering, etc.).

    Unlike Preprocessor (sync, query-only), ResultTransform:
    - Is async (can make API calls, use LLMs/models)
    - Operates on results after search
    - Can be composed in a SearchPipeline

    Design principles:
    - Async (can do I/O, model inference)
    - Receives both results and original query
    - Composable (can be chained as postprocessors)

    Example:
        class MyReranker(ResultTransform):
            @property
            def name(self) -> str:
                return "my_reranker"

            async def process(
                self,
                results: List[SearchResult],
                query: str,
            ) -> List[SearchResult]:
                # Rerank results using a model
                return reranked_results
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Transform identifier for logging/benchmarking.

        Examples: "semantic_reranker", "score_filter", "dedup"
        """
        ...

    @abstractmethod
    async def process(
        self,
        results: List["SearchResult"],
        query: str,
    ) -> List["SearchResult"]:
        """
        Transform search results.

        Args:
            results: Search results from the search method
            query: Original query string (before preprocessing)

        Returns:
            Transformed results (reranked, filtered, etc.)
        """
        ...

    def get_config(self) -> Dict[str, Any]:
        """
        Return configuration for logging/reproducibility.

        Override this to expose transform-specific settings.
        """
        return {"name": self.name}
