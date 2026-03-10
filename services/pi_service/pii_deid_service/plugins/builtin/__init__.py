"""
Built-in plugins for the PII de-identification service.

This module provides plugin wrappers for the existing components,
making them available through the plugin system.
"""

from .models import FlairModelPlugin, SpacyModelPlugin
from .recognizer_plugins import PresidioRecognizerPlugin
from .operators import PresidioOperatorPlugin, EntitySanitizerOperatorPlugin

__all__ = [
    'FlairModelPlugin',
    'SpacyModelPlugin', 
    'PresidioRecognizerPlugin',
    'PresidioOperatorPlugin',
    'EntitySanitizerOperatorPlugin'
] 