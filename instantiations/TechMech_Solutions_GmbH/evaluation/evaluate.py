#!/usr/bin/env python3
"""
Evaluate TechMech production Elasticsearch with BEIR metrics.

Uses:
- Existing TechMech ES index (no re-indexing)
- golden_answers.yaml for evaluation data
- All pipeline configurations for parameter tuning

Usage:
    # Quick test (10 questions, 3 configs)
    python evaluation/evaluate.py --limit 10 --config-set quick

    # Full benchmark (70 questions, 18 configs)
    python evaluation/evaluate.py --config-set comprehensive

    # Specific pipelines
    python evaluation/evaluate.py --pipelines bm25,vector_rerank

    # Compare reranker models (English vs German/multilingual)
    python evaluation/evaluate.py --config-set reranker_comparison --limit 20

    # Use specific reranker model
    python evaluation/evaluate.py --config-set reranker --reranker-model german
    python evaluation/evaluate.py --config-set reranker --reranker-model multilingual

Available reranker models:
    - english: cross-encoder/ms-marco-MiniLM-L-6-v2 (English-only, fast)
    - multilingual: cross-encoder/mmarco-mMiniLMv2-L12-H384-v1 (15 languages, default)
    - german: deepset/gbert-base-germandpr-reranking (German-specific)
    - bge-m3: BAAI/bge-reranker-v2-m3 (Multilingual, larger/better)
"""

import argparse
import asyncio
import json
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

import yaml

# Add paths for imports
TECHMECH_DIR = Path(__file__).parent.parent
PRODUCTS_DIR = TECHMECH_DIR.parent
REPO_ROOT = PRODUCTS_DIR.parent
sys.path.insert(0, str(PRODUCTS_DIR / "beir"))
sys.path.insert(0, str(REPO_ROOT / "services" / "custom-deepresearch"))

import httpx
from beir.retrieval.evaluation import EvaluateRetrieval
from sentence_transformers import SentenceTransformer

from deepsearch.retrievers import SearchPipeline
from deepsearch.retrievers.search_methods import BM25Search, VectorSearch, HybridSearch
from deepsearch.retrievers.preprocessors import (
    StopwordRemover,
    KeywordExtractor,
    SemanticRerankerTransform,
)
from pipeline_benchmark.configs import PipelineConfig, get_comprehensive_benchmark_configs
from pipeline_benchmark.results import BenchmarkResults, PipelineResult


# TechMech-specific configuration
TECHMECH_CONFIG = {
    "es_url": "http://localhost:9201",
    "index": "techmech_confluence_kb",
    "embedding_model": "sentence-transformers/all-MiniLM-L6-v2",
    # Field mappings (different from BEIR defaults)
    "content_field": "content",  # TechMech uses "content", not "text"
    "title_field": "title",
    "id_field": "_id",
    "url_field": "url",
    "vector_field": "vector",
    # Search field boosting (from agents.yaml)
    "search_fields": ["title^4", "headings^2", "content", "product_codes^3"],
    # Default reranker model - multilingual for German content
    "reranker_model": "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1",
}

# Available reranker models for comparison
RERANKER_MODELS = {
    "english": "cross-encoder/ms-marco-MiniLM-L-6-v2",  # English-only, fast
    "multilingual": "cross-encoder/mmarco-mMiniLMv2-L12-H384-v1",  # 15 languages
    "german": "deepset/gbert-base-germandpr-reranking",  # German-specific
    "bge-m3": "BAAI/bge-reranker-v2-m3",  # Multilingual, larger/better
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Evaluate TechMech Elasticsearch with BEIR metrics"
    )
    parser.add_argument(
        "--config-set",
        type=str,
        choices=["quick", "comprehensive", "reranker", "hybrid", "reranker_comparison"],
        default="quick",
        help="Config set: quick (3), comprehensive (18), reranker (4), hybrid (6), reranker_comparison (6)",
    )
    parser.add_argument(
        "--pipelines",
        type=str,
        default=None,
        help="Comma-separated pipeline names to test",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limit number of questions (for quick testing)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=10,
        help="Results to retrieve per query",
    )
    parser.add_argument(
        "--es-url",
        type=str,
        default=TECHMECH_CONFIG["es_url"],
        help="Elasticsearch URL",
    )
    parser.add_argument(
        "--reranker-model",
        type=str,
        default=None,
        choices=list(RERANKER_MODELS.keys()) + list(RERANKER_MODELS.values()),
        help=(
            "Reranker model to use. Can be a short name (english, multilingual, german, bge-m3) "
            "or full model path. Default: multilingual (cross-encoder/mmarco-mMiniLMv2-L12-H384-v1)"
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file for results",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress progress output",
    )
    return parser.parse_args()


def resolve_reranker_model(model_arg: Optional[str]) -> str:
    """
    Resolve reranker model argument to full model path.

    Args:
        model_arg: Short name (e.g., "german") or full path, or None for default

    Returns:
        Full model path (e.g., "deepset/gbert-base-germandpr-reranking")
    """
    if model_arg is None:
        return TECHMECH_CONFIG["reranker_model"]

    # Check if it's a short name
    if model_arg in RERANKER_MODELS:
        return RERANKER_MODELS[model_arg]

    # Otherwise assume it's a full model path
    return model_arg


async def resolve_page_titles_to_ids(
    es_client: httpx.AsyncClient,
    index: str,
    titles: List[str],
) -> Dict[str, List[str]]:
    """
    Search ES to find document IDs for expected_source_pages titles.

    Returns:
        Dict mapping title -> list of matching doc IDs
    """
    title_to_ids = {}

    for title in titles:
        # Search for documents with matching title
        query = {
            "query": {
                "match_phrase": {
                    "title": title
                }
            },
            "size": 10,  # Get multiple chunks of same page
            "_source": ["title"],
        }

        try:
            response = await es_client.post(f"/{index}/_search", json=query)
            data = response.json()

            doc_ids = []
            for hit in data.get("hits", {}).get("hits", []):
                doc_ids.append(hit["_id"])

            if doc_ids:
                title_to_ids[title] = doc_ids
            else:
                # Try fuzzy match if exact match fails
                fuzzy_query = {
                    "query": {
                        "match": {
                            "title": {
                                "query": title,
                                "fuzziness": "AUTO"
                            }
                        }
                    },
                    "size": 5,
                    "_source": ["title"],
                }
                response = await es_client.post(f"/{index}/_search", json=fuzzy_query)
                data = response.json()
                for hit in data.get("hits", {}).get("hits", []):
                    doc_ids.append(hit["_id"])
                if doc_ids:
                    title_to_ids[title] = doc_ids

        except Exception as e:
            print(f"Warning: Could not resolve title '{title}': {e}")

    return title_to_ids


async def load_golden_answers(
    yaml_path: Path,
    es_client: httpx.AsyncClient,
    index: str,
    limit: Optional[int] = None,
) -> Tuple[Dict[str, str], Dict[str, Dict[str, int]]]:
    """
    Load golden_answers.yaml and convert to BEIR format.

    Returns:
        queries: Dict[query_id, query_text]
        qrels: Dict[query_id, Dict[doc_id, relevance_score]]
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    questions = data.get("questions", [])
    if limit:
        questions = questions[:limit]

    # Collect all unique page titles
    all_titles = set()
    for q in questions:
        for title in q.get("expected_source_pages", []):
            all_titles.add(title)

    print(f"Resolving {len(all_titles)} page titles to document IDs...")
    title_to_ids = await resolve_page_titles_to_ids(es_client, index, list(all_titles))

    resolved_count = sum(1 for t in all_titles if t in title_to_ids)
    print(f"Resolved {resolved_count}/{len(all_titles)} titles")

    # Build queries and qrels
    queries = {}
    qrels = {}

    for q in questions:
        qid = q["id"]
        queries[qid] = q["question"]

        # Build relevance judgments
        qrels[qid] = {}
        for title in q.get("expected_source_pages", []):
            if title in title_to_ids:
                for doc_id in title_to_ids[title]:
                    qrels[qid][doc_id] = 1  # Binary relevance

    # Filter out queries with no relevant docs
    valid_queries = {qid: q for qid, q in queries.items() if qrels.get(qid)}
    valid_qrels = {qid: rel for qid, rel in qrels.items() if rel}

    print(f"Loaded {len(valid_queries)} queries with relevance judgments")

    return valid_queries, valid_qrels


def get_techmech_configs(
    config_set: str,
    reranker_model: Optional[str] = None,
) -> List[PipelineConfig]:
    """
    Get pipeline configs with TechMech field mappings.

    Args:
        config_set: Name of the config set to use
        reranker_model: Full path to reranker model (overrides defaults)

    Returns:
        List of PipelineConfig objects configured for TechMech
    """
    # Use default multilingual model if not specified
    default_reranker = reranker_model or TECHMECH_CONFIG["reranker_model"]

    # Base configs from BEIR
    if config_set == "quick":
        base_configs = [
            PipelineConfig(name="bm25", search_type="bm25"),
            PipelineConfig(name="vector", search_type="vector"),
            PipelineConfig(
                name="hybrid_60_40",
                search_type="hybrid",
                bm25_weight=0.6,
                vector_weight=0.4,
            ),
        ]
    elif config_set == "reranker":
        base_configs = [
            PipelineConfig(name="bm25", search_type="bm25"),
            PipelineConfig(
                name="bm25_rerank",
                search_type="bm25",
                postprocessors=["reranker"],
                reranker_model=default_reranker,
            ),
            PipelineConfig(
                name="hybrid_60_40",
                search_type="hybrid",
                bm25_weight=0.6,
                vector_weight=0.4,
            ),
            PipelineConfig(
                name="hybrid_60_40_rerank",
                search_type="hybrid",
                bm25_weight=0.6,
                vector_weight=0.4,
                postprocessors=["reranker"],
                reranker_model=default_reranker,
            ),
        ]
    elif config_set == "hybrid":
        base_configs = [
            PipelineConfig(name="bm25", search_type="bm25"),
            PipelineConfig(name="vector", search_type="vector"),
            PipelineConfig(name="hybrid_80_20", search_type="hybrid", bm25_weight=0.8, vector_weight=0.2),
            PipelineConfig(name="hybrid_60_40", search_type="hybrid", bm25_weight=0.6, vector_weight=0.4),
            PipelineConfig(name="hybrid_40_60", search_type="hybrid", bm25_weight=0.4, vector_weight=0.6),
            PipelineConfig(name="hybrid_20_80", search_type="hybrid", bm25_weight=0.2, vector_weight=0.8),
        ]
    elif config_set == "reranker_comparison":
        # Compare no reranker vs English vs multilingual/German rerankers
        base_configs = [
            # Baseline: no reranker
            PipelineConfig(name="hybrid_60_40_no_rerank", search_type="hybrid", bm25_weight=0.6, vector_weight=0.4),

            # English reranker (MS MARCO, English-only)
            PipelineConfig(
                name="hybrid_60_40_rerank_english",
                search_type="hybrid",
                bm25_weight=0.6,
                vector_weight=0.4,
                postprocessors=["reranker"],
                reranker_model=RERANKER_MODELS["english"],
            ),

            # Multilingual reranker (mMARCO, 15 languages)
            PipelineConfig(
                name="hybrid_60_40_rerank_multilingual",
                search_type="hybrid",
                bm25_weight=0.6,
                vector_weight=0.4,
                postprocessors=["reranker"],
                reranker_model=RERANKER_MODELS["multilingual"],
            ),

            # German-specific reranker (GermanDPR)
            PipelineConfig(
                name="hybrid_60_40_rerank_german",
                search_type="hybrid",
                bm25_weight=0.6,
                vector_weight=0.4,
                postprocessors=["reranker"],
                reranker_model=RERANKER_MODELS["german"],
            ),

            # Also test BM25 with rerankers for comparison
            PipelineConfig(name="bm25_no_rerank", search_type="bm25"),

            PipelineConfig(
                name="bm25_rerank_multilingual",
                search_type="bm25",
                postprocessors=["reranker"],
                reranker_model=RERANKER_MODELS["multilingual"],
            ),
        ]
    else:  # comprehensive
        base_configs = get_comprehensive_benchmark_configs()

    # Apply TechMech field mappings to all configs
    techmech_configs = []
    for config in base_configs:
        # Determine reranker model: use config's if set, else default
        config_reranker = config.reranker_model
        if "reranker" in config.postprocessors and config_reranker == "cross-encoder/ms-marco-MiniLM-L-6-v2":
            # Override default English model with our default (unless in reranker_comparison mode)
            if config_set != "reranker_comparison":
                config_reranker = default_reranker

        # Create new config with TechMech field mappings
        techmech_config = PipelineConfig(
            name=config.name,
            search_type=config.search_type,
            search_fields=TECHMECH_CONFIG["search_fields"],
            vector_field=TECHMECH_CONFIG["vector_field"],
            bm25_weight=config.bm25_weight,
            vector_weight=config.vector_weight,
            fuzziness=config.fuzziness,
            preprocessors=config.preprocessors,
            stopword_languages=config.stopword_languages,
            keyword_max_terms=config.keyword_max_terms,
            stemmer_language=config.stemmer_language,
            postprocessors=config.postprocessors,
            reranker_model=config_reranker,
            reranker_top_k=config.reranker_top_k,
            # TechMech-specific field mappings
            content_field=TECHMECH_CONFIG["content_field"],
            title_field=TECHMECH_CONFIG["title_field"],
            id_field=TECHMECH_CONFIG["id_field"],
            url_field=TECHMECH_CONFIG["url_field"],
        )
        techmech_configs.append(techmech_config)

    return techmech_configs


def create_techmech_pipeline(
    config: PipelineConfig,
    es_client: httpx.AsyncClient,
    embedding_model: Optional[SentenceTransformer],
) -> SearchPipeline:
    """Create a SearchPipeline with TechMech-specific configuration."""

    common_args = {
        "es_client": es_client,
        "index": TECHMECH_CONFIG["index"],
        "id_field": config.id_field,
        "title_field": config.title_field,
        "content_field": config.content_field,
        "url_field": config.url_field,
    }

    # Create search method
    if config.search_type == "bm25":
        search_method = BM25Search(
            **common_args,
            search_fields=config.search_fields,
            fuzziness=config.fuzziness,
        )
    elif config.search_type == "vector":
        if embedding_model is None:
            raise ValueError("Vector search requires embedding_model")
        search_method = VectorSearch(
            **common_args,
            vector_field=config.vector_field,
            embedding_model=embedding_model,
        )
    elif config.search_type == "hybrid":
        if embedding_model is None:
            raise ValueError("Hybrid search requires embedding_model")
        search_method = HybridSearch(
            **common_args,
            search_fields=config.search_fields,
            vector_field=config.vector_field,
            embedding_model=embedding_model,
            bm25_weight=config.bm25_weight,
            vector_weight=config.vector_weight,
            fuzziness=config.fuzziness,
        )
    else:
        raise ValueError(f"Unknown search type: {config.search_type}")

    # Create preprocessors
    preprocessors = []
    for prep in config.preprocessors:
        if prep == "stopwords":
            preprocessors.append(StopwordRemover(languages=config.stopword_languages))
        elif prep == "keywords":
            preprocessors.append(KeywordExtractor(max_terms=config.keyword_max_terms))

    # Create postprocessors
    postprocessors = []
    for post in config.postprocessors:
        if post == "reranker":
            postprocessors.append(
                SemanticRerankerTransform(
                    model_name=config.reranker_model,
                    top_k=config.reranker_top_k,
                )
            )

    return SearchPipeline(
        search_method=search_method,
        preprocessors=preprocessors if preprocessors else None,
        postprocessors=postprocessors if postprocessors else None,
    )


async def evaluate_pipeline(
    pipeline: SearchPipeline,
    config: PipelineConfig,
    queries: Dict[str, str],
    qrels: Dict[str, Dict[str, int]],
    top_k: int,
    verbose: bool = True,
) -> PipelineResult:
    """Evaluate a single pipeline."""

    if verbose:
        print(f"Evaluating: {config.name}")

    results: Dict[str, Dict[str, float]] = {}
    start_time = time.time()

    for i, (qid, query_text) in enumerate(queries.items()):
        if verbose and (i + 1) % 20 == 0:
            print(f"  Progress: {i + 1}/{len(queries)}")

        try:
            search_results = await pipeline.search(query_text, max_results=top_k)
            results[qid] = {r.id: r.score for r in search_results}
        except Exception as e:
            print(f"  Error on query {qid}: {e}")
            results[qid] = {}

    total_time = time.time() - start_time

    # Use BEIR evaluation
    evaluator = EvaluateRetrieval()
    ndcg, map_score, recall, precision = evaluator.evaluate(qrels, results, [1, 3, 5, 10])

    # Compute MRR
    mrr_sum = 0.0
    for query_id in qrels:
        if query_id not in results:
            continue
        sorted_docs = sorted(results[query_id].items(), key=lambda x: x[1], reverse=True)
        for rank, (doc_id, _) in enumerate(sorted_docs[:10], 1):
            if doc_id in qrels[query_id] and qrels[query_id][doc_id] > 0:
                mrr_sum += 1.0 / rank
                break
    mrr_10 = mrr_sum / len(qrels) if qrels else 0.0

    metrics = {
        "NDCG@1": ndcg.get("NDCG@1", 0),
        "NDCG@3": ndcg.get("NDCG@3", 0),
        "NDCG@5": ndcg.get("NDCG@5", 0),
        "NDCG@10": ndcg.get("NDCG@10", 0),
        "MAP@10": map_score.get("MAP@10", 0),
        "Recall@1": recall.get("Recall@1", 0),
        "Recall@3": recall.get("Recall@3", 0),
        "Recall@5": recall.get("Recall@5", 0),
        "Recall@10": recall.get("Recall@10", 0),
        "Precision@1": precision.get("P@1", 0),
        "Precision@10": precision.get("P@10", 0),
        "MRR@10": mrr_10,
        "total_queries": len(queries),
        "queries_per_second": len(queries) / total_time if total_time > 0 else 0,
    }

    if verbose:
        print(f"  NDCG@10: {metrics['NDCG@10']:.4f}, MRR@10: {metrics['MRR@10']:.4f}")

    return PipelineResult(
        pipeline_name=config.name,
        dataset="techmech_golden",
        metrics=metrics,
        config={
            "name": config.name,
            "search_type": config.search_type,
            "bm25_weight": config.bm25_weight,
            "vector_weight": config.vector_weight,
            "preprocessors": config.preprocessors,
            "postprocessors": config.postprocessors,
            "reranker_model": config.reranker_model if config.postprocessors else None,
        },
    )


def print_results_table(results: List[PipelineResult]):
    """Print results as a formatted table."""
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)

    # Sort by NDCG@10
    sorted_results = sorted(
        results,
        key=lambda r: r.metrics.get("NDCG@10", 0),
        reverse=True,
    )

    print(f"\n{'Pipeline':<35} {'NDCG@10':>10} {'MRR@10':>10} {'Recall@10':>10} {'q/s':>8}")
    print("-" * 80)

    for r in sorted_results:
        m = r.metrics
        print(
            f"{r.pipeline_name:<35} "
            f"{m.get('NDCG@10', 0):>10.4f} "
            f"{m.get('MRR@10', 0):>10.4f} "
            f"{m.get('Recall@10', 0):>10.4f} "
            f"{m.get('queries_per_second', 0):>8.1f}"
        )

    # Print best config
    best = sorted_results[0]
    print("\n" + "=" * 80)
    print("RECOMMENDATION")
    print("=" * 80)
    print(f"\nBest configuration: {best.pipeline_name}")
    print(f"  NDCG@10: {best.metrics.get('NDCG@10', 0):.4f}")
    print(f"  MRR@10: {best.metrics.get('MRR@10', 0):.4f}")
    print(f"  Recall@10: {best.metrics.get('Recall@10', 0):.4f}")


def save_tuned_config(results: List[PipelineResult], output_dir: Path):
    """Save the best configuration as a production-ready config file."""
    sorted_results = sorted(
        results,
        key=lambda r: r.metrics.get("NDCG@10", 0),
        reverse=True,
    )
    best = sorted_results[0]

    # Get reranker model from config, default to multilingual
    reranker_model = best.config.get("reranker_model") or TECHMECH_CONFIG["reranker_model"]

    config = {
        "search": {
            "type": best.config.get("search_type", "hybrid"),
            "bm25_weight": best.config.get("bm25_weight", 0.6),
            "vector_weight": best.config.get("vector_weight", 0.4),
            "fields": TECHMECH_CONFIG["search_fields"],
        },
        "preprocessors": {
            "enabled": best.config.get("preprocessors", []),
        },
        "reranker": {
            "enabled": "reranker" in best.config.get("postprocessors", []),
            "model": reranker_model,
            "top_k": 10,
        },
        "metrics": {
            "NDCG@10": best.metrics.get("NDCG@10", 0),
            "MRR@10": best.metrics.get("MRR@10", 0),
            "Recall@10": best.metrics.get("Recall@10", 0),
        },
        "tuned_on": datetime.now().isoformat(),
    }

    output_file = output_dir / "techmech_tuned_config.json"
    with open(output_file, "w") as f:
        json.dump(config, f, indent=2)

    print(f"\nTuned config saved to: {output_file}")


async def main():
    args = parse_args()

    # Resolve reranker model
    reranker_model = resolve_reranker_model(args.reranker_model)

    print("=" * 80)
    print("TechMech Elasticsearch Evaluation")
    print("=" * 80)
    print(f"ES URL: {args.es_url}")
    print(f"Index: {TECHMECH_CONFIG['index']}")
    print(f"Config set: {args.config_set}")
    if args.reranker_model or args.config_set in ("reranker", "reranker_comparison"):
        print(f"Reranker model: {reranker_model}")
    if args.limit:
        print(f"Query limit: {args.limit}")
    print()

    # Check ES connectivity
    try:
        async with httpx.AsyncClient(base_url=args.es_url, timeout=10.0) as client:
            response = await client.get("/_cluster/health")
            if response.status_code != 200:
                print(f"ERROR: Elasticsearch not healthy at {args.es_url}")
                return
            print("Elasticsearch connected")

            # Check index exists
            response = await client.head(f"/{TECHMECH_CONFIG['index']}")
            if response.status_code != 200:
                print(f"ERROR: Index '{TECHMECH_CONFIG['index']}' not found")
                return
            print(f"Index '{TECHMECH_CONFIG['index']}' found")
    except Exception as e:
        print(f"ERROR: Cannot connect to Elasticsearch: {e}")
        print("Make sure TechMech ES is running on port 9201")
        return

    # Load golden answers
    golden_path = TECHMECH_DIR / "deepsearch" / "golden_answers.yaml"
    if not golden_path.exists():
        print(f"ERROR: Golden answers not found at {golden_path}")
        return

    async with httpx.AsyncClient(base_url=args.es_url, timeout=60.0) as es_client:
        queries, qrels = await load_golden_answers(
            golden_path, es_client, TECHMECH_CONFIG["index"], args.limit
        )

        if not queries:
            print("ERROR: No valid queries loaded")
            return

        print(f"\nLoaded {len(queries)} evaluation queries")

        # Get configs
        configs = get_techmech_configs(args.config_set, reranker_model)
        if args.pipelines:
            names = [n.strip() for n in args.pipelines.split(",")]
            configs = [c for c in configs if c.name in names]

        print(f"Testing {len(configs)} pipeline configurations")

        # Load embedding model for vector/hybrid search
        needs_embeddings = any(c.search_type in ("vector", "hybrid") for c in configs)
        embedding_model = None
        if needs_embeddings:
            print(f"\nLoading embedding model: {TECHMECH_CONFIG['embedding_model']}")
            embedding_model = SentenceTransformer(TECHMECH_CONFIG["embedding_model"])

        # Run evaluation
        results = []
        for config in configs:
            # Skip vector/hybrid if no embedding model
            if config.search_type in ("vector", "hybrid") and embedding_model is None:
                print(f"Skipping {config.name} (no embedding model)")
                continue

            try:
                pipeline = create_techmech_pipeline(config, es_client, embedding_model)
                result = await evaluate_pipeline(
                    pipeline,
                    config,
                    queries,
                    qrels,
                    args.top_k,
                    verbose=not args.quiet,
                )
                results.append(result)
            except Exception as e:
                print(f"Error evaluating {config.name}: {e}")

    if not results:
        print("No results to display")
        return

    # Print results
    print_results_table(results)

    # Save results
    output_dir = Path(__file__).parent / "results"
    output_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = args.output or (output_dir / f"techmech_eval_{timestamp}.json")

    benchmark_results = BenchmarkResults(results=results)
    benchmark_results.save(str(output_file))
    print(f"\nFull results saved to: {output_file}")

    # Save tuned config
    save_tuned_config(results, output_dir)


if __name__ == "__main__":
    asyncio.run(main())
