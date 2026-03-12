"""
Jira MCP Agent

Specialized agent for searching Jira live via the mcp-atlassian MCP server.
"""

from typing import TYPE_CHECKING, List, Optional

from deepsearch.agents.base import BaseAgent
from deepsearch.agents.reasoning import ReasoningAgentMixin
from deepsearch.models.agent import AgentResult
from deepsearch.observability import get_logger
from deepsearch.tools import BaseTool

from .tools import JiraSearchTool, JiraGetIssueTool

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

logger = get_logger(__name__)


class JiraMCPAgent(BaseAgent, ReasoningAgentMixin):
    """
    Searches Jira live via the mcp-atlassian MCP server.

    This agent queries Jira in real-time using JQL searches
    and issue content retrieval.

    Example:
        agent = JiraMCPAgent(
            llm=llm,
            prompts=prompts,
            mcp_server_url="http://localhost:8006",
        )
        result = await agent.run("Find issues about hydraulic cylinder failures")
    """

    def __init__(
        self,
        llm: "LLMProvider",
        prompts: "PromptManager",
        mcp_server_url: str,
        max_iterations: int = 3,
        source_type: str = "jira",
    ):
        # Config overrides (set by factory when loading from YAML)
        self._config_name: Optional[str] = None
        self._config_description: Optional[str] = None

        self.mcp_server_url = mcp_server_url

        # Initialize tools before calling super().__init__()
        self._search_tool = JiraSearchTool(mcp_server_url, source_type)
        self._get_issue_tool = JiraGetIssueTool(mcp_server_url, source_type)

        super().__init__(llm, prompts, max_iterations)

        logger.info(
            "jira_mcp_agent_init",
            mcp_server_url=mcp_server_url,
            max_iterations=max_iterations,
        )

    @property
    def name(self) -> str:
        return self._config_name or "jira_mcp"

    @property
    def description(self) -> str:
        if self._config_description:
            return self._config_description
        return (
            "Search Jira issues, bugs, and tasks for "
            "project-specific information via live queries."
        )

    @property
    def tools(self) -> List[BaseTool]:
        return [self._search_tool, self._get_issue_tool]

    @property
    def prompt_category(self) -> str:
        return "jira_agent"

    async def run(self, task: str, **kwargs) -> AgentResult:
        """
        Execute the Jira search task.

        The agent will:
        1. Formulate JQL search queries based on the task
        2. Search Jira via the MCP server
        3. Fetch full issue content for relevant results
        4. Synthesize findings into an answer with citations

        Args:
            task: The research task delegated by the supervisor
            **kwargs: Additional parameters (e.g., context)

        Returns:
            AgentResult with findings, sources, and confidence
        """
        logger.info(
            "jira_mcp_agent_run",
            task=task[:100],
        )

        return await self.reasoning_loop(task, **kwargs)
