"""
API Routes

FastAPI endpoints for the Norizon search service.
"""

import asyncio
import uuid
from datetime import datetime, timedelta
from typing import Dict, Optional

from fastapi import APIRouter, BackgroundTasks, HTTPException, Depends
from fastapi.responses import StreamingResponse

from deepsearch.tools import ToolRegistry
from deepsearch.agents import AgentRegistry
from deepsearch.models import DRResult
from deepsearch.observability import get_logger, set_correlation_id, TracingContext, SpanKind

from .models import (
    searchRequest,
    searchJobResponse,
    searchStatusResponse,
    searchResultResponse,
    ToolsListResponse,
    ToolInfo,
    HealthResponse,
    ErrorResponse,
    JobStatus,
)
from .streaming import stream_manager, EventStream

logger = get_logger(__name__)

# In-memory job storage (replace with Redis/DB for production)
_jobs: Dict[str, Dict] = {}

# Job cleanup configuration
MAX_JOBS = 1000  # Maximum number of jobs to keep
JOB_TTL_SECONDS = 3600  # 1 hour TTL for completed jobs
CLEANUP_INTERVAL_SECONDS = 300  # Run cleanup every 5 minutes

# Background cleanup task handle
_cleanup_task: Optional[asyncio.Task] = None


async def cleanup_expired_jobs(max_age_seconds: int = JOB_TTL_SECONDS) -> int:
    """
    Remove expired jobs from memory.

    Args:
        max_age_seconds: Maximum age for completed/failed jobs

    Returns:
        Number of jobs removed
    """
    now = datetime.utcnow()
    cutoff = now - timedelta(seconds=max_age_seconds)

    jobs_to_remove = []
    for job_id, job in _jobs.items():
        # Only clean up completed or failed jobs
        if job["status"] in (JobStatus.COMPLETED, JobStatus.FAILED):
            completed_at = job.get("updated_at", job.get("created_at"))
            if completed_at and completed_at < cutoff:
                jobs_to_remove.append(job_id)

    for job_id in jobs_to_remove:
        del _jobs[job_id]
        stream_manager.remove(job_id)

    if jobs_to_remove:
        logger.info("jobs_cleaned_up", count=len(jobs_to_remove))

    return len(jobs_to_remove)


async def enforce_max_jobs() -> int:
    """
    Remove oldest completed jobs if we exceed MAX_JOBS.

    Returns:
        Number of jobs removed
    """
    if len(_jobs) <= MAX_JOBS:
        return 0

    # Sort completed/failed jobs by creation time
    removable = [
        (job_id, job["created_at"])
        for job_id, job in _jobs.items()
        if job["status"] in (JobStatus.COMPLETED, JobStatus.FAILED)
    ]
    removable.sort(key=lambda x: x[1])

    # Remove oldest jobs until we're under the limit
    to_remove = len(_jobs) - MAX_JOBS
    removed = 0
    for job_id, _ in removable[:to_remove]:
        del _jobs[job_id]
        stream_manager.remove(job_id)
        removed += 1

    if removed:
        logger.info("jobs_evicted_max_limit", count=removed, max_jobs=MAX_JOBS)

    return removed


async def _cleanup_loop():
    """Background task that periodically cleans up expired jobs."""
    while True:
        try:
            await asyncio.sleep(CLEANUP_INTERVAL_SECONDS)
            await cleanup_expired_jobs()
            await enforce_max_jobs()
        except asyncio.CancelledError:
            break
        except Exception as e:
            logger.error("cleanup_error", error=str(e))


def start_cleanup_task():
    """Start the background cleanup task."""
    global _cleanup_task
    if _cleanup_task is None or _cleanup_task.done():
        _cleanup_task = asyncio.create_task(_cleanup_loop())
        logger.info("cleanup_task_started")


def stop_cleanup_task():
    """Stop the background cleanup task."""
    global _cleanup_task
    if _cleanup_task and not _cleanup_task.done():
        _cleanup_task.cancel()
        logger.info("cleanup_task_stopped")


router = APIRouter(prefix="/api/v1", tags=["search"])


# =============================================================================
# DEPENDENCY INJECTION
# =============================================================================


async def get_supervisor():
    """
    Get supervisor agent instance.

    This should be configured at application startup.
    Override this in your application.
    """
    from deepsearch.supervisor import SupervisorAgent

    # This will be set by the main application
    supervisor = getattr(router, "_supervisor", None)
    if supervisor is None:
        raise HTTPException(
            status_code=503,
            detail="Supervisor not configured",
        )
    return supervisor


# =============================================================================
# search ENDPOINTS
# =============================================================================


@router.post(
    "/search",
    response_model=searchJobResponse,
    responses={500: {"model": ErrorResponse}},
)
async def start_search(
    request: searchRequest,
    background_tasks: BackgroundTasks,
    supervisor=Depends(get_supervisor),
) -> searchJobResponse:
    """
    Start an async search job.

    Returns immediately with a job_id. Use /search/{job_id} to check status
    or /search/{job_id}/stream for real-time updates.
    """
    job_id = str(uuid.uuid4())
    set_correlation_id(job_id)

    logger.info("search_job_created", job_id=job_id, query=request.query[:100])

    # Create job record
    _jobs[job_id] = {
        "status": JobStatus.PENDING,
        "query": request.query,
        "created_at": datetime.utcnow(),
        "result": None,
    }

    # Create event stream
    stream = stream_manager.create(job_id)

    # Start background task
    background_tasks.add_task(
        _execute_search,
        job_id,
        request,
        supervisor,
        stream,
    )

    return searchJobResponse(
        job_id=job_id,
        status=JobStatus.PENDING,
        created_at=_jobs[job_id]["created_at"],
    )


@router.post(
    "/search/sync",
    response_model=searchResultResponse,
    responses={500: {"model": ErrorResponse}},
)
async def search_sync(
    request: searchRequest,
    supervisor=Depends(get_supervisor),
) -> searchResultResponse:
    """
    Execute search synchronously (blocks until complete).

    Use this for simple integrations that don't need streaming.
    """
    import asyncio

    job_id = str(uuid.uuid4())
    set_correlation_id(job_id)

    logger.info("search_sync_start", job_id=job_id, query=request.query[:100])

    async with TracingContext(
        "api.search_sync",
        span_kind=SpanKind.SERVER,
        attributes={
            "http.method": "POST",
            "http.route": "/api/v1/search/sync",
            "input.query": request.query[:200],
            "input.job_id": job_id,
        },
    ) as span:
        try:
            result = await supervisor.search(
                request.query,
                job_id=job_id,
                conversation_history=request.conversation_history,
            )

            if result is None:
                logger.error("search_sync_null_result", job_id=job_id)
                span.set_attribute("error", "null_result")
                raise HTTPException(
                    status_code=500,
                    detail="Search returned no result. Please try again.",
                )

            span.set_attribute("output.success", True)
            return searchResultResponse.from_dr_result(result, job_id)

        except asyncio.TimeoutError:
            logger.error("search_sync_timeout", job_id=job_id)
            span.set_attribute("error", "timeout")
            raise HTTPException(
                status_code=504,
                detail="Search timed out. The query may be too complex.",
            )
        except HTTPException:
            raise
        except Exception as e:
            logger.error("search_sync_error", job_id=job_id, error=str(e))
            span.set_attribute("error", str(e))
            raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/search/{job_id}",
    response_model=searchStatusResponse,
    responses={404: {"model": ErrorResponse}},
)
async def get_search_status(job_id: str) -> searchStatusResponse:
    """Get status of a search job."""
    if job_id not in _jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = _jobs[job_id]
    return searchStatusResponse(
        job_id=job_id,
        status=job["status"],
        progress=job.get("progress"),
        current_iteration=job.get("current_iteration"),
        created_at=job["created_at"],
        updated_at=job.get("updated_at"),
    )


@router.get(
    "/search/{job_id}/result",
    response_model=searchResultResponse,
    responses={
        404: {"model": ErrorResponse},
        425: {"model": ErrorResponse},  # Too Early
    },
)
async def get_search_result(job_id: str) -> searchResultResponse:
    """Get result of a completed search job."""
    if job_id not in _jobs:
        raise HTTPException(status_code=404, detail="Job not found")

    job = _jobs[job_id]

    if job["status"] != JobStatus.COMPLETED:
        raise HTTPException(
            status_code=425,
            detail=f"Job not complete. Status: {job['status']}",
        )

    result = job.get("result")
    if not result:
        raise HTTPException(status_code=500, detail="Result not available")

    return searchResultResponse.from_dr_result(result, job_id)


@router.get("/search/{job_id}/stream")
async def stream_search(job_id: str) -> StreamingResponse:
    """
    Stream search progress via SSE.

    Events:
    - progress: Phase updates (searching, analyzing, etc.)
    - iteration: Iteration complete
    - complete: Final result
    - error: Error occurred
    """
    stream = stream_manager.get(job_id)
    if not stream:
        raise HTTPException(status_code=404, detail="Stream not found")

    async def event_generator():
        async for event in stream.events():
            yield event.to_sse()

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # Disable nginx buffering
        },
    )


# =============================================================================
# TOOL ENDPOINTS
# =============================================================================


@router.get("/tools", response_model=ToolsListResponse)
async def list_tools() -> ToolsListResponse:
    """List all registered tools."""
    tools = [
        ToolInfo(
            name=tool.name,
            description=tool.description,
            parameters=[p.model_dump() for p in tool.parameters],
        )
        for tool in ToolRegistry.all_tools()
    ]

    return ToolsListResponse(tools=tools, count=len(tools))


# =============================================================================
# HEALTH CHECK
# =============================================================================


@router.get("/health", response_model=HealthResponse)
async def health_check(supervisor=Depends(get_supervisor)) -> HealthResponse:
    """Health check with component status."""
    # Check for agents (new architecture) or legacy tools
    has_agents = AgentRegistry.count() > 0
    has_tools = ToolRegistry.count() > 0

    components = {
        "agents": has_agents,
        "tools": has_tools,
        "llm": await supervisor.llm.health_check() if supervisor else False,
    }

    # System is healthy if we have agents (or tools) and LLM is available
    is_healthy = (has_agents or has_tools) and components["llm"]
    status = "healthy" if is_healthy else "degraded"

    return HealthResponse(
        status=status,
        components=components,
    )


# =============================================================================
# BACKGROUND TASK
# =============================================================================


async def _execute_search(
    job_id: str,
    request: searchRequest,
    supervisor,
    stream: EventStream,
) -> None:
    """Background task to execute search."""
    # Set correlation ID for this background task
    set_correlation_id(job_id)

    async with TracingContext(
        "api.search_stream",
        span_kind=SpanKind.SERVER,
        attributes={
            "http.method": "POST",
            "http.route": "/api/v1/search/stream",
            "input.query": request.query[:200],
            "input.job_id": job_id,
        },
    ) as span:
        try:
            _jobs[job_id]["status"] = JobStatus.RUNNING
            _jobs[job_id]["updated_at"] = datetime.utcnow()

            await stream.progress("starting", "search started")

            # Execute search with conversation history if provided
            result = await supervisor.search(
                request.query,
                job_id=job_id,
                conversation_history=request.conversation_history,
                stream=stream,
            )

            # Handle null result
            if result is None:
                logger.error("search_job_null_result", job_id=job_id)
                span.set_attribute("error", "null_result")
                raise ValueError("Search returned no result")

            # Update job
            _jobs[job_id]["status"] = JobStatus.COMPLETED
            _jobs[job_id]["result"] = result
            _jobs[job_id]["updated_at"] = datetime.utcnow()

            # Complete stream
            await stream.complete(searchResultResponse.from_dr_result(result, job_id))

            span.set_attribute("output.success", True)
            logger.info("search_job_complete", job_id=job_id)

        except asyncio.TimeoutError:
            error_msg = "Search timed out"
            logger.error("search_job_timeout", job_id=job_id)
            span.set_attribute("error", "timeout")

            _jobs[job_id]["status"] = JobStatus.FAILED
            _jobs[job_id]["error"] = error_msg
            _jobs[job_id]["updated_at"] = datetime.utcnow()

            await stream.error(error_msg)

        except Exception as e:
            logger.error("search_job_failed", job_id=job_id, error=str(e))
            span.set_attribute("error", str(e))

            _jobs[job_id]["status"] = JobStatus.FAILED
            _jobs[job_id]["error"] = str(e)
            _jobs[job_id]["updated_at"] = datetime.utcnow()

            await stream.error(str(e))
