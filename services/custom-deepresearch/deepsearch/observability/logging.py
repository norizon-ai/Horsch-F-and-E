"""
Structured Logging

Provides JSON-formatted structured logging with correlation IDs for request tracking.
Uses structlog for consistent, parseable log output.
"""

import logging
import sys
from typing import Optional
from contextvars import ContextVar

import structlog
from structlog.types import Processor


correlation_id_var: ContextVar[str] = ContextVar("correlation_id", default="")
user_query_var: ContextVar[str] = ContextVar("user_query", default="")


def add_correlation_context(
    logger: logging.Logger, method_name: str, event_dict: dict
) -> dict:
    """Add correlation context to log events."""
    correlation_id = correlation_id_var.get()
    if correlation_id:
        event_dict["correlation_id"] = correlation_id

    user_query = user_query_var.get()
    if user_query:
        event_dict["query_preview"] = (
            user_query[:100] + "..." if len(user_query) > 100 else user_query
        )

    return event_dict


def setup_logging(
    level: str = "INFO",
    log_format: str = "json",
    service_name: str = "deepsearch",
) -> None:
    """
    Configure structured logging for the application.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        log_format: Output format ('json' or 'console').
        service_name: Name of the service for log context.
    """
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        add_correlation_context,
    ]

    if log_format == "json":
        processors.append(structlog.processors.JSONRenderer())
    else:
        processors.append(structlog.dev.ConsoleRenderer(colors=True))

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, level.upper(), logging.INFO)
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, level.upper(), logging.INFO),
    )


def get_logger(name: str) -> structlog.BoundLogger:
    """
    Get a structured logger instance.

    Args:
        name: Logger name, typically ``__name__``.

    Returns:
        A bound structlog logger.
    """
    return structlog.get_logger(name)


def bind_context(**kwargs) -> None:
    """
    Bind key-value pairs to the structlog context.

    These will appear in all subsequent log entries within the same context.
    """
    structlog.contextvars.bind_contextvars(**kwargs)


def set_correlation_id(correlation_id: str) -> None:
    """Set the correlation ID for the current context."""
    correlation_id_var.set(correlation_id)


def set_user_query(query: str) -> None:
    """Set the user query for the current context."""
    user_query_var.set(query)


def clear_context() -> None:
    """Clear all context variables."""
    correlation_id_var.set("")
    user_query_var.set("")
    structlog.contextvars.clear_contextvars()
