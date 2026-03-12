"""
Norizon search Microservice

FastAPI application entry point.
"""

import uuid
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from deepsearch.config import get_config
from deepsearch.observability import (
    setup_logging,
    get_logger,
    set_correlation_id,
    clear_context,
    init_tracing,
    shutdown_tracing,
)
from deepsearch.api import router
from deepsearch.api.routes import start_cleanup_task, stop_cleanup_task
from deepsearch.llm import create_llm_provider
from deepsearch.prompts import PromptManager
from deepsearch.supervisor import SupervisorAgent, SupervisorConfig
from deepsearch.agents import AgentRegistry
from deepsearch.agents.config import load_agents_config
from deepsearch.agents.factory import AgentFactory

# Import agent modules to trigger factory registration
import deepsearch.agents.websearch  # noqa: F401
import deepsearch.agents.elasticsearch  # noqa: F401
import deepsearch.agents.confluence  # noqa: F401
import deepsearch.agents.jira  # noqa: F401

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    config = get_config()

    # Setup logging
    setup_logging(level=config.log_level, log_format=config.log_format)

    # Initialize tracing (if enabled)
    tracing_enabled = init_tracing(service_name="deepsearch")
    if tracing_enabled:
        export_mode = "immediate" if config.trace_immediate_export else "batched"
        logger.info("tracing_initialized", phoenix_endpoint=config.phoenix_endpoint, export_mode=export_mode)
    else:
        logger.info("tracing_disabled", reason="enable_tracing=false or missing dependencies")

    logger.info("application_starting", config=config.model_dump())

    # Create LLM provider
    llm = create_llm_provider(
        provider_type=config.llm_provider,
        base_url=config.llm_base_url,
        api_key=config.llm_api_key,
        model=config.llm_model,
        timeout=config.llm_timeout,
    )

    # Create prompt manager
    prompts = PromptManager(config.prompts_dir)

    # Load agent configuration from YAML
    agents = []
    if config.agents_config_path:
        agents_config = load_agents_config(config.agents_config_path)

        # Create enabled agents from config
        for name, agent_cfg in agents_config.agents.items():
            agent = await AgentFactory.create(
                name=name,
                config=agent_cfg,
                llm=llm,
                prompts=prompts,
            )
            if agent:
                AgentRegistry.register(agent)
                agents.append(agent)

        logger.info(
            "agents_loaded",
            count=len(agents),
            names=[a.name for a in agents],
            available_types=AgentFactory.registered_types(),
        )

    # Create supervisor with loaded agents
    supervisor = SupervisorAgent(
        llm=llm,
        prompts=prompts,
        config=SupervisorConfig(
            execution_strategy=config.execution_strategy,
            max_iterations=config.max_iterations,
            quality_threshold=config.quality_threshold,
            report_max_tokens=config.report_max_tokens,
            search_timeout_seconds=config.search_timeout,
            tool_timeout_seconds=config.tool_timeout,
        ),
        agents=agents if agents else None,  # Pass agents or None to use registry
    )

    # Inject supervisor into router
    router._supervisor = supervisor

    # Start background job cleanup task
    start_cleanup_task()

    logger.info("application_started", agent_count=len(agents))

    yield

    # Cleanup
    stop_cleanup_task()
    AgentRegistry.clear()
    await llm.close()
    shutdown_tracing()  # Flush and shutdown tracing
    logger.info("application_stopped")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    config = get_config()

    app = FastAPI(
        title="Norizon search Microservice",
        description="Agentic RAG with tool-based retrieval",
        version="1.0.0",
        lifespan=lifespan,
    )

    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Configure for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Request ID middleware
    @app.middleware("http")
    async def add_correlation_id(request: Request, call_next):
        correlation_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        set_correlation_id(correlation_id)

        response = await call_next(request)

        response.headers["X-Request-ID"] = correlation_id
        clear_context()

        return response

    # Include API routes
    app.include_router(router)

    # Root endpoint
    @app.get("/")
    async def root():
        return {
            "service": "Norizon search Microservice",
            "version": "1.0.0",
            "docs": "/docs",
        }

    return app


# Application instance
app = create_app()


if __name__ == "__main__":
    import uvicorn

    config = get_config()
    uvicorn.run(
        "deepsearch.main:app",
        host=config.api_host,
        port=config.api_port,
        reload=True,
    )
