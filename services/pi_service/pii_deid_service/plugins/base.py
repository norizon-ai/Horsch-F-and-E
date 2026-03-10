"""
Base plugin classes for the PII de-identification service.

This module defines the base classes that all plugins must inherit from
to ensure consistent interfaces and behavior.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum


class PluginType(Enum):
    """Types of plugins supported by the system."""
    MODEL = "model"
    RECOGNIZER = "recognizer"
    OPERATOR = "operator"


@dataclass
class PluginMetadata:
    """Metadata for a plugin."""
    name: str
    version: str
    description: str
    author: str
    plugin_type: PluginType
    dependencies: List[str]
    config_schema: Optional[Dict[str, Any]] = None


class BasePlugin(ABC):
    """Base class for all plugins."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.metadata = self.get_metadata()
    
    @abstractmethod
    def get_metadata(self) -> PluginMetadata:
        """Return plugin metadata."""
        pass
    
    @abstractmethod
    def initialize(self) -> bool:
        """Initialize the plugin."""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if the plugin is available and ready to use."""
        pass
    
    def validate_config(self, config: Dict[str, Any]) -> bool:
        """Validate plugin configuration."""
        return True
    
    def get_config_schema(self) -> Dict[str, Any]:
        """Get the configuration schema for this plugin."""
        return self.metadata.config_schema or {}


class ModelPlugin(BasePlugin):
    """Base class for model plugins."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)
        self.model = None
    
    @abstractmethod
    def load_model(self) -> Any:
        """Load the underlying model."""
        pass
    
    @abstractmethod
    def predict(self, text: str) -> List[Dict[str, Any]]:
        """Make predictions on input text."""
        pass
    
    def get_supported_languages(self) -> List[str]:
        """Get list of supported languages."""
        return ["en"]
    
    def get_supported_entities(self) -> List[str]:
        """Get list of supported entity types."""
        return []


class RecognizerPlugin(BasePlugin):
    """Base class for recognizer plugins."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)
        self.recognizer = None
    
    @abstractmethod
    def create_recognizer(self) -> Any:
        """Create the recognizer instance."""
        pass
    
    @abstractmethod
    def recognize(self, text: str, language: str = "en") -> List[Dict[str, Any]]:
        """Recognize entities in text."""
        pass
    
    def get_supported_languages(self) -> List[str]:
        """Get list of supported languages."""
        return ["en"]
    
    def get_supported_entities(self) -> List[str]:
        """Get list of supported entity types."""
        return []


class OperatorPlugin(BasePlugin):
    """Base class for operator plugins."""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(config)
        self.operator = None
    
    @abstractmethod
    def create_operator(self) -> Any:
        """Create the operator instance."""
        pass
    
    @abstractmethod
    def apply(self, text: str, entities: List[Dict[str, Any]]) -> str:
        """Apply the operator to anonymize entities in text."""
        pass
    
    def get_supported_entities(self) -> List[str]:
        """Get list of supported entity types."""
        return []
    
    def get_anonymization_method(self) -> str:
        """Get the anonymization method used by this operator."""
        return "replace" 