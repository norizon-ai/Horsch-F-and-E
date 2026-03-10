"""
Base Processor Interface

Processors are injectable components that can pre-process queries
and post-process results in retrievers.
"""

from abc import ABC
from typing import Any, List, Optional

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger

logger = get_logger(__name__)


class BaseProcessor(ABC):
    """
    Base class for processors that can be injected into retrievers.

    Processors can hook into the retrieval pipeline at two points:
    - pre_process: Before the search (modify query)
    - post_process: After the search (modify results)

    Not all methods need to be implemented - the default implementations
    pass through unchanged.

    Example:
        class MyProcessor(BaseProcessor):
            async def pre_process(self, query: str, context: dict) -> str:
                # Modify query before search
                return query.upper()

            async def post_process(
                self, results: List[SearchResult], query: str, context: dict
            ) -> List[SearchResult]:
                # Modify results after search
                return results[:5]  # Limit to 5
    """

    @property
    def name(self) -> str:
        """Name of this processor, defaults to class name."""
        return self.__class__.__name__

    async def pre_process(
        self,
        query: str,
        context: Optional[dict] = None,
    ) -> str:
        """
        Pre-process a query before search.

        Args:
            query: The search query.
            context: Optional context dictionary.

        Returns:
            The (possibly modified) query string.
        """
        return query

    async def post_process(
        self,
        results: List[SearchResult],
        original_query: str,
        context: Optional[dict] = None,
    ) -> List[SearchResult]:
        """
        Post-process search results.

        Args:
            results: The search results to process.
            original_query: The original search query.
            context: Optional context dictionary.

        Returns:
            The (possibly modified) list of search results.
        """
        return results

    async def process_query(
        self,
        query: str,
        context: Optional[dict] = None,
    ) -> str:
        """Convenience method that delegates to pre_process."""
        return await self.pre_process(query, context)

    async def process_results(
        self,
        results: List[SearchResult],
        original_query: str,
        context: Optional[dict] = None,
    ) -> List[SearchResult]:
        """Convenience method that delegates to post_process."""
        return await self.post_process(results, original_query, context)


class ProcessorChain:
    """
    Chain multiple processors together.

    Processors are executed in order for both pre_process and post_process.
    """

    def __init__(self, processors: List[BaseProcessor]):
        """
        Initialize the processor chain.

        Args:
            processors: Ordered list of processors to execute.
        """
        self.processors = processors

    async def pre_process(
        self,
        query: str,
        context: Optional[dict] = None,
    ) -> str:
        """Run all processors' pre_process in order."""
        ctx = context or {}
        result = query

        for processor in self.processors:
            logger.debug("processor_pre_process", processor=processor.name)
            result = await processor.pre_process(result, ctx)

        return result

    async def post_process(
        self,
        results: List[SearchResult],
        original_query: str,
        context: Optional[dict] = None,
    ) -> List[SearchResult]:
        """Run all processors' post_process in order."""
        ctx = context or {}
        current_results = results

        for processor in self.processors:
            logger.debug(
                "processor_post_process",
                processor=processor.name,
                result_count=len(current_results),
            )
            current_results = await processor.post_process(
                current_results, original_query, ctx
            )

        return current_results
