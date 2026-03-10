"""
Elasticsearch Agent

Specialized agent for searching Elasticsearch indices.
"""

from typing import TYPE_CHECKING, Any, Dict, List, Optional

from deepsearch.agents.base import BaseAgent
from deepsearch.agents.reasoning import ReasoningAgentMixin
from deepsearch.models.agent import AgentResult
from deepsearch.observability import get_logger
from deepsearch.tools import BaseTool

from .tools import ElasticsearchSearchTool

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager
    from deepsearch.processors.base import BaseProcessor

logger = get_logger(__name__)


class ElasticsearchAgent(BaseAgent, ReasoningAgentMixin):
    """
    Specialized agent for searching Elasticsearch indices.

    This agent can:
    - Search documents in a specific Elasticsearch index
    - Use iterative reasoning to refine queries
    - Synthesize findings from search results

    Each instance is configured for a specific index, allowing multiple
    agents to search different indices (docs, tickets, etc.).

    Example:
        agent = ElasticsearchAgent(
            llm=llm,
            prompts=prompts,
            es_url="http://localhost:9200",
            index="documentation",
        )
        result = await agent.run("How do I configure authentication?")
    """

    def __init__(
        self,
        llm: "LLMProvider",
        prompts: "PromptManager",
        es_url: str,
        index: str,
        search_fields: Optional[List[str]] = None,
        max_iterations: int = 3,
        api_key: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        source_type: Optional[str] = None,
        # Hybrid search config
        hybrid_enabled: bool = False,
        vector_field: str = "vector",
        vector_weight: float = 0.5,
        bm25_weight: float = 0.5,
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
        # Preprocessors
        preprocessors: Optional[List["BaseProcessor"]] = None,
    ):
        """
        Initialize the Elasticsearch agent.

        Args:
            llm: LLM provider for reasoning
            prompts: PromptManager for agent prompts
            es_url: Elasticsearch URL
            index: Index name to search
            search_fields: Fields to search with optional boosting
            max_iterations: Max reasoning iterations
            api_key: API key for authentication
            username: Basic auth username
            password: Basic auth password
            source_type: Source type for UI mapping (e.g., 'confluence', 'sharepoint')
            hybrid_enabled: Enable hybrid BM25+vector search
            vector_field: Field containing document embeddings
            vector_weight: Weight for vector similarity (0-1)
            bm25_weight: Weight for BM25 keyword score (0-1)
            embedding_model: Sentence transformer model for query embeddings
            preprocessors: Query preprocessors to apply before search
        """
        # Config overrides (set by factory when loading from YAML)
        # Must be set before super().__init__() because base class logs self.name
        self._config_name: Optional[str] = None
        self._config_description: Optional[str] = None

        # Store index early for use in name property
        self.index = index

        # Initialize tool first (before calling super().__init__)
        self._tools = [
            ElasticsearchSearchTool(
                es_url=es_url,
                index=index,
                search_fields=search_fields,
                api_key=api_key,
                username=username,
                password=password,
                source_type=source_type,
                # Hybrid search config
                hybrid_enabled=hybrid_enabled,
                vector_field=vector_field,
                vector_weight=vector_weight,
                bm25_weight=bm25_weight,
                embedding_model=embedding_model,
            ),
        ]

        # Now call parent init with preprocessors
        super().__init__(llm, prompts, max_iterations, preprocessors=preprocessors)

        self.es_url = es_url

        logger.info(
            "elasticsearch_agent_init",
            es_url=es_url,
            index=index,
            search_fields=search_fields,
            max_iterations=max_iterations,
            hybrid_enabled=hybrid_enabled,
            preprocessor_count=len(preprocessors or []),
        )

    @property
    def name(self) -> str:
        return self._config_name or f"elasticsearch_{self.index}"

    @property
    def description(self) -> str:
        if self._config_description:
            return self._config_description
        return (
            f"Searches the {self.index} index in Elasticsearch for relevant documents. "
            f"Best for questions about internal documentation, knowledge base articles, "
            f"or domain-specific content stored in {self.index}."
        )

    @property
    def tools(self) -> List[BaseTool]:
        return self._tools

    @property
    def prompt_category(self) -> str:
        return "elasticsearch_agent"

    async def run(self, task: str, **kwargs) -> AgentResult:
        """
        Execute the Elasticsearch search task.

        The agent will:
        1. Analyze the research task
        2. Formulate search queries
        3. Search the Elasticsearch index
        4. Refine queries if needed
        5. Synthesize findings into an answer

        Args:
            task: The research task delegated by the supervisor
            **kwargs: Additional parameters (e.g., context)

        Returns:
            AgentResult with findings, sources, and confidence
        """
        logger.info(
            "elasticsearch_agent_run",
            index=self.index,
            task=task[:100],
        )

        # Use the reasoning loop mixin
        return await self.reasoning_loop(task, **kwargs)

    async def _execute_tool(
        self,
        tool: Any,
        tool_args: Dict[str, Any],
        task: str,
    ) -> Any:
        """
        Execute a tool with preprocessing and postprocessing applied.

        Overrides ReasoningAgentMixin._execute_tool to apply configured
        preprocessors:
        - Pre-processing: Query reformulation before search
        - Post-processing: Semantic reranking after search

        Args:
            tool: The tool instance to execute
            tool_args: Arguments from the LLM function call
            task: The original task (used as fallback for query)

        Returns:
            ToolResult from tool execution (with reranked sources if configured)
        """
        # Get the query (from args or fall back to task)
        query = tool_args.get("query", task)
        original_query = query

        # Apply preprocessing if configured (query reformulation)
        if self.preprocessors:
            query = await self.preprocess_query(query)
            if query != original_query:
                logger.info(
                    "query_preprocessed",
                    agent=self.name,
                    original=original_query[:100],
                    processed=query[:100],
                )

        # Execute tool with (possibly preprocessed) query
        result = await tool.execute(
            query=query,
            **{k: v for k, v in tool_args.items() if k != "query"},
        )

        # Apply post-processing if configured (semantic reranking)
        if self.preprocessors and result.success and result.data:
            sources = result.data.get("sources", [])
            if sources:
                # Run post-processors (e.g., semantic reranker)
                reranked_sources = await self.postprocess_results(
                    sources, original_query
                )

                if reranked_sources is not sources:
                    logger.info(
                        "results_postprocessed",
                        agent=self.name,
                        original_count=len(sources),
                        reranked_count=len(reranked_sources),
                    )
                    # Update the result with reranked sources
                    result.data["sources"] = reranked_sources
                    # Also update the formatted results to match reranked order
                    result.data["results"] = [
                        {
                            "id": getattr(r, "id", None),
                            "title": r.title,
                            "content": r.content[:2000] if r.content else "",
                            "score": r.score,
                            "url": r.url,
                            "highlight": getattr(r, "highlight", None),
                        }
                        for r in reranked_sources
                    ]

        return result

    async def close(self) -> None:
        """Close Elasticsearch connections."""
        for tool in self._tools:
            if hasattr(tool, "close"):
                await tool.close()
