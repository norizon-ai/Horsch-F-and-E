#!/usr/bin/env python3
"""
HPC Deep Research (DR) System

A multi-agent system for comprehensive HPC question answering with:
- Supervisor Agent: Orchestrates research and assesses quality
- Research Agent: Performs zero-shot, docs-only, and ticket-based research
- Assumption Checker: Validates user assumptions against documentation
- Final fact-checking against official documentation only

Usage:
    from DR_Pipeline import dr_service
    
    # Initialize the service
    await dr_service.initialize()
    
    # Process a query
    result = await dr_service.process_query("How do I access $WORK in JupyterHub?")
    
    # Access results
    print(result.concise_answer)
    print(result.final_report)
"""

from .dr_models import (
    ResearchType, QualityScore, SearchResult, ResearchAnswer, 
    UserAssumption, QualityAssessment, DRIteration, DRResult,
    HPCSearchRequest, HPCSearchResponse
)

from .dr_config import config, DRConfig
from .search_service import search_service, SearchService
from .research_agent import ResearchAgent
from .assumption_checker import AssumptionChecker
from .supervisor_agent import SupervisorAgent
from .dr_workflow import dr_service, DRService, DRWorkflow

__version__ = "1.0.0"
__author__ = "HPC Deep Research Team"

__all__ = [
    # Main service
    "dr_service",
    
    # Core classes
    "DRService",
    "DRWorkflow", 
    "SupervisorAgent",
    "ResearchAgent",
    "AssumptionChecker",
    "SearchService",
    
    # Data models
    "ResearchType",
    "QualityScore", 
    "SearchResult",
    "ResearchAnswer",
    "UserAssumption",
    "QualityAssessment", 
    "DRIteration",
    "DRResult",
    "HPCSearchRequest",
    "HPCSearchResponse",
    
    # Configuration
    "config",
    "DRConfig",
    
    # Services
    "search_service",
]
