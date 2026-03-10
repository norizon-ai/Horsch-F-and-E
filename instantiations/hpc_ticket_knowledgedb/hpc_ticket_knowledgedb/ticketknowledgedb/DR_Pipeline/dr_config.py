#!/usr/bin/env python3
"""
Configuration for the HPC Deep Research (DR) system
"""

import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class DRConfig:
    """Configuration for the DR system"""
    
    # LLM Configuration (NHR Hub Gateway)
    llm_base_url: str = "https://hub.nhr.fau.de/api/llmgw/v1"
    llm_api_key: str = "sk-a9uOWS13GwXfELWArWcnAA"
    llm_model: str = "gpt-oss-120b"
    llm_temperature: float = 0.2
    llm_max_tokens: int = 2000
    
    # Elasticsearch Configuration
    elastic_url: str = "http://localhost:9200"
    docs_index: str = "docs"
    tickets_index: str = "tickets"
    
    # DR Process Configuration
    max_iterations: int = 3
    quality_threshold: float = 0.7
    confidence_threshold: float = 0.6
    max_assumptions: int = 5
    
    # Search Configuration
    max_search_results: int = 10
    search_timeout: int = 30

    # LLM Timeout Configuration (in seconds)
    llm_timeout: int = 30  # Timeout for individual LLM requests
    
    # Output Configuration
    max_report_length: int = 5000
    max_concise_answer_sentences: int = 4
    
    # Tracing Configuration
    enable_tracing: bool = False
    phoenix_endpoint: str = "http://localhost:6006/v1/traces"
    
    @classmethod
    def from_env(cls) -> 'DRConfig':
        """Create configuration from environment variables"""
        return cls(
            llm_base_url=os.getenv("LLM_BASE_URL", cls.llm_base_url),
            llm_api_key=os.getenv("LLM_API_KEY", cls.llm_api_key),
            llm_model=os.getenv("LLM_MODEL", cls.llm_model),
            llm_timeout=int(os.getenv("LLM_TIMEOUT", str(cls.llm_timeout))),
            elastic_url=os.getenv("ELASTIC_URL", cls.elastic_url),
            docs_index=os.getenv("DOCS_INDEX", cls.docs_index),
            tickets_index=os.getenv("TICKETS_INDEX", cls.tickets_index),
            enable_tracing=os.getenv("ENABLE_TRACING", "false").lower() == "true"
        )
    
    def validate(self) -> bool:
        """Validate configuration"""
        required_fields = [
            self.llm_base_url,
            self.llm_model,
            self.elastic_url,
            self.docs_index,
            self.tickets_index
        ]
        
        return all(field for field in required_fields)


# Global configuration instance
config = DRConfig.from_env()
