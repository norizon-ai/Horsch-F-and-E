"""Chat orchestration with tool integration."""

import asyncio
from typing import AsyncIterator, Dict, Any, List, Optional

from .llm_client import LLMClient
from ..dr.client import DRClient


class ChatAgent:
    """Orchestrates chat with LLM, tools, and deep research."""

    def __init__(self, config):
        """Initialize chat agent.

        Args:
            config: Configuration object
        """
        self.config = config
        self.llm_client = LLMClient(config)
        self.dr_client = DRClient()
        self.conversation_history: List[Dict[str, str]] = []

    async def initialize(self) -> None:
        """Initialize agent and dependencies."""
        await self.llm_client.initialize()

    def _parse_command(self, message: str) -> tuple[Optional[str], str]:
        """Parse slash commands from message.

        Returns:
            (command, rest_of_message) or (None, original_message)
        """
        message = message.strip()
        if message.startswith("/"):
            parts = message.split(maxsplit=1)
            command = parts[0].lower()
            rest = parts[1] if len(parts) > 1 else ""
            return command, rest
        return None, message

    async def stream_response(
        self,
        user_message: str,
        brief: bool = False
    ) -> AsyncIterator[Dict[str, Any]]:
        """Stream LLM response with tool invocation.

        Args:
            user_message: User's message
            brief: Whether to use brief mode

        Yields:
            chunks: Dictionary with type and content:
                - {"type": "content", "content": "..."}
                - {"type": "tool_start", "tool": "...", "params": {...}}
                - {"type": "tool_result", "tool": "...", "result": {...}}
                - {"type": "progress", "message": "..."}
                - {"type": "error", "error": "..."}
        """
        # Parse for slash commands
        command, query = self._parse_command(user_message)

        # Handle /dr command - Deep Research
        if command == "/dr":
            async for chunk in self._handle_dr_command(query, brief):
                yield chunk
            return

        # Handle /search command
        if command == "/search":
            async for chunk in self._handle_search_command(query):
                yield chunk
            return

        # Handle /help command
        if command == "/help":
            yield {"type": "content", "content": self._get_help_text()}
            return

        # Add user message to history for regular chat
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })

        try:
            # Stream LLM response
            full_response = ""

            async for chunk in self.llm_client.stream_chat(
                messages=self.conversation_history,
                brief=brief
            ):
                full_response += chunk
                yield {"type": "content", "content": chunk}

            # Add assistant response to history
            self.conversation_history.append({
                "role": "assistant",
                "content": full_response
            })

        except Exception as e:
            yield {"type": "error", "error": str(e)}

    async def _handle_dr_command(
        self,
        query: str,
        brief: bool
    ) -> AsyncIterator[Dict[str, Any]]:
        """Handle /dr command for deep research."""
        if not query:
            yield {"type": "error", "error": "Usage: /dr <your question>"}
            return

        # Check DR API connection
        is_healthy = await self.dr_client.health_check()
        if not is_healthy:
            yield {"type": "error", "error": f"Cannot connect to DR API at {self.dr_client.base_url}"}
            return

        yield {"type": "tool_start", "tool": "Deep Research", "params": {"query": query}}
        yield {"type": "progress", "message": "Starting deep research..."}

        try:
            full_response = ""

            def on_progress(status: str):
                # Progress callback (can't yield from here, but tracking for future use)
                pass

            async for chunk in self.dr_client.query_stream(
                query=query,
                brief=brief,
                on_progress=on_progress
            ):
                full_response += chunk
                yield {"type": "content", "content": chunk}

            # Add to conversation history
            self.conversation_history.append({
                "role": "user",
                "content": f"/dr {query}"
            })
            self.conversation_history.append({
                "role": "assistant",
                "content": f"[Deep Research]\n\n{full_response}"
            })

        except Exception as e:
            yield {"type": "error", "error": f"Deep Research failed: {e}"}

    async def _handle_search_command(self, query: str) -> AsyncIterator[Dict[str, Any]]:
        """Handle /search command for direct search."""
        if not query:
            yield {"type": "error", "error": "Usage: /search <query>"}
            return

        # Parse index from query (e.g., "/search tickets: GPU error")
        index = "docs"
        if query.startswith("tickets:"):
            index = "tickets"
            query = query[8:].strip()
        elif query.startswith("docs:"):
            query = query[5:].strip()

        is_healthy = await self.dr_client.health_check()
        if not is_healthy:
            yield {"type": "error", "error": f"Cannot connect to DR API at {self.dr_client.base_url}"}
            return

        yield {"type": "tool_start", "tool": "Search", "params": {"query": query, "index": index}}

        try:
            results = await self.dr_client.search(query, index=index, max_results=5)

            if not results:
                yield {"type": "content", "content": f"No results found for '{query}' in {index}"}
                return

            # Format results as markdown
            output = f"**Search Results ({index}):**\n\n"
            for i, result in enumerate(results, 1):
                title = result.get("title", "Untitled")
                text = result.get("text", result.get("problem_description", ""))[:200]
                output += f"**{i}. {title}**\n{text}...\n\n"

            yield {"type": "content", "content": output}

        except Exception as e:
            yield {"type": "error", "error": f"Search failed: {e}"}

    def _get_help_text(self) -> str:
        """Get help text for chat commands."""
        return """**Available Commands:**

- `/dr <question>` - Run deep research on HPC questions
- `/search <query>` - Search documentation directly
- `/search tickets: <query>` - Search support tickets
- `/help` - Show this help message

**Keyboard Shortcuts:**
- `Ctrl+J` - Send message
- `Ctrl+Q` - Quit
- `Ctrl+L` - Clear chat
- `Escape` - Clear input

**Examples:**
- `/dr How do I optimize GPU memory usage?`
- `/search SLURM job arrays`
- `/search tickets: CUDA out of memory`
"""

    async def close(self) -> None:
        """Close agent resources."""
        await self.llm_client.close()
