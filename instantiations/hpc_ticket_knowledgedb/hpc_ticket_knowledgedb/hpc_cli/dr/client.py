"""Deep Research API client.

Connects to the running DR API service for HPC support queries.
"""

import httpx
import json
from typing import Optional, AsyncIterator, Callable
from dataclasses import dataclass

from ..config import get_config


@dataclass
class DRResult:
    """Deep Research result."""
    concise_answer: str
    final_report: str
    confidence_score: float
    iterations_count: int
    sources: list


class DRClient:
    """Client for Deep Research API."""

    def __init__(self, base_url: Optional[str] = None, timeout: Optional[int] = None):
        config = get_config()
        self.base_url = base_url or config.dr.api_url
        self.timeout = timeout or config.dr.timeout

    async def health_check(self) -> bool:
        """Check if DR API is reachable."""
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                response = await client.get(f"{self.base_url}/health")
                return response.status_code == 200
        except Exception:
            return False

    async def query(self, query: str, brief: bool = False) -> DRResult:
        """Run synchronous DR query.

        Args:
            query: The research question
            brief: If True, returns shorter answers

        Returns:
            DRResult with answer and metadata
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(
                f"{self.base_url}/query",
                json={"query": query, "brief": brief}
            )
            response.raise_for_status()
            data = response.json()

            return DRResult(
                concise_answer=data.get("concise_answer", ""),
                final_report=data.get("final_report", ""),
                confidence_score=data.get("confidence_score", 0.0),
                iterations_count=data.get("iterations_count", 0),
                sources=data.get("sources", [])
            )

    async def query_stream(
        self,
        query: str,
        brief: bool = False,
        on_progress: Optional[Callable[[str], None]] = None
    ) -> AsyncIterator[str]:
        """Run streaming DR query with SSE.

        Args:
            query: The research question
            brief: If True, returns shorter answers
            on_progress: Optional callback for progress updates

        Yields:
            Chunks of the response as they arrive
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            async with client.stream(
                "POST",
                f"{self.base_url}/query/stream",
                json={"query": query, "brief": brief},
                headers={"Accept": "text/event-stream"}
            ) as response:
                response.raise_for_status()

                buffer = ""
                async for chunk in response.aiter_text():
                    buffer += chunk

                    # Parse SSE events
                    while "\n\n" in buffer:
                        event, buffer = buffer.split("\n\n", 1)

                        for line in event.split("\n"):
                            if line.startswith("data: "):
                                data = line[6:]  # Remove "data: " prefix

                                # Try to parse as JSON
                                try:
                                    parsed = json.loads(data)

                                    # Handle different event types
                                    if "progress" in parsed:
                                        if on_progress:
                                            on_progress(parsed["progress"])
                                    elif "chunk" in parsed:
                                        yield parsed["chunk"]
                                    elif "answer" in parsed:
                                        yield parsed["answer"]
                                    elif "error" in parsed:
                                        raise Exception(parsed["error"])
                                    elif "done" in parsed:
                                        return
                                except json.JSONDecodeError:
                                    # Plain text chunk
                                    if data and data != "[DONE]":
                                        yield data

    async def search(
        self,
        query: str,
        index: str = "docs",
        max_results: int = 10
    ) -> list:
        """Direct Elasticsearch search (bypasses DR pipeline).

        Args:
            query: Search query
            index: 'docs' or 'tickets'
            max_results: Maximum results to return

        Returns:
            List of search results
        """
        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                f"{self.base_url}/search",
                json={
                    "query": query,
                    "index": index,
                    "max_results": max_results
                }
            )
            response.raise_for_status()
            return response.json().get("results", [])


# Convenience function
async def check_dr_connection() -> tuple[bool, str]:
    """Check DR API connection and return status message."""
    client = DRClient()
    try:
        is_healthy = await client.health_check()
        if is_healthy:
            return True, f"DR API connected at {client.base_url}"
        else:
            return False, f"DR API not responding at {client.base_url}"
    except Exception as e:
        return False, f"DR API connection failed: {e}"
