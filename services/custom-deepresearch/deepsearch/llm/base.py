"""
LLM Provider Base Interface

Abstract base class for all LLM providers.
Supports both regular completion and function calling.
"""

from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Dict, List, Optional

from pydantic import BaseModel, Field


class LLMMessage(BaseModel):
    """A message in an LLM conversation."""

    role: str = Field(..., description="Message role: system, user, assistant, function")
    content: str = Field(default="", description="Message content")
    name: Optional[str] = Field(default=None, description="Function name (for function messages)")

    @classmethod
    def system(cls, content: str) -> "LLMMessage":
        """Create a system message."""
        return cls(role="system", content=content)

    @classmethod
    def user(cls, content: str) -> "LLMMessage":
        """Create a user message."""
        return cls(role="user", content=content)

    @classmethod
    def assistant(cls, content: str) -> "LLMMessage":
        """Create an assistant message."""
        return cls(role="assistant", content=content)

    @classmethod
    def function(cls, name: str, content: str) -> "LLMMessage":
        """Create a function result message."""
        return cls(role="function", name=name, content=content)


class FunctionCall(BaseModel):
    """A function call from the LLM."""

    name: str = Field(..., description="Function name")
    arguments: Dict[str, Any] = Field(default_factory=dict, description="Function arguments")


class LLMResponse(BaseModel):
    """Response from an LLM completion."""

    content: str = Field(default="", description="Response text content")
    function_call: Optional[FunctionCall] = Field(
        default=None, description="Function call if the LLM chose to call a function"
    )
    model: Optional[str] = Field(default=None, description="Model used for generation")
    usage: Optional[Dict[str, Any]] = Field(default=None, description="Token usage stats")
    finish_reason: Optional[str] = Field(default=None, description="Finish reason")


class LLMProvider(ABC):
    """
    Abstract base class for LLM providers.

    All LLM providers must implement complete() and complete_with_functions().
    Providers can optionally implement stream() for streaming responses.

    Usage:
        llm = OpenAICompatProvider(base_url="...", api_key="...")
        response = await llm.complete([LLMMessage.user("Hello")])
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Name of the LLM provider."""
        pass

    @abstractmethod
    async def complete(
        self,
        messages: List[LLMMessage],
        temperature: float = None,
        max_tokens: int = None,
        **kwargs,
    ) -> LLMResponse:
        """
        Generate a completion.

        Args:
            messages: Conversation messages
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional provider-specific options

        Returns:
            LLMResponse with generated content
        """
        pass

    @abstractmethod
    async def complete_with_functions(
        self,
        messages: List[LLMMessage],
        functions: List[Dict[str, Any]],
        temperature: float = None,
        max_tokens: int = None,
        **kwargs,
    ) -> LLMResponse:
        """
        Generate a completion with function calling.

        Args:
            messages: Conversation messages
            functions: Function schemas for function calling
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional options

        Returns:
            LLMResponse with content or function_call
        """
        pass

    async def stream(
        self,
        messages: List[LLMMessage],
        temperature: float = None,
        max_tokens: int = None,
        **kwargs,
    ) -> AsyncIterator[str]:
        """
        Stream a completion.

        Default implementation falls back to non-streaming complete().

        Args:
            messages: Conversation messages
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate

        Yields:
            Text chunks
        """
        response = await self.complete(messages, temperature, max_tokens, **kwargs)
        yield response.content

    @abstractmethod
    async def health_check(self) -> bool:
        """
        Check if the provider is accessible.

        Returns:
            True if provider is healthy
        """
        pass

    @abstractmethod
    async def close(self) -> None:
        """Close any open connections."""
        pass
