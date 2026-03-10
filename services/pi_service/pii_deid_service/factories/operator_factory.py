"""
Factory for creating operator instances using the plugin system.

This module provides a factory that uses the plugin registry to create
operator instances dynamically.
"""

import logging
from typing import Any, Dict, Optional

from ..plugins.registry import plugin_registry
from ..plugins.base import PluginType

logger = logging.getLogger(__name__)


class OperatorFactory:
    """Factory for creating operator instances using plugins."""
    
    def __init__(self):
        self._cache = {}
    
    def create_operator(self, operator_name: str, config: Optional[Dict[str, Any]] = None) -> Optional[Any]:
        """Create an operator instance using the plugin system."""
        try:
            # Check cache first
            cache_key = f"{operator_name}_{hash(str(config))}"
            if cache_key in self._cache:
                return self._cache[cache_key]
            
            # Get plugin instance
            plugin = plugin_registry.create_instance(operator_name, config)
            if plugin is None:
                logger.error(f"Failed to create plugin instance for operator: {operator_name}")
                return None
            
            # Get the actual operator from the plugin
            operator = plugin.create_operator()
            if operator is None:
                logger.error(f"Failed to create operator from plugin: {operator_name}")
                return None
            
            # Cache the result
            self._cache[cache_key] = operator
            logger.info(f"Created operator instance: {operator_name}")
            return operator
            
        except Exception as e:
            logger.error(f"Error creating operator {operator_name}: {e}")
            return None
    
    def get_available_operators(self) -> list:
        """Get list of available operator plugins."""
        return plugin_registry.get_available_plugins(PluginType.OPERATOR)
    
    def get_operator_metadata(self, operator_name: str) -> Optional[Any]:
        """Get metadata for an operator plugin."""
        return plugin_registry.get_plugin_metadata(operator_name)
    
    def validate_operator(self, operator_name: str) -> bool:
        """Validate that an operator plugin is available."""
        return plugin_registry.validate_plugin(operator_name)
    
    def clear_cache(self):
        """Clear the operator cache."""
        self._cache.clear()
        logger.info("Operator factory cache cleared")


# Global operator factory instance
operator_factory = OperatorFactory() 