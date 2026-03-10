"""
Base Agent Interface

Abstract base class for specialized research agents in the multi-agent system.
Agents have their own tools, prompts, and reasoning loops.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from pydantic import BaseModel, Field

from deepsearch.models.agent import AgentResult
from deepsearch.tools import BaseTool, ToolParameter
from deepsearch.observability import get_logger

if TYPE_CHECKING:
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager
    from deepsearch.processors.base import BaseProcessor

logger = get_logger(__name__)


class AgentParameter(BaseModel):
    """Schema for an agent parameter (used in function calling for delegation)."""

    name: str = Field(..., description="Parameter name")
    type: str = Field(default="string", description="Parameter type")
    description: str = Field(default="", description="Parameter description")
    required: bool = Field(default=False, description="Whether parameter is required")
    default: Any = Field(default=None, description="Default value")


class BaseAgent(ABC):
    """
    Abstract base class for specialized research agents.

    Unlike BaseTool which executes deterministically, BaseAgent has:
    - Its own set of tools it can call
    - Its own LLM for reasoning
    - Its own prompts for decision-making
    - An execution loop that can make multiple tool calls

    Agents are autonomous workers that receive a research task from
    the supervisor and return structured findings.

    Example:
        class WebSearchAgent(BaseAgent):
            @property
            def name(self) -> str:
                return "web_search_agent"

            @property
            def description(self) -> str:
                return "Searches the web for current information"

            @property
            def tools(self) -> List[BaseTool]:
                return [self.search_tool, self.fetch_tool]

            async def run(self, task: str, **kwargs) -> AgentResult:
                # Agent reasoning loop with multiple tool calls
                ...
    """

    def __init__(
        self,
        llm: "LLMProvider",
        prompts: "PromptManager",
        max_iterations: int = 5,
        preprocessors: Optional[List["BaseProcessor"]] = None,
    ):
        """
        Initialize the agent.

        Args:
            llm: LLM provider for agent reasoning
            prompts: PromptManager for agent-specific prompts
            max_iterations: Maximum reasoning iterations before stopping
            preprocessors: Query preprocessors to apply before search
        """
        self.llm = llm
        self.prompts = prompts
        self.max_iterations = max_iterations
        self.preprocessors = preprocessors or []

        logger.info(
            "agent_init",
            agent=self.name,
            max_iterations=max_iterations,
            tool_count=len(self.tools),
            preprocessor_count=len(self.preprocessors),
        )

    async def preprocess_query(self, query: str) -> str:
        """
        Run query through configured preprocessors.

        Args:
            query: Original search query

        Returns:
            Processed query (or original if no preprocessors)
        """
        if not self.preprocessors:
            return query

        processed = query
        context: Dict[str, Any] = {}

        for preprocessor in self.preprocessors:
            try:
                # pre_process returns just the query string, not a tuple
                processed = await preprocessor.pre_process(processed, context)
                logger.debug(
                    "preprocessor_applied",
                    preprocessor=preprocessor.__class__.__name__,
                    original_query=query[:50],
                    processed_query=processed[:50] if processed else "",
                )
            except Exception as e:
                logger.error(
                    "preprocessor_failed",
                    preprocessor=preprocessor.__class__.__name__,
                    error=str(e),
                )
                # Continue with current processed value on error

        return processed

    async def postprocess_results(
        self, results: List[Any], original_query: str
    ) -> List[Any]:
        """
        Run search results through configured post-processors (e.g., reranker).

        Args:
            results: List of SearchResult objects from search
            original_query: The original user query (before preprocessing)

        Returns:
            Post-processed results (e.g., reranked, filtered)
        """
        if not self.preprocessors:
            return results

        processed = results
        context: Dict[str, Any] = {}

        for preprocessor in self.preprocessors:
            try:
                # Only call post_process if the processor implements it
                if hasattr(preprocessor, "post_process"):
                    processed = await preprocessor.post_process(
                        processed, original_query, context
                    )
                    logger.debug(
                        "postprocessor_applied",
                        processor=preprocessor.__class__.__name__,
                        input_count=len(results),
                        output_count=len(processed),
                    )
            except Exception as e:
                logger.error(
                    "postprocessor_failed",
                    processor=preprocessor.__class__.__name__,
                    error=str(e),
                )
                # Continue with current processed value on error

        return processed

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique agent name for identification.

        This name is used for:
        - Logging and debugging
        - Function calling schema (delegate_to_<name>)
        - Registry lookup
        """
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Agent description shown to the supervisor LLM.

        This should clearly explain what research domain this agent
        specializes in so the supervisor can delegate appropriately.
        """
        pass

    @property
    @abstractmethod
    def tools(self) -> List[BaseTool]:
        """
        List of tools available to this agent.

        These are the tools the agent can call during its reasoning loop.
        Each tool should be relevant to the agent's specialization.
        """
        pass

    @property
    def parameters(self) -> List[AgentParameter]:
        """
        Parameters for the supervisor to pass when delegating to this agent.

        Default is just the task parameter. Override for additional params.
        """
        return [
            AgentParameter(
                name="task",
                type="string",
                description="The research task to accomplish",
                required=True,
            )
        ]

    @property
    def prompt_category(self) -> str:
        """
        Prompt category (YAML file) for this agent.

        Default uses agent name. Override if prompts are in a different file.
        """
        return self.name

    @property
    def display_name(self) -> str:
        """
        Human-readable display name for UI.

        Falls back to agent name if not configured.
        Set via _config_display_name attribute from YAML config.
        """
        return getattr(self, '_config_display_name', None) or self.name

    @property
    def icon_url(self) -> Optional[str]:
        """
        URL to source icon for UI display.

        Set via _config_icon_url attribute from YAML config.
        Returns None if not configured.
        """
        return getattr(self, '_config_icon_url', None)

    @property
    def source_type(self) -> Optional[str]:
        """
        Source type for UI mapping (e.g., 'confluence', 'sharepoint').

        Set via _config_source_type attribute from YAML config.
        Used to tag search results with the correct source type.
        """
        return getattr(self, '_config_source_type', None)

    @property
    def searching_label(self) -> Optional[str]:
        """
        Label shown while searching (e.g., 'Searching the web...').

        Set via _config_searching_label attribute from YAML config.
        Returns None if not configured.
        """
        return getattr(self, '_config_searching_label', None)

    @property
    def item_label(self) -> Optional[str]:
        """
        Label for counted items (e.g., 'websites', 'pages', 'documents').

        Set via _config_item_label attribute from YAML config.
        Returns None if not configured.
        """
        return getattr(self, '_config_item_label', None)

    @abstractmethod
    async def run(self, task: str, **kwargs) -> AgentResult:
        """
        Execute the agent's research task.

        This is the main entry point called by the supervisor.
        Implement the agent's reasoning loop here.

        Args:
            task: The research task delegated by the supervisor
            **kwargs: Additional parameters from supervisor

        Returns:
            AgentResult with findings, sources, and confidence
        """
        pass

    def to_function_schema(self) -> Dict[str, Any]:
        """
        Convert agent to OpenAI function calling schema.

        The supervisor uses this to know how to delegate to this agent.
        Format follows the delegate_to_<agent_name> pattern.
        """
        properties = {}
        required = []

        for param in self.parameters:
            properties[param.name] = {
                "type": param.type,
                "description": param.description,
            }
            if param.required:
                required.append(param.name)

        return {
            "type": "function",
            "function": {
                "name": f"delegate_to_{self.name}",
                "description": f"Delegate a research task to the {self.name}. {self.description}",
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            },
        }

    def _tool_schemas(self) -> List[Dict[str, Any]]:
        """Get function schemas for all agent tools."""
        return [tool.to_function_schema() for tool in self.tools]

    def _get_tool(self, name: str) -> Optional[BaseTool]:
        """Get a tool by name."""
        for tool in self.tools:
            if tool.name == name:
                return tool
        return None

    async def __call__(self, task: str, **kwargs) -> AgentResult:
        """Allow agents to be called directly."""
        return await self.run(task, **kwargs)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(name={self.name}, tools={len(self.tools)})>"
