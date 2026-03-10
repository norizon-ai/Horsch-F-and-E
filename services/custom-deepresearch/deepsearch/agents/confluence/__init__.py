"""
Confluence MCP Agent Module

Specialized agent for searching Confluence live via the mcp-atlassian MCP server.
"""

from typing import TYPE_CHECKING

from .agent import ConfluenceMCPAgent
from .tools import ConfluenceSearchTool, ConfluenceGetPageTool

if TYPE_CHECKING:
    from deepsearch.agents.base import BaseAgent
    from deepsearch.agents.config import AgentInstanceConfig
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

__all__ = [
    "ConfluenceMCPAgent",
    "ConfluenceSearchTool",
    "ConfluenceGetPageTool",
]


def _register_confluence_mcp_factory() -> None:
    """Register the confluence_mcp agent factory creator."""
    from deepsearch.agents.factory import AgentFactory

    @AgentFactory.register("confluence_mcp")
    async def create_confluence_mcp_agent(
        name: str,
        config: "AgentInstanceConfig",
        llm: "LLMProvider",
        prompts: "PromptManager",
    ) -> "BaseAgent":
        """Create ConfluenceMCPAgent from YAML config."""
        backend = config.backend

        mcp_server_url = backend.get("mcp_server_url", "http://localhost:8005")

        agent = ConfluenceMCPAgent(
            llm=llm,
            prompts=prompts,
            mcp_server_url=mcp_server_url,
            max_iterations=config.max_iterations,
            source_type=config.source_type or "confluence",
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
_register_confluence_mcp_factory()
