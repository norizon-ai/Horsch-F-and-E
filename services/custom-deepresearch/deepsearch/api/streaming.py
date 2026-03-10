"""
SSE Streaming Utilities

Server-Sent Events support for real-time search progress updates.
"""

import asyncio
import json
from typing import AsyncIterator, Any, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime

from deepsearch.observability import get_logger

logger = get_logger(__name__)


@dataclass
class StreamEvent:
    """A server-sent event."""

    event: str  # Event type: "progress", "iteration", "complete", "error"
    data: Dict[str, Any]
    id: Optional[str] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_sse(self) -> str:
        """Format as SSE message."""
        lines = []
        if self.id:
            lines.append(f"id: {self.id}")
        lines.append(f"event: {self.event}")
        lines.append(f"data: {json.dumps(self.data)}")
        return "\n".join(lines) + "\n\n"


class EventStream:
    """
    Manages SSE events for a search job.

    Usage:
        stream = EventStream()

        # Producer (in background task):
        await stream.emit("progress", {"phase": "searching"})
        await stream.emit("iteration", {"number": 1})
        await stream.complete(result)

        # Consumer (in SSE endpoint):
        async for event in stream.events():
            yield event.to_sse()
    """

    def __init__(self, job_id: str):
        self.job_id = job_id
        self._queue: asyncio.Queue[StreamEvent] = asyncio.Queue()
        self._complete = False
        self._event_counter = 0

    async def emit(self, event_type: str, data: Dict[str, Any]) -> None:
        """
        Emit an event to the stream.

        Args:
            event_type: Event type (progress, iteration, error)
            data: Event data
        """
        self._event_counter += 1
        event = StreamEvent(
            event=event_type,
            data=data,
            id=f"{self.job_id}-{self._event_counter}",
        )
        await self._queue.put(event)

        logger.debug(
            "stream_event_emitted",
            job_id=self.job_id,
            event_type=event_type,
        )

    async def progress(self, phase: str, message: str, **extra) -> None:
        """Emit a progress event."""
        await self.emit(
            "progress",
            {
                "phase": phase,
                "message": message,
                **extra,
            },
        )

    async def iteration(
        self,
        number: int,
        tools_called: list,
        decision: Optional[str] = None,
    ) -> None:
        """Emit an iteration complete event."""
        await self.emit(
            "iteration",
            {
                "iteration_number": number,
                "tools_called": tools_called,
                "decision_next_step": decision,
            },
        )

    async def agent_status(
        self,
        iteration_number: int,
        agent_name: str,
        status: str,
        search_query: Optional[str] = None,
        results_count: Optional[int] = None,
        display_name: Optional[str] = None,
        icon_url: Optional[str] = None,
        searching_label: Optional[str] = None,
        item_label: Optional[str] = None,
    ) -> None:
        """Emit an agent status event for real-time parallel execution feedback.

        Args:
            iteration_number: Which iteration this agent is part of
            agent_name: Name of the agent/tool
            status: "searching" when started, "done" when completed
            search_query: The query being searched (optional)
            results_count: Number of results found (optional, for done status)
            display_name: Human-readable name for UI display (optional)
            icon_url: URL to source icon for UI display (optional)
            searching_label: Label to show while searching (e.g., "Searching the web...")
            item_label: Label for counted items (e.g., "websites", "pages")
        """
        await self.emit(
            "agent_status",
            {
                "iteration_number": iteration_number,
                "agent_name": agent_name,
                "status": status,
                "search_query": search_query,
                "results_count": results_count,
                "display_name": display_name,
                "icon_url": icon_url,
                "searching_label": searching_label,
                "item_label": item_label,
            },
        )

    async def report_chunk(self, content: str) -> None:
        """Emit a chunk of the final report for streaming.

        Args:
            content: Text chunk of the report
        """
        logger.debug("report_chunk_emitting", length=len(content), queue_size=self._queue.qsize())
        await self.emit("report_chunk", {"content": content})

    async def complete(self, result: Any) -> None:
        """
        Mark stream as complete with final result.

        Args:
            result: Final result to send
        """
        # Serialize result if it's a Pydantic model
        # Use mode="json" to properly serialize datetime objects to ISO format strings
        if hasattr(result, "model_dump"):
            data = result.model_dump(mode="json")
        elif hasattr(result, "dict"):
            data = result.dict()
        else:
            data = {"result": str(result)}

        await self.emit("complete", data)
        self._complete = True

        logger.info("stream_complete", job_id=self.job_id)

    async def error(self, error: str, detail: Optional[str] = None) -> None:
        """
        Emit an error event and complete the stream.

        Args:
            error: Error message
            detail: Additional detail
        """
        await self.emit(
            "error",
            {
                "error": error,
                "detail": detail,
            },
        )
        self._complete = True

        logger.error("stream_error", job_id=self.job_id, error=error)

    async def events(self) -> AsyncIterator[StreamEvent]:
        """
        Iterate over events as they arrive.

        Yields:
            StreamEvent objects
        """
        while not self._complete:
            try:
                event = await asyncio.wait_for(self._queue.get(), timeout=30)
                yield event
                if event.event in ("complete", "error"):
                    break
            except asyncio.TimeoutError:
                # Send keepalive
                yield StreamEvent(event="keepalive", data={})

    @property
    def is_complete(self) -> bool:
        """Check if stream is complete."""
        return self._complete


class StreamManager:
    """
    Manages multiple event streams for concurrent jobs.

    Usage:
        manager = StreamManager()

        # Create stream for job
        stream = manager.create(job_id)

        # Get stream later
        stream = manager.get(job_id)

        # Clean up
        manager.remove(job_id)
    """

    def __init__(self):
        self._streams: Dict[str, EventStream] = {}

    def create(self, job_id: str) -> EventStream:
        """Create a new event stream for a job."""
        stream = EventStream(job_id)
        self._streams[job_id] = stream
        return stream

    def get(self, job_id: str) -> Optional[EventStream]:
        """Get an existing event stream."""
        return self._streams.get(job_id)

    def remove(self, job_id: str) -> None:
        """Remove a stream."""
        self._streams.pop(job_id, None)

    def cleanup_completed(self) -> int:
        """Remove completed streams. Returns count removed."""
        completed = [
            job_id for job_id, stream in self._streams.items() if stream.is_complete
        ]
        for job_id in completed:
            del self._streams[job_id]
        return len(completed)


# Global stream manager instance
stream_manager = StreamManager()
