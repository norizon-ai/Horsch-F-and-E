"""
Search methods for Elasticsearch.

Modular search implementations (BM25, vector, hybrid) with clean interfaces.
Used by both the benchmark system and production agents.
"""

from .base import SearchMethod
from .bm25 import BM25Search
from .vector import VectorSearch
from .hybrid import HybridSearch

__all__ = [
    "SearchMethod",
    "BM25Search",
    "VectorSearch",
    "HybridSearch",
]
