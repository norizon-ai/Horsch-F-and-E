"""
Azure Entra External ID (CIAM) JWT token verification utilities.

Uses OIDC discovery to auto-resolve JWKS endpoint and issuer
from the CIAM domain, so no hardcoded tenant ID is needed.
"""

import logging
from typing import Dict, Any
import httpx
from jose import jwt, JWTError
from fastapi import HTTPException, status
from app.config import get_settings

logger = logging.getLogger(__name__)

# Cache for JWKS (JSON Web Key Set) and OIDC config
_jwks_cache: Dict[str, Any] | None = None
_oidc_config_cache: Dict[str, Any] | None = None


async def get_oidc_config() -> Dict[str, Any]:
    """
    Fetch OIDC configuration from the CIAM discovery endpoint.

    Returns issuer, jwks_uri, and other OIDC metadata.
    Cached after first fetch.
    """
    global _oidc_config_cache

    if _oidc_config_cache is not None:
        return _oidc_config_cache

    settings = get_settings()
    oidc_url = f"https://{settings.azure_ciam_domain}/{settings.azure_tenant_id}/v2.0/.well-known/openid-configuration"

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(oidc_url)
            response.raise_for_status()
            _oidc_config_cache = response.json()
            logger.info(f"Fetched OIDC config from: {oidc_url}")
            return _oidc_config_cache
    except httpx.HTTPError as e:
        logger.error(f"Failed to fetch OIDC config: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to verify authentication - Azure AD service unavailable"
        )


async def get_jwks() -> Dict[str, Any]:
    """
    Fetch JWKS from the Azure AD CIAM endpoint (auto-discovered via OIDC).

    Returns:
        JWKS dictionary

    Raises:
        HTTPException: If JWKS cannot be fetched
    """
    global _jwks_cache

    if _jwks_cache is not None:
        return _jwks_cache

    oidc_config = await get_oidc_config()
    jwks_url = oidc_config.get("jwks_uri")

    if not jwks_url:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="OIDC config missing jwks_uri"
        )

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(jwks_url)
            response.raise_for_status()
            _jwks_cache = response.json()
            logger.info(f"Fetched JWKS from Azure AD: {jwks_url}")
            return _jwks_cache
    except httpx.HTTPError as e:
        logger.error(f"Failed to fetch JWKS from Azure AD: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to verify authentication - Azure AD service unavailable"
        )


async def verify_token(token: str) -> Dict[str, Any]:
    """
    Verify and decode an Azure AD CIAM JWT token.

    Uses OIDC discovery to resolve JWKS and issuer automatically.

    Args:
        token: JWT token string (without "Bearer " prefix)

    Returns:
        Decoded token payload

    Raises:
        HTTPException: If token is invalid, expired, or verification fails
    """
    settings = get_settings()

    try:
        jwks = await get_jwks()
        oidc_config = await get_oidc_config()

        issuer = oidc_config.get("issuer")

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
            # Key not found — JWKS may be stale, clear cache and retry once
            global _jwks_cache
            _jwks_cache = None
            jwks = await get_jwks()
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

        # Log what we're validating against
        unverified_payload = jwt.get_unverified_claims(token)
        logger.info(f"Token iss={unverified_payload.get('iss')}, aud={unverified_payload.get('aud')}")
        logger.info(f"Expected iss={issuer}, aud={settings.azure_client_id}")

        # Verify and decode the token
        payload = jwt.decode(
            token,
            rsa_key,
            algorithms=["RS256"],
            audience=settings.azure_client_id,
            issuer=issuer,
        )

        logger.info(f"Token verified for user: {payload.get('oid', payload.get('sub'))}")
        logger.info(f"Token claims: iss={payload.get('iss')}, aud={payload.get('aud')}, ver={payload.get('ver')}")
        return payload

    except jwt.ExpiredSignatureError:
        logger.warning("Token verification failed: Token expired")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except jwt.JWTClaimsError as e:
        logger.warning(f"Token verification failed: Invalid claims - {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token claims: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except JWTError as e:
        logger.error(f"Token verification failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    except Exception as e:
        logger.error(f"Unexpected error during token verification: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Authentication verification error"
        )
