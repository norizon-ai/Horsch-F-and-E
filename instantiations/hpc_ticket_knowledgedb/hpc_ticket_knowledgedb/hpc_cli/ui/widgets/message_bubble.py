"""Message bubble widgets for chat interface."""

from textual.widgets import Static
from textual.containers import Vertical
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.panel import Panel
from rich.text import Text
from datetime import datetime


class UserMessage(Vertical):
    """User message bubble with cyan styling."""

    DEFAULT_CSS = """
    UserMessage {
        width: 100%;
        height: auto;
        margin: 0 0 1 0;
        padding: 1 2;
        background: #cef1ff;
        border: round #1b3893;
    }

    UserMessage .message-header {
        color: #1b3893;
        text-style: bold;
    }

    UserMessage .message-content {
        margin: 1 0 0 0;
        color: #0c2c40;
    }
    """

    def __init__(self, content: str, timestamp: datetime = None):
        super().__init__()
        self.content = content
        self.timestamp = timestamp or datetime.now()
        self._content_widget = None

    def compose(self):
        """Compose message bubble."""
        # Header with timestamp
        header_text = Text()
        header_text.append("You", style="bold #1b3893")
        header_text.append(f"  {self.timestamp.strftime('%H:%M:%S')}", style="#6c757d")

        yield Static(header_text, classes="message-header")

        # Content
        self._content_widget = Static(self.content, classes="message-content")
        yield self._content_widget

    def to_dict(self) -> dict:
        """Export message as dict for session saving."""
        return {
            "role": "user",
            "content": self.content,
            "timestamp": self.timestamp.isoformat()
        }


class AssistantMessage(Vertical):
    """Assistant message bubble with markdown rendering."""

    DEFAULT_CSS = """
    AssistantMessage {
        width: 100%;
        height: auto;
        margin: 0 0 1 0;
        padding: 1 2;
        background: #ffffff;
        border: round #f86a0d;
    }

    AssistantMessage .message-header {
        color: #f86a0d;
        text-style: bold;
    }

    AssistantMessage .message-content {
        margin: 1 0 0 0;
        color: #0c2c40;
    }

    AssistantMessage .streaming-indicator {
        color: #f86a0d;
        text-style: italic;
    }

    AssistantMessage .tool-display {
        margin: 1 0;
        padding: 1;
        background: #fef0e3;
        border: solid #f86a0d;
    }

    AssistantMessage .error-display {
        margin: 1 0;
        padding: 1;
        background: #ffe6e6;
        border: solid #d9534f;
        color: #0c2c40;
    }
    """

    def __init__(self, content: str = "", timestamp: datetime = None):
        super().__init__()
        self.content = content
        self.timestamp = timestamp or datetime.now()
        self.is_streaming = not content  # Streaming if initialized empty
        self._content_widget = None
        self._header_widget = None

    def compose(self):
        """Compose message bubble."""
        # Header
        header_text = Text()
        header_text.append("Assistant", style="bold #f86a0d")
        header_text.append(f"  {self.timestamp.strftime('%H:%M:%S')}", style="#6c757d")

        if self.is_streaming:
            header_text.append("  [Thinking...]", style="#f86a0d italic")

        self._header_widget = Static(header_text, classes="message-header")
        yield self._header_widget

        # Content (rendered as Markdown)
        if self.content:
            md = Markdown(self.content)
            self._content_widget = Static(md, classes="message-content")
            yield self._content_widget

    async def update_content(self, content: str) -> None:
        """Update message content (replace existing)."""
        self.content = content
        self.is_streaming = False

        # Update header to remove "Thinking..."
        header_text = Text()
        header_text.append("Assistant", style="bold #f86a0d")
        header_text.append(f"  {self.timestamp.strftime('%H:%M:%S')}", style="#6c757d")
        if self._header_widget:
            self._header_widget.update(header_text)

        # Re-render content
        if self._content_widget:
            await self._content_widget.remove()

        if content:
            md = Markdown(content)
            self._content_widget = Static(md, classes="message-content")
            await self.mount(self._content_widget)

    async def append_content(self, content: str) -> None:
        """Append content (for streaming)."""
        self.content += content
        await self.update_content(self.content)

    async def add_tool_display(self, tool_name: str, params: dict, result: dict = None) -> None:
        """Add tool execution display."""
        tool_text = Text()
        tool_text.append(f"🔧 Using tool: {tool_name}\n", style="bold #f86a0d")

        if params:
            tool_text.append("Parameters:\n", style="#6c757d")
            for key, value in params.items():
                tool_text.append(f"  • {key}: {value}\n", style="#6c757d")

        if result:
            tool_text.append("\nResult:\n", style="bold #5cb85c")
            # Format result (simplified - could be enhanced)
            result_str = str(result)[:500]  # Truncate if too long
            tool_text.append(result_str, style="#6c757d")

        tool_widget = Static(tool_text, classes="tool-display")
        await self.mount(tool_widget)

    async def add_error(self, error: str) -> None:
        """Add error display."""
        error_text = Text()
        error_text.append("⚠️  Error: ", style="bold #d9534f")
        error_text.append(error, style="#d9534f")

        error_widget = Static(error_text, classes="error-display")
        await self.mount(error_widget)

    def to_dict(self) -> dict:
        """Export message as dict for session saving."""
        return {
            "role": "assistant",
            "content": self.content,
            "timestamp": self.timestamp.isoformat()
        }


class SystemMessage(Static):
    """System message for commands and notifications."""

    DEFAULT_CSS = """
    SystemMessage {
        width: 100%;
        height: auto;
        margin: 0 0 1 0;
        padding: 1 2;
        background: #e8f4f8;
        border: round #6c757d;
        color: #6c757d;
        text-align: center;
        text-style: italic;
    }
    """

    def __init__(self, content: str):
        super().__init__(content)

    def to_dict(self) -> dict:
        """Export message as dict."""
        return {
            "role": "system",
            "content": str(self.renderable),
            "timestamp": datetime.now().isoformat()
        }
