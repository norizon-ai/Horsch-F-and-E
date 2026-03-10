"""
Base Retriever

Retrievers are tools that perform search/retrieval operations.
They extend BaseTool and support injectable processors.
"""

from typing import Any, Dict, List, Optional, TYPE_CHECKING

from deepsearch.tools import BaseTool, ToolParameter
from deepsearch.models import ToolResult, SearchResult, searchAnswer, searchType
from deepsearch.processors import BaseProcessor, ProcessorChain
from deepsearch.observability import get_logger

if TYPE_CHECKING:
    from deepsearch.retrievers.search_backends import SearchBackend
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

logger = get_logger(__name__)


class BaseRetriever(BaseTool):
    """
    Base class for retriever tools.

    Retrievers extend BaseTool with:
    - Search backend integration
    - Processor injection (pre/post-processing)
    - Answer generation from sources

    Example:
        class DocsRetriever(BaseRetriever):
            @property
            def name(self) -> str:
                return "docs_retriever"

            @property
            def description(self) -> str:
                return "Search documentation for answers"

            @property
            def search_type(self) -> searchType:
                return searchType.DOCS_ONLY
    """

    def __init__(
        self,
        search_backend: "SearchBackend",
        llm: Optional["LLMProvider"] = None,
        prompts: Optional["PromptManager"] = None,
        processors: Optional[List[BaseProcessor]] = None,
        max_results: int = 10,
        generate_answer: bool = True,
    ):
        """
        Initialize the retriever.

        Args:
            search_backend: The search backend to use.
            llm: Optional LLM provider for answer generation.
            prompts: Optional prompt manager for answer prompts.
            processors: Optional list of processors to inject.
            max_results: Default maximum number of results.
            generate_answer: Whether to generate answers from sources.
        """
        self.search_backend = search_backend
        self.llm = llm
        self.prompts = prompts
        self.max_results = max_results
        self.generate_answer = generate_answer and llm is not None

        self.processors = ProcessorChain(processors) if processors else None

        logger.info(
            "retriever_init",
            retriever=self.name,
            backend=search_backend.backend_name,
            processor_count=len(processors) if processors else 0,
            generate_answer=self.generate_answer,
        )

    @property
    def search_type(self) -> searchType:
        """The type of search this retriever performs."""
        return searchType.CUSTOM

    @property
    def parameters(self) -> List[ToolParameter]:
        """Parameters accepted by this retriever."""
        return [
            ToolParameter(
                name="query",
                type="string",
                description="Search query",
                required=True,
            ),
            ToolParameter(
                name="max_results",
                type="integer",
                description="Maximum number of results",
                required=False,
                default=self.max_results,
            ),
        ]

    async def execute(
        self,
        query: str,
        max_results: Optional[int] = None,
        **kwargs,
    ) -> ToolResult:
        """
        Execute a search and optionally generate an answer.

        Args:
            query: The search query.
            max_results: Override for maximum results.
            **kwargs: Additional keyword arguments.

        Returns:
            ToolResult containing the answer and sources.
        """
        import time

        start_time = time.time()
        context = {"original_query": query}

        try:
            # Pre-process query
            processed_query = query
            if self.processors:
                processed_query = await self.processors.pre_process(query, context)
                logger.debug(
                    "query_preprocessed",
                    original=query[:100],
                    processed=processed_query[:100],
                )

            # Search
            search_response = await self.search_backend.search(
                query=processed_query,
                max_results=max_results or self.max_results,
            )

            if not search_response.success:
                return ToolResult.fail(
                    error=search_response.error or "Search failed",
                    tool_name=self.name,
                )

            # Get results
            results = search_response.results

            # Post-process results
            if self.processors:
                results = await self.processors.post_process(results, query, context)

            # Generate answer if configured
            if self.generate_answer and results:
                answer = await self._generate_answer(query, results)
            else:
                answer = searchAnswer(
                    search_type=self.search_type,
                    answer="",
                    confidence=0.0,
                    sources=results,
                    retriever_name=self.name,
                )

            duration = (time.time() - start_time) * 1000
            logger.info(
                "retriever_execute",
                retriever=self.name,
                query=query[:100],
                result_count=len(results),
                duration_ms=duration,
                confidence=answer.confidence,
            )

            return ToolResult.ok(data=answer, tool_name=self.name)

        except Exception as e:
            logger.error(
                "retriever_error",
                retriever=self.name,
                error=str(e),
            )
            return ToolResult.fail(error=str(e), tool_name=self.name)

    async def _generate_answer(
        self,
        query: str,
        sources: List[SearchResult],
    ) -> searchAnswer:
        """Generate an answer from the search results using the LLM."""
        from deepsearch.llm import LLMMessage

        if not self.llm or not self.prompts:
            return searchAnswer(
                search_type=self.search_type,
                answer="",
                confidence=0.0,
                sources=sources,
                retriever_name=self.name,
            )

        sources_text = self._format_sources(sources)

        try:
            prompt = self.prompts.get_prompt(
                "retriever",
                "generate_answer",
                query=query,
                sources=sources_text,
                retriever_name=self.name,
            )

            response = await self.llm.complete(
                messages=[LLMMessage.user(prompt)],
                temperature=0.2,
                max_tokens=1500,
            )

            confidence = self._estimate_confidence(query, response.content, sources)

            return searchAnswer(
                search_type=self.search_type,
                answer=response.content,
                confidence=confidence,
                sources=sources,
                retriever_name=self.name,
            )

        except Exception as e:
            logger.error("answer_generation_failed", error=str(e))
            return searchAnswer(
                search_type=self.search_type,
                answer=f"Error generating answer: {e}",
                confidence=0.0,
                sources=sources,
                retriever_name=self.name,
            )

    def _format_sources(self, sources: List[SearchResult]) -> str:
        """Format sources for inclusion in the answer generation prompt."""
        formatted = []
        for i, source in enumerate(sources[:8], 1):
            content = source.content[:500] if source.content else ""
            formatted.append(f"[{i}] {source.title}\n{content}")
        return "\n\n".join(formatted)

    def _estimate_confidence(
        self,
        query: str,
        answer: str,
        sources: List[SearchResult],
    ) -> float:
        """Estimate confidence score based on sources and answer quality."""
        if not sources:
            return 0.2

        # Base confidence from number of sources
        base_confidence = min(0.4 + len(sources) * 0.05, 0.7)

        # Boost if top source has high score
        if sources and sources[0].score > 10:
            base_confidence += 0.1

        # Check for uncertainty markers in the answer
        uncertainty_markers = [
            "i'm not sure",
            "might",
            "possibly",
            "unclear",
            "may not",
            "cannot determine",
            "not enough information",
        ]

        answer_lower = answer.lower()
        for marker in uncertainty_markers:
            if marker in answer_lower:
                base_confidence -= 0.1
                break

        return max(0.1, min(0.95, base_confidence))

    async def close(self) -> None:
        """Close the search backend."""
        await self.search_backend.close()
