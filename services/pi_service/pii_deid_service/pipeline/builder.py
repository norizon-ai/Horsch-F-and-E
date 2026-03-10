"""
Pipeline builder using the plugin system.

This module provides a builder that creates pipeline components using
the plugin system for maximum flexibility and extensibility.
"""

import logging
from typing import Any, Dict, List, Optional

from ..config_management.plugin_schemas import PluginPipelineConfig
from ..plugins.manager import plugin_manager
from ..factories.model_factory import model_factory
from ..factories.recognizer_factory import recognizer_factory
from ..factories.operator_factory import operator_factory

logger = logging.getLogger(__name__)


class PluginBasedPipelineBuilder:
    """Pipeline builder that uses the plugin system."""
    
    def __init__(self):
        self._initialized = False
    
    def initialize(self) -> bool:
        """Initialize the pipeline builder with the plugin system."""
        try:
            if not plugin_manager.is_initialized():
                if not plugin_manager.initialize():
                    logger.error("Failed to initialize plugin system")
                    return False
            
            self._initialized = True
            logger.info("Plugin-based pipeline builder initialized")
            return True
            
        except Exception as e:
            logger.error(f"Error initializing pipeline builder: {e}")
            return False
    
    def build_pipeline(self, config: Any) -> Optional[Dict[str, Any]]:
        """Build a complete pipeline using the plugin system.
        
        Args:
            config: Either a PluginPipelineConfig object or a dictionary with pipeline configuration
            
        Returns:
            Pipeline dictionary or None if building fails
        """
        if not self._initialized:
            logger.error("Pipeline builder not initialized")
            return None
        
        try:
            # Convert dictionary to PluginPipelineConfig if needed
            if isinstance(config, dict):
                config = PluginPipelineConfig(**config)
            
            logger.info(f"Building pipeline: {config.name}")
            
            # Build models
            models = self._build_models(config.models)
            if models is None:
                logger.error("Failed to build models")
                return None
            
            # Build recognizers
            recognizers = self._build_recognizers(config.recognizers)
            if recognizers is None:
                logger.error("Failed to build recognizers")
                return None
            
            # Build operators
            operators = self._build_operators(config.operators)
            if operators is None:
                logger.error("Failed to build operators")
                return None
            
            pipeline = {
                "name": config.name,
                "models": models,
                "recognizers": recognizers,
                "operators": operators,
                "config": config
            }
            
            logger.info(f"Pipeline built successfully: {config.name}")
            return pipeline
            
        except Exception as e:
            logger.error(f"Error building pipeline: {e}")
            return None
    
    def _build_models(self, model_configs: List[Any]) -> Optional[List[Any]]:
        """Build model instances using the plugin system."""
        models = []
        
        for model_config in model_configs:
            try:
                model_name = model_config.name
                config = model_config.config
                
                if not model_name:
                    logger.error("Model name not specified in config")
                    return None
                
                # Validate model plugin
                if not model_factory.validate_model(model_name):
                    logger.error(f"Model plugin not available: {model_name}")
                    return None
                
                # Create model instance
                model = model_factory.create_model(model_name, config)
                if model is None:
                    logger.error(f"Failed to create model: {model_name}")
                    return None
                
                models.append(model)
                logger.info(f"Built model: {model_name}")
                
            except Exception as e:
                logger.error(f"Error building model {model_config}: {e}")
                return None
        
        return models
    
    def _build_recognizers(self, recognizer_configs: List[Any]) -> Optional[List[Any]]:
        """Build recognizer instances using the plugin system."""
        recognizers = []
        
        for recognizer_config in recognizer_configs:
            try:
                recognizer_name = recognizer_config.name
                config = recognizer_config.config
                
                # Load config from config_path if config is empty and config_path is provided
                if not config and hasattr(recognizer_config, 'config_path') and recognizer_config.config_path:
                    try:
                        import json
                        from pathlib import Path
                        config_file = Path(recognizer_config.config_path)
                        if config_file.exists():
                            with open(config_file, 'r', encoding='utf-8') as f:
                                loaded_config = json.load(f)
                                config = loaded_config.get('config', {})
                                logger.info(f"Loaded config from {recognizer_config.config_path}")
                        else:
                            logger.warning(f"Config file not found: {recognizer_config.config_path}")
                    except Exception as e:
                        logger.error(f"Error loading config from {recognizer_config.config_path}: {e}")
                
                if not recognizer_name:
                    logger.error("Recognizer name not specified in config")
                    return None
                
                # Validate recognizer plugin
                if not recognizer_factory.validate_recognizer(recognizer_name):
                    logger.error(f"Recognizer plugin not available: {recognizer_name}")
                    return None
                
                # Create recognizer instance
                recognizer = recognizer_factory.create_recognizer(recognizer_name, config)
                if recognizer is None:
                    logger.error(f"Failed to create recognizer: {recognizer_name}")
                    return None
                
                recognizers.append(recognizer)
                logger.info(f"Built recognizer: {recognizer_name}")
                
            except Exception as e:
                logger.error(f"Error building recognizer {recognizer_config}: {e}")
                return None
        
        return recognizers
    
    def _build_operators(self, operator_configs: List[Any]) -> Optional[List[Any]]:
        """Build operator instances using the plugin system."""
        operators = []
        
        for operator_config in operator_configs:
            try:
                operator_name = operator_config.name
                config = operator_config.config
                
                if not operator_name:
                    logger.error("Operator name not specified in config")
                    return None
                
                # Validate operator plugin
                if not operator_factory.validate_operator(operator_name):
                    logger.error(f"Operator plugin not available: {operator_name}")
                    return None
                
                # Create operator instance
                operator = operator_factory.create_operator(operator_name, config)
                if operator is None:
                    logger.error(f"Failed to create operator: {operator_name}")
                    return None
                
                operators.append(operator)
                logger.info(f"Built operator: {operator_name}")
                
            except Exception as e:
                logger.error(f"Error building operator {operator_config}: {e}")
                return None
        
        return operators
    
    def get_available_components(self) -> Dict[str, List[str]]:
        """Get all available components by type."""
        return plugin_manager.get_available_plugins()
    
    def get_component_info(self, component_name: str) -> Optional[Dict]:
        """Get detailed information about a component."""
        return plugin_manager.get_plugin_info(component_name)
    
    def validate_component(self, component_name: str) -> bool:
        """Validate that a component is available."""
        return plugin_manager.validate_plugin(component_name)
    
    def reload_component(self, component_name: str) -> bool:
        """Reload a component."""
        return plugin_manager.reload_plugin(component_name)
    
    def is_initialized(self) -> bool:
        """Check if the pipeline builder is initialized."""
        return self._initialized


# Global plugin-based pipeline builder instance
plugin_pipeline_builder = PluginBasedPipelineBuilder() 