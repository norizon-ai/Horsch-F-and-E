from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class RawArticleSource(BaseModel):
    """Defines the source of the raw article data."""
    uri: str = Field(..., description="The original URI of the document.")
    module: str = Field(..., description="The name of the connector that ingested this, e.g., 'Intranet Connector'.")
    retrieved_at: datetime = Field(default_factory=datetime.utcnow, description="Timestamp when the data was retrieved by the connector.")

class RawArticleAuthor(BaseModel):
    """Represents the author as extracted from the source."""
    name: str = Field(..., description="The author's name as it appears in the source.")
    # The connector likely doesn't know the internal user_id, so we omit it here.

class RawArticle(BaseModel):
    """
    The message model for raw data published by a connector to the message queue.
    This contains the essential information for the ingestion worker to process.
    """
    source_document_id: str = Field(..., description="A unique identifier for the document within its original source (e.g., page ID, article slug).")
    content: str = Field(..., description="The full text content of the article.")
    source: RawArticleSource
    author: Optional[RawArticleAuthor] = Field(None, description="Author of the document, if available.")
    tags: List[str] = Field(default_factory=list, description="A list of tags or keywords extracted from the source.")
    permissions: List[str] = Field(default_factory=list, description="A list of permission strings defining access control.")
    metadata: dict = Field(default_factory=dict, description="Any other relevant metadata from the source, like original creation/update dates.")