"""
Supervisor Module

The supervisor orchestrates tools via LLM function calling.

Usage:
    from deepsearch.supervisor import SupervisorAgent, SupervisorConfig

    supervisor = SupervisorAgent(
        llm=llm,
        prompts=prompts,
        config=SupervisorConfig(
            execution_strategy="iterative",
            max_iterations=3,
        ),
    )

    result = await supervisor.search("How do I submit a SLURM job?")
"""

from .agent import SupervisorAgent, SupervisorConfig

__all__ = [
    "SupervisorAgent",
    "SupervisorConfig",
]
