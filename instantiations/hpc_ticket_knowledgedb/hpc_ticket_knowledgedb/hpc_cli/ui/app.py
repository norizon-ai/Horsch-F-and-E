"""Main Textual application for HPC Assistant chat interface."""

import asyncio
from pathlib import Path
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import Container
from textual.binding import Binding
from textual.reactive import reactive
from rich.console import Console

from .widgets.chat_container import ChatContainer
from .widgets.input_area import ChatInput
from .widgets.status_bar import StatusBar
from ..config import get_config
from ..version import __version__

console = Console()


class HPCAssistantApp(App):
    """HPC Assistant chat interface - Claude Code inspired."""

    CSS_PATH = Path(__file__).parent / "styles" / "chat.tcss"

    TITLE = "HPC Assistant"
    SUB_TITLE = f"v{__version__}"

    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit", priority=True),
        Binding("ctrl+l", "clear_chat", "Clear"),
        Binding("ctrl+s", "save_session", "Save", show=False),
        Binding("ctrl+b", "toggle_brief", "Brief Mode", show=False),
        Binding("escape", "cancel_generation", "Cancel", show=False),
    ]

    # Reactive state
    is_generating: reactive[bool] = reactive(False)
    brief_mode: reactive[bool] = reactive(False)
    message_count: reactive[int] = reactive(0)

    def __init__(self, initial_query: str = None):
        super().__init__()
        self.initial_query = initial_query
        self.current_task = None
        self.config = get_config()

        # Lazy imports to avoid loading heavy dependencies
        self.chat_agent = None

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Header(show_clock=True)

        with Container(id="main-container"):
            yield ChatContainer(id="chat-container")
            yield ChatInput(id="chat-input")

        yield StatusBar(id="status-bar")

    async def on_mount(self) -> None:
        """Initialize app after mounting."""
        # Focus input area
        chat_input = self.query_one(ChatInput)
        chat_input.focus()

        # Update status bar
        status_bar = self.query_one(StatusBar)
        status_bar.set_message_count(0)
        status_bar.set_brief_mode(self.brief_mode)

        # Initialize chat agent (lazy)
        try:
            from ..agents.chat_agent import ChatAgent
            self.chat_agent = ChatAgent(self.config)
            await self.chat_agent.initialize()
        except Exception as e:
            console.print(f"[yellow]Warning: Failed to initialize chat agent: {e}[/yellow]")
            console.print("[dim]You can still use the UI, but LLM features may not work.[/dim]")

        # Process initial query if provided
        if self.initial_query:
            chat_container = self.query_one(ChatContainer)
            await chat_container.add_user_message(self.initial_query)
            self.message_count += 1
            await self._process_message(self.initial_query)

    async def on_chat_input_submitted(self, event: ChatInput.Submitted) -> None:
        """Handle user message submission."""
        message = event.message.strip()

        if not message:
            return

        # Add user message to chat
        chat_container = self.query_one(ChatContainer)
        await chat_container.add_user_message(message)

        self.message_count += 1
        self._update_status_bar()

        # Handle local UI commands (not processed by chat agent)
        if message.startswith("/"):
            cmd = message.lower().split()[0]
            # These are handled locally by the UI
            if cmd in ["/clear", "/save", "/load", "/gpu"]:
                await self._handle_command(message)
                return
            # /dr, /search, /help are handled by chat agent - fall through

        # Process with chat agent (handles /dr, /search, /help, and regular messages)
        await self._process_message(message)

    async def _process_message(self, message: str) -> None:
        """Process user message through chat agent."""
        if not self.chat_agent:
            chat_container = self.query_one(ChatContainer)
            await chat_container.add_system_message(
                "⚠️  Chat agent not initialized. Check your configuration."
            )
            return

        self.is_generating = True
        self._update_status_bar()

        chat_container = self.query_one(ChatContainer)

        # Create assistant message placeholder
        assistant_msg_id = await chat_container.add_assistant_message("")

        try:
            # Stream response from chat agent
            async for chunk in self.chat_agent.stream_response(
                message,
                brief=self.brief_mode
            ):
                chunk_type = chunk.get("type")

                if chunk_type == "content":
                    # Update message content (streaming)
                    await chat_container.append_message_content(
                        assistant_msg_id,
                        chunk.get("content", "")
                    )

                elif chunk_type == "tool_start":
                    # Show tool invocation
                    await chat_container.add_tool_display(
                        assistant_msg_id,
                        tool_name=chunk.get("tool", "unknown"),
                        params=chunk.get("params", {})
                    )

                elif chunk_type == "tool_result":
                    # Tool completed - result already displayed in tool_display
                    pass

                elif chunk_type == "progress":
                    # Update status bar with progress message
                    status_bar = self.query_one(StatusBar)
                    status_bar.set_status(chunk.get("message", "Processing..."))

                elif chunk_type == "error":
                    # Show error
                    await chat_container.add_error(
                        assistant_msg_id,
                        error=chunk.get("error", "Unknown error")
                    )

            self.message_count += 1
            self._update_status_bar()

        except asyncio.CancelledError:
            # User cancelled generation
            await chat_container.update_message(
                assistant_msg_id,
                "*[Generation cancelled by user]*"
            )
        except Exception as e:
            # Show error
            await chat_container.add_error(
                assistant_msg_id,
                error=str(e)
            )
        finally:
            self.is_generating = False
            self._update_status_bar()

    async def _handle_command(self, command: str) -> None:
        """Handle slash commands."""
        chat_container = self.query_one(ChatContainer)

        cmd = command.lower().split()[0]

        if cmd == "/help":
            help_text = """
**Available Commands:**

• `/help` - Show this help message
• `/clear` - Clear chat history
• `/gpu` - Check GPU cluster status
• `/dr <query>` - Deep research mode
• `/save <filename>` - Save conversation
• `/load <filename>` - Load conversation

**Keyboard Shortcuts:**

• `Ctrl+Enter` - Send message
• `Shift+Enter` - New line
• `Ctrl+Q` - Quit
• `Ctrl+L` - Clear chat
• `Ctrl+B` - Toggle brief mode
• `Escape` - Cancel generation
"""
            await chat_container.add_system_message(help_text)

        elif cmd == "/clear":
            await chat_container.clear()
            self.message_count = 0
            self._update_status_bar()
            await chat_container.add_system_message("✓ Chat cleared")

        elif cmd == "/gpu":
            await self._check_gpu_status()

        elif cmd.startswith("/dr"):
            # Extract query after /dr
            query = command[3:].strip()
            if query:
                await self._process_deep_research(query)
            else:
                await chat_container.add_system_message(
                    "Usage: /dr <your question>\nExample: /dr Why is my GPU job slow?"
                )

        elif cmd.startswith("/save"):
            parts = command.split(maxsplit=1)
            filename = parts[1] if len(parts) > 1 else "session.json"
            await self._save_session(filename)

        elif cmd.startswith("/load"):
            parts = command.split(maxsplit=1)
            filename = parts[1] if len(parts) > 1 else "session.json"
            await self._load_session(filename)

        else:
            await chat_container.add_system_message(
                f"Unknown command: {command}\nType /help for available commands"
            )

    async def _check_gpu_status(self) -> None:
        """Check GPU cluster status using cluster tools."""
        chat_container = self.query_one(ChatContainer)

        await chat_container.add_system_message("🔍 Checking GPU cluster status...")

        # TODO: Implement actual cluster check when cluster tools are integrated
        await chat_container.add_system_message(
            "⚠️  Cluster monitoring not yet implemented. Coming soon!"
        )

    async def _process_deep_research(self, query: str) -> None:
        """Process query with deep research mode."""
        chat_container = self.query_one(ChatContainer)

        await chat_container.add_system_message(
            f"🔬 Starting deep research: {query}"
        )

        # TODO: Implement DR integration
        await chat_container.add_system_message(
            "⚠️  Deep research not yet implemented. Coming soon!"
        )

    async def _save_session(self, filename: str) -> None:
        """Save conversation to file."""
        chat_container = self.query_one(ChatContainer)

        try:
            messages = await chat_container.get_all_messages()

            import json
            filepath = Path(filename)

            with filepath.open("w") as f:
                json.dump(messages, f, indent=2)

            await chat_container.add_system_message(
                f"✓ Session saved to {filename}"
            )
        except Exception as e:
            await chat_container.add_system_message(
                f"✗ Failed to save session: {e}"
            )

    async def _load_session(self, filename: str) -> None:
        """Load conversation from file."""
        chat_container = self.query_one(ChatContainer)

        try:
            import json
            filepath = Path(filename)

            if not filepath.exists():
                await chat_container.add_system_message(
                    f"✗ File not found: {filename}"
                )
                return

            with filepath.open("r") as f:
                messages = json.load(f)

            # Clear current chat
            await chat_container.clear()

            # Load messages
            for msg in messages:
                role = msg.get("role")
                content = msg.get("content", "")

                if role == "user":
                    await chat_container.add_user_message(content)
                elif role == "assistant":
                    await chat_container.add_assistant_message(content)
                elif role == "system":
                    await chat_container.add_system_message(content)

            self.message_count = len(messages)
            self._update_status_bar()

            await chat_container.add_system_message(
                f"✓ Session loaded from {filename}"
            )

        except Exception as e:
            await chat_container.add_system_message(
                f"✗ Failed to load session: {e}"
            )

    def _update_status_bar(self) -> None:
        """Update status bar with current state."""
        status_bar = self.query_one(StatusBar)
        status_bar.set_message_count(self.message_count)
        status_bar.set_brief_mode(self.brief_mode)
        status_bar.set_generating(self.is_generating)

    def action_quit(self) -> None:
        """Quit the application."""
        self.exit()

    def action_clear_chat(self) -> None:
        """Clear chat history."""
        self.run_worker(self._handle_command("/clear"))

    def action_save_session(self) -> None:
        """Save session."""
        self.run_worker(self._save_session("session.json"))

    def action_toggle_brief(self) -> None:
        """Toggle brief mode."""
        self.brief_mode = not self.brief_mode
        self._update_status_bar()

        chat_container = self.query_one(ChatContainer)
        mode = "ON" if self.brief_mode else "OFF"
        self.run_worker(
            chat_container.add_system_message(f"Brief mode: {mode}")
        )

    def action_cancel_generation(self) -> None:
        """Cancel ongoing generation."""
        if self.is_generating and self.current_task:
            self.current_task.cancel()


def run_chat_ui(initial_query: str = None):
    """Entry point for the chat UI.

    Args:
        initial_query: Optional initial query to process
    """
    app = HPCAssistantApp(initial_query=initial_query)
    app.run()


if __name__ == "__main__":
    run_chat_ui()
