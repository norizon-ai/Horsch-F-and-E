"""
Golden Answer Dataset for Nora Search (DeepSearch) QA Evaluation.

This module provides classes for loading and managing the golden answer
benchmark dataset based on TechMech Solutions GmbH Confluence content.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import yaml


@dataclass
class GoldenQuestion:
    """A single golden test question with expected answers and metadata."""

    id: str
    question: str
    expected_source_pages: list[str]
    category: str
    difficulty: str = "medium"
    space: Optional[str] = None
    spaces: Optional[list[str]] = None
    expected_answer_contains: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Normalize spaces field."""
        if self.spaces is None and self.space is not None:
            self.spaces = [self.space]
        elif self.spaces is None:
            self.spaces = []

    @property
    def is_cross_domain(self) -> bool:
        """Check if question spans multiple spaces."""
        return len(self.spaces) > 1 if self.spaces else False

    @property
    def expected_sources_count(self) -> int:
        """Number of expected source pages."""
        return len(self.expected_source_pages)


class GoldenDataset:
    """Load and manage golden answer benchmark data."""

    DEFAULT_PATH = Path(__file__).parent / "golden_answers.yaml"

    def __init__(self, yaml_path: Optional[str | Path] = None) -> None:
        """
        Initialize the dataset from a YAML file.

        Args:
            yaml_path: Path to the golden answers YAML file.
                      Defaults to golden_answers.yaml in the same directory.
        """
        self.yaml_path = Path(yaml_path) if yaml_path else self.DEFAULT_PATH
        self._questions: list[GoldenQuestion] = []
        self._metadata: dict = {}
        self._load_questions()

    def _load_questions(self) -> None:
        """Load questions from the YAML file."""
        if not self.yaml_path.exists():
            raise FileNotFoundError(f"Golden answers file not found: {self.yaml_path}")

        with open(self.yaml_path, encoding="utf-8") as f:
            data = yaml.safe_load(f)

        self._metadata = data.get("metadata", {})

        for q_data in data.get("questions", []):
            question = GoldenQuestion(
                id=q_data["id"],
                question=q_data["question"],
                expected_source_pages=q_data.get("expected_source_pages", []),
                category=q_data.get("category", "unknown"),
                difficulty=q_data.get("difficulty", "medium"),
                space=q_data.get("space"),
                spaces=q_data.get("spaces"),
                expected_answer_contains=q_data.get("expected_answer_contains", []),
            )
            self._questions.append(question)

    @property
    def questions(self) -> list[GoldenQuestion]:
        """Get all questions."""
        return self._questions

    @property
    def metadata(self) -> dict:
        """Get dataset metadata."""
        return self._metadata

    @property
    def total_questions(self) -> int:
        """Get total number of questions."""
        return len(self._questions)

    def get_by_id(self, question_id: str) -> Optional[GoldenQuestion]:
        """Get a question by its ID."""
        for q in self._questions:
            if q.id == question_id:
                return q
        return None

    def get_by_category(self, category: str) -> list[GoldenQuestion]:
        """Get all questions in a category."""
        return [q for q in self._questions if q.category == category]

    def get_by_space(self, space: str) -> list[GoldenQuestion]:
        """Get all questions for a specific space."""
        return [q for q in self._questions if space in (q.spaces or [])]

    def get_by_difficulty(self, difficulty: str) -> list[GoldenQuestion]:
        """Get all questions of a specific difficulty."""
        return [q for q in self._questions if q.difficulty == difficulty]

    def get_cross_domain_questions(self) -> list[GoldenQuestion]:
        """Get all questions that span multiple spaces."""
        return [q for q in self._questions if q.is_cross_domain]

    def get_single_source_questions(self) -> list[GoldenQuestion]:
        """Get questions expecting only one source."""
        return [q for q in self._questions if q.expected_sources_count == 1]

    def get_multi_source_questions(self, min_sources: int = 2) -> list[GoldenQuestion]:
        """Get questions expecting multiple sources."""
        return [q for q in self._questions if q.expected_sources_count >= min_sources]

    def sample(self, n: int, category: Optional[str] = None) -> list[GoldenQuestion]:
        """
        Get a random sample of questions.

        Args:
            n: Number of questions to sample.
            category: Optional category to filter by.

        Returns:
            List of sampled questions.
        """
        import random

        questions = self.get_by_category(category) if category else self._questions
        return random.sample(questions, min(n, len(questions)))

    def categories(self) -> list[str]:
        """Get list of unique categories."""
        return list(set(q.category for q in self._questions))

    def spaces(self) -> list[str]:
        """Get list of unique spaces."""
        all_spaces: set[str] = set()
        for q in self._questions:
            if q.spaces:
                all_spaces.update(q.spaces)
        return list(all_spaces)

    def difficulty_distribution(self) -> dict[str, int]:
        """Get distribution of questions by difficulty."""
        dist: dict[str, int] = {}
        for q in self._questions:
            dist[q.difficulty] = dist.get(q.difficulty, 0) + 1
        return dist

    def category_distribution(self) -> dict[str, int]:
        """Get distribution of questions by category."""
        dist: dict[str, int] = {}
        for q in self._questions:
            dist[q.category] = dist.get(q.category, 0) + 1
        return dist

    def space_distribution(self) -> dict[str, int]:
        """Get distribution of questions by space."""
        dist: dict[str, int] = {}
        for q in self._questions:
            for space in q.spaces or []:
                dist[space] = dist.get(space, 0) + 1
        return dist

    def __len__(self) -> int:
        """Get number of questions."""
        return len(self._questions)

    def __iter__(self):
        """Iterate over questions."""
        return iter(self._questions)

    def __getitem__(self, index: int) -> GoldenQuestion:
        """Get question by index."""
        return self._questions[index]

    def __repr__(self) -> str:
        """String representation."""
        return (
            f"GoldenDataset(total={self.total_questions}, "
            f"categories={len(self.categories())}, "
            f"spaces={len(self.spaces())})"
        )


def load_golden_dataset(yaml_path: Optional[str | Path] = None) -> GoldenDataset:
    """
    Convenience function to load the golden dataset.

    Args:
        yaml_path: Optional path to YAML file.

    Returns:
        Loaded GoldenDataset instance.
    """
    return GoldenDataset(yaml_path)
