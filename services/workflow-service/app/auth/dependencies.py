"""
FastAPI dependencies for authentication and user management.
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
    2. Verifies the JWT token with Auth0
    3. Extracts user info (sub, email, name) from token payload
    4. Performs JIT (Just-In-Time) user provisioning:
       - If user exists: Updates last_login and returns user
       - If user doesn't exist: Creates new user and returns it

    Usage:
        @app.get("/protected")
        async def protected_route(user: User = Depends(get_current_user)):
            return {"user_id": user.id, "email": user.email}

    Args:
        credentials: HTTP Bearer token from Authorization header
        db: Database session

    Returns:
        User object (from database)

    Raises:
        HTTPException: 401 if token is invalid, 403 if auth is disabled
    """
    settings = get_settings()

    # Check if Auth0 is enabled
    if not settings.auth0_enabled:
        logger.warning("⚠️  Auth0 is DISABLED - Skipping authentication")
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Authentication is disabled on this server"
        )

    # Extract token from credentials
    token = credentials.credentials

    # Verify token with Auth0
    payload = await verify_token(token)

    # Extract user info from token payload
    # Auth0 Actions add custom claims with namespace to avoid conflicts
    namespace = "https://nora-platform.com"

    # Try namespaced claims first (from Auth0 Action), then fall back to standard claims
    auth0_subject = payload.get(f"{namespace}/sub") or payload.get("sub")
    email = payload.get(f"{namespace}/email") or payload.get("email")
    name = payload.get(f"{namespace}/name") or payload.get("name")

    if not auth0_subject or not email:
        logger.error(f"❌ Token missing required fields: sub or email. Payload keys: {list(payload.keys())}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token: missing user information",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # JIT user provisioning
    user_repo = UserRepository(db)
    user = await user_repo.upsert_user(
        auth0_subject=auth0_subject,
        email=email,
        name=name
    )

    logger.info(f"✅ User authenticated: {user.email} (ID: {user.id})")
    return user


async def get_current_user_optional(
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(security)] = None,
    db: AsyncSession = Depends(get_db),
) -> User | None:
    """
    Optional authentication dependency.

    Returns the authenticated user if a valid token is provided,
    otherwise returns None (allowing anonymous access).

    Usage:
        @app.get("/optional-auth")
        async def optional_route(user: User | None = Depends(get_current_user_optional)):
            if user:
                return {"message": f"Hello {user.email}"}
            else:
                return {"message": "Hello anonymous user"}
    """
    if credentials is None:
        return None

    try:
        return await get_current_user(credentials, db)
    except HTTPException:
        return None
