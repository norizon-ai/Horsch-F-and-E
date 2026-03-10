"""Deep Research module."""

from .client import DRClient, DRResult, check_dr_connection
from .integration import run_research, run_search

__all__ = [
    "DRClient",
    "DRResult",
    "check_dr_connection",
    "run_research",
    "run_search",
]