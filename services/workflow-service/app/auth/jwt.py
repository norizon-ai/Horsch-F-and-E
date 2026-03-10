"""
Auth0 JWT token verification utilities.
"""

import logging
from typing import Dict, Any
import httpx
from jose import jwt, JWTError
from fastapi import HTTPException, status
from app.config import get_settings

logger = logging.getLogger(__name__)

# Cache for JWKS (JSON Web Key Set)
_jwks_cache: Dict[str, Any] | None = None


async def get_jwks() -> Dict[str, Any]:
    """
    Fetch JWKS (JSON Web Key Set) from Auth0.

    The JWKS contains the public keys used to verify JWT signatures.
    This function caches the result to avoid repeated HTTP requests.

    Returns:
        JWKS dictionary

    Raises:
        HTTPException: If JWKS cannot be fetched
    """
    global _jwks_cache

    # Return cached JWKS if available
    if _jwks_cache is not None:
        return _jwks_cache

    settings = get_settings()

    # Construct JWKS URL from Auth0 domain
    jwks_url = f"https://{settings.auth0_domain}/.well-known/jwks.json"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(jwks_url)
            response.raise_for_status()

            _jwks_cache = response.json()
            logger.info(f"✅ Fetched JWKS from Auth0: {jwks_url}")
            return _jwks_cache

    except httpx.HTTPError as e:
        logger.error(f"❌ Failed to fetch JWKS from Auth0: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to verify authentication - Auth0 service unavailable"
        )


async def verify_token(token: str) -> Dict[str, Any]:
    """
    Verify and decode an Auth0 JWT token.

    This function:
    1. Fetches the JWKS from Auth0 (cached)
    2. Extracts the key ID (kid) from the token header
    3. Finds the matching public key in JWKS
    4. Verifies the token signature cryptographically
    5. Validates token expiration and audience
    6. Returns the decoded token payload

    Args:
        token: JWT token string (without "Bearer " prefix)

    Returns:
        Decoded token payload containing user info (sub, email, etc.)

    Raises:
        HTTPException: If token is invalid, expired, or verification fails
    """
    settings = get_settings()

    try:
        # Get JWKS (cached)
        jwks = await get_jwks()

        # Decode token header to get key ID (kid)
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")

        if not kid:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing key ID (kid)",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Find the matching key in JWKS
        rsa_key = None
        for key in jwks.get("keys", []):
            if key.get("kid") == kid:
                rsa_key = {
                    "kty": key.get("kty"),
                    "kid": key.get("kid"),
                    "use": key.get("use"),
                    "n": key.get("n"),
                    "e": key.get("e"),
                }
                break

        if not rsa_key:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: key not found in JWKS",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Verify and decode the token
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=["RS256"],
            audience=settings.auth0_audience,
            issuer=f"https://{settings.auth0_domain}/",
        )

        logger.debug(f"✅ Token verified for user: {payload.get('sub')}")
        return payload

    except jwt.ExpiredSignatureError:
        logger.warning("⚠️  Token verification failed: Token expired")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except jwt.JWTClaimsError as e:
        logger.warning(f"⚠️  Token verification failed: Invalid claims - {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token claims: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except JWTError as e:
        logger.error(f"❌ Token verification failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except Exception as e:
        logger.error(f"❌ Unexpected error during token verification: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authentication verification error"
        )
