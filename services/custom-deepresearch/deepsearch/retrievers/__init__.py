"""
Retrievers Module

Tools for document retrieval with modular search pipelines.

Usage:
    from deepsearch.retrievers import SearchPipeline, SearchPipelineBuilder
    from deepsearch.retrievers.search_methods import BM25Search, HybridSearch
    from deepsearch.retrievers.preprocessors import StopwordRemover, KeywordExtractor
    from deepsearch.retrievers.preprocessors import SemanticRerankerTransform

    # Create pipeline using builder
    pipeline = (
        SearchPipelineBuilder()
        .with_search_method(HybridSearch(...))
        .with_stopwords(["english", "german"])
        .with_keywords(max_terms=8)
        .with_reranker(top_k=10)
        .build()
    )

    # Or create directly
    pipeline = SearchPipeline(
        search_method=BM25Search(es_client, index, fields),
        preprocessors=[StopwordRemover(), KeywordExtractor()],
        postprocessors=[SemanticRerankerTransform(top_k=10)],
    )

    # Execute search
    results = await pipeline.search("what is the RC-3000 error")
"""

from .base import BaseRetriever
from .search_pipeline import SearchPipeline, SearchPipelineBuilder
from .search_backends import (
    SearchBackend,
    SearchBackendConfig,
    ElasticsearchBackend,
    ElasticsearchConfig,
)
from .preprocessors import ResultTransform, SemanticRerankerTransform

__all__ = [
    # Base
    "BaseRetriever",
    # Search Pipeline
    "SearchPipeline",
    "SearchPipelineBuilder",
    # Search Backends
    "SearchBackend",
    "SearchBackendConfig",
    "ElasticsearchBackend",
    "ElasticsearchConfig",
    # Result Transforms (postprocessors)
    "ResultTransform",
    "SemanticRerankerTransform",
]
