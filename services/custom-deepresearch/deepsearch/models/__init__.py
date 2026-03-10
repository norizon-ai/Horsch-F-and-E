"""
Shared Data Models

This module exports all shared data models used across the Norizon search system.
Models that are specific to a processor (like AssumptionChecker) live with that processor.

Usage:
    from deepsearch.models import SearchResult, searchAnswer, DRResult
"""

# Search models
from .search import SearchResult, SearchQuery, SearchResponse

# Research models
from .research import searchType, searchAnswer

# Quality models
from .quality import QualityScore, QualityAssessment

# Workflow models
from .workflow import ToolCallRecord, DRIteration, DRResult

# Tool models
from .tools import ToolResult

# Agent models
from .agent import AgentStatus, AgentToolCall, AgentIteration, AgentResult

# Finding models
from .finding import FindingSource, ResearchFinding

__all__ = [
    "SearchResult",
    "SearchQuery",
    "SearchResponse",
    "searchType",
    "searchAnswer",
    "QualityScore",
    "QualityAssessment",
    "ToolCallRecord",
    "DRIteration",
    "DRResult",
    "ToolResult",
    "AgentStatus",
    "AgentToolCall",
    "AgentIteration",
    "AgentResult",
    "FindingSource",
    "ResearchFinding",
]
