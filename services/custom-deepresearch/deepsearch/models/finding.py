"""
Unified Research Finding Model

A single model for all research outputs - from tools, agents, or direct LLM responses.
This replaces the need to convert between AgentResult and searchAnswer.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from .search import SearchResult
    from .agent import AgentResult, AgentIteration
    from .research import searchAnswer
    from .tools import ToolResult


class FindingSource(str, Enum):
    """The source type that produced this finding."""

    TOOL = "tool"  # Direct tool execution (legacy retrievers)
    AGENT = "agent"  # Agent with reasoning loop
    LLM = "llm"  # Direct LLM response (no retrieval)


class ResearchFinding(BaseModel):
    """
    Unified result from any research source (tool, agent, or LLM).

    This model consolidates the output from different research paradigms:
    - Tools: Deterministic retrievers that fetch and return
    - Agents: Autonomous reasoners with multi-step workflows
    - LLM: Direct responses without retrieval

    It preserves all information from the source while providing
    a consistent interface for the supervisor and downstream consumers.
    """

    # === Core Fields (always present) ===
    source_type: FindingSource = Field(
        ..., description="Type of source that produced this finding"
    )
    source_name: str = Field(
        ..., description="Name of the source (tool name, agent name, or 'llm')"
    )
    answer: str = Field(default="", description="The research finding/answer text")
    confidence: float = Field(
        default=0.0, ge=0.0, le=1.0, description="Confidence score (0.0-1.0)"
    )
    sources: List[Any] = Field(
        default_factory=list,
        description="Source documents used (SearchResult objects)",
    )

    # === Agent-Specific Fields (optional) ===
    task: Optional[str] = Field(
        default=None, description="The delegated task (for agents)"
    )
    reasoning_trace: Optional[List[Any]] = Field(
        default=None,
        description="Agent's reasoning iterations (AgentIteration objects)",
    )

    # === Metadata ===
    success: bool = Field(default=True, description="Whether the research succeeded")
    error: Optional[str] = Field(
        default=None, description="Error message if success=False"
    )
    processing_time_ms: float = Field(
        default=0.0, description="Time taken to produce this finding"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="When this finding was produced"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional source-specific metadata"
    )

    # === Factory Methods ===

    @classmethod
    def from_agent_result(cls, result: "AgentResult") -> "ResearchFinding":
        """
        Convert an AgentResult to a ResearchFinding.

        Preserves the full reasoning trace and all agent-specific information.

        Args:
            result: The AgentResult from a specialized agent

        Returns:
            ResearchFinding with source_type=AGENT
        """
        return cls(
            source_type=FindingSource.AGENT,
            source_name=result.agent_name,
            answer=result.answer,
            confidence=result.confidence,
            sources=result.sources,
            task=result.task,
            reasoning_trace=result.iterations if result.iterations else None,
            success=result.success,
            error=result.error,
            processing_time_ms=result.processing_time_ms,
            metadata=result.metadata if hasattr(result, "metadata") else {},
        )

    @classmethod
    def from_tool_result(
        cls,
        result: "ToolResult",
        tool_name: str,
        processing_time_ms: float = 0.0,
    ) -> "ResearchFinding":
        """
        Convert a ToolResult to a ResearchFinding.

        Handles both ToolResult with searchAnswer data and raw data.

        Args:
            result: The ToolResult from a tool execution
            tool_name: Name of the tool that produced the result
            processing_time_ms: Execution time

        Returns:
            ResearchFinding with source_type=TOOL
        """
        from .research import searchAnswer

        if not result.success:
            return cls(
                source_type=FindingSource.TOOL,
                source_name=tool_name,
                answer="",
                confidence=0.0,
                success=False,
                error=result.error,
                processing_time_ms=processing_time_ms,
            )

        # Handle searchAnswer data (legacy tool output)
        if isinstance(result.data, searchAnswer):
            return cls(
                source_type=FindingSource.TOOL,
                source_name=tool_name,
                answer=result.data.answer,
                confidence=result.data.confidence,
                sources=list(result.data.sources),
                success=True,
                processing_time_ms=processing_time_ms,
                metadata={
                    "search_type": result.data.search_type.value if result.data.search_type else None,
                    "reasoning": result.data.reasoning,
                },
            )

        # Handle raw data
        return cls(
            source_type=FindingSource.TOOL,
            source_name=tool_name,
            answer=str(result.data) if result.data else "",
            confidence=0.5,  # Default confidence for raw data
            success=True,
            processing_time_ms=processing_time_ms,
        )

    @classmethod
    def from_search_answer(
        cls,
        answer: "searchAnswer",
        source_name: Optional[str] = None,
    ) -> "ResearchFinding":
        """
        Convert a legacy searchAnswer to a ResearchFinding.

        For backwards compatibility with existing retrievers.

        Args:
            answer: The searchAnswer from a retriever
            source_name: Override source name (defaults to retriever_name)

        Returns:
            ResearchFinding with source_type=TOOL
        """
        return cls(
            source_type=FindingSource.TOOL,
            source_name=source_name or answer.retriever_name or answer.search_type.value,
            answer=answer.answer,
            confidence=answer.confidence,
            sources=list(answer.sources),
            success=True,
            metadata={
                "search_type": answer.search_type.value,
                "reasoning": answer.reasoning,
            },
        )

    @classmethod
    def from_llm_response(
        cls,
        content: str,
        confidence: float = 0.5,
        model_name: str = "llm",
    ) -> "ResearchFinding":
        """
        Create a ResearchFinding from a direct LLM response.

        For cases where the LLM answers without using tools/agents.

        Args:
            content: The LLM's response content
            confidence: Confidence score (default 0.5 for direct responses)
            model_name: Name of the model

        Returns:
            ResearchFinding with source_type=LLM
        """
        return cls(
            source_type=FindingSource.LLM,
            source_name=model_name,
            answer=content,
            confidence=confidence,
            sources=[],
            success=True,
        )

    @classmethod
    def failure(
        cls,
        source_type: FindingSource,
        source_name: str,
        error: str,
        task: Optional[str] = None,
    ) -> "ResearchFinding":
        """
        Create a failed ResearchFinding.

        Args:
            source_type: Type of source that failed
            source_name: Name of the failed source
            error: Error message
            task: Optional task description

        Returns:
            ResearchFinding with success=False
        """
        return cls(
            source_type=source_type,
            source_name=source_name,
            answer="",
            confidence=0.0,
            success=False,
            error=error,
            task=task,
        )

    # === Utility Methods ===

    @property
    def is_from_agent(self) -> bool:
        """Check if this finding came from an agent."""
        return self.source_type == FindingSource.AGENT

    @property
    def is_from_tool(self) -> bool:
        """Check if this finding came from a tool."""
        return self.source_type == FindingSource.TOOL

    @property
    def is_from_llm(self) -> bool:
        """Check if this finding came from direct LLM response."""
        return self.source_type == FindingSource.LLM

    @property
    def has_reasoning_trace(self) -> bool:
        """Check if this finding includes a reasoning trace."""
        return self.reasoning_trace is not None and len(self.reasoning_trace) > 0

    @property
    def sources_count(self) -> int:
        """Count the number of sources."""
        return len(self.sources)

    def to_dict_summary(self) -> Dict[str, Any]:
        """
        Create a summary dict for logging/display.

        Returns:
            Dict with key information about this finding
        """
        return {
            "source_type": self.source_type.value,
            "source_name": self.source_name,
            "confidence": self.confidence,
            "sources_count": self.sources_count,
            "success": self.success,
            "has_reasoning": self.has_reasoning_trace,
            "answer_length": len(self.answer),
        }
