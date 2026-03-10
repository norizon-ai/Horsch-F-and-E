"""
Title: HPC Deep Research Pipeline
Author: HPC Team
Version: 1.0.0
License: MIT
Description: Multi-agent deep research system for HPC support questions
Requirements: requests
"""

from typing import List, Union, Generator, Iterator
from pydantic import BaseModel
import os
import requests
import json


class Pipeline:
    """OpenWebUI Pipeline for HPC Deep Research System"""

    class Valves(BaseModel):
        """Pipeline configuration"""
        DR_API_URL: str = "http://host.docker.internal:8000"
        DR_API_TIMEOUT: int = 180
        ENABLE_BRIEF_MODE: bool = False
        ENABLE_STREAMING: bool = True

    def __init__(self):
        self.name = "HPC Deep Research"
        self.valves = self.Valves(
            **{
                "DR_API_URL": os.getenv("DR_API_URL", "http://host.docker.internal:8000"),
                "DR_API_TIMEOUT": int(os.getenv("DR_API_TIMEOUT", "180")),
                "ENABLE_BRIEF_MODE": os.getenv("ENABLE_BRIEF_MODE", "false").lower() == "true",
                "ENABLE_STREAMING": os.getenv("ENABLE_STREAMING", "true").lower() == "true",
            }
        )

    async def on_startup(self):
        """Called when the pipeline is initialized"""
        print(f"HPC Deep Research Pipeline started")
        print(f"   API URL: {self.valves.DR_API_URL}")

    async def on_shutdown(self):
        """Called when the pipeline is shut down"""
        print("HPC Deep Research Pipeline shut down")

    def pipe(
        self, user_message: str, model_id: str, messages: List[dict], body: dict
    ) -> Union[str, Generator, Iterator]:
        """Process user message through HPC Deep Research Pipeline"""
        print(f"Processing HPC query: {user_message[:100]}...")

        if self.valves.ENABLE_STREAMING and body.get("stream", True):
            return self._pipe_stream(user_message)
        else:
            return self._pipe_sync(user_message)

    def _pipe_sync(self, user_message: str) -> str:
        """Synchronous (non-streaming) processing"""
        try:
            response = requests.post(
                f"{self.valves.DR_API_URL}/query",
                json={"query": user_message, "brief": self.valves.ENABLE_BRIEF_MODE},
                timeout=self.valves.DR_API_TIMEOUT
            )

            if response.status_code != 200:
                return f"[ERROR] DR API returned {response.status_code}: {response.text}"

            result = response.json()
            answer = result.get("concise_answer", "No answer generated")
            confidence = result.get("confidence_score", 0.0)
            iterations = result.get("total_iterations", 0)
            processing_time = result.get("processing_time", 0.0)

            metadata = f"\n\n---\n*Confidence: {confidence:.2f} | Iterations: {iterations} | Time: {processing_time:.1f}s*"

            if not self.valves.ENABLE_BRIEF_MODE and result.get("final_report"):
                return f"{answer}\n\n## Detailed Research\n\n{result['final_report']}{metadata}"

            return f"{answer}{metadata}"

        except requests.Timeout:
            return "[!] Request timed out. Please try a simpler question."
        except Exception as e:
            return f"[ERROR] Error processing query: {str(e)}"

    def _pipe_stream(self, user_message: str) -> Generator:
        """Streaming processing with Server-Sent Events"""
        try:
            response = requests.post(
                f"{self.valves.DR_API_URL}/query/stream",
                json={"query": user_message, "brief": self.valves.ENABLE_BRIEF_MODE},
                stream=True,
                timeout=self.valves.DR_API_TIMEOUT
            )

            if response.status_code != 200:
                yield f"[ERROR] DR API returned {response.status_code}\n"
                return

            for line in response.iter_lines(decode_unicode=True):
                if not line:
                    continue

                if line.startswith("data: "):
                    data_str = line[6:]
                    try:
                        data = json.loads(data_str)
                        event_type = data.get("type")

                        if event_type == "started":
                            yield "Starting deep research...\n\n"
                        elif event_type == "iteration":
                            yield f"Iteration {data.get('number')}/{data.get('total')}...\n"
                        elif event_type == "completed":
                            answer = data.get("answer", "No answer generated")
                            confidence = data.get("confidence", 0.0)
                            iterations = data.get("iterations", 0)
                            processing_time = data.get("processing_time", 0.0)
                            yield f"\n\n{answer}\n\n"
                            yield f"---\n*Confidence: {confidence:.2f} | Iterations: {iterations} | Time: {processing_time:.1f}s*\n"
                        elif event_type == "error":
                            yield f"\n\n[ERROR] {data.get('message', 'Unknown error')}\n"
                    except json.JSONDecodeError:
                        continue

        except requests.Timeout:
            yield "\n\n[!] Request timed out.\n"
        except Exception as e:
            yield f"\n\n[ERROR] {str(e)}\n"
