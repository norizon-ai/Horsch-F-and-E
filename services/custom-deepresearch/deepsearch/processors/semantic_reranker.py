"""
Semantic Reranker Processor

Uses a cross-encoder model to rerank search results based on semantic
relevance to the query. This significantly improves retrieval accuracy
by using deeper semantic understanding than BM25 or bi-encoder similarity.

Recommended model: cross-encoder/ms-marco-MiniLM-L-6-v2
- Size: ~21MB
- Latency: ~20-50ms for 10-50 results
- Training: MS MARCO passage ranking dataset
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, TYPE_CHECKING

from deepsearch.models import SearchResult
from deepsearch.observability import get_logger
from .base import BaseProcessor

if TYPE_CHECKING:
    pass

logger = get_logger(__name__)

# Lazy-loaded cross-encoder model
_cross_encoder_cache: Dict[str, Any] = {}


@dataclass
class SemanticRerankerConfig:
    """Configuration for the semantic reranker."""

    # Model to use for reranking
    model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"

    # Number of top results to return after reranking
    top_k: int = 10

    # Batch size for cross-encoder inference
    batch_size: int = 32

    # Minimum score threshold (results below this are filtered out)
    score_threshold: Optional[float] = None

    # Whether to store original score in metadata
    preserve_original_score: bool = True

    # Device for inference (None = auto-detect)
    device: Optional[str] = None

    # Whether reranking is enabled
    enabled: bool = True


class SemanticReranker(BaseProcessor):
    """
    Reranks search results using a cross-encoder model.

    Cross-encoders process (query, document) pairs jointly, providing
    more accurate relevance scores than bi-encoders or BM25.

    Usage:
        reranker = SemanticReranker(SemanticRerankerConfig(top_k=10))
        reranked = await reranker.post_process(results, query, context)

    Configuration via agents.yaml:
        processors:
          - type: semantic_reranker
            enabled: true
            config:
              model_name: "cross-encoder/ms-marco-MiniLM-L-6-v2"
              top_k: 10
              score_threshold: 0.1
    """

    def __init__(self, config: Optional[SemanticRerankerConfig] = None):
        """Initialize the reranker with configuration."""
        self.config = config or SemanticRerankerConfig()
        self._model = None
        logger.info(
            "semantic_reranker_initialized",
            model=self.config.model_name,
            top_k=self.config.top_k,
            enabled=self.config.enabled,
        )

    def _load_model(self):
        """Lazy-load the cross-encoder model."""
        if self._model is not None:
            return self._model

        # Check cache first
        if self.config.model_name in _cross_encoder_cache:
            self._model = _cross_encoder_cache[self.config.model_name]
            logger.debug("cross_encoder_loaded_from_cache", model=self.config.model_name)
            return self._model

        try:
            from sentence_transformers import CrossEncoder

            logger.info("loading_cross_encoder", model=self.config.model_name)

            self._model = CrossEncoder(
                self.config.model_name,
                device=self.config.device,
            )

            # Cache for reuse
            _cross_encoder_cache[self.config.model_name] = self._model

            logger.info("cross_encoder_loaded", model=self.config.model_name)
            return self._model

        except ImportError:
            logger.error(
                "sentence_transformers_not_installed",
                message="Install with: pip install sentence-transformers",
            )
            raise
        except Exception as e:
            logger.error("cross_encoder_load_failed", error=str(e))
            raise

    async def pre_process(self, query: str, context: Optional[dict] = None) -> str:
        """Pass-through for pre-processing (reranking is post-processing only)."""
        return query

    async def post_process(
        self,
        results: List[SearchResult],
        original_query: str,
        context: Optional[dict] = None,
    ) -> List[SearchResult]:
        """
        Rerank search results using cross-encoder semantic similarity.

        Args:
            results: List of SearchResult objects from initial retrieval
            original_query: The original user query
            context: Optional context dict (unused)

        Returns:
            Reranked list of SearchResult objects, truncated to top_k
        """
        if not self.config.enabled:
            logger.debug("semantic_reranker_disabled")
            return results

        if not results:
            return results

        # Skip if we have fewer results than top_k
        if len(results) <= self.config.top_k:
            logger.debug(
                "reranking_skipped_few_results",
                result_count=len(results),
                top_k=self.config.top_k,
            )
            # Still compute scores for consistency if we have results
            if not results:
                return results

        logger.info(
            "reranking_started",
            query_preview=original_query[:50],
            result_count=len(results),
            top_k=self.config.top_k,
        )

        try:
            # Load model (lazy)
            model = self._load_model()

            # Prepare (query, passage) pairs for cross-encoder
            pairs = []
            for result in results:
                # Use content for reranking, fall back to title
                passage = result.content or result.title or ""
                # Truncate very long passages (cross-encoders have token limits)
                if len(passage) > 512:
                    passage = passage[:512]
                pairs.append((original_query, passage))

            # Batch inference
            scores = model.predict(
                pairs,
                batch_size=self.config.batch_size,
                show_progress_bar=False,
            )

            # Convert scores to Python floats (some models return numpy arrays)
            # Handle both 1D arrays and scalar returns
            try:
                import numpy as np
                if isinstance(scores, np.ndarray):
                    scores = scores.flatten().tolist()
                elif hasattr(scores, 'tolist'):
                    scores = scores.tolist()
            except ImportError:
                pass

            # Ensure all scores are floats
            scores = [float(s) if hasattr(s, '__float__') else float(s) for s in scores]

            # Combine results with scores
            scored_results = list(zip(results, scores))

            # Filter by threshold if configured
            if self.config.score_threshold is not None:
                scored_results = [
                    (r, s)
                    for r, s in scored_results
                    if s >= self.config.score_threshold
                ]
                logger.debug(
                    "filtered_by_threshold",
                    threshold=self.config.score_threshold,
                    remaining=len(scored_results),
                )

            # Sort by cross-encoder score (descending)
            scored_results.sort(key=lambda x: x[1], reverse=True)

            # Create new SearchResult objects with updated scores
            # (SearchResult is frozen/immutable, so we create new instances)
            reranked = []
            for i, (result, rerank_score) in enumerate(scored_results[: self.config.top_k]):
                # Build new metadata preserving original score
                new_metadata = dict(result.metadata) if result.metadata else {}
                if self.config.preserve_original_score:
                    new_metadata["original_score"] = result.score
                    new_metadata["rerank_score"] = float(rerank_score)
                    new_metadata["rerank_position"] = i + 1

                # Create new SearchResult with rerank score
                reranked.append(
                    SearchResult(
                        id=result.id,
                        title=result.title,
                        content=result.content,
                        url=result.url,
                        score=float(rerank_score),
                        source_type=result.source_type,
                        metadata=new_metadata,
                    )
                )

            logger.info(
                "reranking_completed",
                input_count=len(results),
                output_count=len(reranked),
                top_score=reranked[0].score if reranked else 0,
            )

            return reranked

        except Exception as e:
            logger.error(
                "reranking_failed",
                error=str(e),
                fallback="returning_original_results",
            )
            # Return original results on error
            return results[: self.config.top_k]


def create_semantic_reranker(config_dict: Optional[dict] = None) -> SemanticReranker:
    """
    Factory function to create a SemanticReranker from a config dict.

    Used by the processor factory when loading from agents.yaml.

    Args:
        config_dict: Configuration dictionary from YAML

    Returns:
        Configured SemanticReranker instance
    """
    if config_dict:
        config = SemanticRerankerConfig(**config_dict)
    else:
        config = SemanticRerankerConfig()
    return SemanticReranker(config)
