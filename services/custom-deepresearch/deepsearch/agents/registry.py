"""
Agent Registry

Central registry for discovering and managing specialized research agents.
Similar to ToolRegistry but for agents.
"""

from functools import wraps
from typing import Dict, List, Optional, Type, TYPE_CHECKING

from deepsearch.observability import get_logger

if TYPE_CHECKING:
    from .base import BaseAgent

logger = get_logger(__name__)


class AgentRegistry:
    """
    Registry for all available agents.

    Similar to ToolRegistry but for specialized agents.
    The supervisor queries this registry to discover available agents
    and get their function schemas for delegation.

    Usage:
        # Register an agent instance
        AgentRegistry.register(web_search_agent)

        # Get all registered agents
        agents = AgentRegistry.all_agents()

        # Get function schemas for supervisor LLM
        schemas = AgentRegistry.to_function_schemas()
    """

    _agents: Dict[str, "BaseAgent"] = {}

    @classmethod
    def register(cls, agent: "BaseAgent") -> "BaseAgent":
        """
        Register an agent instance.

        Args:
            agent: Agent instance to register

        Returns:
            The registered agent (for chaining)
        """
        if agent.name in cls._agents:
            logger.warning(
                "agent_already_registered",
                agent_name=agent.name,
                existing_agent=cls._agents[agent.name].__class__.__name__,
                new_agent=agent.__class__.__name__,
            )

        cls._agents[agent.name] = agent
        logger.info(
            "agent_registered",
            agent_name=agent.name,
            agent_class=agent.__class__.__name__,
            tool_count=len(agent.tools),
        )

        return agent

    @classmethod
    def unregister(cls, name: str) -> Optional["BaseAgent"]:
        """
        Unregister an agent by name.

        Args:
            name: Agent name to unregister

        Returns:
            The unregistered agent, or None if not found
        """
        agent = cls._agents.pop(name, None)
        if agent:
            logger.info("agent_unregistered", agent_name=name)
        return agent

    @classmethod
    def get(cls, name: str) -> Optional["BaseAgent"]:
        """
        Get an agent by name.

        Handles the delegate_to_ prefix used in function calling.

        Args:
            name: Agent name (with or without delegate_to_ prefix)

        Returns:
            Agent instance or None
        """
        if name.startswith("delegate_to_"):
            name = name[len("delegate_to_"):]
        return cls._agents.get(name)

    @classmethod
    def all_agents(cls) -> List["BaseAgent"]:
        """Get all registered agents."""
        return list(cls._agents.values())

    @classmethod
    def agent_names(cls) -> List[str]:
        """Get names of all registered agents."""
        return list(cls._agents.keys())

    @classmethod
    def to_function_schemas(cls) -> List[dict]:
        """
        Get function calling schemas for all registered agents.

        Returns schemas in the delegate_to_<agent_name> format
        that the supervisor uses for delegation.

        Returns:
            List of function calling schema dicts
        """
        return [agent.to_function_schema() for agent in cls._agents.values()]

    @classmethod
    def clear(cls) -> None:
        """Clear all registered agents."""
        cls._agents.clear()
        logger.info("agent_registry_cleared")

    @classmethod
    def count(cls) -> int:
        """Get number of registered agents."""
        return len(cls._agents)


def register_agent(agent_class: Type["BaseAgent"]):
    """
    Decorator for auto-registering agent classes.

    When an agent class decorated with @register_agent is instantiated,
    it is automatically registered with the AgentRegistry.

    Usage:
        @register_agent
        class MyAgent(BaseAgent):
            ...
    """
    original_init = agent_class.__init__

    @wraps(original_init)
    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        AgentRegistry.register(self)

    agent_class.__init__ = new_init
    return agent_class
