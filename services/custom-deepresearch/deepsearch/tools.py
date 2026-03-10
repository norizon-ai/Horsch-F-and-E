"""
Tools Module (Legacy Compatibility)

This module provides backward compatibility for legacy tool-based architecture.
The system has migrated to an agent-based architecture, but some imports still reference tools.
"""

from typing import List, Any, Optional
from pydantic import BaseModel


class ToolParameter(BaseModel):
    """Tool parameter definition."""
    name: str
    description: str
    required: bool = True
    type: str = "string"


class BaseTool:
    """
    Base class for tools (legacy compatibility).
    
    In the new architecture, use BaseAgent instead.
    """
    def __init__(self, name: str, description: str, parameters: List[ToolParameter] = None):
        self.name = name
        self.description = description
        self.parameters = parameters or []
    
    async def execute(self, **kwargs) -> Any:
        """Execute the tool."""
        raise NotImplementedError()


class ToolRegistry:
    """
    Registry for tools (legacy compatibility).
    
    In the new architecture, use AgentRegistry instead.
    """
    _tools: List[BaseTool] = []
    
    @classmethod
    def register(cls, tool: BaseTool) -> None:
        """Register a tool."""
        cls._tools.append(tool)
    
    @classmethod
    def get(cls, name: str) -> Optional[BaseTool]:
        """Get a tool by name."""
        for tool in cls._tools:
            if tool.name == name:
                return tool
        return None
    
    @classmethod
    def all_tools(cls) -> List[BaseTool]:
        """Get all registered tools."""
        return cls._tools.copy()
    
    @classmethod
    def count(cls) -> int:
        """Get count of registered tools."""
        return len(cls._tools)
    
    @classmethod
    def clear(cls) -> None:
        """Clear all tools."""
        cls._tools.clear()


__all__ = ["BaseTool", "ToolRegistry", "ToolParameter"]
