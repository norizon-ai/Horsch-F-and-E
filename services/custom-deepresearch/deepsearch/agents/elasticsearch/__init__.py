"""
Elasticsearch Agent Module

Specialized agent for searching Elasticsearch indices.
Supports multiple instances for different indices (docs, tickets, etc.).
Supports hybrid search (BM25 + vector KNN) and query preprocessing.
"""

from typing import List, TYPE_CHECKING

from .agent import ElasticsearchAgent
from .tools import ElasticsearchSearchTool, create_tool_from_config

if TYPE_CHECKING:
    from deepsearch.agents.base import BaseAgent
    from deepsearch.agents.config import AgentInstanceConfig
    from deepsearch.llm import LLMProvider
    from deepsearch.prompts import PromptManager
    from deepsearch.processors.base import BaseProcessor

__all__ = [
    "ElasticsearchAgent",
    "ElasticsearchSearchTool",
    "create_tool_from_config",
]


def _create_preprocessors(
    config: "AgentInstanceConfig",
    llm: "LLMProvider",
    prompts: "PromptManager",
) -> List["BaseProcessor"]:
    """
    Create preprocessor instances from agent config.

    Args:
        config: Agent configuration with preprocessors list
        llm: LLM provider for LLM-based preprocessors
        prompts: Prompt manager for preprocessor prompts

    Returns:
        List of initialized preprocessor instances
    """
    from deepsearch.observability import get_logger

    logger = get_logger(__name__)
    preprocessors: List["BaseProcessor"] = []

    for pp_config in config.preprocessors:
        if not pp_config.enabled:
            continue

        try:
            if pp_config.type == "reformulator":
                from deepsearch.processors import QueryReformulator
                from deepsearch.processors.query_reformulator import (
                    QueryReformulatorConfig,
                )

                pp = QueryReformulator(
                    config=QueryReformulatorConfig(**pp_config.config),
                    llm=llm,
                    prompts=prompts,
                )
                preprocessors.append(pp)
                logger.debug(
                    "preprocessor_created",
                    type=pp_config.type,
                    config=pp_config.config,
                )

            elif pp_config.type == "assumption_checker":
                from deepsearch.processors import AssumptionChecker
                from deepsearch.processors.assumption_checker import (
                    AssumptionCheckerConfig,
                )

                pp = AssumptionChecker(
                    config=AssumptionCheckerConfig(**pp_config.config),
                    llm=llm,
                    prompts=prompts,
                )
                preprocessors.append(pp)
                logger.debug(
                    "preprocessor_created",
                    type=pp_config.type,
                    config=pp_config.config,
                )

            elif pp_config.type == "semantic_reranker":
                from deepsearch.processors import SemanticReranker
                from deepsearch.processors.semantic_reranker import (
                    SemanticRerankerConfig,
                )

                pp = SemanticReranker(
                    config=SemanticRerankerConfig(**pp_config.config),
                )
                preprocessors.append(pp)
                logger.debug(
                    "preprocessor_created",
                    type=pp_config.type,
                    config=pp_config.config,
                )

            else:
                logger.warning(
                    "unknown_preprocessor_type",
                    type=pp_config.type,
                )

        except Exception as e:
            logger.error(
                "preprocessor_creation_failed",
                type=pp_config.type,
                error=str(e),
            )

    return preprocessors


def _register_elasticsearch_factory() -> None:
    """Register the elasticsearch agent factory creator."""
    from deepsearch.agents.factory import AgentFactory

    @AgentFactory.register("elasticsearch")
    async def create_elasticsearch_agent(
        name: str,
        config: "AgentInstanceConfig",
        llm: "LLMProvider",
        prompts: "PromptManager",
    ) -> "BaseAgent":
        """Create ElasticsearchAgent from YAML config."""
        backend = config.backend

        es_url = backend.get("url")
        if not es_url:
            raise ValueError(f"Agent '{name}': backend.url is required")

        index = backend.get("index")
        if not index:
            raise ValueError(f"Agent '{name}': backend.index is required")

        # Create preprocessors from config
        preprocessors = _create_preprocessors(config, llm, prompts)

        # Create agent with hybrid search config and preprocessors
        agent = ElasticsearchAgent(
            llm=llm,
            prompts=prompts,
            es_url=es_url,
            index=index,
            search_fields=backend.get("search_fields"),
            max_iterations=config.max_iterations,
            api_key=backend.get("api_key"),
            username=backend.get("username"),
            password=backend.get("password"),
            source_type=config.source_type,
            # Hybrid search config
            hybrid_enabled=backend.get("hybrid_enabled", False),
            vector_field=backend.get("vector_field", "vector"),
            vector_weight=backend.get("vector_weight", 0.5),
            bm25_weight=backend.get("bm25_weight", 0.5),
            embedding_model=backend.get(
                "embedding_model", "sentence-transformers/all-MiniLM-L6-v2"
            ),
            # Preprocessors
            preprocessors=preprocessors,
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
_register_elasticsearch_factory()
