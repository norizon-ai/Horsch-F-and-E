"""
Plugin system configuration schemas for PII De-identification Service.

This module defines Pydantic models for plugin-based configuration validation and management.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, validator
from pathlib import Path


class PluginComponentConfig(BaseModel):
    """Configuration for a plugin component (model, recognizer, or operator)."""
    
    name: str = Field(..., description="Name of the plugin to use")
    config: Dict[str, Any] = Field(default_factory=dict, description="Configuration for the plugin")
    config_path: Optional[str] = Field(None, description="Path to a JSON file containing the config for the plugin")

    @validator('config', pre=True, always=True)
    def load_config_from_path(cls, v, values):
        # If config_path is provided, load config from file
        if 'config_path' in values and values['config_path']:
            config_path = values['config_path']
            config_file = Path(config_path)
            if not config_file.exists():
                raise FileNotFoundError(f"Config file not found: {config_path}")
            import json
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f).get('config', {})
        return v


class PluginPipelineConfig(BaseModel):
    """Complete plugin-based pipeline configuration."""
    
    name: str = Field(..., description="Name of the pipeline configuration")
    description: Optional[str] = Field(None, description="Description of the pipeline")
    
    # Plugin component configurations
    models: List[PluginComponentConfig] = Field(default_factory=list, description="List of model plugin configurations")
    recognizers: List[PluginComponentConfig] = Field(default_factory=list, description="List of recognizer plugin configurations")
    operators: List[PluginComponentConfig] = Field(default_factory=list, description="List of operator plugin configurations")
    
    @validator('models')
    def validate_model_names(cls, v):
        """Ensure model names are unique."""
        names = [model.name for model in v]
        if len(names) != len(set(names)):
            raise ValueError("Model names must be unique")
        return v
    
    @validator('recognizers')
    def validate_recognizer_names(cls, v):
        """Ensure recognizer names are unique."""
        names = [rec.name for rec in v]
        if len(names) != len(set(names)):
            raise ValueError("Recognizer names must be unique")
        return v
    
    @validator('operators')
    def validate_operator_names(cls, v):
        """Ensure operator names are unique."""
        names = [op.name for op in v]
        if len(names) != len(set(names)):
            raise ValueError("Operator names must be unique")
        return v
    
    class Config:
        use_enum_values = True
        protected_namespaces = () 