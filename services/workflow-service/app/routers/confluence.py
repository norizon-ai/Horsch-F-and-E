"""
Confluence router - Confluence space and page navigation.

Provides endpoints for browsing Confluence spaces and pages,
proxying requests to the confluence-publisher service.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import httpx
import logging

from app.config import get_settings

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/confluence", tags=["confluence"])


# ============================================================================
# Models
# ============================================================================

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


# ============================================================================
# Mock Data
# ============================================================================

MOCK_SPACES = [
    ConfluenceSpace(id="1", key="MARKETING", name="Marketing", icon="briefcase"),
    ConfluenceSpace(id="2", key="ENGINEERING", name="Engineering", icon="code"),
    ConfluenceSpace(id="3", key="PRODUCT", name="Product Management", icon="layers"),
    ConfluenceSpace(id="4", key="HR", name="Human Resources", icon="users"),
    ConfluenceSpace(id="5", key="SALES", name="Sales", icon="trending-up"),
]

MOCK_PAGES = {
    "MARKETING": [
        ConfluencePage(id="m1", title="Q1 Planning", parent_id=None, has_children=True),
        ConfluencePage(id="m2", title="Campaigns", parent_id=None, has_children=True),
        ConfluencePage(id="m3", title="Meeting Protocols", parent_id=None, has_children=True),
        ConfluencePage(id="m4", title="Brand Guidelines", parent_id=None, has_children=False),
    ],
    "ENGINEERING": [
        ConfluencePage(id="e1", title="Sprint Reviews", parent_id=None, has_children=True),
        ConfluencePage(id="e2", title="Architecture Decisions", parent_id=None, has_children=True),
        ConfluencePage(id="e3", title="Team Meetings", parent_id=None, has_children=True),
        ConfluencePage(id="e4", title="Technical Documentation", parent_id=None, has_children=True),
    ],
    "PRODUCT": [
        ConfluencePage(id="p1", title="Roadmap", parent_id=None, has_children=True),
        ConfluencePage(id="p2", title="Stakeholder Meetings", parent_id=None, has_children=True),
        ConfluencePage(id="p3", title="User Research", parent_id=None, has_children=True),
        ConfluencePage(id="p4", title="Feature Specs", parent_id=None, has_children=True),
    ],
    "HR": [
        ConfluencePage(id="h1", title="Onboarding", parent_id=None, has_children=True),
        ConfluencePage(id="h2", title="Interview Notes", parent_id=None, has_children=True),
        ConfluencePage(id="h3", title="Team Events", parent_id=None, has_children=False),
        ConfluencePage(id="h4", title="Policies", parent_id=None, has_children=True),
    ],
    "SALES": [
        ConfluencePage(id="s1", title="Customer Calls", parent_id=None, has_children=True),
        ConfluencePage(id="s2", title="Product Demos", parent_id=None, has_children=True),
        ConfluencePage(id="s3", title="Pipeline Reviews", parent_id=None, has_children=True),
        ConfluencePage(id="s4", title="Proposals", parent_id=None, has_children=True),
    ],
}

# Nested pages (children)
MOCK_CHILD_PAGES = {
    "m1": [  # Q1 Planning children
        ConfluencePage(id="m1-1", title="Budget Planning", parent_id="m1", has_children=False),
        ConfluencePage(id="m1-2", title="Campaign Strategy", parent_id="m1", has_children=False),
    ],
    "m3": [  # Meeting Protocols children
        ConfluencePage(id="m3-1", title="Weekly Syncs", parent_id="m3", has_children=False),
        ConfluencePage(id="m3-2", title="Monthly Reviews", parent_id="m3", has_children=False),
    ],
    "e1": [  # Sprint Reviews children
        ConfluencePage(id="e1-1", title="Sprint 24", parent_id="e1", has_children=False),
        ConfluencePage(id="e1-2", title="Sprint 25", parent_id="e1", has_children=False),
    ],
    "e3": [  # Team Meetings children
        ConfluencePage(id="e3-1", title="Backend Team", parent_id="e3", has_children=False),
        ConfluencePage(id="e3-2", title="Frontend Team", parent_id="e3", has_children=False),
        ConfluencePage(id="e3-3", title="All Hands", parent_id="e3", has_children=False),
    ],
}


# ============================================================================
# Endpoints
# ============================================================================

@router.get("/spaces", response_model=SpacesResponse)
async def get_spaces():
    """
    Get list of available Confluence spaces.
    Proxies request to confluence-publisher service.
    """
    settings = get_settings()

    if settings.use_mocks:
        logger.info("Using mock Confluence spaces")
        return SpacesResponse(spaces=MOCK_SPACES)

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{settings.confluence_publisher_url}/internal/confluence/spaces",
                timeout=10.0,
            )
            response.raise_for_status()
            data = response.json()
            logger.info(f"Retrieved {len(data.get('spaces', []))} Confluence spaces")
            return SpacesResponse(**data)
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch Confluence spaces: {e}")
            # Fallback to mock data on error
            logger.info("Falling back to mock Confluence spaces")
            return SpacesResponse(spaces=MOCK_SPACES)


@router.get("/spaces/{space_key}/pages", response_model=PagesResponse)
async def get_pages(space_key: str, parent_id: Optional[str] = None):
    """
    Get pages in a Confluence space.

    Args:
        space_key: The space key (e.g., "MARKETING", "ENGINEERING")
        parent_id: Optional parent page ID to get children

    Returns:
        List of pages in the space (or children of the parent page)
    """
    settings = get_settings()

    if settings.use_mocks:
        logger.info(f"Using mock pages for space {space_key}")
        if parent_id:
            children = MOCK_CHILD_PAGES.get(parent_id, [])
            return PagesResponse(pages=children)
        pages = MOCK_PAGES.get(space_key.upper(), [])
        return PagesResponse(pages=pages)

    async with httpx.AsyncClient() as client:
        try:
            url = f"{settings.confluence_publisher_url}/internal/confluence/spaces/{space_key}/pages"
            if parent_id:
                url += f"?parent_id={parent_id}"

            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            logger.info(f"Retrieved {len(data.get('pages', []))} pages from space {space_key}")
            return PagesResponse(**data)
        except httpx.HTTPError as e:
            logger.error(f"Failed to fetch pages for space {space_key}: {e}")
            # Fallback to mock data on error
            logger.info(f"Falling back to mock pages for space {space_key}")
            if parent_id:
                children = MOCK_CHILD_PAGES.get(parent_id, [])
                return PagesResponse(pages=children)
            pages = MOCK_PAGES.get(space_key.upper(), [])
            return PagesResponse(pages=pages)
