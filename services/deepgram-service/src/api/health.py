"""Health check endpoints for Kubernetes liveness and readiness probes."""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
import httpx
import logging
from src.config import settings
from src.services.redis_manager import RedisManager

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/health")
async def health_check():
    """
    Liveness probe: Is the process running?

    Kubernetes uses this to determine if the container should be restarted.
    Should return 200 as long as the process is alive (even if dependencies are down).

    Returns:
        dict: Health status
    """
    return {
        "status": "healthy",
        "service": settings.app_name
    }


@router.get("/ready")
async def readiness_check():
    """
    Readiness probe: Can the service accept traffic?

    Kubernetes uses this to determine if the container should receive traffic.
    Should return 200 only if all critical dependencies are available.

    Checks:
    - Redis connection
    - Deepgram API reachability (optional - doesn't fail if down)
    - S3/MinIO availability (optional - doesn't fail if down)

    Returns:
        dict: Readiness status with dependency checks
    """
    checks = {}
    all_critical_healthy = True

    # Check 1: Redis (CRITICAL)
    try:
        redis = RedisManager()
        redis.redis.ping()
        redis.close()
        checks["redis"] = {"status": "ok", "critical": True}
        logger.debug("Redis health check: OK")
    except Exception as e:
        checks["redis"] = {"status": "error", "error": str(e), "critical": True}
        all_critical_healthy = False
        logger.error(f"Redis health check failed: {e}")

    # Check 2: Deepgram API (NON-CRITICAL)
    # We check if the API is reachable but don't fail readiness if it's down
    # because temporary API outages shouldn't stop the container
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://api.deepgram.com/v1/status",
                headers={"Authorization": f"Token {settings.deepgram_api_key}"},
                timeout=5.0
            )
            if response.status_code == 200:
                checks["deepgram_api"] = {"status": "ok", "critical": False}
            else:
                checks["deepgram_api"] = {
                    "status": "degraded",
                    "http_code": response.status_code,
                    "critical": False
                }
    except Exception as e:
        checks["deepgram_api"] = {
            "status": "unreachable",
            "error": str(e),
            "critical": False
        }
        logger.warning(f"Deepgram API health check failed (non-critical): {e}")

    # Check 3: S3/MinIO (NON-CRITICAL)
    if settings.s3_access_key:
        try:
            from src.storage.s3_client import S3Storage
            s3 = S3Storage()
            # Try to list objects (lightweight operation)
            s3.s3.list_objects_v2(Bucket=settings.s3_bucket, MaxKeys=1)
            checks["s3_storage"] = {"status": "ok", "critical": False}
        except Exception as e:
            checks["s3_storage"] = {
                "status": "error",
                "error": str(e),
                "critical": False
            }
            logger.warning(f"S3 health check failed (non-critical): {e}")
    else:
        checks["s3_storage"] = {"status": "not_configured", "critical": False}

    # Determine overall readiness
    if all_critical_healthy:
        return {
            "status": "ready",
            "service": settings.app_name,
            "checks": checks
        }
    else:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "not_ready",
                "service": settings.app_name,
                "checks": checks
            }
        )
