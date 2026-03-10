"""
Processors Module

Injectable processors that can be composed into retrievers.
Each processor can modify queries (pre_process) and results (post_process).

Usage:
    from deepsearch.processors import (
        BaseProcessor,
        ProcessorChain,
        QueryReformulator,
        AssumptionChecker,
    )

    # Create processors
    reformulator = QueryReformulator(config=QueryReformulatorConfig(max_terms=8))
    checker = AssumptionChecker(llm=llm, prompts=prompts)

    # Inject into retriever
    retriever = MyRetriever(processors=[reformulator, checker])
"""

from .base import BaseProcessor, ProcessorChain
from .query_reformulator import (
    QueryReformulator,
    QueryReformulatorConfig,
    SimpleTermExtractor,
    get_stopwords,
)
from .assumption_checker import (
    AssumptionChecker,
    AssumptionCheckerConfig,
    # Models co-located with processor
    AssumptionValidation,
    UserAssumption,
    AssumptionCheckResult,
)
from .semantic_reranker import (
    SemanticReranker,
    SemanticRerankerConfig,
    create_semantic_reranker,
)

__all__ = [
    # Base
    "BaseProcessor",
    "ProcessorChain",
    # Query Reformulator
    "QueryReformulator",
    "QueryReformulatorConfig",
    "SimpleTermExtractor",
    "get_stopwords",
    # Assumption Checker
    "AssumptionChecker",
    "AssumptionCheckerConfig",
    "AssumptionValidation",
    "UserAssumption",
    "AssumptionCheckResult",
    # Semantic Reranker
    "SemanticReranker",
    "SemanticRerankerConfig",
    "create_semantic_reranker",
]
