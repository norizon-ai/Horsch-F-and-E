"""
Semantic reranker as a SearchPipeline postprocessor.

This adapter wraps the SemanticReranker (from deepsearch.processors)
to work as a ResultTransform in SearchPipeline.
"""

from typing import Any, Dict, List, Optional

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger
from .base import ResultTransform

logger = get_logger(__name__)


class SemanticRerankerTransform(ResultTransform):
    """
    Adapter for SemanticReranker as a SearchPipeline postprocessor.

    Wraps the async SemanticReranker to conform to the ResultTransform
    protocol, enabling reranking in SearchPipeline.

    Example:
        from deepsearch.retrievers import SearchPipeline
        from deepsearch.retrievers.preprocessors import SemanticRerankerTransform

        pipeline = SearchPipeline(
            search_method=HybridSearch(...),
            postprocessors=[SemanticRerankerTransform(top_k=10)],
        )
        results = await pipeline.search("test query")
    """

    def __init__(
        self,
        model_name: Optional[str] = None,
        top_k: int = 10,
        score_threshold: Optional[float] = None,
        batch_size: int = 32,
        enabled: bool = True,
    ):
        """
        Initialize the reranker transform.

        Args:
            model_name: Cross-encoder model name. Defaults to
                        "cross-encoder/ms-marco-MiniLM-L-6-v2"
            top_k: Number of top results to return after reranking
            score_threshold: Minimum score threshold for filtering
            batch_size: Batch size for cross-encoder inference
            enabled: Whether reranking is enabled
        """
        # Lazy import to avoid loading model at import time
        from deepsearch.processors.semantic_reranker import (
            SemanticReranker,
            SemanticRerankerConfig,
        )

        config = SemanticRerankerConfig(
            model_name=model_name or "cross-encoder/ms-marco-MiniLM-L-6-v2",
            top_k=top_k,
            score_threshold=score_threshold,
            batch_size=batch_size,
            enabled=enabled,
        )
        self._reranker = SemanticReranker(config)
        self._config = config

        logger.debug(
            "semantic_reranker_transform_init",
            model=config.model_name,
            top_k=config.top_k,
        )

    @property
    def name(self) -> str:
        return "semantic_reranker"

    async def process(
        self,
        results: List[SearchResult],
        query: str,
    ) -> List[SearchResult]:
        """
        Rerank search results using cross-encoder semantic similarity.

        Args:
            results: Search results from the search method
            query: Original query string

        Returns:
            Reranked results, truncated to top_k
        """
        return await self._reranker.post_process(results, query)

    def get_config(self) -> Dict[str, Any]:
        """Return configuration for logging/reproducibility."""
        return {
            "name": self.name,
            "model_name": self._config.model_name,
            "top_k": self._config.top_k,
            "score_threshold": self._config.score_threshold,
            "batch_size": self._config.batch_size,
            "enabled": self._config.enabled,
        }
