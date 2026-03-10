"""
Quality assessment data models.

Models for evaluating search answer quality.
"""

from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from enum import IntEnum


class QualityScore(IntEnum):
    """Quality score levels (1-5)."""

    INSUFFICIENT = 1
    POOR = 2
    ADEQUATE = 3
    GOOD = 4
    EXCELLENT = 5


class QualityAssessment(BaseModel):
    """
    Quality assessment of a search answer.

    Evaluates an answer across multiple dimensions.
    """

    score: QualityScore = Field(..., description="Overall quality score (1-5)")
    reasoning: str = Field(..., description="Explanation of the assessment")
    contributes_to_answer: bool = Field(
        ..., description="Whether this answer contributes to the final response"
    )
    addresses_user_question: bool = Field(
        ..., description="Whether the answer addresses the user's question"
    )
    factual_accuracy: float = Field(
        ..., ge=0.0, le=1.0, description="Estimated factual accuracy (0.0-1.0)"
    )
    completeness: float = Field(
        ..., ge=0.0, le=1.0, description="Completeness of the answer (0.0-1.0)"
    )

    model_config = ConfigDict(frozen=True)

    @property
    def is_acceptable(self) -> bool:
        """Check if quality is at least adequate."""
        return self.score >= QualityScore.ADEQUATE
