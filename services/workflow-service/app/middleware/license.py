"""
Keygen License Validation Middleware - Master Power Switch

This module implements a global license check using Keygen.sh to ensure
the server is legally authorized to run. If the license is invalid or
expired, ALL API requests are blocked with a 503 Service Unavailable.

Features:
- Validates license on server startup
- Re-validates every hour in background
- Global in-memory state for instant checks
- Graceful error handling (network failures = unlicensed)
- Middleware blocks all requests if unlicensed
"""

import os
import asyncio
import logging
from datetime import datetime
from typing import Optional
import httpx
from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger(__name__)

# =============================================================================
# Global License State (In-Memory)
# =============================================================================

IS_SERVER_LICENSED = False
LAST_VALIDATION_TIME: Optional[datetime] = None
LICENSE_DETAILS: dict = {}

# Lock to prevent race conditions during validation
_validation_lock = asyncio.Lock()


# =============================================================================
# Keygen License Validation Function
# =============================================================================

async def validate_license() -> bool:
    """
    Validate the server license with Keygen.sh API.

    This function:
    1. Reads KEYGEN_ACCOUNT_ID and KEYGEN_LICENSE_KEY from environment
    2. Makes HTTP request to Keygen validation API
    3. Updates global IS_SERVER_LICENSED state
    4. Returns True if license is valid, False otherwise

    Error handling:
    - Network timeouts: Returns False (unlicensed)
    - Invalid response: Returns False (unlicensed)
    - Missing env vars: Returns False (unlicensed)

    Returns:
        bool: True if license is valid, False otherwise
    """
    global IS_SERVER_LICENSED, LAST_VALIDATION_TIME, LICENSE_DETAILS

    async with _validation_lock:
        try:
            # Check if license validation is enabled
            license_check_enabled = os.getenv("LICENSE_CHECK_ENABLED", "true").lower() == "true"
            if not license_check_enabled:
                logger.warning("⚠️  License check is DISABLED via LICENSE_CHECK_ENABLED=false")
                IS_SERVER_LICENSED = True
                LAST_VALIDATION_TIME = datetime.now()
                return True

            # Get Keygen credentials from environment
            account_id = os.getenv("KEYGEN_ACCOUNT_ID")
            license_key = os.getenv("KEYGEN_LICENSE_KEY")
            api_url = os.getenv("KEYGEN_API_URL", "https://api.keygen.sh/v1")

            if not account_id or not license_key:
                logger.error("❌ Missing KEYGEN_ACCOUNT_ID or KEYGEN_LICENSE_KEY environment variables")
                IS_SERVER_LICENSED = False
                LAST_VALIDATION_TIME = datetime.now()
                return False

            # Prepare Keygen validation request (JSON:API format)
            # CRITICAL: Keygen API endpoint requires EXACT format:
            # POST https://api.keygen.sh/v1/accounts/{ACCOUNT_ID}/licenses/actions/validate-key
            validation_url = f"{api_url}/accounts/{account_id}/licenses/actions/validate-key"

            # Prepare request body (JSON:API format - must be wrapped in "meta")
            request_body = {
                "meta": {
                    "key": license_key
                }
            }

            # Prepare headers (JSON:API content type required)
            request_headers = {
                "Content-Type": "application/vnd.api+json",
                "Accept": "application/vnd.api+json"
            }

            logger.info(f"🔐 Validating license with Keygen...")
            logger.debug(f"   Account ID: {account_id}")
            logger.debug(f"   URL: {validation_url}")
            logger.debug(f"   License Key: {license_key[:8]}...{license_key[-4:]}")

            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    validation_url,
                    json=request_body,
                    headers=request_headers
                )

                # Log response for debugging
                logger.debug(f"   Response Status: {response.status_code}")
                logger.debug(f"   Response Body: {response.text[:500]}")

                # Parse response
                if response.status_code == 200:
                    data = response.json()

                    # Check if license is valid (Keygen returns "valid": true/false in meta)
                    is_valid = data.get("meta", {}).get("valid", False)
                    license_data = data.get("data", {})

                    if is_valid:
                        # Extract license details from JSON:API response
                        attributes = license_data.get("attributes", {})
                        LICENSE_DETAILS = {
                            "id": license_data.get("id"),
                            "status": attributes.get("status"),
                            "expiry": attributes.get("expiry"),
                            "name": attributes.get("name"),
                            "created": attributes.get("created"),
                            "metadata": attributes.get("metadata", {})
                        }

                        IS_SERVER_LICENSED = True
                        LAST_VALIDATION_TIME = datetime.now()

                        expiry = LICENSE_DETAILS.get("expiry")
                        logger.info(f"✅ License is VALID (expires: {expiry or 'never'})")
                        logger.debug(f"   License ID: {LICENSE_DETAILS.get('id')}")
                        logger.debug(f"   License Status: {LICENSE_DETAILS.get('status')}")
                        return True
                    else:
                        # License is invalid
                        validation_code = data.get("meta", {}).get("code")
                        validation_detail = data.get("meta", {}).get("detail")

                        IS_SERVER_LICENSED = False
                        LAST_VALIDATION_TIME = datetime.now()

                        logger.error(f"❌ License is INVALID")
                        logger.error(f"   Code: {validation_code}")
                        logger.error(f"   Detail: {validation_detail}")
                        return False
                else:
                    # Keygen API returned error (non-200 status)
                    try:
                        error_data = response.json()
                        errors = error_data.get("errors", [])
                        if errors:
                            error_title = errors[0].get("title", "Unknown")
                            error_detail = errors[0].get("detail", "Unknown")
                            error_code = errors[0].get("code", "Unknown")
                            logger.error(f"❌ Keygen API error: {response.status_code}")
                            logger.error(f"   Title: {error_title}")
                            logger.error(f"   Detail: {error_detail}")
                            logger.error(f"   Code: {error_code}")
                        else:
                            logger.error(f"❌ Keygen API error: {response.status_code} - {response.text}")
                    except Exception:
                        logger.error(f"❌ Keygen API error: {response.status_code} - {response.text}")

                    IS_SERVER_LICENSED = False
                    LAST_VALIDATION_TIME = datetime.now()
                    return False

        except httpx.TimeoutException:
            logger.error("❌ License validation TIMEOUT - Keygen API unreachable")
            IS_SERVER_LICENSED = False
            LAST_VALIDATION_TIME = datetime.now()
            return False

        except Exception as e:
            logger.error(f"❌ License validation ERROR: {str(e)}", exc_info=True)
            IS_SERVER_LICENSED = False
            LAST_VALIDATION_TIME = datetime.now()
            return False


# =============================================================================
# Background License Re-validation Task
# =============================================================================

async def background_license_validator():
    """
    Background task that re-validates the license every hour.

    This runs indefinitely in the background and updates the global
    IS_SERVER_LICENSED state periodically.

    Interval: 1 hour (3600 seconds)
    """
    logger.info("🔄 Starting background license validator (re-checks every 1 hour)")

    while True:
        try:
            # Wait 1 hour before next validation
            await asyncio.sleep(3600)

            # Re-validate license
            logger.info("🔄 Running scheduled license re-validation...")
            is_valid = await validate_license()

            if is_valid:
                logger.info("✅ License re-validation PASSED")
            else:
                logger.error("❌ License re-validation FAILED - Server will block requests")

        except asyncio.CancelledError:
            logger.info("⏹️  Background license validator stopped")
            break
        except Exception as e:
            logger.error(f"❌ Background validator error: {str(e)}", exc_info=True)
            # Continue running even if one validation fails
            await asyncio.sleep(3600)


# =============================================================================
# License Bouncer Middleware
# =============================================================================

class LicenseBouncerMiddleware(BaseHTTPMiddleware):
    """
    Middleware that blocks ALL requests if the server is not licensed.

    Exempt endpoints:
    - /health, /healthz, /readyz (health checks)
    - /docs, /redoc, /openapi.json (API documentation)

    If IS_SERVER_LICENSED is False, returns:
    - Status: 503 Service Unavailable
    - JSON: {"detail": "Server license is invalid or expired"}
    """

    # Endpoints that don't require license check
    EXEMPT_PATHS = {
        "/health",
        "/healthz",
        "/readyz",
        "/docs",
        "/redoc",
        "/openapi.json",
        "/"  # Root endpoint
    }

    async def dispatch(self, request: Request, call_next):
        # Check if path is exempt from license check
        if request.url.path in self.EXEMPT_PATHS:
            return await call_next(request)

        # Check global license state
        if not IS_SERVER_LICENSED:
            logger.warning(f"🚫 Blocked request to {request.url.path} - Server is UNLICENSED")

            return JSONResponse(
                status_code=503,
                content={
                    "detail": "Server license is invalid or expired",
                    "error": "SERVICE_UNLICENSED",
                    "message": "This server is not properly licensed. Please contact your administrator.",
                    "last_check": LAST_VALIDATION_TIME.isoformat() if LAST_VALIDATION_TIME else None
                }
            )

        # License is valid, proceed with request
        return await call_next(request)


# =============================================================================
# License Status Endpoint (for debugging)
# =============================================================================

def get_license_status() -> dict:
    """
    Get current license status for debugging/monitoring.

    Returns:
        dict: Current license state including validation time and details
    """
    return {
        "licensed": IS_SERVER_LICENSED,
        "last_validation": LAST_VALIDATION_TIME.isoformat() if LAST_VALIDATION_TIME else None,
        "details": LICENSE_DETAILS if IS_SERVER_LICENSED else None,
        "check_enabled": os.getenv("LICENSE_CHECK_ENABLED", "true").lower() == "true"
    }
