"""
Specialized Research Agents

Agents are autonomous workers that can use multiple tools and have their own
reasoning loops. The supervisor delegates research tasks to specialized agents.

This module provides:
- BaseAgent: Abstract base class for creating agents
- AgentRegistry: Registry for discovering available agents
- ReasoningAgentMixin: Common reasoning loop implementation

Example usage:
    from deepsearch.agents import BaseAgent, AgentRegistry, ReasoningAgentMixin

    class MyAgent(BaseAgent, ReasoningAgentMixin):
        @property
        def name(self) -> str:
            return "my_agent"

        @property
        def description(self) -> str:
            return "Does specialized research"

        @property
        def tools(self) -> List[BaseTool]:
            return [self.search_tool]

        async def run(self, task: str, **kwargs) -> AgentResult:
            return await self.reasoning_loop(task, **kwargs)

    # Register and use
    agent = MyAgent(llm, prompts)
    AgentRegistry.register(agent)
"""

from .base import BaseAgent, AgentParameter
from .registry import AgentRegistry, register_agent
from .reasoning import ReasoningAgentMixin
from .config import AgentInstanceConfig, AgentsConfig, load_agents_config
from .factory import AgentFactory

__all__ = [
    "BaseAgent",
    "AgentParameter",
    "AgentRegistry",
    "register_agent",
    "ReasoningAgentMixin",
    "AgentInstanceConfig",
    "AgentsConfig",
    "load_agents_config",
    "AgentFactory",
]
