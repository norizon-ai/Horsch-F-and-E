"""Scrollable chat container with message management."""

from textual.widgets import Static
from textual.containers import VerticalScroll
from datetime import datetime
import uuid

from .message_bubble import UserMessage, AssistantMessage, SystemMessage
from .welcome_screen import WelcomeScreen


class ChatContainer(VerticalScroll):
    """Scrollable container for chat messages."""

    DEFAULT_CSS = """
    ChatContainer {
        height: 1fr;
        width: 100%;
        padding: 1 2;
        background: #fef0e3;
    }

    ChatContainer:focus {
        border: none;
    }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.messages = {}  # message_id -> widget mapping
        self.message_order = []  # ordered list of message IDs
        self._welcome_screen = None

    def on_mount(self) -> None:
        """Show welcome screen when empty."""
        self._welcome_screen = WelcomeScreen()
        self.mount(self._welcome_screen)

    async def add_user_message(self, content: str) -> str:
        """Add user message to chat.

        Args:
            content: Message content

        Returns:
            message_id: Unique identifier for the message
        """
        # Remove welcome screen if present
        if self._welcome_screen and self._welcome_screen.is_mounted:
            await self._welcome_screen.remove()
            self._welcome_screen = None

        message_id = str(uuid.uuid4())
        timestamp = datetime.now()

        message = UserMessage(content, timestamp)
        await self.mount(message)

        self.messages[message_id] = message
        self.message_order.append(message_id)

        # Auto-scroll to bottom
        self.scroll_end(animate=True)

        return message_id

    async def add_assistant_message(self, content: str = "") -> str:
        """Add assistant message to chat.

        Args:
            content: Initial message content (empty for streaming)

        Returns:
            message_id: Unique identifier for the message
        """
        # Remove welcome screen if present
        if self._welcome_screen and self._welcome_screen.is_mounted:
            await self._welcome_screen.remove()
            self._welcome_screen = None

        message_id = str(uuid.uuid4())
        timestamp = datetime.now()

        message = AssistantMessage(content, timestamp)
        await self.mount(message)

        self.messages[message_id] = message
        self.message_order.append(message_id)

        # Auto-scroll to bottom
        self.scroll_end(animate=True)

        return message_id

    async def add_system_message(self, content: str) -> str:
        """Add system message to chat.

        Args:
            content: Message content

        Returns:
            message_id: Unique identifier for the message
        """
        message_id = str(uuid.uuid4())

        message = SystemMessage(content)
        await self.mount(message)

        self.messages[message_id] = message
        self.message_order.append(message_id)

        # Auto-scroll to bottom
        self.scroll_end(animate=True)

        return message_id

    async def update_message(self, message_id: str, content: str) -> None:
        """Update message content (for streaming).

        Args:
            message_id: Message identifier
            content: New content to replace existing
        """
        if message_id in self.messages:
            message = self.messages[message_id]
            if isinstance(message, AssistantMessage):
                await message.update_content(content)

                # Auto-scroll if near bottom (within 5 lines)
                if self.scroll_offset.y >= self.max_scroll_y - 5:
                    self.scroll_end(animate=False)

    async def append_message_content(self, message_id: str, content: str) -> None:
        """Append content to existing message (for streaming).

        Args:
            message_id: Message identifier
            content: Content to append
        """
        if message_id in self.messages:
            message = self.messages[message_id]
            if isinstance(message, AssistantMessage):
                await message.append_content(content)

                # Auto-scroll if near bottom
                if self.scroll_offset.y >= self.max_scroll_y - 5:
                    self.scroll_end(animate=False)

    async def add_tool_display(
        self,
        message_id: str,
        tool_name: str,
        params: dict,
        result: dict = None
    ) -> None:
        """Add tool execution display to message.

        Args:
            message_id: Message identifier
            tool_name: Name of the tool
            params: Tool parameters
            result: Tool result (optional)
        """
        if message_id in self.messages:
            message = self.messages[message_id]
            if isinstance(message, AssistantMessage):
                await message.add_tool_display(tool_name, params, result)
                self.scroll_end(animate=True)

    async def add_error(self, message_id: str, error: str) -> None:
        """Add error display to message.

        Args:
            message_id: Message identifier
            error: Error message
        """
        if message_id in self.messages:
            message = self.messages[message_id]
            if isinstance(message, AssistantMessage):
                await message.add_error(error)
                self.scroll_end(animate=True)

    async def clear(self) -> None:
        """Clear all messages and show welcome screen."""
        # Remove all messages
        for message_id in list(self.message_order):
            if message_id in self.messages:
                message = self.messages[message_id]
                if message.is_mounted:
                    await message.remove()

        self.messages.clear()
        self.message_order.clear()

        # Show welcome screen again
        if not self._welcome_screen or not self._welcome_screen.is_mounted:
            self._welcome_screen = WelcomeScreen()
            await self.mount(self._welcome_screen)

    async def get_all_messages(self) -> list:
        """Get all messages for session export.

        Returns:
            list: List of message dictionaries
        """
        messages = []

        for message_id in self.message_order:
            if message_id in self.messages:
                message = self.messages[message_id]
                messages.append(message.to_dict())

        return messages

    def get_message_count(self) -> int:
        """Get total number of messages.

        Returns:
            int: Number of messages
        """
        return len(self.message_order)
