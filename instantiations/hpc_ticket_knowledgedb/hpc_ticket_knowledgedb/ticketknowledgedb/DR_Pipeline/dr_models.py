#!/usr/bin/env python3
"""
Data models and types for the HPC Deep Research (DR) system
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Any, Literal
from enum import Enum
from pydantic import BaseModel, Field


class ResearchType(Enum):
    """Types of research that can be performed"""
    ZERO_SHOT = "zero_shot"
    DOCS_ONLY = "docs_only"
    TICKETS_ONLY = "tickets_only"
    SOLUTION_FOCUSED = "solution_focused"


class QualityScore(Enum):
    """Quality assessment scores"""
    EXCELLENT = 5
    GOOD = 4
    ADEQUATE = 3
    POOR = 2
    INSUFFICIENT = 1


@dataclass
class SearchResult:
    """Individual search result from Elasticsearch"""
    id: str
    title: str
    content: str
    score: float
    source_type: str  # 'docs' or 'tickets'
    url: Optional[str] = None
    ticket_id: Optional[str] = None
    keywords: Optional[List[str]] = None
    highlight: Optional[str] = None


@dataclass
class ResearchAnswer:
    """Answer from a specific research type"""
    research_type: ResearchType
    answer: str
    confidence: float
    sources: List[SearchResult]
    reasoning: str
    token_count: int


@dataclass
class UserAssumption:
    """User assumption extracted from query"""
    assumption: str
    is_valid: bool
    evidence: str
    confidence: float


@dataclass
class QualityAssessment:
    """Quality assessment of a research answer"""
    score: QualityScore
    reasoning: str
    contributes_to_answer: bool
    addresses_user_question: bool
    factual_accuracy: float
    completeness: float


@dataclass
class DRIteration:
    """Single iteration of the DR process"""
    iteration_number: int
    research_answers: List[ResearchAnswer]
    user_assumptions: List[UserAssumption]
    quality_assessments: List[QualityAssessment]
    supervisor_decision: str


@dataclass
class DRResult:
    """Final result of the DR process"""
    user_query: str
    iterations: List[DRIteration]
    final_report: str
    concise_answer: str
    total_iterations: int
    processing_time: float
    confidence_score: float


class HPCSearchRequest(BaseModel):
    """Request for HPC knowledge search"""
    query: str = Field(description="Search query")
    search_type: Literal["docs", "tickets", "both"] = Field(description="Type of search to perform")
    max_results: int = Field(default=10, description="Maximum number of results")


class HPCSearchResponse(BaseModel):
    """Response from HPC knowledge search"""
    query: str = Field(description="Original search query")
    results: List[SearchResult] = Field(description="Search results")
    total_found: int = Field(description="Total results found")
    search_time: float = Field(description="Search execution time")
    error: Optional[str] = Field(description="Error message if search failed")
