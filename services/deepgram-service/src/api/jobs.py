from fastapi import APIRouter, HTTPException
from src.models.schemas import Speaker, SpeakersResponse
from src.services.redis_manager import RedisManager
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/{job_id}/speakers", response_model=SpeakersResponse)
async def get_speakers(job_id: str):
    """Get detected speakers for a job. Retrieved from Redis after processing completes."""

    logger.info(f"Speakers requested for job {job_id}")

    redis_manager = RedisManager()
    speakers_data = redis_manager.get_speakers(job_id)

    if speakers_data is None:
        raise HTTPException(
            status_code=404,
            detail=f"Speakers not found for job {job_id}"
        )

    speakers = [Speaker(**s) for s in speakers_data]

    logger.info(f"Speakers retrieved for job {job_id}: {len(speakers)} speakers")

    return SpeakersResponse(speakers=speakers)