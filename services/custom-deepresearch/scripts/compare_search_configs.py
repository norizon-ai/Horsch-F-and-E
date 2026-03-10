#!/usr/bin/env python3
"""
Search Configuration Comparison Script for Nora Search (DeepSearch).

Compares BM25, Vector, and Hybrid search configurations to find
optimal retrieval settings.

Usage:
    # Compare all standard configurations
    python scripts/compare_search_configs.py

    # Run weight sweep (find optimal vector/BM25 weights)
    python scripts/compare_search_configs.py --sweep weights --steps 10

    # Run title boost sweep
    python scripts/compare_search_configs.py --sweep title-boost

    # Test on specific category
    python scripts/compare_search_configs.py --category troubleshooting

    # Limit number of questions
    python scripts/compare_search_configs.py --limit 20
"""

import argparse
import asyncio
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Optional

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from tests.evaluation import (
    GoldenDataset,
    GoldenQuestion,
    SearchMethodComparison,
    SearchConfiguration,
    ParameterSweep,
    SEARCH_CONFIGURATIONS,
)

# Import Elasticsearch backend
from deepsearch.retrievers.search_backends.elasticsearch import (
    ElasticsearchBackend,
    ElasticsearchConfig,
)


class SearchConfigTester:
    """Test different search configurations against Elasticsearch."""

    def __init__(
        self,
        es_url: str,
        es_index: str,
        verbose: bool = True,
    ):
        self.es_url = es_url
        self.es_index = es_index
        self.verbose = verbose
        self._backends: dict[str, ElasticsearchBackend] = {}

    def log(self, message: str) -> None:
        """Print message if verbose mode is on."""
        if self.verbose:
            print(message)

    async def _get_backend(self, config: SearchConfiguration) -> ElasticsearchBackend:
        """Get or create an Elasticsearch backend for a configuration."""
        config_key = f"{config.hybrid_enabled}_{config.vector_weight}_{config.bm25_weight}_{config.top_k}"

        if config_key not in self._backends:
            es_config = ElasticsearchConfig(
                url=self.es_url,
                index=self.es_index,
                search_fields=config.search_fields,
                hybrid_enabled=config.hybrid_enabled,
                vector_weight=config.vector_weight,
                bm25_weight=config.bm25_weight,
            )
            self._backends[config_key] = ElasticsearchBackend(es_config)

        return self._backends[config_key]

    async def search(
        self,
        query: str,
        config: SearchConfiguration,
    ) -> list[str]:
        """
        Run search with a specific configuration.

        Args:
            query: Search query.
            config: Search configuration to use.

        Returns:
            List of retrieved document titles.
        """
        backend = await self._get_backend(config)

        result = await backend.search(
            query=query,
            max_results=config.top_k,
        )

        if result.error:
            self.log(f"  Search error: {result.error}")
            return []

        return [doc.title for doc in result.results if doc.title]

    async def close(self) -> None:
        """Close all backends."""
        for backend in self._backends.values():
            await backend.close()
        self._backends.clear()

    async def compare_standard_configs(
        self,
        questions: list[GoldenQuestion],
    ) -> dict[str, Any]:
        """
        Compare all standard search configurations.

        Args:
            questions: Golden questions to test on.

        Returns:
            Comparison results.
        """
        self.log("\n" + "=" * 70)
        self.log("SEARCH CONFIGURATION COMPARISON")
        self.log("=" * 70)
        self.log(f"Testing {len(questions)} questions across {len(SEARCH_CONFIGURATIONS)} configurations")

        comparison = SearchMethodComparison(search_fn=self.search)
        report = await comparison.compare_all_standard_configs(questions)

        # Print formatted report
        print(comparison.format_comparison_report(report))

        # Return structured results
        return {
            "evaluation_type": "search_comparison",
            "timestamp": datetime.utcnow().isoformat(),
            "total_questions": len(questions),
            "configurations": [
                {
                    "name": cfg.name,
                    "description": cfg.description,
                    "hybrid_enabled": cfg.hybrid_enabled,
                    "vector_weight": cfg.vector_weight,
                    "bm25_weight": cfg.bm25_weight,
                }
                for cfg in report.configurations
            ],
            "results": {
                name: {
                    "metrics": result.metrics,
                }
                for name, result in report.results.items()
            },
            "best_by_metric": report.best_by_metric,
        }

    async def run_weight_sweep(
        self,
        questions: list[GoldenQuestion],
        steps: int = 10,
        optimize_for: str = "mrr",
    ) -> dict[str, Any]:
        """
        Sweep over vector/BM25 weight combinations to find optimal settings.

        Args:
            questions: Golden questions to test on.
            steps: Number of steps (e.g., 10 = test at 0%, 10%, 20%, ..., 100%).
            optimize_for: Metric to optimize for.

        Returns:
            Sweep results including optimal weights.
        """
        self.log("\n" + "=" * 70)
        self.log("WEIGHT SWEEP")
        self.log("=" * 70)
        self.log(f"Testing {steps + 1} weight combinations on {len(questions)} questions")
        self.log(f"Optimizing for: {optimize_for}")

        sweep = ParameterSweep(search_fn=self.search)
        configs = sweep.generate_weight_sweep_configs(steps)

        self.log(f"\nConfigurations to test:")
        for cfg in configs:
            self.log(f"  - {cfg.name}: {int(cfg.vector_weight*100)}% vector, {int(cfg.bm25_weight*100)}% BM25")

        comparison = SearchMethodComparison(search_fn=self.search)
        report = await comparison.compare_configurations(configs, questions)

        # Print formatted report
        print(comparison.format_comparison_report(report))

        # Find optimal weights
        ranking = report.get_ranking(optimize_for)
        if ranking:
            best_name, best_score = ranking[0]
            best_config = report.results[best_name].configuration

            self.log("\n" + "-" * 70)
            self.log(f"OPTIMAL WEIGHTS (optimized for {optimize_for})")
            self.log("-" * 70)
            self.log(f"Configuration: {best_name}")
            self.log(f"Vector weight: {best_config.vector_weight:.2f} ({int(best_config.vector_weight*100)}%)")
            self.log(f"BM25 weight: {best_config.bm25_weight:.2f} ({int(best_config.bm25_weight*100)}%)")
            self.log(f"Best {optimize_for}: {best_score:.4f}")
            self.log("-" * 70)

        return {
            "evaluation_type": "weight_sweep",
            "timestamp": datetime.utcnow().isoformat(),
            "total_questions": len(questions),
            "steps": steps,
            "optimize_for": optimize_for,
            "results": {
                name: {
                    "vector_weight": result.configuration.vector_weight,
                    "bm25_weight": result.configuration.bm25_weight,
                    "metrics": result.metrics,
                }
                for name, result in report.results.items()
            },
            "ranking": ranking,
            "optimal": {
                "vector_weight": best_config.vector_weight if ranking else 0.5,
                "bm25_weight": best_config.bm25_weight if ranking else 0.5,
                "score": best_score if ranking else 0.0,
            },
        }

    async def run_title_boost_sweep(
        self,
        questions: list[GoldenQuestion],
        boost_values: Optional[list[int]] = None,
    ) -> dict[str, Any]:
        """
        Sweep over title boost values.

        Args:
            questions: Golden questions to test on.
            boost_values: List of boost values to test.

        Returns:
            Sweep results.
        """
        if boost_values is None:
            boost_values = [1, 2, 3, 5, 10]

        self.log("\n" + "=" * 70)
        self.log("TITLE BOOST SWEEP")
        self.log("=" * 70)
        self.log(f"Testing title boost values: {boost_values}")
        self.log(f"On {len(questions)} questions")

        sweep = ParameterSweep(search_fn=self.search)
        configs = sweep.generate_boost_sweep_configs(boost_values)

        comparison = SearchMethodComparison(search_fn=self.search)
        report = await comparison.compare_configurations(configs, questions)

        # Print formatted report
        print(comparison.format_comparison_report(report))

        return {
            "evaluation_type": "title_boost_sweep",
            "timestamp": datetime.utcnow().isoformat(),
            "total_questions": len(questions),
            "boost_values": boost_values,
            "results": {
                name: {
                    "metrics": result.metrics,
                }
                for name, result in report.results.items()
            },
            "best_by_metric": report.best_by_metric,
        }

    async def run_top_k_sweep(
        self,
        questions: list[GoldenQuestion],
        k_values: Optional[list[int]] = None,
    ) -> dict[str, Any]:
        """
        Sweep over top_k values.

        Args:
            questions: Golden questions to test on.
            k_values: List of top_k values to test.

        Returns:
            Sweep results.
        """
        if k_values is None:
            k_values = [5, 10, 15, 20, 30]

        self.log("\n" + "=" * 70)
        self.log("TOP_K SWEEP")
        self.log("=" * 70)
        self.log(f"Testing top_k values: {k_values}")
        self.log(f"On {len(questions)} questions")

        sweep = ParameterSweep(search_fn=self.search)
        configs = sweep.generate_top_k_sweep_configs(k_values)

        comparison = SearchMethodComparison(search_fn=self.search)
        report = await comparison.compare_configurations(configs, questions)

        # Print formatted report
        print(comparison.format_comparison_report(report))

        return {
            "evaluation_type": "top_k_sweep",
            "timestamp": datetime.utcnow().isoformat(),
            "total_questions": len(questions),
            "k_values": k_values,
            "results": {
                name: {
                    "metrics": result.metrics,
                }
                for name, result in report.results.items()
            },
            "best_by_metric": report.best_by_metric,
        }


async def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Compare search configurations for Nora Search (DeepSearch)"
    )
    parser.add_argument(
        "--sweep",
        choices=["none", "weights", "title-boost", "top-k"],
        default="none",
        help="Type of parameter sweep to run (default: none, runs standard comparison)",
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=10,
        help="Number of steps for weight sweep (default: 10)",
    )
    parser.add_argument(
        "--optimize-for",
        type=str,
        default="mrr",
        help="Metric to optimize for in sweeps (default: mrr)",
    )
    parser.add_argument(
        "--category",
        type=str,
        help="Run only on specific category",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of questions to test",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file for results (JSON)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress verbose output",
    )

    args = parser.parse_args()

    # Get Elasticsearch settings from environment
    es_url = os.getenv("ES_URL", "http://localhost:9200")
    es_index = os.getenv("ES_INDEX", "demo_confluence_kb")

    print("=" * 70)
    print("Search Configuration Comparison")
    print("=" * 70)
    print(f"Elasticsearch URL: {es_url}")
    print(f"Elasticsearch Index: {es_index}")

    # Load golden dataset
    dataset = GoldenDataset()
    print(f"\nGolden dataset loaded: {len(dataset)} questions")
    print(f"Categories: {dataset.categories()}")

    # Filter questions
    if args.category:
        questions = dataset.get_by_category(args.category)
        print(f"Filtered to category '{args.category}': {len(questions)} questions")
    else:
        questions = dataset.questions

    if args.limit:
        questions = questions[:args.limit]
        print(f"Limited to {len(questions)} questions")

    # Create tester
    tester = SearchConfigTester(
        es_url=es_url,
        es_index=es_index,
        verbose=not args.quiet,
    )

    try:
        # Run appropriate evaluation
        if args.sweep == "weights":
            results = await tester.run_weight_sweep(
                questions=questions,
                steps=args.steps,
                optimize_for=args.optimize_for,
            )
        elif args.sweep == "title-boost":
            results = await tester.run_title_boost_sweep(questions=questions)
        elif args.sweep == "top-k":
            results = await tester.run_top_k_sweep(questions=questions)
        else:
            # Standard comparison
            results = await tester.compare_standard_configs(questions=questions)

        # Save results if output specified
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, default=str)

            print(f"\nResults saved to: {output_path}")

    finally:
        await tester.close()

    print("\nComparison complete.")


if __name__ == "__main__":
    asyncio.run(main())
