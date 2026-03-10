"""
WebSearch Agent

Specialized agent for web search research using SearXNG.
"""

from typing import List, Optional, TYPE_CHECKING

from deepsearch.agents.base import BaseAgent
from deepsearch.agents.reasoning import ReasoningAgentMixin
from deepsearch.models.agent import AgentResult
from deepsearch.tools import BaseTool
from deepsearch.observability import get_logger

from .tools import SearXNGSearchTool, FetchUrlTool, ExtractContentTool

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

logger = get_logger(__name__)


class WebSearchAgent(BaseAgent, ReasoningAgentMixin):
    """
    Specialized agent for web search research.

    This agent can:
    - Search the web using SearXNG metasearch engine
    - Fetch specific URLs for detailed content
    - Extract and analyze content from web pages

    It uses an iterative reasoning loop to gather comprehensive information
    from multiple sources before synthesizing an answer.

    Example:
        agent = WebSearchAgent(
            llm=llm,
            prompts=prompts,
            searxng_url="http://localhost:8080",
        )
        result = await agent.run("What are the latest developments in quantum computing?")
    """

    def __init__(
        self,
        llm: "LLMProvider",
        prompts: "PromptManager",
        searxng_url: str,
        max_iterations: int = 5,
        default_engines: Optional[List[str]] = None,
    ):
        """
        Initialize the WebSearch agent.

        Args:
            llm: LLM provider for reasoning.
            prompts: Prompt manager for agent prompts.
            searxng_url: URL of the SearXNG instance.
            max_iterations: Maximum reasoning loop iterations.
            default_engines: Search engines to use (default: google, bing, duckduckgo).
        """
        self._config_name = None
        self._config_description = None

        self._tools = [
            SearXNGSearchTool(
                searxng_url=searxng_url,
                default_engines=default_engines or ["google", "bing", "duckduckgo"],
            ),
            FetchUrlTool(),
            ExtractContentTool(),
        ]

        super().__init__(llm, prompts, max_iterations)

        self.searxng_url = searxng_url

        logger.info(
            "websearch_agent_init",
            searxng_url=searxng_url,
            tool_count=len(self._tools),
            max_iterations=max_iterations,
        )

    @property
    def name(self) -> str:
        """Agent name, can be overridden by config."""
        return self._config_name or "web_search_agent"

    @property
    def description(self) -> str:
        """Agent description, can be overridden by config."""
        if self._config_description:
            return self._config_description
        return (
            "Searches the web for current information, news, documentation, "
            "and general knowledge using SearXNG metasearch. Can fetch and "
            "analyze specific web pages. Best for questions requiring "
            "up-to-date web information or external sources."
        )

    @property
    def tools(self) -> List[BaseTool]:
        """Tools available to this agent."""
        return self._tools

    @property
    def prompt_category(self) -> str:
        """Prompt category for this agent's prompts."""
        return "websearch_agent"

    async def run(self, task: str, **kwargs) -> AgentResult:
        """
        Run the web search agent on a task.

        Args:
            task: The research task or question.
            **kwargs: Additional arguments passed to the reasoning loop.

        Returns:
            AgentResult with findings and sources.
        """
        logger.info(
            "websearch_agent_run",
            task=task[:100],
        )

        return await self.reasoning_loop(task, **kwargs)
