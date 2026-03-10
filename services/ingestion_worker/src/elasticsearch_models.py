"""
Pydantic models for the 'knowledge_articles' Elasticsearch index.

This file defines the data structure for documents that will be stored in Elasticsearch.
These models are used by the Ingestion Worker to validate and serialize data before
indexing, and by the Search Service to structure queries and deserialize results.

The structure is based on the denormalized schema proposed in:
@services/database/_model_contexts/elastic_plan.md
"""

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Source(BaseModel):
    """Represents the origin of the knowledge article."""
    id: UUID
    uri: str
    module: str
    ingested_at: datetime


class Author(BaseModel):
    """Represents the creator of the content."""
    user_id: Optional[UUID] = None
    name: str


class AccessControl(BaseModel):
    """Defines who can access the document."""
    users: List[UUID] = Field(default_factory=list)
    groups: List[UUID] = Field(default_factory=list)


class Metadata(BaseModel):
    """Contains metadata about the document."""
    created_at: datetime
    updated_at: datetime
    version: int
    language: str
    is_verified: bool = False
    is_obsolete: bool = False


class Engagement(BaseModel):
    """Tracks user engagement metrics."""
    upvotes: int = 0
    downvotes: int = 0
    retrieval_count: int = 0


class Comment(BaseModel):
    """Represents a single comment on the document."""
    user: str
    timestamp: datetime
    comment: str


class KnowledgeArticle(BaseModel):
    """
    The main model for a document in the 'knowledge_articles' Elasticsearch index.
    This is a denormalized model designed for efficient searching and retrieval.
    """
    document_id: UUID
    content: str
    content_vector: List[float]
    source: Source
    author: Author
    access_control: AccessControl
    metadata: Metadata
    tags: List[str] = Field(default_factory=list)
    engagement: Engagement
    comments: List[Comment] = Field(default_factory=list)

    class Config:
        """Pydantic configuration."""
        from_attributes = True
