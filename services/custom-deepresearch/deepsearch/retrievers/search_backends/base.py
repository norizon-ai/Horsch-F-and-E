"""
Search Backend Base Interface

Defines the abstract interface for pluggable search backends.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from deepsearch.models import SearchResult, SearchQuery, SearchResponse
from deepsearch.observability import get_logger

logger = get_logger(__name__)


class SearchBackendConfig(BaseModel):
    """Base configuration for search backends."""

    timeout: int = 30
    max_retries: int = 3
    retry_delay: float = 1.0

    model_config = ConfigDict(extra="allow")


class SearchBackend(ABC):
    """
    Abstract interface for search backends.

    Implementations must provide ``search``, ``health_check``, and
    ``backend_name``.  Backends can be used as async context managers.

    Example:
        async with MyBackend(config) as backend:
            response = await backend.search("query", max_results=5)
    """

    def __init__(self, config: Optional[SearchBackendConfig] = None):
        self.config = config or SearchBackendConfig()

    @property
    @abstractmethod
    def backend_name(self) -> str:
        """Unique name for this backend."""
        ...

    @abstractmethod
    async def search(
        self,
        query: str,
        max_results: int = 10,
        filters: Optional[Dict[str, Any]] = None,
    ) -> SearchResponse:
        """
        Execute a search query.

        Args:
            query: The search query string.
            max_results: Maximum number of results to return.
            filters: Optional filters to apply.

        Returns:
            A SearchResponse with results and metadata.
        """
        ...

    @abstractmethod
    async def health_check(self) -> bool:
        """Check if the backend is healthy and reachable."""
        ...

    async def close(self) -> None:
        """Close any open connections. Override if cleanup is needed."""
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()
