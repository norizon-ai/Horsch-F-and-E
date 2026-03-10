"""
Tool-related data models.

Models for tool execution results - used by BaseTool and all tools.
"""

from pydantic import BaseModel, Field
from typing import Any, Optional


class ToolResult(BaseModel):
    """
    Standardized tool execution result.

    All tools return this format for consistency.
    """

    success: bool = Field(..., description="Whether execution succeeded")
    data: Any = Field(default=None, description="Result data (type depends on tool)")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    tool_name: Optional[str] = Field(default=None, description="Name of tool that produced result")

    @classmethod
    def ok(cls, data: Any, tool_name: str = None) -> "ToolResult":
        """Create a successful result."""
        return cls(success=True, data=data, tool_name=tool_name)

    @classmethod
    def fail(cls, error: str, tool_name: str = None) -> "ToolResult":
        """Create a failed result."""
        return cls(success=False, error=error, tool_name=tool_name)
