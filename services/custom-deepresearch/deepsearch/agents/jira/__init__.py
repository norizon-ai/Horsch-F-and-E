"""
Jira MCP Agent Module

Specialized agent for searching Jira live via the mcp-atlassian MCP server.
"""

from typing import TYPE_CHECKING

from .agent import JiraMCPAgent
from .tools import JiraSearchTool, JiraGetIssueTool

if TYPE_CHECKING:
    from deepsearch.agents.base import BaseAgent
    from deepsearch.agents.config import AgentInstanceConfig
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

__all__ = [
    "JiraMCPAgent",
    "JiraSearchTool",
    "JiraGetIssueTool",
]


def _register_jira_mcp_factory() -> None:
    """Register the jira_mcp agent factory creator."""
    from deepsearch.agents.factory import AgentFactory

    @AgentFactory.register("jira_mcp")
    async def create_jira_mcp_agent(
        name: str,
        config: "AgentInstanceConfig",
        llm: "LLMProvider",
        prompts: "PromptManager",
    ) -> "BaseAgent":
        """Create JiraMCPAgent from YAML config."""
        backend = config.backend

        mcp_server_url = backend.get("mcp_server_url", "http://localhost:8006")

        agent = JiraMCPAgent(
            llm=llm,
            prompts=prompts,
            mcp_server_url=mcp_server_url,
            max_iterations=config.max_iterations,
            source_type=config.source_type or "jira",
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
_register_jira_mcp_factory()
