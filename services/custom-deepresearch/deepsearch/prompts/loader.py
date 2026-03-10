"""
Prompt Manager

Loads and manages prompts from external YAML files.
All prompts are configurable - no hardcoded prompts in the codebase.
"""

from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from deepsearch.observability import get_logger

logger = get_logger(__name__)


class PromptNotFoundError(Exception):
    """Raised when a prompt is not found."""


class PromptManager:
    """
    Manages loading and rendering prompts from YAML files.

    Prompts are organized by category (filename) and name (key in file).

    Directory structure:
        prompts/
        ├── supervisor.yaml
        ├── query_reformulator.yaml
        ├── assumption_checker.yaml
        └── ...

    File format:
        # prompts/query_reformulator.yaml
        reformulate_query: |
          Extract the most important search terms from this query.
          Return only the key terms separated by spaces.
          Limit to {max_terms} terms maximum.

          Query: {query}

          Search terms:

        another_prompt: |
          ...

    Usage:
        manager = PromptManager(Path("prompts"))
        prompt = manager.get_prompt(
            "query_reformulator",
            "reformulate_query",
            query="How do I submit a job?",
            max_terms=10,
        )
    """

    def __init__(self, prompts_dir: Path):
        """
        Initialize the prompt manager.

        Args:
            prompts_dir: Path to the directory containing prompt YAML files.
        """
        self.prompts_dir = Path(prompts_dir)
        self._cache: Dict[str, Any] = {}

        if not self.prompts_dir.exists():
            logger.warning(
                "prompts_dir_not_found",
                path=str(self.prompts_dir),
                message="Prompts directory does not exist",
            )

    def get_prompt(
        self,
        category: str,
        name: str,
        **variables,
    ) -> str:
        """
        Get a rendered prompt template.

        Args:
            category: The prompt category (YAML filename without extension).
            name: The prompt name (key in the YAML file).
            **variables: Variables to substitute in the template.

        Returns:
            The rendered prompt string.

        Raises:
            PromptNotFoundError: If the prompt is not found.
            ValueError: If a required variable is missing.
        """
        template = self._get_template(category, name)
        try:
            return template.format(**variables)
        except KeyError as e:
            logger.error(
                "prompt_variable_missing",
                category=category,
                name=name,
                missing_variable=str(e),
            )
            raise ValueError(
                f"Missing variable in prompt {category}/{name}: {e}"
            )

    def get_prompt_metadata(
        self,
        category: str,
        name: str,
    ) -> Dict[str, Any]:
        """
        Get metadata for a prompt entry.

        Args:
            category: The prompt category.
            name: The prompt name.

        Returns:
            Dictionary with prompt metadata. If the entry is a plain string,
            returns ``{"template": entry}``.
        """
        prompts = self._load_category(category)

        if name not in prompts:
            raise PromptNotFoundError(f"Prompt not found: {category}/{name}")

        entry = prompts[name]

        if isinstance(entry, dict):
            return entry

        return {"template": entry}

    def _get_template(self, category: str, name: str) -> str:
        """Load and return the raw template string for a prompt."""
        prompts = self._load_category(category)

        if name not in prompts:
            raise PromptNotFoundError(f"Prompt not found: {category}/{name}")

        entry = prompts[name]

        if isinstance(entry, dict):
            template = entry.get("template")
            if not template:
                raise PromptNotFoundError(
                    f"Prompt {category}/{name} is a dict but has no 'template' key"
                )
            return template

        return str(entry)

    def _load_category(self, category: str) -> Dict[str, Any]:
        """Load prompts from a YAML file, using cache when available."""
        if category in self._cache:
            return self._cache[category]

        file_path = self.prompts_dir / f"{category}.yaml"

        if not file_path.exists():
            logger.error("prompt_file_not_found", path=str(file_path))
            raise PromptNotFoundError(f"Prompt file not found: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                prompts = yaml.safe_load(f) or {}

            self._cache[category] = prompts
            logger.debug(
                "prompts_loaded",
                category=category,
                prompt_count=len(prompts),
            )

            return prompts
        except yaml.YAMLError as e:
            logger.error(
                "prompt_yaml_error",
                path=str(file_path),
                error=str(e),
            )
            raise PromptNotFoundError(f"Invalid YAML in {file_path}: {e}")

    def reload(self, category: Optional[str] = None) -> None:
        """
        Reload prompts from disk.

        Args:
            category: If provided, only reload this category.
                      If None, reload all categories.
        """
        if category:
            self._cache.pop(category, None)
            logger.info("prompts_reloaded", category=category)
        else:
            self._cache.clear()
            logger.info("all_prompts_reloaded")

    def list_categories(self) -> list:
        """List all available prompt categories."""
        if not self.prompts_dir.exists():
            return []
        return [f.stem for f in self.prompts_dir.glob("*.yaml")]

    def list_prompts(self, category: str) -> list:
        """List all prompt names in a category."""
        try:
            prompts = self._load_category(category)
            return list(prompts.keys())
        except PromptNotFoundError:
            return []
