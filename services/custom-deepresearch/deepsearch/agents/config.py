"""
Agent Configuration

Pydantic models for per-agent YAML configuration.
Supports multiple instances of the same agent type and env var substitution.
"""

import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml
from pydantic import BaseModel, Field

from deepsearch.observability import get_logger

logger = get_logger(__name__)


class PreprocessorConfig(BaseModel):
    """Configuration for a query preprocessor."""

    type: str = Field(
        ..., description="Preprocessor type: reformulator, assumption_checker"
    )
    enabled: bool = Field(default=True, description="Whether this preprocessor is enabled")
    config: Dict[str, Any] = Field(
        default_factory=dict, description="Preprocessor-specific configuration"
    )


class AgentInstanceConfig(BaseModel):
    """Configuration for a single agent instance."""

    type: str = Field(
        ..., description="Agent type: websearch, elasticsearch, custom"
    )
    enabled: bool = Field(default=True, description="Whether the agent is enabled")
    description: Optional[str] = Field(
        default=None, description="Human-readable description for supervisor"
    )
    display_name: Optional[str] = Field(
        default=None, description="Human-readable name shown in UI"
    )
    icon_url: Optional[str] = Field(
        default=None, description="URL to source icon (e.g., /icons/confluence.svg)"
    )
    source_type: Optional[str] = Field(
        default=None, description="Source type for UI mapping (e.g., 'confluence', 'sharepoint', 'jira')"
    )
    searching_label: Optional[str] = Field(
        default=None, description="Label shown while searching (e.g., 'Searching the web...')"
    )
    item_label: Optional[str] = Field(
        default=None, description="Label for counted items (e.g., 'websites', 'pages', 'documents')"
    )
    max_iterations: int = Field(
        default=5, ge=1, le=20, description="Max reasoning iterations"
    )
    backend: Dict[str, Any] = Field(
        default_factory=dict, description="Backend-specific configuration"
    )
    # Query preprocessors (abstracted, per-agent)
    preprocessors: List[PreprocessorConfig] = Field(
        default_factory=list,
        description="Query preprocessors to apply before search",
    )
    # For custom agents loaded via import
    class_path: Optional[str] = Field(
        default=None, alias="class", description="Python class path for custom agents"
    )

    model_config = {"populate_by_name": True}


class AgentsConfig(BaseModel):
    """Root configuration for all agents."""

    agents: Dict[str, AgentInstanceConfig] = Field(
        default_factory=dict, description="Map of agent name to config"
    )


def _substitute_env_vars(content: str) -> str:
    """
    Substitute ${VAR} placeholders with environment variable values.

    Args:
        content: YAML content as string

    Returns:
        Content with env vars substituted
    """

    def replace_var(match: re.Match) -> str:
        var_name = match.group(1)
        value = os.environ.get(var_name, "")
        if not value:
            logger.warning("env_var_not_set", var_name=var_name)
        return value

    return re.sub(r"\$\{(\w+)\}", replace_var, content)


def load_agents_config(path: Path) -> AgentsConfig:
    """
    Load and parse agents.yaml with env var substitution.

    Args:
        path: Path to agents.yaml file

    Returns:
        AgentsConfig with parsed agent configurations

    Notes:
        - Returns empty config if file doesn't exist (backwards compatible)
        - Substitutes ${VAR} with environment variable values
        - Logs warnings for missing env vars
    """
    if not path.exists():
        logger.info("agents_config_not_found", path=str(path))
        return AgentsConfig()

    try:
        content = path.read_text()
        content = _substitute_env_vars(content)
        data = yaml.safe_load(content) or {}

        config = AgentsConfig(**data)
        logger.info(
            "agents_config_loaded",
            path=str(path),
            agent_count=len(config.agents),
            agents=list(config.agents.keys()),
        )
        return config

    except yaml.YAMLError as e:
        logger.error("agents_config_yaml_error", path=str(path), error=str(e))
        return AgentsConfig()
    except Exception as e:
        logger.error("agents_config_load_error", path=str(path), error=str(e))
        return AgentsConfig()
