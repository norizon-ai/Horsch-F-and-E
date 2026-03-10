"""
API Request/Response Models

Pydantic models for the REST API.
"""

from datetime import datetime
from typing import List, Optional, Any, Dict, Literal
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field, field_validator


class JobStatus(str, Enum):
    """search job status."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


# =============================================================================
# REQUEST MODELS
# =============================================================================


class ConversationMessage(BaseModel):
    """A message in the conversation history for context."""

    role: Literal["user", "assistant"] = Field(
        ..., description="Role of the message sender"
    )
    content: str = Field(
        ..., max_length=5000, description="Message content (truncated for context)"
    )
    sources: Optional[List[str]] = Field(
        default=None, description="List of source titles for assistant messages"
    )


class searchRequest(BaseModel):
    """Request to start a search job."""

    query: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="search question (max 10KB)",
    )
    conversation_history: Optional[List[ConversationMessage]] = Field(
        default=None,
        description="Previous messages for conversation context (optimized, not full traces)",
    )
    max_iterations: Optional[int] = Field(
        default=None, ge=1, le=10, description="Override max iterations"
    )
    execution_strategy: Optional[str] = Field(
        default=None, description="Override execution strategy (iterative/parallel)"
    )

    @field_validator("query")
    @classmethod
    def validate_query_not_whitespace(cls, v: str) -> str:
        """Reject queries that are only whitespace."""
        stripped = v.strip()
        if not stripped:
            raise ValueError("Query cannot be empty or whitespace-only")
        return stripped  # Return stripped version

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "query": "How do I submit a SLURM job with GPU resources?",
                "conversation_history": [
                    {"role": "user", "content": "What is SLURM?"},
                    {"role": "assistant", "content": "SLURM is a workload manager...", "sources": ["SLURM Docs"]},
                ],
                "max_iterations": 3,
            }
        }
    )


# =============================================================================
# RESPONSE MODELS
# =============================================================================


class SourceReference(BaseModel):
    """Reference to a source document."""

    id: str
    title: str
    url: Optional[str] = None
    score: float
    source_type: Optional[str] = Field(default=None, description="Source type (e.g., 'docs', 'confluence', 'web')")
    snippet: Optional[str] = Field(default=None, description="Text snippet or highlight from the source")


class FindingSummary(BaseModel):
    """Summary of a research finding for API response."""

    source_type: str = Field(..., description="Type: tool, agent, or llm")
    source_name: str = Field(..., description="Name of the source")
    confidence: float = Field(..., description="Confidence score (0.0-1.0)")
    sources_count: int = Field(..., description="Number of sources used")
    success: bool = Field(default=True, description="Whether the finding succeeded")

    @classmethod
    def from_research_finding(cls, finding: "ResearchFinding") -> "FindingSummary":
        """Create from ResearchFinding model."""
        from deepsearch.models import ResearchFinding

        return cls(
            source_type=finding.source_type.value,
            source_name=finding.source_name,
            confidence=finding.confidence,
            sources_count=finding.sources_count,
            success=finding.success,
        )


class IterationSummary(BaseModel):
    """Summary of a search iteration."""

    iteration_number: int
    tools_called: List[str]
    findings_count: int = Field(..., description="Number of research findings")
    findings: List[FindingSummary] = Field(
        default_factory=list, description="Summary of each finding"
    )
    decision: Optional[str] = None

    # Deprecated: kept for backwards compatibility
    answer_count: Optional[int] = Field(
        default=None, description="[DEPRECATED] Use findings_count instead"
    )


class searchJobResponse(BaseModel):
    """Response when starting a search job."""

    job_id: str
    status: JobStatus
    created_at: datetime

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "job_id": "abc123",
                "status": "pending",
                "created_at": "2024-01-01T00:00:00Z",
            }
        }
    )


class searchStatusResponse(BaseModel):
    """Response for job status check."""

    job_id: str
    status: JobStatus
    progress: Optional[str] = None
    current_iteration: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime] = None


class searchResultResponse(BaseModel):
    """Response with search results."""

    job_id: str
    status: JobStatus
    query: str
    final_report: str
    concise_answer: str
    confidence_score: float
    total_iterations: int
    processing_time_ms: float
    sources: List[SourceReference]
    iterations: List[IterationSummary]
    created_at: datetime
    completed_at: Optional[datetime] = None

    @classmethod
    def from_dr_result(cls, result: "DRResult", job_id: str) -> "searchResultResponse":
        """Create from DRResult."""
        from deepsearch.models import DRResult

        # Extract source references from all findings (unified model)
        sources = []
        seen_ids = set()
        for iteration in result.iterations:
            # Use all_findings to include both new findings and legacy search_answers
            for finding in iteration.all_findings:
                for source in finding.sources:
                    # Handle both SearchResult objects and dict sources
                    if isinstance(source, dict):
                        source_id = source.get("id")
                        source_title = source.get("title", "")
                        source_url = source.get("url")
                        source_score = source.get("score", 0.0)
                        source_type = source.get("source_type")
                        # Use highlight if available, otherwise use content snippet
                        source_snippet = source.get("highlight") or source.get("content", "")[:200] if source.get("content") else None
                    else:
                        source_id = getattr(source, "id", None)
                        source_title = getattr(source, "title", "")
                        source_url = getattr(source, "url", None)
                        source_score = getattr(source, "score", 0.0)
                        source_type = getattr(source, "source_type", None)
                        # Use highlight if available, otherwise use content snippet
                        highlight = getattr(source, "highlight", None)
                        content = getattr(source, "content", None)
                        source_snippet = highlight or (content[:200] if content else None)

                    if source_id and source_id not in seen_ids:
                        sources.append(
                            SourceReference(
                                id=source_id,
                                title=source_title,
                                url=source_url,
                                score=source_score,
                                source_type=source_type,
                                snippet=source_snippet,
                            )
                        )
                        seen_ids.add(source_id)

        # Create iteration summaries with findings
        iterations = []
        for it in result.iterations:
            all_findings = it.all_findings
            iterations.append(
                IterationSummary(
                    iteration_number=it.iteration_number,
                    tools_called=[tc.tool_name for tc in it.tool_calls],
                    findings_count=len(all_findings),
                    findings=[
                        FindingSummary.from_research_finding(f) for f in all_findings
                    ],
                    decision=it.supervisor_decision,
                    # Backwards compatibility
                    answer_count=len(all_findings),
                )
            )

        return cls(
            job_id=job_id,
            status=JobStatus.COMPLETED,
            query=result.user_query,
            final_report=result.final_report,
            concise_answer=result.concise_answer,
            confidence_score=result.confidence_score,
            total_iterations=result.total_iterations,
            processing_time_ms=result.processing_time_ms,
            sources=sources,
            iterations=iterations,
            created_at=result.created_at,
            completed_at=result.completed_at,
        )


class ToolInfo(BaseModel):
    """Information about a registered tool."""

    name: str
    description: str
    parameters: List[Dict[str, Any]]


class ToolsListResponse(BaseModel):
    """Response listing available tools."""

    tools: List[ToolInfo]
    count: int


class HealthResponse(BaseModel):
    """Health check response."""

    status: str
    version: str = "1.0.0"
    components: Dict[str, bool]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "healthy",
                "version": "1.0.0",
                "components": {
                    "llm": True,
                    "tools": True,
                },
            }
        }
    )


class ErrorResponse(BaseModel):
    """Error response."""

    error: str
    detail: Optional[str] = None
    code: Optional[str] = None
