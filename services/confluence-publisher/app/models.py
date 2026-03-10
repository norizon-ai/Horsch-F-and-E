"""
Confluence Publisher - Request/Response models.
"""

from pydantic import BaseModel, Field
from typing import Dict, Any, List, Optional


class PublishRequest(BaseModel):
    """Request to publish a protocol to Confluence."""

    protocol: Dict[str, Any]
    space_key: Optional[str] = None


class PublishResponse(BaseModel):
    """Response after publishing to Confluence."""

    success: bool
    confluence_url: str
    page_id: str


class ExportPdfRequest(BaseModel):
    """Request to export a protocol as PDF."""

    protocol: Dict[str, Any]


class UserSuggestion(BaseModel):
    """User from LDAP/AD."""

    id: str
    name: str
    email: str
    department: Optional[str] = None


class UsersSearchResponse(BaseModel):
    """User search results."""

    users: List[UserSuggestion]


class ConfluenceSpace(BaseModel):
    """A Confluence space."""

    id: str
    key: str
    name: str
    icon: str
    type: str = "global"


class ConfluencePage(BaseModel):
    """A Confluence page in a space."""

    id: str
    title: str
    parent_id: Optional[str] = Field(None, alias="parentId")
    has_children: bool = Field(default=False, alias="hasChildren")

    model_config = {"populate_by_name": True}


class SpacesResponse(BaseModel):
    """Response containing list of Confluence spaces."""

    spaces: List[ConfluenceSpace]


class PagesResponse(BaseModel):
    """Response containing list of pages in a space."""

    pages: List[ConfluencePage]
