"""
Plugin registry for managing and discovering plugins.

This module provides a centralized registry for all plugins in the system,
enabling dynamic discovery and instantiation of plugins.
"""

import logging
from typing import Any, Dict, List, Optional, Type, Union
from collections import defaultdict

from .base import BasePlugin, ModelPlugin, RecognizerPlugin, OperatorPlugin, PluginType, PluginMetadata

logger = logging.getLogger(__name__)


class PluginRegistry:
    """Central registry for managing plugins."""
    
    def __init__(self):
        self._plugins: Dict[PluginType, Dict[str, Type[BasePlugin]]] = defaultdict(dict)
        self._instances: Dict[str, BasePlugin] = {}
        self._metadata: Dict[str, PluginMetadata] = {}
    
    def register(self, plugin_class: Type[BasePlugin], metadata: Optional[PluginMetadata] = None) -> bool:
        """Register a plugin class."""
        try:
            # Create temporary instance to get metadata if not provided
            if metadata is None:
                temp_instance = plugin_class()
                metadata = temp_instance.get_metadata()
            
            plugin_type = metadata.plugin_type
            plugin_name = metadata.name
            
            # Register the plugin
            self._plugins[plugin_type][plugin_name] = plugin_class
            self._metadata[plugin_name] = metadata
            
            logger.info(f"Registered {plugin_type.value} plugin: {plugin_name} v{metadata.version}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to register plugin {plugin_class.__name__}: {e}")
            return False
    
    def unregister(self, plugin_name: str) -> bool:
        """Unregister a plugin."""
        try:
            if plugin_name in self._metadata:
                plugin_type = self._metadata[plugin_name].plugin_type
                if plugin_name in self._plugins[plugin_type]:
                    del self._plugins[plugin_type][plugin_name]
                    del self._metadata[plugin_name]
                    
                    # Remove instance if it exists
                    if plugin_name in self._instances:
                        del self._instances[plugin_name]
                    
                    logger.info(f"Unregistered plugin: {plugin_name}")
                    return True
            
            return False
            
        except Exception as e:
            logger.error(f"Failed to unregister plugin {plugin_name}: {e}")
            return False
    
    def get_plugin_class(self, plugin_name: str) -> Optional[Type[BasePlugin]]:
        """Get a plugin class by name."""
        if plugin_name in self._metadata:
            plugin_type = self._metadata[plugin_name].plugin_type
            return self._plugins[plugin_type].get(plugin_name)
        return None
    
    def create_instance(self, plugin_name: str, config: Optional[Dict[str, Any]] = None) -> Optional[BasePlugin]:
        """Create a plugin instance."""
        try:
            # Use a cache key that includes both name and config
            config_hash = hash(str(config)) if config else 0
            cache_key = f"{plugin_name}_{config_hash}"
            if cache_key in self._instances:
                return self._instances[cache_key]
            
            plugin_class = self.get_plugin_class(plugin_name)
            if plugin_class is None:
                logger.error(f"Plugin not found: {plugin_name}")
                return None
            
            # Create new instance
            instance = plugin_class(config or {})
            if instance.initialize():
                self._instances[cache_key] = instance
                logger.info(f"Created instance of plugin: {plugin_name} with config hash {config_hash}")
                return instance
            else:
                logger.error(f"Failed to initialize plugin: {plugin_name}")
                return None
                
        except Exception as e:
            logger.error(f"Failed to create instance of plugin {plugin_name}: {e}")
            return None
    
    def get_available_plugins(self, plugin_type: Optional[PluginType] = None) -> List[str]:
        """Get list of available plugin names."""
        if plugin_type:
            return list(self._plugins[plugin_type].keys())
        else:
            return list(self._metadata.keys())
    
    def get_plugin_metadata(self, plugin_name: str) -> Optional[PluginMetadata]:
        """Get metadata for a plugin."""
        return self._metadata.get(plugin_name)
    
    def get_plugins_by_type(self, plugin_type: PluginType) -> Dict[str, PluginMetadata]:
        """Get all plugins of a specific type with their metadata."""
        result = {}
        for name, metadata in self._metadata.items():
            if metadata.plugin_type == plugin_type:
                result[name] = metadata
        return result
    
    def validate_plugin(self, plugin_name: str) -> bool:
        """Validate that a plugin is properly configured and available."""
        try:
            plugin_class = self.get_plugin_class(plugin_name)
            if plugin_class is None:
                return False
            
            # Create temporary instance for validation
            temp_instance = plugin_class()
            return temp_instance.is_available()
            
        except Exception as e:
            logger.error(f"Plugin validation failed for {plugin_name}: {e}")
            return False
    
    def get_dependencies(self, plugin_name: str) -> List[str]:
        """Get dependencies for a plugin."""
        metadata = self.get_plugin_metadata(plugin_name)
        return metadata.dependencies if metadata else []
    
    def check_dependencies(self, plugin_name: str) -> bool:
        """Check if all dependencies for a plugin are available."""
        dependencies = self.get_dependencies(plugin_name)
        for dep in dependencies:
            if not self.validate_plugin(dep):
                logger.warning(f"Dependency {dep} for plugin {plugin_name} is not available")
                return False
        return True
    
    def list_plugins(self) -> Dict[str, List[str]]:
        """List all registered plugins by type."""
        result = {}
        for plugin_type in PluginType:
            result[plugin_type.value] = self.get_available_plugins(plugin_type)
        return result
    
    def clear(self):
        """Clear all registered plugins."""
        self._plugins.clear()
        self._instances.clear()
        self._metadata.clear()
        logger.info("Plugin registry cleared")


# Global plugin registry instance
plugin_registry = PluginRegistry() 