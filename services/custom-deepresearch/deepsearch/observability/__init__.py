"""
Observability Module

Provides logging and tracing capabilities for the Norizon search system.
"""

from .logging import (
    setup_logging,
    get_logger,
    bind_context,
    set_correlation_id,
    set_user_query,
    clear_context,
)

from .tracing import (
    init_tracing,
    is_tracing_enabled,
    traced,
    TracingContext,
    SpanKind,
    add_span_attributes,
    add_span_event,
    set_span_error,
    get_current_span,
    flush_traces,
    shutdown_tracing,
)

__all__ = [
    # Logging
    "setup_logging",
    "get_logger",
    "bind_context",
    "set_correlation_id",
    "set_user_query",
    "clear_context",
    # Tracing
    "init_tracing",
    "is_tracing_enabled",
    "traced",
    "TracingContext",
    "SpanKind",
    "add_span_attributes",
    "add_span_event",
    "set_span_error",
    "get_current_span",
    "flush_traces",
    "shutdown_tracing",
]
