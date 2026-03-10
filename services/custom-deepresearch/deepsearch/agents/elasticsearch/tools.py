"""
Elasticsearch Search Tool

Tool wrapper around SearchPipeline for agent use.
Supports both legacy ElasticsearchBackend and new SearchPipeline interfaces.
"""

from typing import Any, Dict, List, Optional, TYPE_CHECKING

from deepsearch.models import SearchResult, ToolResult
from deepsearch.observability import get_logger, TracingContext, SpanKind, add_span_event
from deepsearch.retrievers.search_backends.elasticsearch import (
    ElasticsearchBackend,
    ElasticsearchConfig,
)
from deepsearch.tools import BaseTool
from deepsearch.tools.base import ToolParameter

if TYPE_CHECKING:
    from deepsearch.retrievers import SearchPipeline

logger = get_logger(__name__)


class ElasticsearchSearchTool(BaseTool):
    """
    Tool for searching Elasticsearch indices.

    Can be initialized with either:
    - Legacy: ElasticsearchBackend configuration parameters
    - New: SearchPipeline instance (recommended for benchmarked configurations)

    The SearchPipeline approach is preferred as it uses the same code path
    as BEIR benchmarks, ensuring consistent behavior.
    """

    def __init__(
        self,
        es_url: Optional[str] = None,
        index: Optional[str] = None,
        search_fields: Optional[List[str]] = None,
        api_key: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        timeout: float = 30.0,
        max_results: int = 10,
        source_type: Optional[str] = None,
        # Hybrid search config
        hybrid_enabled: bool = False,
        vector_field: str = "vector",
        vector_weight: float = 0.5,
        bm25_weight: float = 0.5,
        embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
        # New: SearchPipeline support
        pipeline: Optional["SearchPipeline"] = None,
    ):
        """
        Initialize Elasticsearch search tool.

        Args:
            es_url: Elasticsearch URL (legacy mode)
            index: Index name to search
            search_fields: Fields to search with optional boosting
            api_key: API key for authentication (not yet supported, use username/password)
            username: Basic auth username
            password: Basic auth password
            timeout: Request timeout in seconds
            max_results: Default max results per search
            source_type: Source type for UI mapping (e.g., 'confluence', 'sharepoint')
            hybrid_enabled: Enable hybrid BM25+vector search
            vector_field: Field containing document embeddings
            vector_weight: Weight for vector similarity (0-1)
            bm25_weight: Weight for BM25 keyword score (0-1)
            embedding_model: Sentence transformer model for query embeddings
            pipeline: SearchPipeline instance (new mode, preferred)
        """
        self.index = index or "unknown"
        self.max_results = max_results
        self._pipeline = pipeline
        self._backend: Optional[ElasticsearchBackend] = None

        if pipeline is not None:
            # New mode: use SearchPipeline
            logger.info(
                "elasticsearch_tool_init_pipeline",
                pipeline_name=pipeline.name,
                index=index,
            )
        elif es_url is not None:
            # Legacy mode: create backend from parameters
            config = ElasticsearchConfig(
                url=es_url,
                index=index or "documents",
                search_fields=search_fields or ["title^3", "content"],
                username=username,
                password=password,
                timeout=timeout,
                source_type=source_type,
                # Hybrid search settings
                hybrid_enabled=hybrid_enabled,
                vector_field=vector_field,
                vector_weight=vector_weight,
                bm25_weight=bm25_weight,
                embedding_model=embedding_model,
            )

            self._backend = ElasticsearchBackend(config)

            logger.info(
                "elasticsearch_tool_init",
                url=es_url,
                index=index,
                search_fields=search_fields,
                hybrid_enabled=hybrid_enabled,
            )
        else:
            raise ValueError("Either 'pipeline' or 'es_url' must be provided")

    @property
    def name(self) -> str:
        return f"search_{self.index}"

    @property
    def description(self) -> str:
        return f"Search the {self.index} index in Elasticsearch for relevant documents."

    @property
    def parameters(self) -> List[ToolParameter]:
        return [
            ToolParameter(
                name="query",
                type="string",
                description="The search query to find relevant documents",
                required=True,
            ),
            ToolParameter(
                name="max_results",
                type="integer",
                description=f"Maximum results to return (default: {self.max_results})",
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
        Execute search against Elasticsearch.

        Uses SearchPipeline if configured, otherwise falls back to
        ElasticsearchBackend directly.

        Args:
            query: Search query
            max_results: Max results to return
            **kwargs: Additional options (filters, etc.)

        Returns:
            ToolResult with search results
        """
        async with TracingContext(
            f"elasticsearch.search.{self.index}",
            span_kind=SpanKind.CLIENT,
            attributes={
                "db.system": "elasticsearch",
                "elasticsearch.index": self.index,
                "elasticsearch.max_results": max_results or self.max_results,
                "search.pipeline": self._pipeline.name if self._pipeline else "legacy",
            },
        ) as span:
            # Set OpenInference span kind for Phoenix
            from openinference.semconv.trace import SpanAttributes, OpenInferenceSpanKindValues
            span.set_attribute(SpanAttributes.OPENINFERENCE_SPAN_KIND, OpenInferenceSpanKindValues.RETRIEVER.value)
            span.set_attribute(SpanAttributes.INPUT_VALUE, query)
            try:
                # Use pipeline or backend
                if self._pipeline is not None:
                    # New mode: use SearchPipeline
                    results = await self._pipeline.search(
                        query=query,
                        max_results=max_results or self.max_results,
                        **kwargs,
                    )
                    total_found = len(results)
                    error = None
                else:
                    # Legacy mode: use backend
                    response = await self._backend.search(
                        query=query,
                        max_results=max_results or self.max_results,
                        **kwargs,
                    )
                    results = response.results
                    total_found = response.total_found
                    error = response.error

                if error:
                    span.set_attribute("error", True)
                    span.set_attribute("error.message", error)
                    return ToolResult.fail(f"Search error: {error}")

                # Format results for agent consumption
                # Use 2000 chars to give agent enough context for technical details
                results_data = [
                    {
                        "id": r.id,
                        "title": r.title,
                        "content": r.content[:2000] if r.content else "",
                        "score": r.score,
                        "url": r.url,
                        "highlight": r.highlight,
                    }
                    for r in results
                ]

                # Add output attributes to span
                span.set_attribute("output.total_found", total_found)
                span.set_attribute("output.results_count", len(results_data))

                # OpenInference indexed format for retrieved documents
                for i, r in enumerate(results[:10]):
                    span.set_attribute(f"retrieval.documents.{i}.document.id", str(r.id) if r.id else "")
                    span.set_attribute(f"retrieval.documents.{i}.document.score", r.score if r.score else 0.0)
                    span.set_attribute(f"retrieval.documents.{i}.document.content", (r.content[:2000] if r.content else ""))
                    span.set_attribute(f"retrieval.documents.{i}.document.metadata", str({"title": r.title, "url": r.url}))

                # Also log for text-based log viewers
                logger.info(
                    "elasticsearch_documents_retrieved",
                    index=self.index,
                    query=query,
                    total_found=total_found,
                    results_count=len(results_data),
                    pipeline=self._pipeline.name if self._pipeline else "legacy",
                    documents=[
                        {
                            "id": r.id,
                            "title": r.title,
                            "score": r.score,
                            "url": r.url,
                        }
                        for r in results[:10]
                    ],
                )

                # Note: The reasoning loop extracts sources from data["results"]
                # So we include SearchResult objects there for source attribution
                return ToolResult.ok(
                    data={
                        "results": results_data,
                        "total_found": total_found,
                        "query": query,
                        "sources": results,  # Include raw SearchResult objects for reasoning loop
                    },
                )

            except Exception as e:
                span.set_attribute("error", True)
                span.set_attribute("error.type", type(e).__name__)
                span.set_attribute("error.message", str(e))
                logger.error(
                    "elasticsearch_tool_error",
                    index=self.index,
                    error=str(e),
                    pipeline=self._pipeline.name if self._pipeline else "legacy",
                )
                return ToolResult.fail(f"Elasticsearch search failed: {e}")

    async def close(self) -> None:
        """Close the backend connection."""
        if self._backend is not None:
            await self._backend.close()


def create_tool_from_config(config: Dict[str, Any]) -> ElasticsearchSearchTool:
    """
    Create ElasticsearchSearchTool from YAML configuration.

    This factory function creates a tool with a SearchPipeline
    configured according to the benchmarked settings.

    Args:
        config: Configuration dict with keys:
            - es_url: Elasticsearch URL
            - index: Index name
            - search_fields: Fields to search (optional)
            - search_type: "bm25", "vector", or "hybrid"
            - bm25_weight: Weight for BM25 (hybrid only)
            - vector_weight: Weight for vector (hybrid only)
            - vector_field: Field with embeddings (vector/hybrid)
            - embedding_model: Model name (vector/hybrid)
            - preprocessors: List of preprocessor configs
            - max_results: Default max results
            - source_type: Source type for UI

    Returns:
        Configured ElasticsearchSearchTool

    Example config:
        ```yaml
        es_url: http://localhost:9200
        index: documents
        search_type: hybrid
        bm25_weight: 0.6
        vector_weight: 0.4
        vector_field: vector
        embedding_model: sentence-transformers/all-MiniLM-L6-v2
        preprocessors:
          - type: stopwords
            languages: [english, german]
          - type: keywords
            max_terms: 8
        ```
    """
    import httpx
    from deepsearch.retrievers import SearchPipeline
    from deepsearch.retrievers.search_methods import BM25Search, VectorSearch, HybridSearch
    from deepsearch.retrievers.preprocessors import (
        StopwordRemover,
        Stemmer,
        KeywordExtractor,
    )

    es_url = config["es_url"]
    index = config["index"]
    search_type = config.get("search_type", "bm25")
    search_fields = config.get("search_fields", ["title^3", "content"])
    source_type = config.get("source_type")
    max_results = config.get("max_results", 10)

    # Create HTTP client
    username = config.get("username")
    password = config.get("password")
    auth = httpx.BasicAuth(username, password) if username and password else None

    es_client = httpx.AsyncClient(
        base_url=es_url,
        auth=auth,
        timeout=httpx.Timeout(config.get("timeout", 30.0)),
    )

    # Create search method
    common_args = {
        "es_client": es_client,
        "index": index,
        "source_type": source_type,
    }

    embedding_model = None
    if search_type in ("vector", "hybrid"):
        from sentence_transformers import SentenceTransformer
        model_name = config.get("embedding_model", "sentence-transformers/all-MiniLM-L6-v2")
        embedding_model = SentenceTransformer(model_name)

    if search_type == "bm25":
        search_method = BM25Search(
            **common_args,
            search_fields=search_fields,
            fuzziness=config.get("fuzziness", "AUTO"),
        )
    elif search_type == "vector":
        search_method = VectorSearch(
            **common_args,
            vector_field=config.get("vector_field", "vector"),
            embedding_model=embedding_model,
        )
    elif search_type == "hybrid":
        search_method = HybridSearch(
            **common_args,
            search_fields=search_fields,
            vector_field=config.get("vector_field", "vector"),
            embedding_model=embedding_model,
            bm25_weight=config.get("bm25_weight", 0.6),
            vector_weight=config.get("vector_weight", 0.4),
            fuzziness=config.get("fuzziness", "AUTO"),
        )
    else:
        raise ValueError(f"Unknown search_type: {search_type}")

    # Create preprocessors
    preprocessors = []
    for prep_config in config.get("preprocessors", []):
        prep_type = prep_config.get("type")
        if prep_type == "stopwords":
            preprocessors.append(StopwordRemover(
                languages=prep_config.get("languages", ["english", "german"]),
            ))
        elif prep_type == "stemmer":
            preprocessors.append(Stemmer(
                language=prep_config.get("language", "english"),
            ))
        elif prep_type == "keywords":
            preprocessors.append(KeywordExtractor(
                max_terms=prep_config.get("max_terms", 8),
            ))

    # Create pipeline
    pipeline = SearchPipeline(
        search_method=search_method,
        preprocessors=preprocessors if preprocessors else None,
    )

    return ElasticsearchSearchTool(
        pipeline=pipeline,
        index=index,
        max_results=max_results,
        source_type=source_type,
    )
