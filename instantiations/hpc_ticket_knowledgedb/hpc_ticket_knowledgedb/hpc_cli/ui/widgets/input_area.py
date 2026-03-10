"""Multi-line input area with keyboard shortcuts."""

from textual.widgets import TextArea
from textual.message import Message
from textual.binding import Binding


class ChatInput(TextArea):
    """Multi-line chat input with custom key bindings."""

    BINDINGS = [
        Binding("ctrl+j", "submit", "Send", show=False),
        Binding("escape", "clear_input", "Clear", show=False),
    ]

    DEFAULT_CSS = """
    ChatInput {
        height: 5;
        min-height: 3;
        max-height: 10;
        margin: 0 2 1 2;
        padding: 1;
        border: tall #1b3893;
        background: #ffffff;
        color: #0c2c40;
    }

    ChatInput:focus {
        border: tall #f86a0d;
    }
    """

    class Submitted(Message):
        """Message sent when user submits input."""

        def __init__(self, message: str):
            super().__init__()
            self.message = message

    def __init__(self, **kwargs):
        super().__init__(
            text="",
            language="markdown",
            theme="monokai",
            show_line_numbers=False,
            **kwargs
        )

    def on_mount(self) -> None:
        """Set up input area after mounting."""
        # Placeholder hint
        if not self.text:
            self.text = ""

    def action_submit(self) -> None:
        """Submit message action."""
        message = self.text.strip()
        if message:
            self.post_message(self.Submitted(message))
            self.clear_input()

    def action_clear_input(self) -> None:
        """Clear input action."""
        self.clear_input()

    def clear_input(self) -> None:
        """Clear input area."""
        self.text = ""
        self.move_cursor((0, 0))
