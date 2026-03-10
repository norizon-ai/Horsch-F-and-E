"""
Plugin system for PII de-identification service.

This module provides a plugin architecture that allows easy addition of new
models, recognizers, and operators without modifying core code.
"""

from .registry import PluginRegistry, plugin_registry
from .base import BasePlugin, ModelPlugin, RecognizerPlugin, OperatorPlugin
from .loader import PluginLoader
from .manager import PluginManager, plugin_manager

__all__ = [
    'PluginRegistry',
    'plugin_registry',
    'BasePlugin', 
    'ModelPlugin',
    'RecognizerPlugin',
    'OperatorPlugin',
    'PluginLoader',
    'PluginManager',
    'plugin_manager'
] 