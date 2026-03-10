"""LLM client with streaming support."""

import httpx
import asyncio
from typing import AsyncIterator, List, Dict, Any


class LLMClient:
    """Streaming LLM client for OpenAI-compatible APIs."""

    def __init__(self, config):
        """Initialize LLM client.

        Args:
            config: Configuration object with LLM settings
        """
        self.config = config
        # Use longer timeout for LLM requests (GPT-OSS 120B can be slow)
        timeout = httpx.Timeout(
            connect=10.0,
            read=120.0,  # Long read timeout for streaming
            write=10.0,
            pool=10.0
        )
        self.client = httpx.AsyncClient(timeout=timeout)

    async def initialize(self) -> None:
        """Initialize client (test connection)."""
        try:
            # Test connection
            response = await self.client.get(
                f"{self.config.llm.url}/models",
                timeout=5
            )
            if response.status_code != 200:
                print(f"Warning: LLM endpoint returned {response.status_code}")
        except Exception as e:
            print(f"Warning: Could not connect to LLM endpoint: {e}")

    async def stream_chat(
        self,
        messages: List[Dict[str, str]],
        brief: bool = False
    ) -> AsyncIterator[str]:
        """Stream chat completion.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            brief: Whether to request brief responses

        Yields:
            str: Content chunks
        """
        # Build request
        payload = {
            "model": self.config.llm.model,
            "messages": messages,
            "temperature": self.config.llm.temperature,
            "max_tokens": self.config.llm.max_tokens,
            "stream": True
        }

        # Add system prompt for brief mode
        if brief:
            payload["messages"] = [
                {
                    "role": "system",
                    "content": "Provide concise, brief answers. Be direct and to the point."
                }
            ] + messages

        try:
            async with self.client.stream(
                "POST",
                f"{self.config.llm.url}/chat/completions",
                json=payload,
                headers={"Authorization": f"Bearer {self.config.llm.api_key}"}
            ) as response:
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        data_str = line[6:]  # Remove "data: " prefix

                        if data_str.strip() == "[DONE]":
                            break

                        try:
                            import json
                            data = json.loads(data_str)

                            # Extract content
                            if "choices" in data and len(data["choices"]) > 0:
                                delta = data["choices"][0].get("delta", {})
                                content = delta.get("content", "")

                                if content:
                                    yield content

                        except json.JSONDecodeError:
                            continue

        except Exception as e:
            yield f"\n\n[Error: {str(e)}]"

    async def chat(
        self,
        messages: List[Dict[str, str]],
        brief: bool = False
    ) -> str:
        """Non-streaming chat completion.

        Args:
            messages: List of message dictionaries
            brief: Whether to request brief responses

        Returns:
            str: Complete response
        """
        chunks = []
        async for chunk in self.stream_chat(messages, brief):
            chunks.append(chunk)

        return "".join(chunks)

    async def close(self) -> None:
        """Close client."""
        await self.client.aclose()
