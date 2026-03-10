"""
Factory for creating model instances using the plugin system.

This module provides a factory that uses the plugin registry to create
model instances dynamically.
"""

import logging
from typing import Any, Dict, Optional

from ..plugins.registry import plugin_registry
from ..plugins.base import PluginType

logger = logging.getLogger(__name__)


class ModelFactory:
    """Factory for creating model instances using plugins."""
    
    def __init__(self):
        self._cache = {}
    
    def create_model(self, model_name: str, config: Optional[Dict[str, Any]] = None) -> Optional[Any]:
        """Create a model instance using the plugin system."""
        try:
            # Check cache first
            cache_key = f"{model_name}_{hash(str(config))}"
            if cache_key in self._cache:
                return self._cache[cache_key]
            
            # Get plugin instance
            plugin = plugin_registry.create_instance(model_name, config)
            if plugin is None:
                logger.error(f"Failed to create plugin instance for model: {model_name}")
                return None
            
            # Get the actual model from the plugin
            model = plugin.load_model()
            if model is None:
                logger.error(f"Failed to load model from plugin: {model_name}")
                return None
            
            # Cache the result
            self._cache[cache_key] = model
            logger.info(f"Created model instance: {model_name}")
            return model
            
        except Exception as e:
            logger.error(f"Error creating model {model_name}: {e}")
            return None
    
    def get_available_models(self) -> list:
        """Get list of available model plugins."""
        return plugin_registry.get_available_plugins(PluginType.MODEL)
    
    def get_model_metadata(self, model_name: str) -> Optional[Any]:
        """Get metadata for a model plugin."""
        return plugin_registry.get_plugin_metadata(model_name)
    
    def validate_model(self, model_name: str) -> bool:
        """Validate that a model plugin is available."""
        return plugin_registry.validate_plugin(model_name)
    
    def clear_cache(self):
        """Clear the model cache."""
        self._cache.clear()
        logger.info("Model factory cache cleared")


# Global model factory instance
model_factory = ModelFactory() 