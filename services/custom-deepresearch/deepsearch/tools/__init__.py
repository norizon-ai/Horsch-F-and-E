"""
Tools Module

Provides the base tool interface and registry for all tools.

Usage:
    from deepsearch.tools import BaseTool, ToolRegistry, register_tool

    # Create a tool
    class MyTool(BaseTool):
        @property
        def name(self) -> str:
            return "my_tool"

        @property
        def description(self) -> str:
            return "Does something useful"

        async def execute(self, query: str, **kwargs) -> ToolResult:
            return ToolResult.ok(data="result")

    # Register it
    ToolRegistry.register(MyTool())

    # Or use decorator for auto-registration
    @register_tool
    class AutoRegisteredTool(BaseTool):
        ...
"""

from .base import BaseTool, ToolParameter
from .registry import ToolRegistry, register_tool

__all__ = [
    "BaseTool",
    "ToolParameter",
    "ToolRegistry",
    "register_tool",
]
