"""
title: HPC Deep Research
author: HPC Team
version: 1.0.0
license: MIT
requirements: requests
"""

import requests
from typing import Callable, Any
from pydantic import BaseModel, Field


class Pipe:
    """OpenWebUI Function for HPC Deep Research System"""

    class Valves(BaseModel):
        """Configuration"""
        DR_API_URL: str = Field(
            default="http://172.17.70.18:8001",
            description="URL of the DR API server (OpenStack deployment)"
        )
        DR_API_TIMEOUT: int = Field(
            default=180,
            description="Request timeout in seconds"
        )
        ENABLE_BRIEF_MODE: bool = Field(
            default=False,
            description="Enable brief mode for faster responses"
        )

    def __init__(self):
        self.type = "manifold"
        self.id = "hpc_deep_research"
        self.name = "HPC Deep Research"
        self.valves = self.Valves()

    def pipes(self):
        """Return available models"""
        return [
            {
                "id": "hpc-dr",
                "name": "HPC Deep Research"
            }
        ]

    def pipe(self, body: dict) -> str:
        """Process user query through DR API"""

        # Extract user message
        messages = body.get("messages", [])
        if not messages:
            return "Error: No messages provided"

        user_message = messages[-1].get("content", "")
        if not user_message:
            return "Error: Empty message"

        try:
            # Call DR API
            response = requests.post(
                f"{self.valves.DR_API_URL}/query",
                json={
                    "query": user_message,
                    "brief": self.valves.ENABLE_BRIEF_MODE
                },
                timeout=self.valves.DR_API_TIMEOUT
            )

            if response.status_code != 200:
                return f"[ERROR] DR API returned {response.status_code}: {response.text}"

            result = response.json()

            # Format response
            answer = result.get("concise_answer", "No answer generated")
            confidence = result.get("confidence_score", 0.0)
            iterations = result.get("total_iterations", 0)
            processing_time = result.get("processing_time", 0.0)

            # Add metadata
            metadata = f"\n\n---\n*Confidence: {confidence:.2f} | Iterations: {iterations} | Time: {processing_time:.1f}s*"

            # Include detailed report if not in brief mode
            if not self.valves.ENABLE_BRIEF_MODE and result.get("final_report"):
                return f"{answer}\n\n## Detailed Research\n\n{result['final_report']}{metadata}"

            return f"{answer}{metadata}"

        except requests.Timeout:
            return "[ERROR] Request timed out. The query is taking longer than expected. Please try a simpler question."
        except Exception as e:
            return f"[ERROR] Error processing query: {str(e)}"
