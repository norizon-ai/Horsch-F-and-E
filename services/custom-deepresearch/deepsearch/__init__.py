"""
Norizon search Microservice

A modular, configurable Norizon search middleware with:
- Multi-provider LLM support (GPT-OSS, OpenAI, Anthropic, Ollama)
- Pluggable retriever architecture
- Injectable processors (QueryReformulator, AssumptionChecker)
- Tool-based supervisor with function calling
- REST API with SSE streaming

Quick Start:
    from deepsearch import create_app
    app = create_app()

Or use components directly:
    from deepsearch.llm import create_llm_provider
    from deepsearch.retrievers import BaseRetriever, ElasticsearchBackend
    from deepsearch.processors import QueryReformulator
    from deepsearch.supervisor import SupervisorAgent
    from deepsearch.tools import ToolRegistry
"""

__version__ = "1.0.0"

# Application
from deepsearch.main import create_app

# Configuration
from deepsearch.config import DRConfig, get_config

# LLM Providers
from deepsearch.llm import (
    LLMProvider,
    LLMMessage,
    LLMResponse,
    create_llm_provider,
)

# Tools
from deepsearch.tools import BaseTool, ToolRegistry, register_tool

# Retrievers
from deepsearch.retrievers import (
    BaseRetriever,
    ElasticsearchBackend,
    ElasticsearchConfig,
)

# Processors
from deepsearch.processors import (
    BaseProcessor,
    QueryReformulator,
    AssumptionChecker,
)

# Supervisor
from deepsearch.supervisor import SupervisorAgent, SupervisorConfig

# Prompts
from deepsearch.prompts import PromptManager

__all__ = [
    "__version__",
    "create_app",
    "DRConfig",
    "get_config",
    "LLMProvider",
    "LLMMessage",
    "LLMResponse",
    "create_llm_provider",
    "BaseTool",
    "ToolRegistry",
    "register_tool",
    "BaseRetriever",
    "ElasticsearchBackend",
    "ElasticsearchConfig",
    "BaseProcessor",
    "QueryReformulator",
    "AssumptionChecker",
    "SupervisorAgent",
    "SupervisorConfig",
    "PromptManager",
]
