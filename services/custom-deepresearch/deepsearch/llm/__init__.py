"""
LLM Provider Module

Provides LLM provider abstraction for multi-provider support.

Usage:
    from deepsearch.llm import LLMProvider, create_llm_provider, LLMMessage

    # Create provider
    llm = create_llm_provider(
        provider_type="gpt-oss",
        base_url="http://localhost:8000/v1",
        api_key="dummy",
        model="openai/gpt-oss-120b",
    )

    # Use it
    response = await llm.complete([
        LLMMessage.system("You are a helpful assistant."),
        LLMMessage.user("Hello!"),
    ])
"""

from .base import LLMProvider, LLMMessage, LLMResponse, FunctionCall
from .openai_compat import OpenAICompatProvider, ResponseProcessor, create_llm_provider

__all__ = [
    "LLMProvider",
    "LLMMessage",
    "LLMResponse",
    "FunctionCall",
    "OpenAICompatProvider",
    "ResponseProcessor",
    "create_llm_provider",
]
