"""
Factory for creating recognizer instances using the plugin system.

This module provides a factory that uses the plugin registry to create
recognizer instances dynamically.
"""

import logging
from typing import Any, Dict, Optional

from ..plugins.registry import plugin_registry
from ..plugins.base import PluginType

logger = logging.getLogger(__name__)


class RecognizerFactory:
    """Factory for creating recognizer instances using plugins."""
    
    def __init__(self):
        self._cache = {}
    
    def create_recognizer(self, recognizer_name: str, config: Optional[Dict[str, Any]] = None) -> Optional[Any]:
        """Create a recognizer instance using the plugin system."""
        try:
            # Check cache first
            cache_key = f"{recognizer_name}_{hash(str(config))}"
            if cache_key in self._cache:
                return self._cache[cache_key]
            
            # Get plugin instance
            plugin = plugin_registry.create_instance(recognizer_name, config)
            if plugin is None:
                logger.error(f"Failed to create plugin instance for recognizer: {recognizer_name}")
                return None
            
            # Get the actual recognizer from the plugin
            recognizer = plugin.create_recognizer()
            if recognizer is None:
                logger.error(f"Failed to create recognizer from plugin: {recognizer_name}")
                return None
            
            # Cache the result
            self._cache[cache_key] = recognizer
            logger.info(f"Created recognizer instance: {recognizer_name}")
            return recognizer
            
        except Exception as e:
            logger.error(f"Error creating recognizer {recognizer_name}: {e}")
            return None
    
    def get_available_recognizers(self) -> list:
        """Get list of available recognizer plugins."""
        return plugin_registry.get_available_plugins(PluginType.RECOGNIZER)
    
    def get_recognizer_metadata(self, recognizer_name: str) -> Optional[Any]:
        """Get metadata for a recognizer plugin."""
        return plugin_registry.get_plugin_metadata(recognizer_name)
    
    def validate_recognizer(self, recognizer_name: str) -> bool:
        """Validate that a recognizer plugin is available."""
        return plugin_registry.validate_plugin(recognizer_name)
    
    def clear_cache(self):
        """Clear the recognizer cache."""
        self._cache.clear()
        logger.info("Recognizer factory cache cleared")


# Global recognizer factory instance
recognizer_factory = RecognizerFactory() 