"""
FastAPI dependencies for authentication and user management.
Uses Azure Entra External ID (CIAM) for JWT verification.
"""

import logging
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.jwt import verify_token
from app.db.database import get_db
from app.db.models import User
from app.db.repositories.user_repository import UserRepository
from app.config import get_settings

logger = logging.getLogger(__name__)

# HTTP Bearer token security scheme
security = HTTPBearer()


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    FastAPI dependency for getting the current authenticated user.

    This dependency:
    1. Extracts the Bearer token from the Authorization header
    2. Verifies the JWT token with Azure AD CIAM
    3. Extracts user info (oid, email, name) from token payload
    4. Performs JIT (Just-In-Time) user provisioning:
       - If user exists: Updates last_login and returns user
       - If user doesn't exist: Creates new user and returns it
    """
    settings = get_settings()

    if not settings.azure_ad_enabled:
        logger.warning("Azure AD is DISABLED - Skipping authentication")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authentication is disabled on this server"
        )

    token = credentials.credentials
    payload = await verify_token(token)

    # Azure AD CIAM standard claims
    # oid = Object ID (stable user identifier across apps in the tenant)
    # preferred_username / email = user's email
    # name = display name
    external_subject = payload.get("oid") or payload.get("sub")
    email = payload.get("email") or payload.get("preferred_username") or payload.get("emails", [None])[0]
    name = payload.get("name")

    if not external_subject or not email:
        logger.error(f"Token missing required fields: oid/sub or email. Payload keys: {list(payload.keys())}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token: missing user information",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # JIT user provisioning
    user_repo = UserRepository(db)
    user = await user_repo.upsert_user(
        external_subject=external_subject,
        email=email,
        name=name
    )

    logger.info(f"User authenticated: {user.email} (ID: {user.id})")
    return user


async def get_current_user_optional(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(security)] = None,
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """
    Optional authentication dependency.

    Returns the authenticated user if a valid token is provided,
    otherwise returns None (allowing anonymous access).
    """
    if credentials is None:
        return None

    try:
        return await get_current_user(credentials, db)
    except HTTPException:
        return None
