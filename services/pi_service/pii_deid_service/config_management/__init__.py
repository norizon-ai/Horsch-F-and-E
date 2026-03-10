"""
Configuration management module for PII De-identification Service.

This module provides configuration schemas and management for the plugin-based system.
"""

from .plugin_schemas import PluginPipelineConfig, PluginComponentConfig
from .config_manager import config_manager

__all__ = [
    "PluginPipelineConfig",
    "PluginComponentConfig",
    "config_manager"
] 