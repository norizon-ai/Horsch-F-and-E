"""
OpenTelemetry Tracing Module

Provides distributed tracing with Phoenix as the trace consumer.
Integrates with existing structlog correlation IDs.

Usage:
    from deepsearch.observability import init_tracing, traced, TracingContext

    # Initialize at startup
    init_tracing(service_name="deepsearch")

    # Decorator for functions
    @traced("supervisor.search", record_args=["query"])
    async def search(self, query: str) -> DRResult:
        ...

    # Context manager for manual spans
    async with TracingContext("llm.complete", attributes={"model": model}) as span:
        span.set_attribute("tokens", token_count)
        result = await client.post(...)
"""

from __future__ import annotations
import functools
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union
from contextvars import ContextVar

# Type variables for decorator
F = TypeVar("F", bound=Callable[..., Any])

# Module state
_tracer = None
_tracing_enabled = False
_provider = None  # Keep reference to flush on shutdown

# Context variable for tracking span context in async code
_span_context_var: ContextVar[Optional[Any]] = ContextVar("span_context", default=None)


def init_tracing(service_name: str = "deepsearch") -> bool:
    """
    Initialize OpenTelemetry tracing with Phoenix exporter.

    Args:
        service_name: Service name for trace identification

    Returns:
        True if tracing was initialized, False otherwise
    """
    global _tracer, _tracing_enabled, _provider

    from deepsearch.config import get_config

    config = get_config()
    if not config.enable_tracing:
        return False

    try:
        from opentelemetry import trace
        from opentelemetry.sdk.trace import TracerProvider
        from opentelemetry.sdk.trace.export import BatchSpanProcessor, SimpleSpanProcessor
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.resources import Resource, SERVICE_NAME

        # Create resource with service name
        resource = Resource.create({SERVICE_NAME: service_name})

        # Create tracer provider
        provider = TracerProvider(resource=resource)

        # Configure Phoenix OTLP exporter
        exporter = OTLPSpanExporter(endpoint=config.phoenix_endpoint)

        # Use SimpleSpanProcessor for immediate export (dev/debug)
        # Use BatchSpanProcessor for production (better performance)
        if config.trace_immediate_export:
            processor = SimpleSpanProcessor(exporter)
        else:
            processor = BatchSpanProcessor(
                exporter,
                schedule_delay_millis=1000,  # Export every 1 second
                max_export_batch_size=64,
            )
        provider.add_span_processor(processor)

        # Set as global provider
        trace.set_tracer_provider(provider)

        _tracer = trace.get_tracer(__name__, "1.0.0")
        _tracing_enabled = True
        _provider = provider  # Keep reference for flushing

        return True

    except ImportError as e:
        # OpenTelemetry packages not installed
        from deepsearch.observability.logging import get_logger
        logger = get_logger(__name__)
        logger.warning("tracing_init_failed", reason="missing_dependencies", error=str(e))
        return False
    except Exception as e:
        from deepsearch.observability.logging import get_logger
        logger = get_logger(__name__)
        logger.error("tracing_init_failed", error=str(e))
        return False


def get_tracer():
    """Get the OpenTelemetry tracer instance."""
    return _tracer


def flush_traces(timeout_millis: int = 5000) -> bool:
    """
    Force flush all pending traces to the exporter.

    Call this before shutdown to ensure all spans are exported.

    Args:
        timeout_millis: Maximum time to wait for flush

    Returns:
        True if flush succeeded
    """
    if _provider is not None:
        return _provider.force_flush(timeout_millis)
    return False


def shutdown_tracing() -> None:
    """Shutdown tracing and flush remaining spans."""
    global _provider, _tracing_enabled
    if _provider is not None:
        _provider.shutdown()
        _provider = None
        _tracing_enabled = False


def is_tracing_enabled() -> bool:
    """Check if tracing is enabled and initialized."""
    return _tracing_enabled and _tracer is not None


def get_current_span():
    """Get the current active span."""
    if not is_tracing_enabled():
        return None
    from opentelemetry import trace
    return trace.get_current_span()


class SpanKind:
    """Span kind constants."""
    INTERNAL = "internal"
    SERVER = "server"
    CLIENT = "client"


def _map_span_kind(kind: str):
    """Map string span kind to OpenTelemetry SpanKind."""
    if not is_tracing_enabled():
        return None

    from opentelemetry.trace import SpanKind as OTelSpanKind

    mapping = {
        SpanKind.INTERNAL: OTelSpanKind.INTERNAL,
        SpanKind.SERVER: OTelSpanKind.SERVER,
        SpanKind.CLIENT: OTelSpanKind.CLIENT,
    }
    return mapping.get(kind, OTelSpanKind.INTERNAL)


def _safe_attribute_value(value: Any) -> Union[str, int, float, bool, List]:
    """Convert value to a safe span attribute value."""
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, (list, tuple)):
        # Limit list size and convert items
        return [_safe_attribute_value(v) for v in list(value)[:10]]
    if isinstance(value, dict):
        # Convert dict to truncated string
        return str(value)[:1000]
    # Default: convert to truncated string
    return str(value)[:1000]


def _get_correlation_id() -> Optional[str]:
    """Get correlation ID from logging context if available."""
    try:
        from deepsearch.observability.logging import correlation_id_var
        return correlation_id_var.get()
    except Exception:
        return None


def traced(
    span_name: Optional[str] = None,
    span_kind: str = SpanKind.INTERNAL,
    attributes: Optional[Dict[str, Any]] = None,
    record_args: Optional[List[str]] = None,
):
    """
    Decorator for tracing synchronous and async functions.

    Args:
        span_name: Custom span name (defaults to function name)
        span_kind: Span kind (internal, server, client)
        attributes: Static attributes to add to span
        record_args: List of argument names to record as span attributes

    Example:
        @traced("supervisor.search", record_args=["query"])
        async def search(self, query: str) -> DRResult:
            ...
    """
    def decorator(func: F) -> F:
        name = span_name or f"{func.__module__}.{func.__qualname__}"

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            if not is_tracing_enabled():
                return await func(*args, **kwargs)

            from opentelemetry import trace
            from opentelemetry.trace import Status, StatusCode

            tracer = get_tracer()
            span_attrs = dict(attributes or {})

            # Record specified arguments
            if record_args:
                for arg_name in record_args:
                    if arg_name in kwargs:
                        value = kwargs[arg_name]
                        span_attrs[f"input.{arg_name}"] = _safe_attribute_value(value)

            # Link to correlation ID if available
            correlation_id = _get_correlation_id()
            if correlation_id:
                span_attrs["correlation_id"] = correlation_id

            with tracer.start_as_current_span(name, kind=_map_span_kind(span_kind)) as span:
                # Add attributes
                for key, value in span_attrs.items():
                    span.set_attribute(key, _safe_attribute_value(value))

                try:
                    result = await func(*args, **kwargs)
                    span.set_status(Status(StatusCode.OK))
                    return result
                except Exception as e:
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    span.record_exception(e)
                    raise

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            if not is_tracing_enabled():
                return func(*args, **kwargs)

            from opentelemetry import trace
            from opentelemetry.trace import Status, StatusCode

            tracer = get_tracer()
            span_attrs = dict(attributes or {})

            if record_args:
                for arg_name in record_args:
                    if arg_name in kwargs:
                        value = kwargs[arg_name]
                        span_attrs[f"input.{arg_name}"] = _safe_attribute_value(value)

            correlation_id = _get_correlation_id()
            if correlation_id:
                span_attrs["correlation_id"] = correlation_id

            with tracer.start_as_current_span(name, kind=_map_span_kind(span_kind)) as span:
                for key, value in span_attrs.items():
                    span.set_attribute(key, _safe_attribute_value(value))

                try:
                    result = func(*args, **kwargs)
                    span.set_status(Status(StatusCode.OK))
                    return result
                except Exception as e:
                    span.set_status(Status(StatusCode.ERROR, str(e)))
                    span.record_exception(e)
                    raise

        import asyncio
        if asyncio.iscoroutinefunction(func):
            return async_wrapper  # type: ignore
        return sync_wrapper  # type: ignore

    return decorator


class _NoOpSpan:
    """No-op span for when tracing is disabled."""

    def set_attribute(self, key: str, value: Any) -> None:
        pass

    def add_event(self, name: str, attributes: Optional[Dict] = None) -> None:
        pass

    def set_status(self, status: Any) -> None:
        pass

    def record_exception(self, exception: Exception) -> None:
        pass

    def end(self) -> None:
        pass


class TracingContext:
    """
    Context manager for manual span creation with proper parent-child relationships.

    Uses tracer.start_as_current_span() internally to ensure spans are properly
    nested in the trace hierarchy.

    Example:
        async with TracingContext("llm.complete", attributes={"model": model}) as span:
            span.set_attribute("tokens.prompt", prompt_tokens)
            result = await client.post(...)
            span.set_attribute("tokens.completion", completion_tokens)
    """

    def __init__(
        self,
        name: str,
        span_kind: str = SpanKind.INTERNAL,
        attributes: Optional[Dict[str, Any]] = None,
    ):
        self.name = name
        self.span_kind = span_kind
        self.attributes = attributes or {}
        self._span = None
        self._cm = None  # Context manager from start_as_current_span

    def _enter(self):
        """Enter the span context."""
        from deepsearch.observability.logging import get_logger
        _logger = get_logger(__name__)

        # Always log to verify this code is reached
        _logger.info("tracing_context_enter", span_name=self.name, tracing_enabled=is_tracing_enabled())

        if not is_tracing_enabled():
            return _NoOpSpan()

        from opentelemetry.trace import Status, StatusCode

        tracer = get_tracer()

        # Use start_as_current_span which properly handles parent-child relationships
        self._cm = tracer.start_as_current_span(
            self.name,
            kind=_map_span_kind(self.span_kind)
        )
        self._span = self._cm.__enter__()

        # Set attributes
        for key, value in self.attributes.items():
            self._span.set_attribute(key, _safe_attribute_value(value))

        # Link to correlation ID
        correlation_id = _get_correlation_id()
        if correlation_id:
            self._span.set_attribute("correlation_id", correlation_id)

        return self._span

    def _exit(self, exc_type, exc_val, exc_tb):
        """Exit the span context."""
        if self._cm is None:
            return

        from opentelemetry.trace import Status, StatusCode

        # Set status based on exception
        if exc_val is not None:
            self._span.set_status(Status(StatusCode.ERROR, str(exc_val)))
            self._span.record_exception(exc_val)
        else:
            self._span.set_status(Status(StatusCode.OK))

        # Exit the context manager (this ends the span and restores context)
        self._cm.__exit__(exc_type, exc_val, exc_tb)

    async def __aenter__(self):
        return self._enter()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._exit(exc_type, exc_val, exc_tb)

    def __enter__(self):
        return self._enter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._exit(exc_type, exc_val, exc_tb)


def add_span_attributes(**kwargs) -> None:
    """
    Add attributes to the current span.

    Args:
        **kwargs: Key-value pairs to add as span attributes

    Example:
        add_span_attributes(
            output_confidence=0.85,
            output_sources_count=5,
        )
    """
    if not is_tracing_enabled():
        return

    from opentelemetry import trace

    span = trace.get_current_span()
    if span and span.is_recording():
        for key, value in kwargs.items():
            span.set_attribute(key, _safe_attribute_value(value))


def add_span_event(name: str, attributes: Optional[Dict[str, Any]] = None) -> None:
    """
    Add an event to the current span.

    Args:
        name: Event name
        attributes: Event attributes

    Example:
        add_span_event("quality_check_complete", {"score": 4, "decision": "COMPLETE"})
    """
    if not is_tracing_enabled():
        return

    from opentelemetry import trace

    span = trace.get_current_span()
    if span and span.is_recording():
        safe_attrs = {k: _safe_attribute_value(v) for k, v in (attributes or {}).items()}
        span.add_event(name, attributes=safe_attrs)


def set_span_error(error: Exception) -> None:
    """
    Mark the current span as errored.

    Args:
        error: The exception that occurred
    """
    if not is_tracing_enabled():
        return

    from opentelemetry import trace
    from opentelemetry.trace import Status, StatusCode

    span = trace.get_current_span()
    if span and span.is_recording():
        span.set_status(Status(StatusCode.ERROR, str(error)))
        span.record_exception(error)
