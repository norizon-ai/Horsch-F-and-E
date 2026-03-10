"""
Search Backends

Pluggable search backend implementations.

Usage:
    from deepsearch.retrievers.search_backends import (
        SearchBackend,
        SearchBackendConfig,
        ElasticsearchBackend,
        ElasticsearchConfig,
    )
"""

from .base import SearchBackend, SearchBackendConfig
from .elasticsearch import ElasticsearchBackend, ElasticsearchConfig

__all__ = [
    "SearchBackend",
    "SearchBackendConfig",
    "ElasticsearchBackend",
    "ElasticsearchConfig",
]
