"""
Norizon search Configuration

All configuration is managed via Pydantic Settings with environment variable support.
Set environment variables with DR_ prefix (e.g., DR_LLM_MODEL=gpt-4).

NOTE: Search backend configuration is NOT here - it belongs to each retriever.
Each retriever manages its own backend configuration for proper separation of concerns.
"""

from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Literal, Optional
from pathlib import Path
from functools import lru_cache


class DRConfig(BaseSettings):
    """
    Norizon search global configuration.

    This contains only settings that are truly global:
    - LLM provider settings (shared across all agents)
    - Supervisor workflow settings
    - Prompts location
    - API settings
    - Observability settings

    Search backend settings belong in retriever configs.
    """

    # === LLM Configuration ===
    llm_provider: Literal["openai", "anthropic", "gpt-oss", "ollama"] = Field(
        default="gpt-oss", description="LLM provider type"
    )
    llm_base_url: str = Field(
        default="http://lme49.cs.fau.de:30000/v1", description="Base URL for LLM API"
    )
    llm_api_key: str = Field(default="dummy", description="API key for LLM provider")
    llm_model: str = Field(
        default="openai/gpt-oss-120b", description="Model identifier"
    )
    llm_temperature: float = Field(
        default=0.1, ge=0.0, le=2.0, description="LLM temperature (lower = more deterministic)"
    )
    llm_max_tokens: int = Field(
        default=2000, ge=1, le=32000, description="Maximum tokens in response"
    )
    report_max_tokens: int = Field(
        default=4000,
        ge=500,
        le=8000,
        description="Maximum tokens for final report generation",
    )
    llm_timeout: int = Field(
        default=120, ge=1, description="Request timeout in seconds"
    )

    # === Supervisor Configuration ===
    execution_strategy: Literal["iterative", "parallel"] = Field(
        default="iterative",
        description="How supervisor executes tools: iterative (one at a time) or parallel",
    )
    max_iterations: int = Field(
        default=3, ge=1, le=10, description="Maximum search iterations"
    )
    quality_threshold: float = Field(
        default=0.7, ge=0.0, le=1.0, description="Quality threshold for early stopping"
    )
    confidence_threshold: float = Field(
        default=0.6, ge=0.0, le=1.0, description="Confidence threshold"
    )
    search_timeout: float = Field(
        default=300.0, ge=30.0, le=600.0, description="Total search timeout in seconds"
    )
    tool_timeout: float = Field(
        default=90.0,
        ge=10.0,
        le=300.0,
        description="Individual tool/agent timeout in seconds",
    )

    # === Prompts Configuration ===
    prompts_dir: Path = Field(
        default=Path("prompts"), description="Directory containing prompt YAML files"
    )

    # === Agent Configuration ===
    agents_config_path: Optional[Path] = Field(
        default=Path("agents.yaml"),
        description="Path to agents YAML configuration file",
    )

    # === API Configuration ===
    api_host: str = Field(default="0.0.0.0", description="API server host")
    api_port: int = Field(default=8000, ge=1, le=65535, description="API server port")

    # === Observability ===
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = Field(
        default="INFO", description="Logging level"
    )
    log_format: Literal["json", "text"] = Field(
        default="json", description="Log output format"
    )
    enable_tracing: bool = Field(
        default=True, description="Enable Phoenix/OpenTelemetry tracing"
    )
    phoenix_endpoint: str = Field(
        default="http://localhost:6006/v1/traces",
        description="Phoenix/OTLP endpoint for traces",
    )
    trace_immediate_export: bool = Field(
        default=True,
        description="Export traces immediately (dev). Set False for batched export (prod).",
    )

    model_config = {
        "env_prefix": "DR_",
        "env_file": ".env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


@lru_cache()
def get_config() -> DRConfig:
    """Get cached configuration singleton."""
    return DRConfig()
