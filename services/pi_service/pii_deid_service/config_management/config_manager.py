"""
Configuration Manager for PII De-identification Service.

This module provides centralized configuration management using Pydantic schemas.
"""

import json
import os
from typing import Dict, Any, Optional, List
from pathlib import Path
import logging

from pydantic import BaseModel, Field, ValidationError
from pydantic.json import pydantic_encoder

logger = logging.getLogger(__name__)


class ModelConfig(BaseModel):
    """Configuration for a model component."""
    name: str = Field(..., description="Model name")
    type: str = Field(..., description="Model type (flair, spacy, etc.)")
    model_path: Optional[str] = Field(None, description="Path to model file")
    language: str = Field("en", description="Language code")
    entities: List[str] = Field(default_factory=list, description="Entities to detect")
    confidence_threshold: float = Field(0.5, description="Confidence threshold")
    additional_params: Dict[str, Any] = Field(default_factory=dict, description="Additional parameters")


class RecognizerConfig(BaseModel):
    """Configuration for a recognizer component."""
    name: str = Field(..., description="Recognizer name")
    type: str = Field(..., description="Recognizer type (presidio, custom, etc.)")
    language: str = Field("en", description="Language code")
    entities: List[str] = Field(default_factory=list, description="Entities to detect")
    confidence_threshold: float = Field(0.5, description="Confidence threshold")
    additional_params: Dict[str, Any] = Field(default_factory=dict, description="Additional parameters")


class OperatorConfig(BaseModel):
    """Configuration for an operator component."""
    name: str = Field(..., description="Operator name")
    type: str = Field(..., description="Operator type (presidio, custom, etc.)")
    anonymization_method: str = Field("replace", description="Anonymization method")
    language: str = Field("en", description="Language code")
    additional_params: Dict[str, Any] = Field(default_factory=dict, description="Additional parameters")


class PipelineConfig(BaseModel):
    """Configuration for a complete pipeline."""
    name: str = Field(..., description="Pipeline name")
    description: Optional[str] = Field(None, description="Pipeline description")
    models: List[ModelConfig] = Field(default_factory=list, description="List of models")
    recognizers: List[RecognizerConfig] = Field(default_factory=list, description="List of recognizers")
    operators: List[OperatorConfig] = Field(default_factory=list, description="List of operators")
    enabled: bool = Field(True, description="Whether pipeline is enabled")
    additional_params: Dict[str, Any] = Field(default_factory=dict, description="Additional parameters")


class ServiceConfig(BaseModel):
    """Main service configuration."""
    service_name: str = Field("PII De-identification Service", description="Service name")
    version: str = Field("1.0.0", description="Service version")
    log_level: str = Field("INFO", description="Logging level")
    config_dir: str = Field("configs", description="Configuration directory")
    model_dir: str = Field("pii-resources/models", description="Model directory")
    output_dir: str = Field("output", description="Output directory")
    max_text_length: int = Field(10000, description="Maximum text length to process")
    batch_size: int = Field(100, description="Batch size for processing")
    additional_params: Dict[str, Any] = Field(default_factory=dict, description="Additional parameters")


class ConfigManager:
    """Manages configuration for the PII de-identification service."""
    
    def __init__(self, config_dir: str = "configs"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        
        self.service_config: Optional[ServiceConfig] = None
        self.pipelines: Dict[str, PipelineConfig] = {}
        self.models: Dict[str, ModelConfig] = {}
        self.recognizers: Dict[str, RecognizerConfig] = {}
        self.operators: Dict[str, OperatorConfig] = {}
        
        self._load_configurations()
    
    def _load_configurations(self):
        """Load all configuration files."""
        try:
            # Load service configuration
            service_config_path = self.config_dir / "service_config.json"
            if service_config_path.exists():
                with open(service_config_path, "r", encoding="utf-8") as f:
                    config_data = json.load(f)
                self.service_config = ServiceConfig(**config_data)
            else:
                # Create default service configuration
                self.service_config = ServiceConfig()
                self._save_service_config()
            
            # Load pipeline configurations
            pipeline_dir = self.config_dir / "pipelines"
            pipeline_dir.mkdir(exist_ok=True)
            
            for config_file in pipeline_dir.glob("*.json"):
                try:
                    with open(config_file, "r", encoding="utf-8") as f:
                        config_data = json.load(f)
                    pipeline_config = PipelineConfig(**config_data)
                    self.pipelines[pipeline_config.name] = pipeline_config
                    logger.info(f"Loaded pipeline configuration: {pipeline_config.name}")
                except Exception as e:
                    logger.error(f"Failed to load pipeline config {config_file}: {e}")
            
            # Load individual component configurations
            self._load_component_configs("models", ModelConfig, self.models)
            self._load_component_configs("recognizers", RecognizerConfig, self.recognizers)
            self._load_component_configs("operators", OperatorConfig, self.operators)
            
            logger.info("Configuration loading completed")
            
        except Exception as e:
            logger.error(f"Failed to load configurations: {e}")
            raise
    
    def _load_component_configs(self, component_type: str, config_class, storage_dict: Dict):
        """Load component configurations from directory."""
        component_dir = self.config_dir / component_type
        component_dir.mkdir(exist_ok=True)
        
        for config_file in component_dir.glob("*.json"):
            try:
                with open(config_file, "r", encoding="utf-8") as f:
                    config_data = json.load(f)
                config = config_class(**config_data)
                storage_dict[config.name] = config
                logger.info(f"Loaded {component_type} configuration: {config.name}")
            except Exception as e:
                logger.error(f"Failed to load {component_type} config {config_file}: {e}")
    
    def _save_service_config(self):
        """Save service configuration to file."""
        try:
            service_config_path = self.config_dir / "service_config.json"
            with open(service_config_path, "w", encoding="utf-8") as f:
                json.dump(self.service_config.dict(), f, indent=2, ensure_ascii=False, default=pydantic_encoder)
            logger.info("Service configuration saved")
        except Exception as e:
            logger.error(f"Failed to save service configuration: {e}")
    
    def get_service_config(self) -> ServiceConfig:
        """Get the service configuration."""
        return self.service_config
    
    def get_pipeline_config(self, name: str) -> Optional[PipelineConfig]:
        """Get a pipeline configuration by name."""
        return self.pipelines.get(name)
    
    def get_all_pipeline_configs(self) -> Dict[str, PipelineConfig]:
        """Get all pipeline configurations."""
        return self.pipelines.copy()
    
    def get_model_config(self, name: str) -> Optional[ModelConfig]:
        """Get a model configuration by name."""
        return self.models.get(name)
    
    def get_recognizer_config(self, name: str) -> Optional[RecognizerConfig]:
        """Get a recognizer configuration by name."""
        return self.recognizers.get(name)
    
    def get_operator_config(self, name: str) -> Optional[OperatorConfig]:
        """Get an operator configuration by name."""
        return self.operators.get(name)
    
    def add_pipeline_config(self, config: PipelineConfig) -> bool:
        """Add a new pipeline configuration."""
        try:
            self.pipelines[config.name] = config
            
            # Save to file
            pipeline_dir = self.config_dir / "pipelines"
            pipeline_dir.mkdir(exist_ok=True)
            
            config_path = pipeline_dir / f"{config.name}.json"
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config.dict(), f, indent=2, ensure_ascii=False, default=pydantic_encoder)
            
            logger.info(f"Added pipeline configuration: {config.name}")
            return True
        except Exception as e:
            logger.error(f"Failed to add pipeline configuration: {e}")
            return False
    
    def update_pipeline_config(self, name: str, config: PipelineConfig) -> bool:
        """Update an existing pipeline configuration."""
        if name not in self.pipelines:
            logger.error(f"Pipeline configuration not found: {name}")
            return False
        
        return self.add_pipeline_config(config)
    
    def delete_pipeline_config(self, name: str) -> bool:
        """Delete a pipeline configuration."""
        try:
            if name in self.pipelines:
                del self.pipelines[name]
                
                # Delete file
                pipeline_dir = self.config_dir / "pipelines"
                config_path = pipeline_dir / f"{name}.json"
                if config_path.exists():
                    config_path.unlink()
                
                logger.info(f"Deleted pipeline configuration: {name}")
                return True
            else:
                logger.warning(f"Pipeline configuration not found: {name}")
                return False
        except Exception as e:
            logger.error(f"Failed to delete pipeline configuration: {e}")
            return False
    
    def validate_configuration(self) -> List[str]:
        """Validate all configurations and return list of errors."""
        errors = []
        
        # Validate service configuration
        if not self.service_config:
            errors.append("Service configuration is missing")
        
        # Validate pipeline configurations
        for name, pipeline in self.pipelines.items():
            if not pipeline.models and not pipeline.recognizers:
                errors.append(f"Pipeline '{name}' has no models or recognizers")
            
            # Check if referenced components exist
            for model in pipeline.models:
                if not self.get_model_config(model.name):
                    errors.append(f"Pipeline '{name}' references unknown model: {model.name}")
            
            for recognizer in pipeline.recognizers:
                if not self.get_recognizer_config(recognizer.name):
                    errors.append(f"Pipeline '{name}' references unknown recognizer: {recognizer.name}")
            
            for operator in pipeline.operators:
                if not self.get_operator_config(operator.name):
                    errors.append(f"Pipeline '{name}' references unknown operator: {operator.name}")
        
        return errors
    
    def get_config_summary(self) -> Dict[str, Any]:
        """Get a summary of all configurations."""
        return {
            "service_config": self.service_config.dict() if self.service_config else None,
            "pipelines": {
                name: {
                    "description": config.description,
                    "models": len(config.models),
                    "recognizers": len(config.recognizers),
                    "operators": len(config.operators),
                    "enabled": config.enabled
                }
                for name, config in self.pipelines.items()
            },
            "components": {
                "models": len(self.models),
                "recognizers": len(self.recognizers),
                "operators": len(self.operators)
            }
        }

    def load_pipeline_config(self, config_path: str) -> Dict[str, Any]:
        """Load a plugin pipeline configuration from a JSON file.
        
        Args:
            config_path: Path to the JSON configuration file
            
        Returns:
            Dictionary containing the pipeline configuration
            
        Raises:
            FileNotFoundError: If the configuration file doesn't exist
            json.JSONDecodeError: If the JSON is invalid
        """
        try:
            config_file = Path(config_path)
            if not config_file.exists():
                raise FileNotFoundError(f"Configuration file not found: {config_path}")
            
            with open(config_file, "r", encoding="utf-8") as f:
                config_data = json.load(f)
            
            logger.info(f"Loaded pipeline configuration from: {config_path}")
            return config_data
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in configuration file {config_path}: {e}")
            raise
        except Exception as e:
            logger.error(f"Failed to load pipeline configuration from {config_path}: {e}")
            raise


# Global configuration manager instance
config_manager = ConfigManager() 