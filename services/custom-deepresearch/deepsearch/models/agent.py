"""
Agent Data Models

Models for the multi-agent research system where specialized agents
have their own tools and reasoning loops.
"""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AgentStatus(str, Enum):
    """Agent execution status."""

    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentToolCall(BaseModel):
    """Record of a tool call made by an agent during its reasoning loop."""

    tool_name: str = Field(..., description="Name of the tool called")
    arguments: Dict[str, Any] = Field(
        default_factory=dict, description="Arguments passed to the tool"
    )
    result: Any = Field(default=None, description="Result returned by the tool")
    success: bool = Field(default=True, description="Whether the tool call succeeded")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    duration_ms: float = Field(default=0.0, description="Execution time in milliseconds")
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="When the call was made"
    )


class AgentIteration(BaseModel):
    """A single iteration of an agent's reasoning loop."""

    iteration_number: int = Field(..., ge=1, description="Iteration number (1-indexed)")
    thought: Optional[str] = Field(
        default=None, description="Agent's reasoning/thought process"
    )
    tool_calls: List[AgentToolCall] = Field(
        default_factory=list, description="Tool calls made in this iteration"
    )
    observation: Optional[str] = Field(
        default=None, description="Observation from tool results"
    )
    decision: Optional[str] = Field(
        default=None, description="Decision: CONTINUE or COMPLETE"
    )


class AgentResult(BaseModel):
    """
    Result returned by an agent to the supervisor.

    This is the structured output that agents return after completing
    their research task. It includes the answer, confidence, sources,
    and a trace of the reasoning process.
    """

    success: bool = Field(default=True, description="Whether the agent succeeded")
    agent_name: str = Field(..., description="Name of the agent that produced this result")
    task: str = Field(..., description="The delegated task that was researched")
    answer: str = Field(default="", description="The agent's answer/finding")
    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence score (0.0-1.0)",
    )
    sources: List[Any] = Field(
        default_factory=list, description="Sources used (SearchResult or other source types)"
    )
    iterations: List[AgentIteration] = Field(
        default_factory=list, description="Trace of reasoning iterations"
    )
    error: Optional[str] = Field(default=None, description="Error message if failed")
    processing_time_ms: float = Field(
        default=0.0, description="Total processing time in milliseconds"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict, description="Additional metadata"
    )

    @classmethod
    def ok(
        cls,
        agent_name: str,
        task: str,
        answer: str,
        confidence: float = 0.5,
        sources: Optional[List[Any]] = None,
        iterations: Optional[List[AgentIteration]] = None,
        processing_time_ms: float = 0.0,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> "AgentResult":
        """Create a successful agent result."""
        return cls(
            success=True,
            agent_name=agent_name,
            task=task,
            answer=answer,
            confidence=confidence,
            sources=sources or [],
            iterations=iterations or [],
            processing_time_ms=processing_time_ms,
            metadata=metadata or {},
        )

    @classmethod
    def fail(
        cls,
        agent_name: str,
        task: str,
        error: str,
        iterations: Optional[List[AgentIteration]] = None,
        processing_time_ms: float = 0.0,
    ) -> "AgentResult":
        """Create a failed agent result."""
        return cls(
            success=False,
            agent_name=agent_name,
            task=task,
            error=error,
            iterations=iterations or [],
            processing_time_ms=processing_time_ms,
        )
