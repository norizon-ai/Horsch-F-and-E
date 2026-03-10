"""
Retrieval Performance Metrics for Nora Search (DeepSearch) QA Evaluation.

This module provides metrics for evaluating search retrieval quality:
- Precision@K: Proportion of top-k results that are relevant
- Recall@K: Proportion of relevant docs found in top-k
- MRR (Mean Reciprocal Rank): Position of first relevant result
- NDCG@K: Normalized Discounted Cumulative Gain with graded relevance
"""

import math
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class RetrievalResult:
    """Result from a single retrieval query."""

    query: str
    retrieved_docs: list[str]  # List of document IDs/titles in ranked order
    relevant_docs: set[str]  # Set of relevant document IDs/titles
    relevance_scores: dict[str, int] = field(default_factory=dict)  # doc -> grade (for NDCG)

    @property
    def has_graded_relevance(self) -> bool:
        """Check if graded relevance scores are available."""
        return len(self.relevance_scores) > 0


@dataclass
class MetricsReport:
    """Report containing all retrieval metrics."""

    precision_at_k: dict[int, float]  # k -> precision
    recall_at_k: dict[int, float]  # k -> recall
    mrr: float
    ndcg_at_k: dict[int, float]  # k -> ndcg
    hit_rate_at_k: dict[int, float]  # k -> hit rate
    avg_precision: float  # MAP component for single query

    def __repr__(self) -> str:
        return (
            f"MetricsReport(\n"
            f"  P@10={self.precision_at_k.get(10, 0):.3f}, "
            f"R@10={self.recall_at_k.get(10, 0):.3f},\n"
            f"  MRR={self.mrr:.3f}, "
            f"NDCG@10={self.ndcg_at_k.get(10, 0):.3f}\n"
            f")"
        )


class RetrievalEvaluator:
    """Evaluate search retrieval quality with standard IR metrics."""

    DEFAULT_K_VALUES = [1, 3, 5, 10, 15, 20]

    def __init__(self, k_values: Optional[list[int]] = None) -> None:
        """
        Initialize the evaluator.

        Args:
            k_values: List of k values to compute metrics for.
        """
        self.k_values = k_values or self.DEFAULT_K_VALUES

    def precision_at_k(
        self, retrieved_docs: list[str], relevant_docs: set[str], k: int
    ) -> float:
        """
        Calculate Precision@K.

        Precision@K = |relevant docs in top-k| / k

        Args:
            retrieved_docs: List of retrieved document IDs in ranked order.
            relevant_docs: Set of relevant document IDs.
            k: Number of top results to consider.

        Returns:
            Precision score between 0 and 1.
        """
        if k <= 0:
            return 0.0

        retrieved_at_k = retrieved_docs[:k]
        relevant_retrieved = sum(1 for doc in retrieved_at_k if doc in relevant_docs)
        return relevant_retrieved / k

    def recall_at_k(
        self, retrieved_docs: list[str], relevant_docs: set[str], k: int
    ) -> float:
        """
        Calculate Recall@K.

        Recall@K = |relevant docs in top-k| / |all relevant docs|

        Args:
            retrieved_docs: List of retrieved document IDs in ranked order.
            relevant_docs: Set of relevant document IDs.
            k: Number of top results to consider.

        Returns:
            Recall score between 0 and 1.
        """
        if not relevant_docs:
            return 0.0

        retrieved_at_k = retrieved_docs[:k]
        relevant_retrieved = sum(1 for doc in retrieved_at_k if doc in relevant_docs)
        return relevant_retrieved / len(relevant_docs)

    def mrr(self, retrieved_docs: list[str], relevant_docs: set[str]) -> float:
        """
        Calculate Mean Reciprocal Rank.

        MRR = 1 / (position of first relevant result)

        Args:
            retrieved_docs: List of retrieved document IDs in ranked order.
            relevant_docs: Set of relevant document IDs.

        Returns:
            MRR score between 0 and 1.
        """
        for i, doc in enumerate(retrieved_docs, 1):
            if doc in relevant_docs:
                return 1.0 / i
        return 0.0

    def hit_rate_at_k(
        self, retrieved_docs: list[str], relevant_docs: set[str], k: int
    ) -> float:
        """
        Calculate Hit Rate@K (binary: did we find at least one relevant doc?).

        Args:
            retrieved_docs: List of retrieved document IDs in ranked order.
            relevant_docs: Set of relevant document IDs.
            k: Number of top results to consider.

        Returns:
            1.0 if at least one relevant doc in top-k, else 0.0.
        """
        retrieved_at_k = retrieved_docs[:k]
        return 1.0 if any(doc in relevant_docs for doc in retrieved_at_k) else 0.0

    def dcg_at_k(self, relevance_scores: list[int], k: int) -> float:
        """
        Calculate Discounted Cumulative Gain at K.

        DCG@K = sum(rel_i / log2(i + 1)) for i in 1..k

        Args:
            relevance_scores: List of relevance grades in ranked order.
            k: Number of top results to consider.

        Returns:
            DCG score.
        """
        dcg = 0.0
        for i, rel in enumerate(relevance_scores[:k], 1):
            dcg += rel / math.log2(i + 1)
        return dcg

    def ndcg_at_k(
        self,
        retrieved_docs: list[str],
        relevance_scores: dict[str, int],
        k: int,
    ) -> float:
        """
        Calculate Normalized Discounted Cumulative Gain at K.

        NDCG@K = DCG@K / IDCG@K

        Args:
            retrieved_docs: List of retrieved document IDs in ranked order.
            relevance_scores: Dict mapping doc IDs to relevance grades (e.g., 0-3).
            k: Number of top results to consider.

        Returns:
            NDCG score between 0 and 1.
        """
        # Get actual relevance scores for retrieved docs
        actual_rels = [relevance_scores.get(doc, 0) for doc in retrieved_docs[:k]]
        dcg = self.dcg_at_k(actual_rels, k)

        # Ideal ranking: sort all known relevant scores in descending order
        ideal_rels = sorted(relevance_scores.values(), reverse=True)[:k]
        idcg = self.dcg_at_k(ideal_rels, k)

        if idcg == 0:
            return 0.0
        return dcg / idcg

    def average_precision(
        self, retrieved_docs: list[str], relevant_docs: set[str]
    ) -> float:
        """
        Calculate Average Precision (for MAP computation).

        AP = (1/|relevant|) * sum(P@k * rel(k)) for all k

        Args:
            retrieved_docs: List of retrieved document IDs in ranked order.
            relevant_docs: Set of relevant document IDs.

        Returns:
            Average precision score.
        """
        if not relevant_docs:
            return 0.0

        ap_sum = 0.0
        relevant_count = 0

        for i, doc in enumerate(retrieved_docs, 1):
            if doc in relevant_docs:
                relevant_count += 1
                precision_at_i = relevant_count / i
                ap_sum += precision_at_i

        return ap_sum / len(relevant_docs)

    def evaluate_single(self, result: RetrievalResult) -> MetricsReport:
        """
        Evaluate a single retrieval result.

        Args:
            result: RetrievalResult containing query and retrieved docs.

        Returns:
            MetricsReport with all metrics.
        """
        precision_at_k = {}
        recall_at_k = {}
        hit_rate_at_k = {}
        ndcg_at_k = {}

        for k in self.k_values:
            precision_at_k[k] = self.precision_at_k(
                result.retrieved_docs, result.relevant_docs, k
            )
            recall_at_k[k] = self.recall_at_k(
                result.retrieved_docs, result.relevant_docs, k
            )
            hit_rate_at_k[k] = self.hit_rate_at_k(
                result.retrieved_docs, result.relevant_docs, k
            )

            if result.has_graded_relevance:
                ndcg_at_k[k] = self.ndcg_at_k(
                    result.retrieved_docs, result.relevance_scores, k
                )
            else:
                # Use binary relevance (1 for relevant, 0 for not)
                binary_scores = {
                    doc: 1 for doc in result.relevant_docs
                }
                ndcg_at_k[k] = self.ndcg_at_k(
                    result.retrieved_docs, binary_scores, k
                )

        mrr = self.mrr(result.retrieved_docs, result.relevant_docs)
        avg_precision = self.average_precision(
            result.retrieved_docs, result.relevant_docs
        )

        return MetricsReport(
            precision_at_k=precision_at_k,
            recall_at_k=recall_at_k,
            mrr=mrr,
            ndcg_at_k=ndcg_at_k,
            hit_rate_at_k=hit_rate_at_k,
            avg_precision=avg_precision,
        )

    def evaluate_batch(
        self, results: list[RetrievalResult]
    ) -> dict[str, float]:
        """
        Evaluate a batch of retrieval results and compute aggregate metrics.

        Args:
            results: List of RetrievalResult objects.

        Returns:
            Dict with aggregated metrics (means across all queries).
        """
        if not results:
            return {}

        reports = [self.evaluate_single(r) for r in results]

        aggregated: dict[str, float] = {}

        # Aggregate precision@k
        for k in self.k_values:
            key = f"precision@{k}"
            aggregated[key] = sum(r.precision_at_k.get(k, 0) for r in reports) / len(reports)

        # Aggregate recall@k
        for k in self.k_values:
            key = f"recall@{k}"
            aggregated[key] = sum(r.recall_at_k.get(k, 0) for r in reports) / len(reports)

        # Aggregate hit_rate@k
        for k in self.k_values:
            key = f"hit_rate@{k}"
            aggregated[key] = sum(r.hit_rate_at_k.get(k, 0) for r in reports) / len(reports)

        # Aggregate NDCG@k
        for k in self.k_values:
            key = f"ndcg@{k}"
            aggregated[key] = sum(r.ndcg_at_k.get(k, 0) for r in reports) / len(reports)

        # MRR
        aggregated["mrr"] = sum(r.mrr for r in reports) / len(reports)

        # MAP (Mean Average Precision)
        aggregated["map"] = sum(r.avg_precision for r in reports) / len(reports)

        return aggregated

    def format_report(self, aggregated: dict[str, float]) -> str:
        """
        Format aggregated metrics as a readable report.

        Args:
            aggregated: Dict of aggregated metrics.

        Returns:
            Formatted string report.
        """
        lines = ["=" * 50]
        lines.append("RETRIEVAL METRICS REPORT")
        lines.append("=" * 50)
        lines.append("")

        # Group by metric type
        lines.append("Precision@K:")
        for k in self.k_values:
            key = f"precision@{k}"
            if key in aggregated:
                lines.append(f"  @{k:2d}: {aggregated[key]:.4f}")

        lines.append("")
        lines.append("Recall@K:")
        for k in self.k_values:
            key = f"recall@{k}"
            if key in aggregated:
                lines.append(f"  @{k:2d}: {aggregated[key]:.4f}")

        lines.append("")
        lines.append("Hit Rate@K:")
        for k in self.k_values:
            key = f"hit_rate@{k}"
            if key in aggregated:
                lines.append(f"  @{k:2d}: {aggregated[key]:.4f}")

        lines.append("")
        lines.append("NDCG@K:")
        for k in self.k_values:
            key = f"ndcg@{k}"
            if key in aggregated:
                lines.append(f"  @{k:2d}: {aggregated[key]:.4f}")

        lines.append("")
        lines.append("Ranking Metrics:")
        if "mrr" in aggregated:
            lines.append(f"  MRR: {aggregated['mrr']:.4f}")
        if "map" in aggregated:
            lines.append(f"  MAP: {aggregated['map']:.4f}")

        lines.append("")
        lines.append("=" * 50)

        return "\n".join(lines)


def create_retrieval_result(
    query: str,
    retrieved_docs: list[str],
    relevant_docs: list[str],
    relevance_grades: Optional[dict[str, int]] = None,
) -> RetrievalResult:
    """
    Convenience function to create a RetrievalResult.

    Args:
        query: The search query.
        retrieved_docs: List of retrieved document IDs/titles.
        relevant_docs: List of relevant document IDs/titles.
        relevance_grades: Optional dict mapping docs to relevance grades.

    Returns:
        RetrievalResult instance.
    """
    return RetrievalResult(
        query=query,
        retrieved_docs=retrieved_docs,
        relevant_docs=set(relevant_docs),
        relevance_scores=relevance_grades or {},
    )
