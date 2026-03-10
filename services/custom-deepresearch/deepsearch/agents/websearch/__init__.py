"""
WebSearch Agent Module

Specialized agent for web search research using SearXNG.
"""

from typing import TYPE_CHECKING

from .agent import WebSearchAgent
from .tools import ExtractContentTool, FetchUrlTool, SearXNGSearchTool

if TYPE_CHECKING:
    from deepsearch.agents.base import BaseAgent
    from deepsearch.agents.config import AgentInstanceConfig
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

__all__ = [
    "WebSearchAgent",
    "SearXNGSearchTool",
    "FetchUrlTool",
    "ExtractContentTool",
]


def _register_websearch_factory() -> None:
    """Register the websearch agent factory creator."""
    from deepsearch.agents.factory import AgentFactory

    @AgentFactory.register("websearch")
    async def create_websearch_agent(
        name: str,
        config: "AgentInstanceConfig",
        llm: "LLMProvider",
        prompts: "PromptManager",
    ) -> "BaseAgent":
        """Create WebSearchAgent from YAML config."""
        backend = config.backend

        searxng_url = backend.get("searxng_url")
        if not searxng_url:
            raise ValueError(f"Agent '{name}': backend.searxng_url is required")

        agent = WebSearchAgent(
            llm=llm,
            prompts=prompts,
            searxng_url=searxng_url,
            max_iterations=config.max_iterations,
            default_engines=backend.get("default_engines"),
        )

        # Override name/description/display from config
        agent._config_name = name
        agent._config_description = config.description
        agent._config_display_name = config.display_name
        agent._config_icon_url = config.icon_url
        agent._config_source_type = config.source_type
        agent._config_searching_label = config.searching_label
        agent._config_item_label = config.item_label

        return agent


# Register on import
_register_websearch_factory()
