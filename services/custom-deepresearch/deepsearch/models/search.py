"""
Search-related data models.

These models are shared across all retrievers and search backends.
"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Dict, Any, List


class SearchResult(BaseModel):
    """
    Unified search result across all backends.

    This is the standard output format that all search backends must produce,
    regardless of whether they use Elasticsearch, ChromaDB, or other systems.
    """

    id: str = Field(..., description="Unique document identifier")
    title: str = Field(..., description="Document title")
    content: str = Field(..., description="Document content or snippet")
    score: float = Field(..., description="Relevance score (higher is better, can be negative for cross-encoder)")
    source_type: str = Field(..., description="Source type identifier (e.g., 'docs', 'tickets')")
    url: Optional[str] = Field(default=None, description="URL to original document")
    highlight: Optional[str] = Field(default=None, description="Highlighted snippet if available")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

    model_config = ConfigDict(frozen=True)


class SearchQuery(BaseModel):
    """
    Search query parameters.

    Used to pass search parameters from processors/retrievers to search backends.
    """

    query: str = Field(..., min_length=1, description="Search query string")
    max_results: int = Field(default=10, ge=1, le=100, description="Maximum results to return")
    filters: Dict[str, Any] = Field(default_factory=dict, description="Optional filters")
    fields: Optional[List[str]] = Field(default=None, description="Fields to search in")


class SearchResponse(BaseModel):
    """
    Search response wrapper.

    Contains results plus metadata about the search operation.
    """

    results: List[SearchResult] = Field(default_factory=list, description="Search results")
    total_found: int = Field(default=0, ge=0, description="Total matching documents")
    query: str = Field(..., description="Original query")
    search_time_ms: float = Field(default=0.0, ge=0.0, description="Search time in milliseconds")
    error: Optional[str] = Field(default=None, description="Error message if search failed")

    @property
    def success(self) -> bool:
        """Check if search was successful."""
        return self.error is None
