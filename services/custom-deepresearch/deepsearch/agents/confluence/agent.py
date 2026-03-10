"""
Confluence MCP Agent

Specialized agent for searching Confluence live via the mcp-atlassian MCP server.
"""

from typing import TYPE_CHECKING, List, Optional

from deepsearch.agents.base import BaseAgent
from deepsearch.agents.reasoning import ReasoningAgentMixin
from deepsearch.models.agent import AgentResult
from deepsearch.observability import get_logger
from deepsearch.tools import BaseTool

from .tools import ConfluenceSearchTool, ConfluenceGetPageTool

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

logger = get_logger(__name__)


class ConfluenceMCPAgent(BaseAgent, ReasoningAgentMixin):
    """
    Searches Confluence live via the mcp-atlassian MCP server.

    This agent queries Confluence in real-time using CQL searches
    and page content retrieval, rather than searching a pre-indexed
    Elasticsearch copy.

    Example:
        agent = ConfluenceMCPAgent(
            llm=llm,
            prompts=prompts,
            mcp_server_url="http://localhost:8005",
        )
        result = await agent.run("How do I set up the VPN?")
    """

    def __init__(
        self,
        llm: "LLMProvider",
        prompts: "PromptManager",
        mcp_server_url: str,
        max_iterations: int = 3,
        source_type: str = "confluence",
    ):
        # Config overrides (set by factory when loading from YAML)
        self._config_name: Optional[str] = None
        self._config_description: Optional[str] = None

        self.mcp_server_url = mcp_server_url

        # Initialize tools before calling super().__init__()
        self._search_tool = ConfluenceSearchTool(mcp_server_url, source_type)
        self._get_page_tool = ConfluenceGetPageTool(mcp_server_url, source_type)

        super().__init__(llm, prompts, max_iterations)

        logger.info(
            "confluence_mcp_agent_init",
            mcp_server_url=mcp_server_url,
            max_iterations=max_iterations,
        )

    @property
    def name(self) -> str:
        return self._config_name or "confluence_mcp"

    @property
    def description(self) -> str:
        if self._config_description:
            return self._config_description
        return (
            "Search Confluence documentation and knowledge base for "
            "company-specific information via live queries."
        )

    @property
    def tools(self) -> List[BaseTool]:
        return [self._search_tool, self._get_page_tool]

    @property
    def prompt_category(self) -> str:
        return "confluence_agent"

    async def run(self, task: str, **kwargs) -> AgentResult:
        """
        Execute the Confluence search task.

        The agent will:
        1. Formulate CQL search queries based on the task
        2. Search Confluence via the MCP server
        3. Fetch full page content for relevant results
        4. Synthesize findings into an answer with citations

        Args:
            task: The research task delegated by the supervisor
            **kwargs: Additional parameters (e.g., context)

        Returns:
            AgentResult with findings, sources, and confidence
        """
        logger.info(
            "confluence_mcp_agent_run",
            task=task[:100],
        )

        return await self.reasoning_loop(task, **kwargs)
