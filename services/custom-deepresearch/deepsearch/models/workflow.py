"""
Workflow data models.

Models for the Norizon search workflow orchestration.
These are used by the supervisor to track iterations and produce final results.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Any, Union
from datetime import datetime
import warnings

from .research import searchAnswer
from .quality import QualityAssessment
from .finding import ResearchFinding


class ToolCallRecord(BaseModel):
    """
    Record of a tool call made by the supervisor.
    """

    tool_name: str = Field(..., description="Name of the tool called")
    arguments: dict[str, Any] = Field(
        default_factory=dict, description="Arguments passed to tool"
    )
    result: Any = Field(default=None, description="Result returned by tool")
    success: bool = Field(default=True, description="Whether call succeeded")
    error: Optional[str] = Field(default=None, description="Error message if failed")
    duration_ms: float = Field(
        default=0.0, description="Execution time in milliseconds"
    )
    timestamp: datetime = Field(
        default_factory=datetime.utcnow, description="When call was made"
    )


class DRIteration(BaseModel):
    """
    A single iteration of the Norizon search process.

    Each iteration may involve multiple tool calls and produces research findings.

    Note: The `findings` field is the new unified format. The `search_answers`
    field is deprecated but maintained for backwards compatibility.
    """

    iteration_number: int = Field(..., ge=1, description="Iteration number (1-indexed)")
    tool_calls: List[ToolCallRecord] = Field(
        default_factory=list, description="Tools called in this iteration"
    )
    findings: List[ResearchFinding] = Field(
        default_factory=list,
        description="Research findings from tools, agents, or LLM",
    )
    search_answers: List[searchAnswer] = Field(
        default_factory=list,
        description="[DEPRECATED] Use 'findings' instead. Legacy search answers.",
    )
    quality_assessment: Optional[QualityAssessment] = Field(
        default=None, description="Quality assessment of this iteration's results"
    )
    supervisor_decision: Optional[str] = Field(
        default=None, description="Supervisor's decision (CONTINUE/COMPLETE)"
    )
    supervisor_reasoning: Optional[str] = Field(
        default=None, description="Supervisor's reasoning for decision"
    )

    @property
    def all_findings(self) -> List[ResearchFinding]:
        """
        Get all findings, including converted legacy search_answers.

        Returns:
            Combined list of findings and converted search_answers
        """
        result = list(self.findings)

        for answer in self.search_answers:
            result.append(ResearchFinding.from_search_answer(answer))

        return result

    @property
    def best_finding(self) -> Optional[ResearchFinding]:
        """Get the finding with highest confidence."""
        all_f = self.all_findings
        if not all_f:
            return None
        return max(all_f, key=lambda f: f.confidence)


class DRResult(BaseModel):
    """
    Final result of a Norizon search workflow.

    This is the complete output containing all iterations and the final answer.
    """

    user_query: str = Field(..., description="Original user query")
    iterations: List[DRIteration] = Field(
        default_factory=list, description="All search iterations"
    )
    final_report: str = Field(default="", description="Comprehensive final report")
    concise_answer: str = Field(
        default="", description="Brief answer (max 4 sentences)"
    )
    confidence_score: float = Field(
        default=0.0, ge=0.0, le=1.0, description="Overall confidence score"
    )
    total_iterations: int = Field(
        default=0, ge=0, description="Total iterations executed"
    )
    processing_time_ms: float = Field(
        default=0.0, description="Total processing time in ms"
    )
    job_id: Optional[str] = Field(default=None, description="Unique job identifier")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = Field(default=None)

    @property
    def sources_count(self) -> int:
        """Count total unique sources used."""
        source_ids = set()
        for iteration in self.iterations:
            for finding in iteration.all_findings:
                for source in finding.sources:
                    if not hasattr(source, "id"):
                        continue
                    source_ids.add(source.id)
        return len(source_ids)

    @property
    def all_findings(self) -> List[ResearchFinding]:
        """Get all findings from all iterations."""
        result = []
        for iteration in self.iterations:
            result.extend(iteration.all_findings)
        return result
