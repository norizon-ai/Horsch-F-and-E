"""Welcome screen shown when chat is empty."""

from textual.widgets import Static
from textual.containers import Center, Middle
from rich.text import Text
from rich.panel import Panel


class WelcomeScreen(Center):
    """Welcome screen with helpful information."""

    DEFAULT_CSS = """
    WelcomeScreen {
        width: 100%;
        height: 100%;
        align: center middle;
    }

    WelcomeScreen Static {
        width: auto;
        height: auto;
    }
    """

    def compose(self):
        """Compose welcome screen."""
        # Create welcome content
        content = Text()
        content.append("🤖 ", style="bold #f86a0d")
        content.append("HPC Assistant\n\n", style="bold #0c2c40")

        content.append("Welcome! I can help you with:\n", style="#0c2c40")
        content.append("  • SLURM job submission and troubleshooting\n", style="#6c757d")
        content.append("  • GPU cluster monitoring and optimization\n", style="#6c757d")
        content.append("  • Deep research on HPC topics\n", style="#6c757d")
        content.append("  • Performance tuning and debugging\n\n", style="#6c757d")

        content.append("Quick commands:\n", style="#0c2c40")
        content.append("  /dr <question>  - Deep research with knowledge base\n", style="#f86a0d")
        content.append("  /search <query> - Direct search in docs/tickets\n", style="#f86a0d")
        content.append("  /help           - Show all commands\n", style="#f86a0d")
        content.append("  /clear          - Clear chat history\n\n", style="#f86a0d")

        content.append("Keyboard shortcuts:\n", style="#0c2c40")
        content.append("  Ctrl+J   - Send message\n", style="#1b3893")
        content.append("  Enter    - New line\n", style="#1b3893")
        content.append("  Ctrl+Q   - Quit\n", style="#1b3893")
        content.append("  Ctrl+L   - Clear chat\n\n", style="#1b3893")

        content.append("Type your question below to get started!", style="italic #5cb85c")

        yield Static(content)
