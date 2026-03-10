"""
Base Tool Interface

Abstract base class for all tools that can be registered and called by the supervisor.
This is the foundation of the tool-based architecture.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field

from deepsearch.models import ToolResult
from deepsearch.observability import get_logger

logger = get_logger(__name__)


class ToolParameter(BaseModel):
    """Schema for a tool parameter."""

    name: str = Field(..., description="Parameter name")
    type: str = Field(
        default="string", description="Parameter type (string, integer, boolean, etc.)"
    )
    description: str = Field(default="", description="Parameter description")
    required: bool = Field(default=False, description="Whether parameter is required")
    default: Any = Field(default=None, description="Default value if not provided")


class BaseTool(ABC):
    """
    Abstract base class for all tools.

    Tools are the units of work that the supervisor can call.
    Each tool has a name, description, and execute method.

    Example:
        class MyTool(BaseTool):
            @property
            def name(self) -> str:
                return "my_tool"

            @property
            def description(self) -> str:
                return "Does something useful"

            async def execute(self, query: str, **kwargs) -> ToolResult:
                # Do work
                return ToolResult.ok(data=result, tool_name=self.name)
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique tool name for identification.

        Used in function calling schemas and logging.
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Tool description shown to the LLM.

        Should clearly explain what the tool does.
        """
        pass

    @property
    def parameters(self) -> List[ToolParameter]:
        """
        Tool parameters for function calling schema.

        Default returns a single required 'query' parameter.
        Override for custom parameters.
        """
        return [
            ToolParameter(
                name="query",
                type="string",
                description="The search query or question",
                required=True,
            )
        ]

    @abstractmethod
    async def execute(self, query: str, **kwargs) -> ToolResult:
        """
        Execute the tool.

        Args:
            query: The search query or input
            **kwargs: Additional parameters

        Returns:
            ToolResult with execution output
        """
        pass

    def to_function_schema(self) -> Dict[str, Any]:
        """
        Convert tool to OpenAI function calling schema.

        Returns:
            Dict with function calling schema
        """
        properties = {}
        required = []

        for param in self.parameters:
            properties[param.name] = {
                "type": param.type,
                "description": param.description,
            }
            if param.required:
                required.append(param.name)

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            },
        }

    async def __call__(self, query: str, **kwargs) -> ToolResult:
        """Allow tools to be called directly."""
        return await self.execute(query=query, **kwargs)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name})>"
