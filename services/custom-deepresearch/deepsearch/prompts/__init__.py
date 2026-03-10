"""
Prompts Module

Manages loading and rendering prompts from external YAML files.

Usage:
    from deepsearch.prompts import PromptManager

    manager = PromptManager(Path("prompts"))
    prompt = manager.get_prompt("supervisor", "assess_quality", query="...")
"""

from .loader import PromptManager, PromptNotFoundError

__all__ = [
    "PromptManager",
    "PromptNotFoundError",
]
