"""
Agent Factory

Factory for creating agents from YAML configuration.
Supports built-in agents via @register decorator and custom agents via class path.
"""

from importlib import import_module
from typing import TYPE_CHECKING, Callable, Dict, List, Optional

from deepsearch.agents.config import AgentInstanceConfig
from deepsearch.observability import get_logger

if TYPE_CHECKING:
    from deepsearch.agents.base import BaseAgent
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager

logger = get_logger(__name__)


class AgentFactory:
    """
    Factory for creating agents from configuration.

    Built-in agent types register their creator functions via the @register decorator.
    Custom agents are loaded dynamically from a class path.

    Usage:
        # Register a creator for a built-in type
        @AgentFactory.register("websearch")
        async def create_websearch(name, config, llm, prompts):
            return WebSearchAgent(...)

        # Create agents from config
        agent = await AgentFactory.create("my_agent", config, llm, prompts)
    """

    _creators: Dict[str, Callable] = {}

    @classmethod
    def register(cls, agent_type: str):
        """
        Register a creator function for an agent type.

        Args:
            agent_type: The agent type string (e.g., "websearch", "elasticsearch")

        Returns:
            Decorator function
        """
        def decorator(func: Callable):
            cls._creators[agent_type] = func
            logger.debug("agent_creator_registered", agent_type=agent_type)
            return func

        return decorator

    @classmethod
    def registered_types(cls) -> List[str]:
        """Get list of registered agent types."""
        return list(cls._creators.keys())

    @classmethod
    async def create(
        cls,
        name: str,
        config: AgentInstanceConfig,
        llm: "LLMProvider",
        prompts: "PromptManager",
    ) -> Optional["BaseAgent"]:
        """
        Create an agent from configuration.

        Handles:
        - Disabled agents (returns None)
        - Custom agents (loaded from class path)
        - Built-in agents (via registered creators)

        Args:
            name: Agent instance name
            config: Agent configuration
            llm: LLM provider
            prompts: Prompt manager

        Returns:
            Agent instance or None if disabled/failed
        """
        if not config.enabled:
            logger.info("agent_disabled", name=name, type=config.type)
            return None

        if config.type == "custom":
            return await cls._create_custom(name, config, llm, prompts)

        creator = cls._creators.get(config.type)
        if not creator:
            logger.error(
                "unknown_agent_type",
                name=name,
                type=config.type,
                available=cls.registered_types(),
            )
            return None

        try:
            agent = await creator(name, config, llm, prompts)
            logger.info(
                "agent_created",
                name=name,
                type=config.type,
                agent_class=agent.__class__.__name__,
            )
            return agent

        except Exception as e:
            logger.error(
                "agent_creation_failed",
                name=name,
                type=config.type,
                error=str(e),
            )
            return None

    @classmethod
    async def _create_custom(
        cls,
        name: str,
        config: AgentInstanceConfig,
        llm: "LLMProvider",
        prompts: "PromptManager",
    ) -> Optional["BaseAgent"]:
        """
        Create a custom agent from a class path.

        The class path should point to a BaseAgent subclass.
        The agent is instantiated with llm, prompts, max_iterations,
        and any additional backend config as kwargs.

        Args:
            name: Agent instance name
            config: Agent configuration with class_path
            llm: LLM provider
            prompts: Prompt manager

        Returns:
            Agent instance or None if failed
        """
        if not config.class_path:
            logger.error("custom_agent_missing_class", name=name)
            return None

        try:
            module_path, class_name = config.class_path.rsplit(".", 1)
            module = import_module(module_path)
            agent_class = getattr(module, class_name)

            # Create agent with standard kwargs + backend config
            agent = agent_class(
                llm=llm,
                prompts=prompts,
                max_iterations=config.max_iterations,
                **config.backend,
            )

            # Set config overrides if supported
            if hasattr(agent, "_config_name"):
                agent._config_name = name
            if hasattr(agent, "_config_description"):
                agent._config_description = config.description

            logger.info(
                "custom_agent_created",
                name=name,
                class_path=config.class_path,
            )

            return agent

        except ImportError as e:
            logger.error(
                "custom_agent_import_failed",
                name=name,
                class_path=config.class_path,
                error=str(e),
            )
            return None

        except Exception as e:
            logger.error(
                "custom_agent_creation_failed",
                name=name,
                class_path=config.class_path,
                error=str(e),
            )
            return None

    @classmethod
    def clear(cls) -> None:
        """Clear all registered creators."""
        cls._creators.clear()
