"""
Plugin manager for the PII de-identification service.

This module provides a centralized manager for initializing and managing
all plugins in the system.
"""

import logging
from typing import Dict, List, Optional

from .registry import plugin_registry
from .loader import PluginLoader
from .builtin import (
    FlairModelPlugin, SpacyModelPlugin,
    PresidioRecognizerPlugin, PresidioOperatorPlugin,
    EntitySanitizerOperatorPlugin
)

logger = logging.getLogger(__name__)


class PluginManager:
    """Manager for all plugins in the system."""
    
    def __init__(self):
        self.loader = PluginLoader()
        self._initialized = False
    
    def initialize(self, plugin_directories: Optional[List[str]] = None) -> bool:
        """Initialize the plugin system."""
        try:
            logger.info("Initializing plugin system...")
            
            # Register built-in plugins
            self._register_builtin_plugins()
            
            # Add plugin directories if provided
            if plugin_directories:
                for directory in plugin_directories:
                    self.loader.add_plugin_directory(directory)
            
            # Discover and load external plugins
            discovered = self.loader.discover_plugins()
            logger.info(f"Discovered plugins: {discovered}")
            
            # Validate all plugins
            validation_results = self.loader.validate_all_plugins()
            failed_plugins = [name for name, valid in validation_results.items() if not valid]
            
            if failed_plugins:
                logger.warning(f"Some plugins failed validation: {failed_plugins}")
            
            self._initialized = True
            logger.info("Plugin system initialized successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to initialize plugin system: {e}")
            return False
    
    def _register_builtin_plugins(self):
        """Register all built-in plugins."""
        builtin_plugins = [
            FlairModelPlugin,
            SpacyModelPlugin,
            PresidioRecognizerPlugin,
            PresidioOperatorPlugin,
            EntitySanitizerOperatorPlugin
        ]
        
        for plugin_class in builtin_plugins:
            try:
                if plugin_registry.register(plugin_class):
                    logger.info(f"Registered built-in plugin: {plugin_class.__name__}")
                else:
                    logger.warning(f"Failed to register built-in plugin: {plugin_class.__name__}")
            except Exception as e:
                logger.error(f"Error registering built-in plugin {plugin_class.__name__}: {e}")
    
    def get_available_plugins(self) -> Dict[str, List[str]]:
        """Get all available plugins by type."""
        return plugin_registry.list_plugins()
    
    def get_plugin_info(self, plugin_name: str) -> Optional[Dict]:
        """Get detailed information about a plugin."""
        metadata = plugin_registry.get_plugin_metadata(plugin_name)
        if not metadata:
            return None
        
        return {
            "name": metadata.name,
            "version": metadata.version,
            "description": metadata.description,
            "author": metadata.author,
            "type": metadata.plugin_type.value,
            "dependencies": metadata.dependencies,
            "config_schema": metadata.config_schema,
            "available": plugin_registry.validate_plugin(plugin_name),
            "source": self.loader.get_loaded_plugins().get(plugin_name, "built-in")
        }
    
    def load_plugin(self, plugin_name: str) -> bool:
        """Load a specific plugin."""
        return self.loader.load_plugin_by_name(plugin_name)
    
    def reload_plugin(self, plugin_name: str) -> bool:
        """Reload a plugin."""
        return self.loader.reload_plugin(plugin_name)
    
    def unregister_plugin(self, plugin_name: str) -> bool:
        """Unregister a plugin."""
        return plugin_registry.unregister(plugin_name)
    
    def create_plugin_instance(self, plugin_name: str, config: Optional[Dict] = None):
        """Create an instance of a plugin."""
        return plugin_registry.create_instance(plugin_name, config)
    
    def validate_plugin(self, plugin_name: str) -> bool:
        """Validate a plugin."""
        return plugin_registry.validate_plugin(plugin_name)
    
    def check_dependencies(self, plugin_name: str) -> bool:
        """Check if all dependencies for a plugin are available."""
        return plugin_registry.check_dependencies(plugin_name)
    
    def get_plugin_dependencies(self, plugin_name: str) -> List[str]:
        """Get dependencies for a plugin."""
        return plugin_registry.get_dependencies(plugin_name)
    
    def add_plugin_directory(self, directory: str) -> bool:
        """Add a directory to search for plugins."""
        return self.loader.add_plugin_directory(directory)
    
    def get_loaded_plugins(self) -> Dict[str, str]:
        """Get information about loaded plugins."""
        return self.loader.get_loaded_plugins()
    
    def clear_all(self):
        """Clear all plugins and reset the system."""
        plugin_registry.clear()
        self.loader = PluginLoader()
        self._initialized = False
        logger.info("Plugin system cleared")
    
    def is_initialized(self) -> bool:
        """Check if the plugin system is initialized."""
        return self._initialized
    
    def get_status(self) -> Dict:
        """Get the status of the plugin system."""
        if not self._initialized:
            return {"status": "not_initialized"}
        
        available_plugins = self.get_available_plugins()
        validation_results = self.loader.validate_all_plugins()
        
        return {
            "status": "initialized",
            "total_plugins": sum(len(plugins) for plugins in available_plugins.values()),
            "plugins_by_type": available_plugins,
            "validation_results": validation_results,
            "loaded_plugins": self.get_loaded_plugins()
        }


# Global plugin manager instance
plugin_manager = PluginManager() 