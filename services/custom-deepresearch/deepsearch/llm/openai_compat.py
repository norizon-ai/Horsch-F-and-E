"""
OpenAI-Compatible LLM Provider

Supports any OpenAI-compatible API including:
- OpenAI
- GPT-OSS (with channel tag cleanup)
- Anthropic (via litellm or OpenAI proxy)
- Ollama
- vLLM
- Any OpenAI-compatible endpoint
"""

import json
import re
from typing import Any, AsyncIterator, Dict, List, Optional

import httpx

from deepsearch.observability import (
    get_logger,
    TracingContext,
    SpanKind,
    add_span_event,
)
from .base import LLMProvider, LLMMessage, LLMResponse, FunctionCall

logger = get_logger(__name__)


class ResponseProcessor:
    """
    Process LLM responses to clean up provider-specific artifacts.

    GPT-OSS in particular adds channel tags that need to be stripped.
    """

    # GPT-OSS channel tags to remove
    CHANNEL_TAG_PATTERNS = [
        r"<\|channel\|>.*?<\|message\|>",
        r"<\|channel\|>final<\|message\|>",
        r"<\|channel\|>",
        r"<\|message\|>",
        r"<\|end\|>",
        r"<\|start\|>",
    ]

    @classmethod
    def clean_response(cls, text: str, provider: str = "openai") -> str:
        """
        Clean response text from provider-specific artifacts.

        Args:
            text: Raw response text
            provider: Provider name for provider-specific cleaning

        Returns:
            Cleaned text
        """
        if not text:
            return ""

        cleaned = text

        # GPT-OSS specific cleanup
        if provider in ("gpt-oss", "gpt_oss"):
            # Extract content after final message tag if present
            if "<|channel|>final<|message|>" in cleaned:
                cleaned = cleaned.split("<|channel|>final<|message|>")[-1]

            # Remove all channel tags
            for pattern in cls.CHANNEL_TAG_PATTERNS:
                cleaned = re.sub(pattern, "", cleaned, flags=re.DOTALL)

        return cleaned.strip()


class OpenAICompatProvider(LLMProvider):
    """
    LLM provider for OpenAI-compatible APIs.

    Works with OpenAI, GPT-OSS, Ollama, vLLM, and other compatible endpoints.
    Handles provider-specific quirks like GPT-OSS channel tags.
    """

    def __init__(
        self,
        base_url: str,
        api_key: str = "dummy",
        model: str = "gpt-4",
        provider_type: str = "openai",
        timeout: int = 60,
        default_temperature: float = 0.2,
        default_max_tokens: int = 2000,
    ):
        """
        Initialize the provider.

        Args:
            base_url: API base URL (e.g., "https://api.openai.com/v1")
            api_key: API key for authentication
            model: Default model to use
            provider_type: Provider type for response processing ("openai", "gpt-oss", etc.)
            timeout: Request timeout in seconds
            default_temperature: Default sampling temperature
            default_max_tokens: Default max tokens
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model = model
        self.provider_type = provider_type
        self.timeout = timeout
        self.default_temperature = default_temperature
        self.default_max_tokens = default_max_tokens

        # HTTP client with connection pooling
        self._client: Optional[httpx.AsyncClient] = None

    @property
    def provider_name(self) -> str:
        return self.provider_type

    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create HTTP client."""
        if self._client is None:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                timeout=httpx.Timeout(self.timeout),
            )
        return self._client

    async def close(self) -> None:
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
            self._client = None

    async def health_check(self) -> bool:
        """
        Check if the provider is accessible.

        Just checks if the API is reachable by hitting /models endpoint.
        No token generation needed.

        Returns:
            True if provider is healthy
        """
        try:
            client = await self._get_client()
            response = await client.get("/models")
            return response.status_code in (200, 401, 403)  # API is reachable
        except Exception:
            return False

    def _messages_to_dict(self, messages: List[LLMMessage]) -> List[Dict[str, Any]]:
        """Convert LLMMessage list to API format."""
        result = []
        for msg in messages:
            d = {"role": msg.role, "content": msg.content}
            if msg.name:
                d["name"] = msg.name
            result.append(d)
        return result

    async def complete(
        self,
        messages: List[LLMMessage],
        temperature: float = None,
        max_tokens: int = None,
        **kwargs,
    ) -> LLMResponse:
        """Generate a completion."""
        async with TracingContext(
            "llm.complete",
            span_kind=SpanKind.CLIENT,
            attributes={
                # OpenInference semantic conventions for Phoenix LLM icon
                "openinference.span.kind": "LLM",
                "llm.model_name": kwargs.get("model", self.model),
                "llm.provider": self.provider_type,
                "llm.model": kwargs.get("model", self.model),
                "llm.temperature": (
                    temperature if temperature is not None else self.default_temperature
                ),
                "llm.max_tokens": (
                    max_tokens if max_tokens is not None else self.default_max_tokens
                ),
                "input.message_count": len(messages),
            },
        ) as span:
            client = await self._get_client()

            payload = {
                "model": kwargs.get("model", self.model),
                "messages": self._messages_to_dict(messages),
                "temperature": (
                    temperature if temperature is not None else self.default_temperature
                ),
                "max_tokens": (
                    max_tokens if max_tokens is not None else self.default_max_tokens
                ),
            }

            # Detailed input logging for prompt tuning
            # Extract system prompt for easy visibility
            system_prompt = next(
                (m.content for m in messages if m.role == "system"), None
            )

            # OpenInference semantic convention attributes for Phoenix Info tab
            # Use indexed format: llm.input_messages.{i}.message.role/content
            from openinference.semconv.trace import SpanAttributes, OpenInferenceSpanKindValues
            span.set_attribute(SpanAttributes.OPENINFERENCE_SPAN_KIND, OpenInferenceSpanKindValues.LLM.value)

            for i, m in enumerate(messages):
                span.set_attribute(f"llm.input_messages.{i}.message.role", m.role)
                span.set_attribute(f"llm.input_messages.{i}.message.content", m.content[:4000])

            logger.info(
                "llm_input",
                provider=self.provider_type,
                model=payload["model"],
                temperature=payload["temperature"],
                max_tokens=payload["max_tokens"],
                system_prompt=system_prompt,
                messages=[{"role": m.role, "content": m.content} for m in messages],
            )

            try:
                response = await client.post("/chat/completions", json=payload)
                response.raise_for_status()
                data = response.json()

                choice = data["choices"][0]
                content = choice.get("message", {}).get("content", "")

                # Clean response
                cleaned_content = ResponseProcessor.clean_response(
                    content, self.provider_type
                )

                # Add output attributes to span
                span.set_attribute("output.content_length", len(cleaned_content))
                span.set_attribute(
                    "output.finish_reason", choice.get("finish_reason", "")
                )
                if data.get("usage"):
                    span.set_attribute(
                        "usage.prompt_tokens", data["usage"].get("prompt_tokens", 0)
                    )
                    span.set_attribute(
                        "usage.completion_tokens",
                        data["usage"].get("completion_tokens", 0),
                    )
                    span.set_attribute(
                        "usage.total_tokens", data["usage"].get("total_tokens", 0)
                    )

                # OpenInference semantic convention for Phoenix Info tab
                span.set_attribute("llm.output_messages.0.message.role", "assistant")
                span.set_attribute("llm.output_messages.0.message.content", cleaned_content[:4000] if cleaned_content else "")

                # Detailed output logging for prompt tuning
                logger.info(
                    "llm_output",
                    provider=self.provider_type,
                    model=data.get("model", self.model),
                    content=cleaned_content,
                    finish_reason=choice.get("finish_reason"),
                    usage=data.get("usage"),
                )

                return LLMResponse(
                    content=cleaned_content,
                    model=data.get("model", self.model),
                    usage=data.get("usage"),
                    finish_reason=choice.get("finish_reason"),
                )

            except httpx.HTTPStatusError as e:
                span.set_attribute("error.type", "http_error")
                span.set_attribute("error.status_code", e.response.status_code)
                logger.error(
                    "llm_http_error", status=e.response.status_code, detail=str(e)
                )
                raise
            except Exception as e:
                span.set_attribute("error.type", type(e).__name__)
                logger.error("llm_error", error=str(e), error_type=type(e).__name__)
                raise

    async def complete_streaming(
        self,
        messages: List[LLMMessage],
        temperature: float = None,
        max_tokens: int = None,
        **kwargs,
    ) -> AsyncIterator[str]:
        """
        Stream completion text chunks.

        Args:
            messages: List of messages in the conversation
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional options

        Yields:
            Text content chunks as they arrive
        """
        client = await self._get_client()

        payload = {
            "model": kwargs.get("model", self.model),
            "messages": self._messages_to_dict(messages),
            "temperature": (
                temperature if temperature is not None else self.default_temperature
            ),
            "max_tokens": (
                max_tokens if max_tokens is not None else self.default_max_tokens
            ),
            "stream": True,
        }

        logger.info(
            "llm_streaming_start",
            provider=self.provider_type,
            model=payload["model"],
        )

        chunk_count = 0
        total_chars = 0
        try:
            # Use longer timeout for streaming
            async with client.stream(
                "POST",
                "/chat/completions",
                json=payload,
                timeout=httpx.Timeout(120.0, connect=30.0),
            ) as response:
                logger.info(
                    "llm_streaming_response",
                    status=response.status_code,
                    headers=dict(response.headers),
                )
                response.raise_for_status()

                buffer = ""
                async for raw_chunk in response.aiter_text():
                    buffer += raw_chunk
                    # Process complete lines
                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        line = line.strip()
                        if not line:
                            continue

                        # Handle SSE data lines
                        if line.startswith("data:"):
                            data_str = line[5:].strip()
                            if data_str == "[DONE]":
                                logger.info("llm_streaming_done", chunks=chunk_count, total_chars=total_chars)
                                return

                            try:
                                data = json.loads(data_str)
                                choices = data.get("choices", [])
                                if choices:
                                    delta = choices[0].get("delta", {})
                                    content = delta.get("content", "")
                                    if content:
                                        chunk_count += 1
                                        total_chars += len(content)
                                        logger.debug("llm_chunk_yielded", chunk=chunk_count, length=len(content))
                                        yield content
                            except json.JSONDecodeError as e:
                                logger.warning("llm_streaming_json_error", error=str(e), data=data_str[:200])
                                continue
                            except (KeyError, IndexError) as e:
                                logger.warning("llm_streaming_structure_error", error=str(e), data=data_str[:200])
                                continue

                # Stream ended without [DONE]
                logger.info("llm_streaming_ended_no_done", chunks=chunk_count, total_chars=total_chars)
        except httpx.HTTPStatusError as e:
            logger.error("llm_streaming_http_error", status=e.response.status_code, error=str(e))
            raise
        except Exception as e:
            import traceback
            logger.error("llm_streaming_error", error=str(e), traceback=traceback.format_exc(), chunks_so_far=chunk_count)
            raise

    async def complete_with_functions(
        self,
        messages: List[LLMMessage],
        functions: List[Dict[str, Any]],
        temperature: float = None,
        max_tokens: int = None,
        function_call: str = "auto",
        **kwargs,
    ) -> LLMResponse:
        """Generate a completion with function calling."""
        async with TracingContext(
            "llm.complete_with_functions",
            span_kind=SpanKind.CLIENT,
            attributes={
                # OpenInference semantic conventions for Phoenix LLM icon
                "openinference.span.kind": "LLM",
                "llm.model_name": kwargs.get("model", self.model),
                "llm.provider": self.provider_type,
                "llm.model": kwargs.get("model", self.model),
                "llm.temperature": (
                    temperature if temperature is not None else self.default_temperature
                ),
                "llm.max_tokens": (
                    max_tokens if max_tokens is not None else self.default_max_tokens
                ),
                "input.message_count": len(messages),
                "input.function_count": len(functions) if functions else 0,
            },
        ) as span:
            client = await self._get_client()

            # Convert to tools format (newer API)
            tools = functions if functions else None

            payload = {
                "model": kwargs.get("model", self.model),
                "messages": self._messages_to_dict(messages),
                "temperature": (
                    temperature if temperature is not None else self.default_temperature
                ),
                "max_tokens": (
                    max_tokens if max_tokens is not None else self.default_max_tokens
                ),
            }

            if tools:
                payload["tools"] = tools
                if function_call != "auto":
                    payload["tool_choice"] = function_call

            # Detailed input logging for prompt tuning (with functions)
            # Extract system prompt for easy visibility
            system_prompt = next(
                (m.content for m in messages if m.role == "system"), None
            )
            function_names = (
                [t.get("function", {}).get("name") for t in tools] if tools else []
            )

            # OpenInference semantic convention attributes for Phoenix Info tab
            from openinference.semconv.trace import SpanAttributes, OpenInferenceSpanKindValues
            span.set_attribute(SpanAttributes.OPENINFERENCE_SPAN_KIND, OpenInferenceSpanKindValues.LLM.value)

            # Use indexed format for messages
            for i, m in enumerate(messages):
                span.set_attribute(f"llm.input_messages.{i}.message.role", m.role)
                span.set_attribute(f"llm.input_messages.{i}.message.content", m.content[:4000])

            # Add function/tool info
            span.set_attribute("input.function_names", str(function_names))
            span.set_attribute("input.function_count", len(function_names))

            logger.info(
                "llm_input_with_functions",
                provider=self.provider_type,
                model=payload["model"],
                temperature=payload["temperature"],
                max_tokens=payload["max_tokens"],
                system_prompt=system_prompt,
                messages=[{"role": m.role, "content": m.content} for m in messages],
                functions=function_names,
                function_schemas=tools,
            )

            try:
                response = await client.post("/chat/completions", json=payload)
                response.raise_for_status()
                data = response.json()

                choice = data["choices"][0]
                message = choice.get("message", {})
                content = message.get("content", "") or ""

                # Clean content
                cleaned_content = ResponseProcessor.clean_response(
                    content, self.provider_type
                )

                # Check for function/tool call
                function_call_result = None

                # Handle tool_calls (newer format)
                tool_calls = message.get("tool_calls", [])
                if tool_calls:
                    tc = tool_calls[0]
                    func = tc.get("function", {})
                    try:
                        args = json.loads(func.get("arguments", "{}"))
                    except json.JSONDecodeError:
                        args = {}
                    function_call_result = FunctionCall(
                        name=func.get("name", ""),
                        arguments=args,
                    )

                # Handle function_call (older format)
                elif "function_call" in message:
                    fc = message["function_call"]
                    try:
                        args = json.loads(fc.get("arguments", "{}"))
                    except json.JSONDecodeError:
                        args = {}
                    function_call_result = FunctionCall(
                        name=fc.get("name", ""),
                        arguments=args,
                    )

                # Add output attributes to span
                span.set_attribute(
                    "output.has_function_call", function_call_result is not None
                )
                if function_call_result:
                    span.set_attribute(
                        "output.function_name", function_call_result.name
                    )
                span.set_attribute("output.content_length", len(cleaned_content))
                if data.get("usage"):
                    span.set_attribute(
                        "usage.prompt_tokens", data["usage"].get("prompt_tokens", 0)
                    )
                    span.set_attribute(
                        "usage.completion_tokens",
                        data["usage"].get("completion_tokens", 0),
                    )
                    span.set_attribute(
                        "usage.total_tokens", data["usage"].get("total_tokens", 0)
                    )

                # OpenInference semantic convention for Phoenix Info tab
                output_content = cleaned_content or ""
                if function_call_result:
                    output_content = f"Function call: {function_call_result.name}({function_call_result.arguments})"

                span.set_attribute("llm.output_messages.0.message.role", "assistant")
                span.set_attribute("llm.output_messages.0.message.content", output_content[:4000])

                # Add tool call info if present
                if function_call_result:
                    span.set_attribute("llm.output_messages.0.message.tool_calls.0.tool_call.function.name", function_call_result.name)
                    span.set_attribute("llm.output_messages.0.message.tool_calls.0.tool_call.function.arguments", str(function_call_result.arguments))

                # Detailed output logging for prompt tuning (with functions)
                logger.info(
                    "llm_output_with_functions",
                    provider=self.provider_type,
                    model=data.get("model", self.model),
                    content=cleaned_content if cleaned_content else None,
                    function_call=(
                        {
                            "name": function_call_result.name,
                            "arguments": function_call_result.arguments,
                        }
                        if function_call_result
                        else None
                    ),
                    finish_reason=choice.get("finish_reason"),
                    usage=data.get("usage"),
                )

                return LLMResponse(
                    content=cleaned_content,
                    function_call=function_call_result,
                    model=data.get("model", self.model),
                    usage=data.get("usage"),
                    finish_reason=choice.get("finish_reason"),
                )

            except httpx.HTTPStatusError as e:
                span.set_attribute("error.type", "http_error")
                span.set_attribute("error.status_code", e.response.status_code)
                logger.error("llm_function_http_error", status=e.response.status_code)
                raise
            except Exception as e:
                span.set_attribute("error.type", type(e).__name__)
                logger.error("llm_function_error", error=str(e))
                raise

    async def stream(
        self,
        messages: List[LLMMessage],
        temperature: float = None,
        max_tokens: int = None,
        **kwargs,
    ) -> AsyncIterator[str]:
        """Stream a completion."""
        client = await self._get_client()

        payload = {
            "model": kwargs.get("model", self.model),
            "messages": self._messages_to_dict(messages),
            "temperature": (
                temperature if temperature is not None else self.default_temperature
            ),
            "max_tokens": (
                max_tokens if max_tokens is not None else self.default_max_tokens
            ),
            "stream": True,
        }

        try:
            async with client.stream(
                "POST", "/chat/completions", json=payload
            ) as response:
                response.raise_for_status()
                async for line in response.aiter_lines():
                    if line.startswith("data: "):
                        data_str = line[6:]
                        if data_str.strip() == "[DONE]":
                            break
                        try:
                            data = json.loads(data_str)
                            delta = data["choices"][0].get("delta", {})
                            content = delta.get("content", "")
                            if content:
                                # Clean streaming content too
                                cleaned = ResponseProcessor.clean_response(
                                    content, self.provider_type
                                )
                                if cleaned:
                                    yield cleaned
                        except json.JSONDecodeError:
                            continue

        except Exception as e:
            logger.error("llm_stream_error", error=str(e))
            raise


def create_llm_provider(
    provider_type: str,
    base_url: str,
    api_key: str,
    model: str,
    **kwargs,
) -> LLMProvider:
    """
    Factory function to create an LLM provider.

    Args:
        provider_type: Provider type ("openai", "gpt-oss", "anthropic", "ollama")
        base_url: API base URL
        api_key: API key
        model: Model name
        **kwargs: Additional provider options

    Returns:
        LLMProvider instance
    """
    return OpenAICompatProvider(
        base_url=base_url,
        api_key=api_key,
        model=model,
        provider_type=provider_type,
        **kwargs,
    )
