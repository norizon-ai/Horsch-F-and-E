"""
search-related data models.

Models for search answers, types, and related structures.
"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, List
from enum import Enum

from .search import SearchResult


class searchType(str, Enum):
    """Types of search strategies."""

    ZERO_SHOT = "zero_shot"
    DOCS_ONLY = "docs_only"
    TICKETS_ONLY = "tickets_only"
    HYBRID = "hybrid"
    CUSTOM = "custom"


class searchAnswer(BaseModel):
    """
    A search answer from a single retriever/search strategy.

    Each retriever produces a searchAnswer with its findings.
    """

    search_type: searchType = Field(..., description="Type of search performed")
    answer: str = Field(..., description="Generated answer text")
    confidence: float = Field(
        ..., ge=0.0, le=1.0, description="Confidence score (0.0-1.0)"
    )
    sources: List[SearchResult] = Field(
        default_factory=list, description="Sources used to generate answer"
    )
    reasoning: Optional[str] = Field(
        default=None, description="Reasoning behind the answer"
    )
    retriever_name: Optional[str] = Field(
        default=None, description="Name of the retriever that produced this answer"
    )

    model_config = ConfigDict(frozen=True)
