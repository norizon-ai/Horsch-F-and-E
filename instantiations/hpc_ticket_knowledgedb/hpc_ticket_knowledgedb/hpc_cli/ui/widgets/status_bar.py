"""Status bar with session information."""

from textual.widgets import Static
from textual.containers import Horizontal
from rich.text import Text


class StatusBar(Static):
    """Bottom status bar with session info and hints."""

    DEFAULT_CSS = """
    StatusBar {
        height: 1;
        width: 100%;
        background: #cef1ff;
        color: #0c2c40;
        padding: 0 2;
    }

    StatusBar .status-left {
        width: 1fr;
    }

    StatusBar .status-right {
        width: auto;
        text-align: right;
    }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.message_count = 0
        self.brief_mode = False
        self.is_generating = False
        self.custom_status = ""

    def compose(self):
        """Compose status bar."""
        yield Static(self._render_status())

    def _render_status(self) -> Text:
        """Render status bar content."""
        status = Text()

        # Left side - hints or custom status
        if self.is_generating:
            if self.custom_status:
                status.append(f"⏳ {self.custom_status} ", style="#f86a0d")
            else:
                status.append("⏳ Generating... ", style="#f86a0d")
            status.append("[Esc to cancel] ", style="#6c757d")
        else:
            status.append("[Ctrl+J: Send] ", style="#6c757d")
            status.append("[Ctrl+Q: Quit] ", style="#6c757d")

        # Spacer
        status.append(" " * 10)

        # Right side - session info
        status.append(f"Brief: ", style="#6c757d")
        if self.brief_mode:
            status.append("ON", style="bold #5cb85c")
        else:
            status.append("OFF", style="#6c757d")

        status.append(f"  |  Messages: {self.message_count}", style="#6c757d")

        return status

    def set_message_count(self, count: int) -> None:
        """Update message count."""
        self.message_count = count
        self.update(self._render_status())

    def set_brief_mode(self, enabled: bool) -> None:
        """Update brief mode indicator."""
        self.brief_mode = enabled
        self.update(self._render_status())

    def set_generating(self, is_generating: bool) -> None:
        """Update generating status."""
        self.is_generating = is_generating
        if not is_generating:
            self.custom_status = ""  # Clear custom status when done
        self.update(self._render_status())

    def set_status(self, message: str) -> None:
        """Set custom status message."""
        self.custom_status = message
        self.update(self._render_status())
