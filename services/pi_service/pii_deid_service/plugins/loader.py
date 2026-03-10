"""
Plugin loader for discovering and loading plugins.

This module provides functionality to automatically discover and load
plugins from directories and packages.
"""

import os
import sys
import importlib
import importlib.util
import logging
from pathlib import Path
from typing import List, Dict, Any, Optional

from .registry import plugin_registry
from .base import BasePlugin, PluginType

logger = logging.getLogger(__name__)


class PluginLoader:
    """Loader for discovering and loading plugins."""
    
    def __init__(self, plugin_directories: Optional[List[str]] = None):
        self.plugin_directories = plugin_directories or []
        self.loaded_plugins: Dict[str, str] = {}  # plugin_name -> source_path
    
    def add_plugin_directory(self, directory: str) -> bool:
        """Add a directory to search for plugins."""
        if os.path.exists(directory) and os.path.isdir(directory):
            self.plugin_directories.append(directory)
            logger.info(f"Added plugin directory: {directory}")
            return True
        else:
            logger.warning(f"Plugin directory does not exist: {directory}")
            return False
    
    def discover_plugins(self) -> Dict[str, List[str]]:
        """Discover plugins in all registered directories."""
        discovered = {
            PluginType.MODEL.value: [],
            PluginType.RECOGNIZER.value: [],
            PluginType.OPERATOR.value: []
        }
        
        for directory in self.plugin_directories:
            try:
                dir_plugins = self._discover_plugins_in_directory(directory)
                for plugin_type, plugins in dir_plugins.items():
                    discovered[plugin_type].extend(plugins)
            except Exception as e:
                logger.error(f"Error discovering plugins in {directory}: {e}")
        
        return discovered
    
    def _discover_plugins_in_directory(self, directory: str) -> Dict[str, List[str]]:
        """Discover plugins in a specific directory."""
        discovered = {
            PluginType.MODEL.value: [],
            PluginType.RECOGNIZER.value: [],
            PluginType.OPERATOR.value: []
        }
        
        dir_path = Path(directory)
        
        # Look for Python files and directories
        for item in dir_path.iterdir():
            if item.is_file() and item.suffix == '.py':
                plugin_name = self._load_plugin_from_file(item)
                if plugin_name:
                    # Determine plugin type from loaded plugin
                    metadata = plugin_registry.get_plugin_metadata(plugin_name)
                    if metadata:
                        discovered[metadata.plugin_type.value].append(plugin_name)
            
            elif item.is_dir() and (item / '__init__.py').exists():
                plugin_name = self._load_plugin_from_package(item)
                if plugin_name:
                    metadata = plugin_registry.get_plugin_metadata(plugin_name)
                    if metadata:
                        discovered[metadata.plugin_type.value].append(plugin_name)
        
        return discovered
    
    def _load_plugin_from_file(self, file_path: Path) -> Optional[str]:
        """Load a plugin from a Python file."""
        try:
            # Create a unique module name
            module_name = f"plugin_{file_path.stem}_{id(file_path)}"
            
            # Load the module
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if spec is None or spec.loader is None:
                return None
            
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
            
            # Find plugin classes in the module
            plugin_name = self._find_plugin_classes_in_module(module, str(file_path))
            if plugin_name:
                self.loaded_plugins[plugin_name] = str(file_path)
                return plugin_name
            
            return None
            
        except Exception as e:
            logger.error(f"Error loading plugin from file {file_path}: {e}")
            return None
    
    def _load_plugin_from_package(self, package_path: Path) -> Optional[str]:
        """Load a plugin from a Python package."""
        try:
            # Create a unique module name
            package_name = f"plugin_package_{package_path.name}_{id(package_path)}"
            
            # Add the package directory to sys.path temporarily
            original_path = sys.path.copy()
            sys.path.insert(0, str(package_path.parent))
            
            try:
                # Import the package
                module = importlib.import_module(package_path.name)
                
                # Find plugin classes in the module
                plugin_name = self._find_plugin_classes_in_module(module, str(package_path))
                if plugin_name:
                    self.loaded_plugins[plugin_name] = str(package_path)
                    return plugin_name
                
                return None
                
            finally:
                # Restore original sys.path
                sys.path = original_path
                
        except Exception as e:
            logger.error(f"Error loading plugin from package {package_path}: {e}")
            return None
    
    def _find_plugin_classes_in_module(self, module: Any, source_path: str) -> Optional[str]:
        """Find and register plugin classes in a module."""
        try:
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                
                # Check if it's a class that inherits from BasePlugin
                if (isinstance(attr, type) and 
                    issubclass(attr, BasePlugin) and 
                    attr != BasePlugin):
                    
                    # Try to register the plugin
                    if plugin_registry.register(attr):
                        logger.info(f"Registered plugin {attr_name} from {source_path}")
                        return attr_name
            
            return None
            
        except Exception as e:
            logger.error(f"Error finding plugin classes in module: {e}")
            return None
    
    def load_plugin_by_name(self, plugin_name: str) -> bool:
        """Load a specific plugin by name."""
        try:
            # Check if plugin is already registered
            if plugin_registry.get_plugin_class(plugin_name):
                logger.info(f"Plugin {plugin_name} is already registered")
                return True
            
            # Try to find and load the plugin
            for directory in self.plugin_directories:
                plugin_path = self._find_plugin_file(directory, plugin_name)
                if plugin_path:
                    if plugin_path.is_file():
                        loaded_name = self._load_plugin_from_file(plugin_path)
                    else:
                        loaded_name = self._load_plugin_from_package(plugin_path)
                    
                    if loaded_name == plugin_name:
                        return True
            
            logger.warning(f"Plugin {plugin_name} not found in any plugin directory")
            return False
            
        except Exception as e:
            logger.error(f"Error loading plugin {plugin_name}: {e}")
            return False
    
    def _find_plugin_file(self, directory: str, plugin_name: str) -> Optional[Path]:
        """Find a plugin file or directory by name."""
        dir_path = Path(directory)
        
        # Look for exact matches
        for item in dir_path.iterdir():
            if (item.name == f"{plugin_name}.py" or 
                (item.is_dir() and item.name == plugin_name and (item / '__init__.py').exists())):
                return item
        
        # Look for files containing the plugin name
        for item in dir_path.iterdir():
            if item.is_file() and item.suffix == '.py':
                try:
                    with open(item, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if plugin_name in content:
                            return item
                except Exception:
                    continue
        
        return None
    
    def reload_plugin(self, plugin_name: str) -> bool:
        """Reload a plugin."""
        try:
            # Unregister the plugin
            if plugin_registry.unregister(plugin_name):
                # Remove from loaded plugins
                if plugin_name in self.loaded_plugins:
                    del self.loaded_plugins[plugin_name]
                
                # Reload the plugin
                return self.load_plugin_by_name(plugin_name)
            
            return False
            
        except Exception as e:
            logger.error(f"Error reloading plugin {plugin_name}: {e}")
            return False
    
    def get_loaded_plugins(self) -> Dict[str, str]:
        """Get information about loaded plugins."""
        return self.loaded_plugins.copy()
    
    def list_available_plugins(self) -> Dict[str, List[str]]:
        """List all available plugins by type."""
        return plugin_registry.list_plugins()
    
    def validate_all_plugins(self) -> Dict[str, bool]:
        """Validate all loaded plugins."""
        results = {}
        for plugin_name in plugin_registry.get_available_plugins():
            results[plugin_name] = plugin_registry.validate_plugin(plugin_name)
        return results 