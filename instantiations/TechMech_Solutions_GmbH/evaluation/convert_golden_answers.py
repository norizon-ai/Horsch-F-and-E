#!/usr/bin/env python3
"""
Convert golden_answers.yaml to BEIR format.

Creates:
- queries.jsonl: Questions in BEIR format
- qrels/test.tsv: Relevance judgments (query_id -> doc_id -> score)

Usage:
    python convert_golden_answers.py --output data/techmech_beir

This is useful for:
- Running standard BEIR evaluation tools
- Comparing with other datasets
- Sharing evaluation data
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Dict, List, Set

import yaml
import httpx


TECHMECH_CONFIG = {
    "es_url": "http://localhost:9201",
    "index": "techmech_confluence_kb",
}


async def resolve_page_titles_to_ids(
    es_client: httpx.AsyncClient,
    index: str,
    titles: Set[str],
) -> Dict[str, List[str]]:
    """Search ES to find document IDs for page titles."""
    title_to_ids = {}

    for title in titles:
        query = {
            "query": {
                "match_phrase": {"title": title}
            },
            "size": 10,
            "_source": ["title"],
        }

        try:
            response = await es_client.post(f"/{index}/_search", json=query)
            data = response.json()

            doc_ids = [hit["_id"] for hit in data.get("hits", {}).get("hits", [])]

            if not doc_ids:
                # Try fuzzy match
                fuzzy_query = {
                    "query": {
                        "match": {
                            "title": {"query": title, "fuzziness": "AUTO"}
                        }
                    },
                    "size": 5,
                }
                response = await es_client.post(f"/{index}/_search", json=fuzzy_query)
                data = response.json()
                doc_ids = [hit["_id"] for hit in data.get("hits", {}).get("hits", [])]

            if doc_ids:
                title_to_ids[title] = doc_ids
            else:
                print(f"Warning: No docs found for title '{title}'")

        except Exception as e:
            print(f"Error resolving '{title}': {e}")

    return title_to_ids


async def convert_golden_to_beir(
    golden_path: Path,
    output_dir: Path,
    es_url: str,
    index: str,
):
    """Convert golden_answers.yaml to BEIR format."""

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "qrels").mkdir(exist_ok=True)

    # Load golden answers
    with open(golden_path) as f:
        data = yaml.safe_load(f)

    questions = data.get("questions", [])
    print(f"Loaded {len(questions)} questions")

    # Collect all unique page titles
    all_titles = set()
    for q in questions:
        for title in q.get("expected_source_pages", []):
            all_titles.add(title)

    print(f"Resolving {len(all_titles)} page titles...")

    async with httpx.AsyncClient(base_url=es_url, timeout=60.0) as es_client:
        title_to_ids = await resolve_page_titles_to_ids(es_client, index, all_titles)

    resolved = sum(1 for t in all_titles if t in title_to_ids)
    print(f"Resolved {resolved}/{len(all_titles)} titles")

    # Write queries.jsonl
    queries_file = output_dir / "queries.jsonl"
    qrels_file = output_dir / "qrels" / "test.tsv"

    valid_queries = 0
    total_judgments = 0

    with open(queries_file, "w", encoding="utf-8") as qf, \
         open(qrels_file, "w", encoding="utf-8") as rf:

        rf.write("query-id\tcorpus-id\tscore\n")

        for q in questions:
            qid = q["id"]
            question = q["question"]

            # Check if we have any relevant docs
            has_relevant = False
            for title in q.get("expected_source_pages", []):
                if title in title_to_ids:
                    has_relevant = True
                    for doc_id in title_to_ids[title]:
                        rf.write(f"{qid}\t{doc_id}\t1\n")
                        total_judgments += 1

            if has_relevant:
                # Write query
                query_obj = {
                    "_id": qid,
                    "text": question,
                    "metadata": {
                        "category": q.get("category", ""),
                        "difficulty": q.get("difficulty", ""),
                        "space": q.get("space", ""),
                    },
                }
                qf.write(json.dumps(query_obj, ensure_ascii=False) + "\n")
                valid_queries += 1

    print(f"\nConversion complete:")
    print(f"  Queries: {valid_queries}")
    print(f"  Relevance judgments: {total_judgments}")
    print(f"  Output: {output_dir}")

    # Print usage instructions
    print(f"\nTo run BEIR evaluation:")
    print(f"  python scripts/evaluate_pipelines.py --dataset {output_dir.name} --data-dir {output_dir.parent}")


def main():
    parser = argparse.ArgumentParser(description="Convert golden_answers.yaml to BEIR format")
    parser.add_argument(
        "--input",
        type=Path,
        default=Path(__file__).parent.parent / "deepsearch" / "golden_answers.yaml",
        help="Path to golden_answers.yaml",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).parent / "data" / "techmech_beir",
        help="Output directory for BEIR format",
    )
    parser.add_argument(
        "--es-url",
        type=str,
        default=TECHMECH_CONFIG["es_url"],
        help="Elasticsearch URL",
    )
    parser.add_argument(
        "--index",
        type=str,
        default=TECHMECH_CONFIG["index"],
        help="Elasticsearch index name",
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"ERROR: Input file not found: {args.input}")
        sys.exit(1)

    asyncio.run(convert_golden_to_beir(
        args.input,
        args.output,
        args.es_url,
        args.index,
    ))


if __name__ == "__main__":
    main()
