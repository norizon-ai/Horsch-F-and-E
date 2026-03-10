"""
Search Method Comparison Framework for Nora Search (DeepSearch) QA Evaluation.

This module provides tools for comparing different search configurations:
- BM25-only (keyword search)
- Vector-only (semantic search)
- Hybrid (BM25 + vector) with different weight combinations

Compares retrieval performance using P@K, R@K, MRR, NDCG metrics.
"""

from dataclasses import dataclass, field
from typing import Any, Optional

from .golden_dataset import GoldenDataset, GoldenQuestion
from .retrieval_metrics import (
    RetrievalEvaluator,
    RetrievalResult,
    create_retrieval_result,
)


@dataclass
class SearchConfiguration:
    """A search configuration to test."""

    name: str
    description: str
    hybrid_enabled: bool = False
    vector_weight: float = 0.5
    bm25_weight: float = 0.5
    search_fields: list[str] = field(default_factory=lambda: ["title^3", "content"])
    top_k: int = 10

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for backend configuration."""
        return {
            "hybrid_enabled": self.hybrid_enabled,
            "vector_weight": self.vector_weight,
            "bm25_weight": self.bm25_weight,
            "search_fields": self.search_fields,
        }


# Predefined search configurations to compare
SEARCH_CONFIGURATIONS = {
    "bm25_only": SearchConfiguration(
        name="bm25_only",
        description="BM25 keyword search only (no vector)",
        hybrid_enabled=False,
        vector_weight=0.0,
        bm25_weight=1.0,
    ),
    "vector_only": SearchConfiguration(
        name="vector_only",
        description="Vector semantic search only (no BM25)",
        hybrid_enabled=True,
        vector_weight=1.0,
        bm25_weight=0.0,
    ),
    "hybrid_balanced": SearchConfiguration(
        name="hybrid_balanced",
        description="Balanced hybrid (50% BM25, 50% vector)",
        hybrid_enabled=True,
        vector_weight=0.5,
        bm25_weight=0.5,
    ),
    "hybrid_semantic": SearchConfiguration(
        name="hybrid_semantic",
        description="Semantic-heavy hybrid (30% BM25, 70% vector)",
        hybrid_enabled=True,
        vector_weight=0.7,
        bm25_weight=0.3,
    ),
    "hybrid_keyword": SearchConfiguration(
        name="hybrid_keyword",
        description="Keyword-heavy hybrid (70% BM25, 30% vector)",
        hybrid_enabled=True,
        vector_weight=0.3,
        bm25_weight=0.7,
    ),
}


@dataclass
class ConfigurationResult:
    """Results for a single configuration."""

    configuration: SearchConfiguration
    retrieval_results: list[RetrievalResult]
    metrics: dict[str, float]

    @property
    def precision_at_10(self) -> float:
        return self.metrics.get("precision@10", 0.0)

    @property
    def recall_at_10(self) -> float:
        return self.metrics.get("recall@10", 0.0)

    @property
    def mrr(self) -> float:
        return self.metrics.get("mrr", 0.0)

    @property
    def ndcg_at_10(self) -> float:
        return self.metrics.get("ndcg@10", 0.0)


@dataclass
class ComparisonReport:
    """Report comparing multiple search configurations."""

    configurations: list[SearchConfiguration]
    results: dict[str, ConfigurationResult]  # config name -> results
    best_by_metric: dict[str, str]  # metric name -> best config name

    def get_ranking(self, metric: str = "mrr") -> list[tuple[str, float]]:
        """
        Get configurations ranked by a specific metric.

        Args:
            metric: Metric name (e.g., "mrr", "precision@10", "ndcg@10").

        Returns:
            List of (config_name, score) tuples sorted by score descending.
        """
        rankings = []
        for name, result in self.results.items():
            score = result.metrics.get(metric, 0.0)
            rankings.append((name, score))
        return sorted(rankings, key=lambda x: x[1], reverse=True)


class SearchMethodComparison:
    """Compare different search configurations on a benchmark dataset."""

    def __init__(
        self,
        search_fn: Optional[Any] = None,
        k_values: Optional[list[int]] = None,
    ) -> None:
        """
        Initialize the comparison framework.

        Args:
            search_fn: Async function that takes (query, config) and returns
                      list of retrieved document titles.
            k_values: List of k values for metrics (default: [1, 3, 5, 10, 15, 20]).
        """
        self.search_fn = search_fn
        self.evaluator = RetrievalEvaluator(k_values=k_values)

    async def evaluate_configuration(
        self,
        config: SearchConfiguration,
        questions: list[GoldenQuestion],
    ) -> ConfigurationResult:
        """
        Evaluate a single search configuration on the question set.

        Args:
            config: Search configuration to test.
            questions: List of golden questions.

        Returns:
            ConfigurationResult with metrics.
        """
        retrieval_results = []

        for question in questions:
            # Run search with this configuration
            if self.search_fn:
                retrieved_docs = await self.search_fn(question.question, config)
            else:
                # Placeholder - in production, would call actual search backend
                retrieved_docs = []

            # Create retrieval result
            result = create_retrieval_result(
                query=question.question,
                retrieved_docs=retrieved_docs,
                relevant_docs=question.expected_source_pages,
            )
            retrieval_results.append(result)

        # Compute aggregated metrics
        metrics = self.evaluator.evaluate_batch(retrieval_results)

        return ConfigurationResult(
            configuration=config,
            retrieval_results=retrieval_results,
            metrics=metrics,
        )

    async def compare_configurations(
        self,
        configurations: list[SearchConfiguration],
        questions: list[GoldenQuestion],
    ) -> ComparisonReport:
        """
        Compare multiple search configurations.

        Args:
            configurations: List of configurations to compare.
            questions: List of golden questions.

        Returns:
            ComparisonReport with results for all configurations.
        """
        results: dict[str, ConfigurationResult] = {}

        for config in configurations:
            result = await self.evaluate_configuration(config, questions)
            results[config.name] = result

        # Determine best configuration for each metric
        metrics_to_track = ["mrr", "map", "precision@10", "recall@10", "ndcg@10"]
        best_by_metric: dict[str, str] = {}

        for metric in metrics_to_track:
            best_config = None
            best_score = -1.0

            for name, result in results.items():
                score = result.metrics.get(metric, 0.0)
                if score > best_score:
                    best_score = score
                    best_config = name

            if best_config:
                best_by_metric[metric] = best_config

        return ComparisonReport(
            configurations=configurations,
            results=results,
            best_by_metric=best_by_metric,
        )

    async def compare_all_standard_configs(
        self,
        questions: list[GoldenQuestion],
    ) -> ComparisonReport:
        """
        Compare all standard configurations.

        Args:
            questions: List of golden questions.

        Returns:
            ComparisonReport for all standard configurations.
        """
        configs = list(SEARCH_CONFIGURATIONS.values())
        return await self.compare_configurations(configs, questions)

    def format_comparison_report(self, report: ComparisonReport) -> str:
        """
        Format comparison report as readable text.

        Args:
            report: ComparisonReport to format.

        Returns:
            Formatted string report.
        """
        lines = ["=" * 70]
        lines.append("SEARCH METHOD COMPARISON REPORT")
        lines.append("=" * 70)
        lines.append("")

        lines.append(f"Configurations tested: {len(report.configurations)}")
        for config in report.configurations:
            lines.append(f"  - {config.name}: {config.description}")
        lines.append("")

        # Metrics table header
        lines.append("-" * 70)
        lines.append(
            f"{'Configuration':<20} {'P@10':>8} {'R@10':>8} {'MRR':>8} {'NDCG@10':>8} {'MAP':>8}"
        )
        lines.append("-" * 70)

        # Metrics for each configuration
        for name in sorted(report.results.keys()):
            result = report.results[name]
            p10 = result.metrics.get("precision@10", 0)
            r10 = result.metrics.get("recall@10", 0)
            mrr = result.metrics.get("mrr", 0)
            ndcg10 = result.metrics.get("ndcg@10", 0)
            map_score = result.metrics.get("map", 0)

            lines.append(
                f"{name:<20} {p10:>8.4f} {r10:>8.4f} {mrr:>8.4f} {ndcg10:>8.4f} {map_score:>8.4f}"
            )

        lines.append("-" * 70)
        lines.append("")

        # Best configurations
        lines.append("Best Configuration by Metric:")
        for metric, config_name in report.best_by_metric.items():
            score = report.results[config_name].metrics.get(metric, 0)
            lines.append(f"  {metric}: {config_name} ({score:.4f})")

        lines.append("")
        lines.append("=" * 70)

        return "\n".join(lines)


class ParameterSweep:
    """Sweep over parameter values to find optimal settings."""

    def __init__(
        self,
        search_fn: Optional[Any] = None,
    ) -> None:
        """
        Initialize parameter sweep.

        Args:
            search_fn: Async function that takes (query, config) and returns
                      list of retrieved document titles.
        """
        self.comparison = SearchMethodComparison(search_fn=search_fn)

    def generate_weight_sweep_configs(
        self,
        steps: int = 5,
    ) -> list[SearchConfiguration]:
        """
        Generate configurations for sweeping vector/BM25 weights.

        Args:
            steps: Number of steps in the sweep (0.0 to 1.0).

        Returns:
            List of configurations with different weight combinations.
        """
        configs = []
        step_size = 1.0 / steps

        for i in range(steps + 1):
            vector_weight = round(i * step_size, 2)
            bm25_weight = round(1.0 - vector_weight, 2)

            config = SearchConfiguration(
                name=f"hybrid_{int(vector_weight*100)}v_{int(bm25_weight*100)}b",
                description=f"Hybrid: {int(vector_weight*100)}% vector, {int(bm25_weight*100)}% BM25",
                hybrid_enabled=True,
                vector_weight=vector_weight,
                bm25_weight=bm25_weight,
            )
            configs.append(config)

        return configs

    def generate_top_k_sweep_configs(
        self,
        k_values: Optional[list[int]] = None,
        base_config: Optional[SearchConfiguration] = None,
    ) -> list[SearchConfiguration]:
        """
        Generate configurations for sweeping top_k values.

        Args:
            k_values: List of top_k values to test.
            base_config: Base configuration to modify.

        Returns:
            List of configurations with different top_k values.
        """
        if k_values is None:
            k_values = [5, 10, 15, 20, 30]

        if base_config is None:
            base_config = SEARCH_CONFIGURATIONS["hybrid_balanced"]

        configs = []
        for k in k_values:
            config = SearchConfiguration(
                name=f"{base_config.name}_k{k}",
                description=f"{base_config.description} (top_k={k})",
                hybrid_enabled=base_config.hybrid_enabled,
                vector_weight=base_config.vector_weight,
                bm25_weight=base_config.bm25_weight,
                search_fields=base_config.search_fields,
                top_k=k,
            )
            configs.append(config)

        return configs

    def generate_boost_sweep_configs(
        self,
        title_boost_values: Optional[list[int]] = None,
    ) -> list[SearchConfiguration]:
        """
        Generate configurations for sweeping title boost values.

        Args:
            title_boost_values: List of title boost values to test.

        Returns:
            List of configurations with different title boosts.
        """
        if title_boost_values is None:
            title_boost_values = [1, 2, 3, 5, 10]

        configs = []
        for boost in title_boost_values:
            config = SearchConfiguration(
                name=f"bm25_title_boost_{boost}",
                description=f"BM25 with title boost {boost}x",
                hybrid_enabled=False,
                search_fields=[f"title^{boost}", "content"],
            )
            configs.append(config)

        return configs

    async def run_weight_sweep(
        self,
        questions: list[GoldenQuestion],
        steps: int = 5,
    ) -> ComparisonReport:
        """
        Run weight sweep and return results.

        Args:
            questions: Golden questions for evaluation.
            steps: Number of steps in the sweep.

        Returns:
            ComparisonReport with all weight combinations.
        """
        configs = self.generate_weight_sweep_configs(steps)
        return await self.comparison.compare_configurations(configs, questions)

    async def find_optimal_weights(
        self,
        questions: list[GoldenQuestion],
        optimize_for: str = "mrr",
        steps: int = 10,
    ) -> tuple[float, float, float]:
        """
        Find optimal vector/BM25 weights for a metric.

        Args:
            questions: Golden questions for evaluation.
            optimize_for: Metric to optimize (default: MRR).
            steps: Number of steps in the sweep.

        Returns:
            Tuple of (optimal_vector_weight, optimal_bm25_weight, best_score).
        """
        report = await self.run_weight_sweep(questions, steps)
        ranking = report.get_ranking(optimize_for)

        if not ranking:
            return 0.5, 0.5, 0.0

        best_config_name = ranking[0][0]
        best_score = ranking[0][1]
        best_result = report.results[best_config_name]

        return (
            best_result.configuration.vector_weight,
            best_result.configuration.bm25_weight,
            best_score,
        )
