"""
Users router - User search for autocomplete (LDAP/AD proxy).
"""

from fastapi import APIRouter, Query
import httpx

from app.models import UsersSearchResponse
from app.config import get_settings

router = APIRouter(tags=["users"])


@router.get("/users/search", response_model=UsersSearchResponse)
async def search_users(q: str = Query(..., min_length=2, description="Search query")):
    """
    Search users by name, email, or department.
    Used for autocomplete in speaker name assignment.

    In production, this proxies to confluence-publisher which queries LDAP/AD.
    """
    settings = get_settings()

    # Proxy to confluence-publisher service (which handles LDAP)
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{settings.confluence_publisher_url}/internal/users/search",
                params={"q": q},
                timeout=10.0,
            )
            response.raise_for_status()
            data = response.json()
            return UsersSearchResponse(**data)

        except httpx.HTTPError:
            # Fallback to empty results on error
            return UsersSearchResponse(users=[])
