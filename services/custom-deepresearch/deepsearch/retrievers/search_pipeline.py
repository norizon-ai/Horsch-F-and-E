"""
Search pipeline combining search methods and preprocessors.

This is the main interface used by both:
- ElasticsearchSearchTool (production)
- BEIR benchmark (evaluation)

Same interface, same behavior - benchmark code becomes production code.
"""

import time
from typing import Any, Dict, List, Optional

from deepsearch.models import SearchResult, SearchResponse
from deepsearch.observability import get_logger
from .search_methods import SearchMethod
from .preprocessors import Preprocessor, ResultTransform

logger = get_logger(__name__)


class SearchPipeline:
    """
    Composable search pipeline.

    Combines:
    - Preprocessors: Query transformations (stopwords, stemming, keywords)
    - Search method: The actual retrieval (BM25, vector, hybrid)
    - Postprocessors: Result transformations (reranking, filtering)

    Used by both production agents and benchmark evaluation,
    ensuring consistent behavior across environments.

    Example:
        pipeline = SearchPipeline(
            search_method=HybridSearch(...),
            preprocessors=[StopwordRemover(), KeywordExtractor()],
            postprocessors=[SemanticRerankerTransform(top_k=10)],
        )
        results = await pipeline.search("what is the RC-3000 error")
    """

    def __init__(
        self,
        search_method: SearchMethod,
        preprocessors: Optional[List[Preprocessor]] = None,
        postprocessors: Optional[List[ResultTransform]] = None,
    ):
        """
        Initialize search pipeline.

        Args:
            search_method: The search method to use (BM25, vector, hybrid)
            preprocessors: Optional list of query preprocessors
            postprocessors: Optional list of result transforms (reranking, etc.)
        """
        self.search_method = search_method
        self.preprocessors = preprocessors or []
        self.postprocessors = postprocessors or []

    @property
    def name(self) -> str:
        """Pipeline name for logging/benchmarking."""
        parts = [self.search_method.name]
        if self.preprocessors:
            prep_names = "+".join(p.name for p in self.preprocessors)
            parts.append(prep_names)
        if self.postprocessors:
            post_names = "+".join(p.name for p in self.postprocessors)
            parts.append(post_names)
        return "_".join(parts)

    def get_config(self) -> Dict[str, Any]:
        """Return full pipeline configuration."""
        return {
            "name": self.name,
            "search_method": self.search_method.get_config(),
            "preprocessors": [p.get_config() for p in self.preprocessors],
            "postprocessors": [p.get_config() for p in self.postprocessors],
        }

    def preprocess(self, query: str) -> str:
        """
        Apply all preprocessors in order.

        Args:
            query: Original query string

        Returns:
            Processed query string
        """
        processed = query
        for preprocessor in self.preprocessors:
            try:
                processed = preprocessor.process(processed)
            except Exception as e:
                logger.warning(
                    "preprocessor_error",
                    preprocessor=preprocessor.name,
                    error=str(e),
                    query=query[:100],
                )
                # Continue with current processed value
        return processed

    async def postprocess(
        self,
        results: List[SearchResult],
        original_query: str,
    ) -> List[SearchResult]:
        """
        Apply all postprocessors in order.

        Args:
            results: Search results from the search method
            original_query: Original query string (before preprocessing)

        Returns:
            Transformed results
        """
        current_results = results
        for postprocessor in self.postprocessors:
            try:
                current_results = await postprocessor.process(
                    current_results, original_query
                )
                logger.debug(
                    "postprocessor_applied",
                    postprocessor=postprocessor.name,
                    input_count=len(results),
                    output_count=len(current_results),
                )
            except Exception as e:
                logger.warning(
                    "postprocessor_error",
                    postprocessor=postprocessor.name,
                    error=str(e),
                    query=original_query[:100],
                )
                # Continue with current results on error
        return current_results

    async def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> List[SearchResult]:
        """
        Execute full search pipeline.

        1. Preprocess query
        2. Execute search method
        3. Postprocess results (reranking, filtering)
        4. Return results

        Args:
            query: Raw query string
            max_results: Maximum results to return
            filters: Optional field filters
            **kwargs: Additional method-specific parameters

        Returns:
            List of SearchResult ordered by score (descending)
        """
        start_time = time.time()

        # 1. Preprocess query
        original_query = query
        processed_query = self.preprocess(query)

        # Log preprocessing result
        if processed_query != original_query:
            logger.debug(
                "query_preprocessed",
                original=original_query[:100],
                processed=processed_query[:100],
                pipeline=self.name,
            )

        # 2. Execute search
        # If we have postprocessors (like reranker), fetch more results
        # so the reranker has more candidates to work with
        fetch_count = max_results
        if self.postprocessors:
            # Fetch 3x results for reranking (common practice)
            fetch_count = max(max_results * 3, 30)

        results = await self.search_method.search(
            processed_query,
            max_results=fetch_count,
            filters=filters,
            **kwargs,
        )

        # 3. Postprocess results (reranking, filtering)
        if self.postprocessors:
            results = await self.postprocess(results, original_query)
            # Ensure we don't return more than requested
            results = results[:max_results]

        # 4. Log and return
        search_time_ms = (time.time() - start_time) * 1000
        logger.debug(
            "pipeline_search_complete",
            pipeline=self.name,
            original_query=original_query[:100],
            processed_query=processed_query[:100],
            result_count=len(results),
            search_time_ms=search_time_ms,
        )

        return results

    async def search_with_response(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
        **kwargs,
    ) -> SearchResponse:
        """
        Execute search and return full SearchResponse.

        Same as search() but returns a SearchResponse with metadata.

        Args:
            query: Raw query string
            max_results: Maximum results to return
            filters: Optional field filters
            **kwargs: Additional parameters

        Returns:
            SearchResponse with results and metadata
        """
        start_time = time.time()

        try:
            results = await self.search(
                query,
                max_results=max_results,
                filters=filters,
                **kwargs,
            )
            search_time_ms = (time.time() - start_time) * 1000

            return SearchResponse(
                results=results,
                total_found=len(results),  # Approximation without ES total
                query=query,
                search_time_ms=search_time_ms,
            )
        except Exception as e:
            search_time_ms = (time.time() - start_time) * 1000
            logger.error(
                "pipeline_search_error",
                pipeline=self.name,
                query=query[:100],
                error=str(e),
            )
            return SearchResponse(
                results=[],
                total_found=0,
                query=query,
                search_time_ms=search_time_ms,
                error=str(e),
            )


class SearchPipelineBuilder:
    """
    Builder for creating SearchPipeline instances.

    Provides a fluent interface for configuring pipelines.

    Example:
        pipeline = (
            SearchPipelineBuilder()
            .with_bm25(es_client, index, fields)
            .with_stopwords(["english", "german"])
            .with_keywords(max_terms=8)
            .with_reranker(top_k=10)
            .build()
        )
    """

    def __init__(self):
        self._search_method: Optional[SearchMethod] = None
        self._preprocessors: List[Preprocessor] = []
        self._postprocessors: List[ResultTransform] = []

    def with_search_method(self, method: SearchMethod) -> "SearchPipelineBuilder":
        """Set the search method."""
        self._search_method = method
        return self

    def with_preprocessor(self, preprocessor: Preprocessor) -> "SearchPipelineBuilder":
        """Add a preprocessor."""
        self._preprocessors.append(preprocessor)
        return self

    def with_preprocessors(self, preprocessors: List[Preprocessor]) -> "SearchPipelineBuilder":
        """Add multiple preprocessors."""
        self._preprocessors.extend(preprocessors)
        return self

    def with_postprocessor(self, postprocessor: ResultTransform) -> "SearchPipelineBuilder":
        """Add a postprocessor (result transform)."""
        self._postprocessors.append(postprocessor)
        return self

    def with_postprocessors(self, postprocessors: List[ResultTransform]) -> "SearchPipelineBuilder":
        """Add multiple postprocessors."""
        self._postprocessors.extend(postprocessors)
        return self

    def with_stopwords(
        self,
        languages: Optional[List[str]] = None,
        **kwargs,
    ) -> "SearchPipelineBuilder":
        """Add stopword removal preprocessor."""
        from .preprocessors import StopwordRemover
        self._preprocessors.append(StopwordRemover(languages=languages, **kwargs))
        return self

    def with_stemmer(
        self,
        language: str = "english",
        **kwargs,
    ) -> "SearchPipelineBuilder":
        """Add stemming preprocessor."""
        from .preprocessors import Stemmer
        self._preprocessors.append(Stemmer(language=language, **kwargs))
        return self

    def with_keywords(
        self,
        max_terms: int = 8,
        **kwargs,
    ) -> "SearchPipelineBuilder":
        """Add keyword extraction preprocessor."""
        from .preprocessors import KeywordExtractor
        self._preprocessors.append(KeywordExtractor(max_terms=max_terms, **kwargs))
        return self

    def with_reranker(
        self,
        model_name: Optional[str] = None,
        top_k: int = 10,
        score_threshold: Optional[float] = None,
    ) -> "SearchPipelineBuilder":
        """
        Add semantic reranker postprocessor.

        Args:
            model_name: Cross-encoder model name (defaults to ms-marco-MiniLM-L-6-v2)
            top_k: Number of top results to return after reranking
            score_threshold: Minimum score threshold for filtering

        Returns:
            Self for chaining
        """
        from .preprocessors import SemanticRerankerTransform
        self._postprocessors.append(
            SemanticRerankerTransform(
                model_name=model_name,
                top_k=top_k,
                score_threshold=score_threshold,
            )
        )
        return self

    def build(self) -> SearchPipeline:
        """Build the SearchPipeline."""
        if self._search_method is None:
            raise ValueError("Search method is required. Call with_search_method() first.")
        return SearchPipeline(
            search_method=self._search_method,
            preprocessors=self._preprocessors if self._preprocessors else None,
            postprocessors=self._postprocessors if self._postprocessors else None,
        )
