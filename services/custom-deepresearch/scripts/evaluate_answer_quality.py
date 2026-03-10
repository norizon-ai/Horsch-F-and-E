#!/usr/bin/env python3
"""
Answer Quality Evaluation Script for Nora Search (DeepSearch).

Two-phase evaluation with idempotent re-runs:
1. SEARCH phase: Run all queries in parallel, save results
2. JUDGE phase: Evaluate answers sequentially, update same file

Usage:
    # Full run (search + judge)
    python scripts/evaluate_answer_quality.py --limit 10

    # Continue/re-run existing evaluation (idempotent)
    python scripts/evaluate_answer_quality.py --output results/evaluation_20260122.json

    # Search only (no judging)
    python scripts/evaluate_answer_quality.py --search-only --limit 10

    # Judge only (requires existing file with search results)
    python scripts/evaluate_answer_quality.py --judge-only --output results/evaluation_20260122.json
"""

import argparse
import asyncio
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import httpx

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from deepsearch.llm import create_llm_provider
from tests.evaluation import (
    GoldenDataset,
    GoldenQuestion,
    RigorousEvaluator,
)


class EvaluationRunner:
    """Two-phase evaluation: parallel search, then sequential judging."""

    def __init__(
        self,
        api_url: str,
        dataset: GoldenDataset,
        output_path: Path,
        verbose: bool = True,
        concurrency: int = 5,
    ):
        self.api_url = api_url.rstrip("/")
        self.dataset = dataset
        self.output_path = output_path
        self.verbose = verbose
        self.concurrency = concurrency
        self.http_client: Optional[httpx.AsyncClient] = None

    def log(self, message: str) -> None:
        if self.verbose:
            print(message)

    def load_results(self) -> dict[str, Any]:
        """Load existing results or create new structure."""
        if self.output_path.exists():
            with open(self.output_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "search_completed": False,
            "judge_completed": False,
            "total": 0,
            "passed": 0,
            "pass_rate": 0.0,
            "mean_score": 0.0,
            "results": [],
        }

    def save_results(self, data: dict[str, Any]) -> None:
        """Save results to JSON."""
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    async def run_single_search(
        self,
        question: GoldenQuestion,
        semaphore: asyncio.Semaphore,
    ) -> dict[str, Any]:
        """Run a single search query with concurrency control."""
        async with semaphore:
            endpoint = f"{self.api_url}/api/v1/search/sync"
            start_time = time.time()

            try:
                response = await self.http_client.post(
                    endpoint,
                    json={"query": question.question},
                )
                response.raise_for_status()
                data = response.json()

                latency_ms = (time.time() - start_time) * 1000

                # Extract data
                answer = data.get("final_report") or data.get("concise_answer") or ""
                confidence = data.get("confidence_score", 0.0)
                iterations = data.get("total_iterations", 0)

                # Extract sources
                sources = [s.get("title", "") for s in data.get("sources", [])]
                source_content = [
                    s.get("snippet", "")
                    for s in data.get("sources", [])
                    if s.get("snippet")
                ]

                # Build context for evaluation
                context = (
                    "\n\n---\n\n".join(
                        [
                            f"[Quelle: {sources[i] if i < len(sources) else 'Unbekannt'}]\n{content}"
                            for i, content in enumerate(source_content)
                        ]
                    )
                    if source_content
                    else ""
                )

                self.log(f"  ✓ {question.id}: {latency_ms:.0f}ms, {len(sources)} sources")

                return {
                    "question_id": question.id,
                    "question": question.question,
                    "category": question.category,
                    "answer": answer,
                    "confidence": confidence,
                    "sources": sources,
                    "context": context,
                    "latency_ms": latency_ms,
                    "iterations": iterations,
                    "search_success": True,
                    "search_error": None,
                    "search_timestamp": datetime.now(timezone.utc).isoformat(),
                }

            except Exception as e:
                latency_ms = (time.time() - start_time) * 1000
                self.log(f"  ✗ {question.id}: {e}")
                return {
                    "question_id": question.id,
                    "question": question.question,
                    "category": question.category,
                    "answer": "",
                    "confidence": 0.0,
                    "sources": [],
                    "context": "",
                    "latency_ms": latency_ms,
                    "iterations": 0,
                    "search_success": False,
                    "search_error": str(e),
                    "search_timestamp": datetime.now(timezone.utc).isoformat(),
                }

    async def phase_search(
        self,
        questions: list[GoldenQuestion],
        existing_data: dict[str, Any],
    ) -> dict[str, Any]:
        """Phase 1: Run all searches in parallel."""
        self.log("\n" + "=" * 70)
        self.log("PHASE 1: SEARCH (parallel)")
        self.log("=" * 70)

        # Build map of existing results by question_id
        existing_by_id = {r["question_id"]: r for r in existing_data.get("results", [])}

        # Determine which questions need searching
        questions_to_search = []
        for q in questions:
            existing = existing_by_id.get(q.id)
            if existing and existing.get("search_success"):
                self.log(f"  ⏭ {q.id}: already searched, skipping")
            else:
                questions_to_search.append(q)

        if not questions_to_search:
            self.log("\nAll questions already searched. Skipping search phase.")
            return existing_data

        self.log(f"\nSearching {len(questions_to_search)} questions (concurrency={self.concurrency})...\n")

        # Create HTTP client and semaphore
        self.http_client = httpx.AsyncClient(timeout=120.0)
        semaphore = asyncio.Semaphore(self.concurrency)

        try:
            # Run all searches in parallel
            start_time = time.time()
            tasks = [self.run_single_search(q, semaphore) for q in questions_to_search]
            new_results = await asyncio.gather(*tasks)
            total_time = time.time() - start_time

            # Merge new results with existing
            for result in new_results:
                existing_by_id[result["question_id"]] = result

            # Rebuild results list in question order
            all_results = [existing_by_id.get(q.id, {}) for q in questions]
            all_results = [r for r in all_results if r]  # Filter out empty

            # Update data
            existing_data["results"] = all_results
            existing_data["search_completed"] = True
            existing_data["search_timestamp"] = datetime.now(timezone.utc).isoformat()
            existing_data["total"] = len(all_results)

            # Save immediately
            self.save_results(existing_data)

            # Summary
            success_count = sum(1 for r in new_results if r.get("search_success"))
            self.log(f"\nSearch complete: {success_count}/{len(new_results)} successful in {total_time:.1f}s")
            self.log(f"Saved to: {self.output_path}")

        finally:
            await self.http_client.aclose()
            self.http_client = None

        return existing_data

    async def phase_judge(
        self,
        judge_llm: Any,
        existing_data: dict[str, Any],
    ) -> dict[str, Any]:
        """Phase 2: Judge answers sequentially."""
        self.log("\n" + "=" * 70)
        self.log("PHASE 2: JUDGE (sequential)")
        self.log("=" * 70)
        self.log("Hard fail: language_match, direct_resolution")
        self.log("Pass threshold: 0.7")
        self.log("=" * 70)

        evaluator = RigorousEvaluator(judge_llm)
        results = existing_data.get("results", [])

        # Count how many need judging
        to_judge = [r for r in results if "overall_pass" not in r and r.get("search_success")]
        already_judged = [r for r in results if "overall_pass" in r]

        self.log(f"\nAlready judged: {len(already_judged)}")
        self.log(f"To judge: {len(to_judge)}")

        if not to_judge:
            self.log("\nAll results already judged. Skipping judge phase.")
            return existing_data

        self.log("")

        for i, result in enumerate(results):
            qid = result.get("question_id", "?")

            # Skip if already judged
            if "overall_pass" in result:
                continue

            # Skip if search failed
            if not result.get("search_success") or not result.get("answer"):
                result["overall_pass"] = False
                result["overall_score"] = 0.0
                result["failure_reasons"] = [f"Search failed: {result.get('search_error', 'No answer')}"]
                result["dimensions"] = {}
                result["judge_timestamp"] = datetime.now(timezone.utc).isoformat()
                self.save_results(existing_data)
                continue

            self.log(f"[{i+1}/{len(results)}] Judging {qid}...")
            self.log(f"  Q: {result['question'][:60]}...")
            self.log(f"  A: {result['answer'][:100]}...")

            try:
                report = await evaluator.evaluate(
                    question_id=qid,
                    question=result["question"],
                    answer=result["answer"],
                    context=result.get("context", ""),
                )

                # Add judgment fields
                result["overall_pass"] = report.overall_pass
                result["overall_score"] = report.overall_score
                result["failure_reasons"] = report.failure_reasons
                result["dimensions"] = {k: v.to_dict() for k, v in report.dimensions.items()}
                result["judge_timestamp"] = datetime.now(timezone.utc).isoformat()

                status = "✓ PASS" if report.overall_pass else "✗ FAIL"
                self.log(f"  {status} (score: {report.overall_score:.2f})")

            except Exception as e:
                self.log(f"  ✗ Judge error: {e}")
                result["overall_pass"] = False
                result["overall_score"] = 0.0
                result["failure_reasons"] = [f"Judge error: {e}"]
                result["dimensions"] = {}
                result["judge_timestamp"] = datetime.now(timezone.utc).isoformat()

            # Save after each judgment (crash recovery)
            self.save_results(existing_data)
            self.log("")

        # Final aggregation
        judged = [r for r in results if "overall_pass" in r]
        passed = sum(1 for r in judged if r.get("overall_pass"))
        total = len(judged)
        mean_score = sum(r.get("overall_score", 0) for r in judged) / total if total > 0 else 0

        existing_data["judge_completed"] = True
        existing_data["judge_timestamp"] = datetime.now(timezone.utc).isoformat()
        existing_data["total"] = total
        existing_data["passed"] = passed
        existing_data["pass_rate"] = passed / total if total > 0 else 0
        existing_data["mean_score"] = mean_score

        self.save_results(existing_data)

        return existing_data

    def print_summary(self, data: dict[str, Any]) -> None:
        """Print final summary."""
        self.log("\n" + "=" * 70)
        self.log("SUMMARY")
        self.log("=" * 70)
        self.log(f"Total:      {data.get('total', 0)}")
        self.log(f"Passed:     {data.get('passed', 0)} ({data.get('pass_rate', 0)*100:.1f}%)")
        self.log(f"Mean score: {data.get('mean_score', 0):.2f}")
        self.log("=" * 70)
        self.log(f"\nResults: {self.output_path}")


async def main():
    parser = argparse.ArgumentParser(
        description="Evaluate answer quality for Nora Search (two-phase, idempotent)"
    )
    parser.add_argument("--api-url", default="http://localhost:8000", help="API URL")
    parser.add_argument("--dataset", type=str, help="Path to golden_answers.yaml")
    parser.add_argument("--category", type=str, help="Filter by category")
    parser.add_argument("--limit", type=int, help="Limit questions")
    parser.add_argument("--output", type=str, help="Output file (for continuing previous run)")
    parser.add_argument("--concurrency", type=int, default=5, help="Parallel search requests")
    parser.add_argument("--search-only", action="store_true", help="Only run search phase")
    parser.add_argument("--judge-only", action="store_true", help="Only run judge phase")
    parser.add_argument("--quiet", action="store_true", help="Less output")
    args = parser.parse_args()

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = Path(f"results/evaluation_{timestamp}.json")

    # Load dataset
    dataset = GoldenDataset(args.dataset) if args.dataset else GoldenDataset()
    print(f"Loaded {len(dataset)} questions from: {dataset.yaml_path}")

    # Filter questions
    if args.category:
        questions = dataset.get_by_category(args.category)
        print(f"Filtered to category '{args.category}': {len(questions)} questions")
    else:
        questions = dataset.questions

    if args.limit:
        questions = questions[: args.limit]
        print(f"Limited to {len(questions)} questions")

    # Create runner
    runner = EvaluationRunner(
        api_url=args.api_url,
        dataset=dataset,
        output_path=output_path,
        verbose=not args.quiet,
        concurrency=args.concurrency,
    )

    # Load existing results (for idempotent re-runs)
    data = runner.load_results()

    # Phase 1: Search
    if not args.judge_only:
        data = await runner.phase_search(questions, data)

    # Phase 2: Judge
    if not args.search_only:
        # Get OpenAI API key
        openai_key = os.getenv("OPENAI_API_KEY")
        if not openai_key:
            print("ERROR: OPENAI_API_KEY environment variable not set")
            sys.exit(1)

        print("\nInitializing judge LLM (gpt-4o-mini)...")
        judge_llm = create_llm_provider(
            provider_type="openai",
            base_url="https://api.openai.com/v1",
            api_key=openai_key,
            model="gpt-4o-mini",
            timeout=60,
        )

        try:
            data = await runner.phase_judge(judge_llm, data)
        finally:
            await judge_llm.close()

    # Print summary
    runner.print_summary(data)


if __name__ == "__main__":
    asyncio.run(main())
