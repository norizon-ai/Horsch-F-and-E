"""Health check endpoints."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok", "service": "transcription-service"}


@router.get("/ready")
async def ready():
    return {"status": "ready", "service": "transcription-service"}
