"""
Confluence Publisher Service - Internal service for publishing to Confluence.

This service handles:
- Publishing protocols to Confluence (via MCP → mcp-atlassian)
- Exporting protocols as PDF (ReportLab)
- User search (LDAP/AD mock)
"""

import logging

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import StreamingResponse
from typing import List, Optional
from datetime import datetime

from app.config import get_settings
from app.models import (
    PublishRequest,
    PublishResponse,
    ExportPdfRequest,
    UserSuggestion,
    UsersSearchResponse,
    ConfluenceSpace,
    ConfluencePage,
    SpacesResponse,
    PagesResponse,
)
from app.markdown_renderer import render_protocol_to_markdown
from app.mcp_client import ConfluenceMCPPublisher
from app.pdf_generator import generate_confluence_pdf

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Confluence Publisher",
    description="Publish documentation to Confluence via MCP",
    version="0.2.0",
)


# ============================================================================
# Mock Data (user search — will be replaced with LDAP/AD in production)
# ============================================================================

MOCK_USERS = [
    UserSuggestion(id="user-1", name="Max Mustermann", email="max.mustermann@company.de", department="Engineering"),
    UserSuggestion(id="user-2", name="Anna Schmidt", email="anna.schmidt@company.de", department="Product"),
    UserSuggestion(id="user-3", name="Thomas Weber", email="thomas.weber@company.de", department="IT-Abteilung"),
    UserSuggestion(id="user-4", name="Maria Bauer", email="maria.bauer@company.de", department="Marketing"),
    UserSuggestion(id="user-5", name="Klaus Fischer", email="klaus.fischer@company.de", department="Sales"),
    UserSuggestion(id="user-6", name="Thomas Müller", email="thomas.mueller@company.de", department="IT-Abteilung"),
    UserSuggestion(id="user-7", name="Sabine Schneider", email="sabine.schneider@company.de", department="HR"),
    UserSuggestion(id="user-8", name="Martin Hoffmann", email="martin.hoffmann@company.de", department="Finance"),
    UserSuggestion(id="user-9", name="Julia Wagner", email="julia.wagner@company.de", department="Engineering"),
    UserSuggestion(id="user-10", name="Stefan Braun", email="stefan.braun@company.de", department="Operations"),
]


# ============================================================================
# Endpoints
# ============================================================================

@app.get("/health")
async def health():
    """Health check endpoint."""
    settings = get_settings()
    return {
        "status": "ok",
        "service": "confluence-publisher",
        "mcp_server_url": settings.mcp_server_url,
    }


@app.post("/internal/publish", response_model=PublishResponse)
async def publish_to_confluence(request: PublishRequest):
    """
    Publish a protocol to Confluence.

    Converts the protocol to markdown and creates a page via the MCP server.
    """
    settings = get_settings()

    # Render protocol to markdown
    markdown = render_protocol_to_markdown(request.protocol)
    title = request.protocol.get("title", "Meeting Protocol")
    space_key = request.space_key or "DOCS"

    # Publish via MCP
    publisher = ConfluenceMCPPublisher(settings.mcp_server_url)
    try:
        result = await publisher.create_page(
            space_key=space_key,
            title=title,
            content_markdown=markdown,
        )

        return PublishResponse(
            success=True,
            confluence_url=result["url"],
            page_id=result["page_id"],
        )

    except Exception as e:
        logger.error("Confluence publish failed: %s", e)
        raise HTTPException(
            status_code=502,
            detail=f"Failed to publish to Confluence: {e}",
        )


@app.post("/internal/export/pdf")
async def export_pdf(request: ExportPdfRequest):
    """
    Export a protocol as PDF with Confluence styling and Norizon watermark.

    Returns the PDF file directly as a downloadable response.
    Follows PDF_EXPORT_BACKEND_SPEC.md specification.
    """
    # Generate PDF with Confluence styling
    pdf_buffer = generate_confluence_pdf(request.protocol)

    # Generate filename from protocol title and date
    protocol_title = request.protocol.get("title", "Meeting Protocol")
    protocol_date = request.protocol.get("date", "")

    # Extract just date part if it's ISO format, otherwise use current date
    if protocol_date:
        if 'T' in protocol_date or ' ' in protocol_date:
            protocol_date = protocol_date.split('T')[0].split(' ')[0].replace('-', '')
        else:
            protocol_date = protocol_date.replace('-', '')
    else:
        protocol_date = datetime.now().strftime('%Y%m%d')

    # Sanitize title for filename
    safe_title = "".join(c if c.isalnum() or c in (' ', '-', '_') else '' for c in protocol_title)
    safe_title = safe_title.replace(" ", "-").strip('-')[:50]

    # Ensure we have at least something in the title
    if not safe_title:
        safe_title = "Meeting-Protocol"

    filename = f"{safe_title}-{protocol_date}.pdf"

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"'
        }
    )


# ============================================================================
# User Search (mock LDAP — kept from original)
# ============================================================================

@app.get("/internal/users/search", response_model=UsersSearchResponse)
async def search_users(q: str = Query(..., min_length=2)):
    """
    Search users by name, email, or department.

    In production, this would query LDAP/Active Directory.
    """
    q_lower = q.lower()

    filtered = [
        u for u in MOCK_USERS
        if q_lower in u.name.lower()
        or q_lower in u.email.lower()
        or (u.department and q_lower in u.department.lower())
    ]

    return UsersSearchResponse(users=filtered[:5])


@app.get("/internal/users", response_model=UsersSearchResponse)
async def list_users():
    """List all available users (for testing)."""
    return UsersSearchResponse(users=MOCK_USERS)


# ============================================================================
# Confluence Spaces & Pages Navigation
# ============================================================================

@app.get("/internal/confluence/spaces", response_model=SpacesResponse)
async def get_confluence_spaces():
    """
    Get list of available Confluence spaces.
    Fetches from MCP server (which connects to real Confluence).
    """
    settings = get_settings()
    publisher = ConfluenceMCPPublisher(settings.mcp_server_url)

    try:
        spaces_data = await publisher.get_spaces()
        # Convert MCP response to our model
        spaces = [
            ConfluenceSpace(
                id=space.get("id", ""),
                key=space.get("key", ""),
                name=space.get("name", ""),
                icon=space.get("icon", "folder"),
                type=space.get("type", "global")
            )
            for space in spaces_data
        ]
        logger.info(f"Retrieved {len(spaces)} Confluence spaces from MCP")
        return SpacesResponse(spaces=spaces)
    except Exception as e:
        logger.error(f"Failed to fetch Confluence spaces: {e}")
        raise HTTPException(
            status_code=502,
            detail=f"Failed to fetch Confluence spaces: {e}"
        )


@app.get("/internal/confluence/spaces/{space_key}/pages", response_model=PagesResponse)
async def get_confluence_pages(space_key: str, parent_id: Optional[str] = None):
    """
    Get pages in a Confluence space.

    Args:
        space_key: The space key (e.g., "ENG", "MARKETING")
        parent_id: Optional parent page ID to get children

    Returns:
        List of pages in the space (or children of the parent page)
    """
    settings = get_settings()
    publisher = ConfluenceMCPPublisher(settings.mcp_server_url)

    try:
        pages_data = await publisher.get_pages(space_key, parent_id)
        # Convert MCP response to our model
        pages = [
            ConfluencePage(
                id=page.get("id", ""),
                title=page.get("title", ""),
                parent_id=page.get("parentId"),
                has_children=page.get("hasChildren", False)
            )
            for page in pages_data
        ]
        logger.info(f"Retrieved {len(pages)} pages from space {space_key}")
        return PagesResponse(pages=pages)
    except Exception as e:
        logger.error(f"Failed to fetch pages for space {space_key}: {e}")
        raise HTTPException(
            status_code=502,
            detail=f"Failed to fetch Confluence pages: {e}"
        )
