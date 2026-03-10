"""
Tool Registry

Central registry for all tools that the supervisor can call.
Supports auto-registration and provides function schemas for LLM function calling.
"""

from typing import Dict, List, Optional, Type
from functools import wraps

from deepsearch.observability import get_logger
from .base import BaseTool

logger = get_logger(__name__)


class ToolRegistry:
    """
    Registry for all available tools.

    The supervisor queries this registry to discover available tools
    and get their function schemas for LLM function calling.

    Usage:
        # Register a tool instance
        ToolRegistry.register(MyTool())

        # Get all registered tools
        tools = ToolRegistry.all_tools()

        # Get function schemas for LLM
        schemas = ToolRegistry.to_function_schemas()
    """

    _tools: Dict[str, BaseTool] = {}

    @classmethod
    def register(cls, tool: BaseTool) -> BaseTool:
        """
        Register a tool instance.

        Args:
            tool: Tool instance to register

        Returns:
            The registered tool (for chaining)
        """
        if tool.name in cls._tools:
            logger.warning(
                "tool_already_registered",
                tool_name=tool.name,
                existing_tool=cls._tools[tool.name].__class__.__name__,
                new_tool=tool.__class__.__name__,
            )

        cls._tools[tool.name] = tool
        logger.info(
            "tool_registered",
            tool_name=tool.name,
            tool_class=tool.__class__.__name__,
        )

        return tool

    @classmethod
    def unregister(cls, name: str) -> Optional[BaseTool]:
        """
        Unregister a tool by name.

        Args:
            name: Tool name to unregister

        Returns:
            The unregistered tool, or None if not found
        """
        tool = cls._tools.pop(name, None)
        if tool:
            logger.info("tool_unregistered", tool_name=name)
        return tool

    @classmethod
    def get(cls, name: str) -> Optional[BaseTool]:
        """
        Get a tool by name.

        Args:
            name: Tool name

        Returns:
            Tool instance or None
        """
        return cls._tools.get(name)

    @classmethod
    def all_tools(cls) -> List[BaseTool]:
        """Get all registered tools."""
        return list(cls._tools.values())

    @classmethod
    def tool_names(cls) -> List[str]:
        """Get names of all registered tools."""
        return list(cls._tools.keys())

    @classmethod
    def to_function_schemas(cls) -> List[dict]:
        """
        Get function calling schemas for all registered tools.

        Returns:
            List of function calling schema dicts
        """
        return [tool.to_function_schema() for tool in cls._tools.values()]

    @classmethod
    def clear(cls) -> None:
        """Clear all registered tools."""
        cls._tools.clear()
        logger.info("tool_registry_cleared")

    @classmethod
    def count(cls) -> int:
        """Get number of registered tools."""
        return len(cls._tools)


def register_tool(tool_class: Type[BaseTool]):
    """
    Decorator for auto-registering tool classes.

    When a tool class decorated with @register_tool is instantiated,
    it is automatically registered with the ToolRegistry.

    Usage:
        @register_tool
        class MyTool(BaseTool):
            ...
    """
    original_init = tool_class.__init__

    @wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        ToolRegistry.register(self)

    tool_class.__init__ = new_init
    return tool_class
