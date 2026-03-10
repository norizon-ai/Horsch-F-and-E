"""
Built-in operator plugins.

This module provides plugin wrappers for the existing operator components.
"""

from typing import Any, Dict, List, Optional
import logging

from ..base import OperatorPlugin, PluginMetadata, PluginType
from ...operators.presidio_operator import PresidioOperator
from ...operators.entity_sanitizer import EntitySanitizer

logger = logging.getLogger(__name__)


class PresidioOperatorPlugin(OperatorPlugin):
    """Plugin wrapper for Presidio operator."""
    
    def get_metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="presidio_operator",
            version="1.0.0",
            description="Microsoft Presidio anonymizer operator",
            author="PII DeID Service",
            plugin_type=PluginType.OPERATOR,
            dependencies=["presidio-anonymizer"],
            config_schema={
                "language": {"type": "string", "default": "en"},
                "anonymization_method": {"type": "string", "default": "replace"}
            }
        )
    
    def initialize(self) -> bool:
        try:
            language = self.config.get("language", "en")
            anonymization_method = self.config.get("anonymization_method", "replace")
            
            self.operator = PresidioOperator(language, anonymization_method)
            return True
        except Exception as e:
            logger.error(f"Failed to initialize Presidio operator: {e}")
            return False
    
    def is_available(self) -> bool:
        try:
            from presidio_anonymizer import AnonymizerEngine
            return True
        except ImportError:
            return False
    
    def create_operator(self) -> Any:
        return self.operator
    
    def apply(self, text: str, entities: List[Dict[str, Any]]) -> str:
        if not self.operator:
            logger.error("Presidio operator not initialized")
            return text
        
        try:
            return self.operator.apply(text, entities)
        except Exception as e:
            logger.error(f"Error applying Presidio operator: {e}")
            return text
    
    def get_supported_entities(self) -> List[str]:
        return [
            "PERSON", "EMAIL", "PHONE_NUMBER", "CREDIT_CARD", 
            "IBAN_CODE", "IP_ADDRESS", "LOCATION", "DATE_TIME",
            "NRP", "MEDICAL_LICENSE", "US_SSN", "UK_NHS", "CA_SIN",
            "AU_TFN", "AU_ABN", "IN_PAN", "IN_AADHAAR", "ZA_ID"
        ]
    
    def get_anonymization_method(self) -> str:
        return self.config.get("anonymization_method", "replace") 


class EntitySanitizerOperatorPlugin(OperatorPlugin):
    """
    Plugin wrapper for EntitySanitizer operator.
    """
    def __init__(self, config=None):
        super().__init__(config)
        self.operator = EntitySanitizer(config)

    def get_metadata(self):
        from ..base import PluginMetadata, PluginType
        return PluginMetadata(
            name="entity_sanitizer",
            version="1.0.0",
            description="Post-processing operator for entity deduplication, merging, filtering, etc.",
            author="PII DeID Service",
            plugin_type=PluginType.OPERATOR,
            dependencies=[],
            config_schema={
                "strategies": {"type": "list", "default": ["deduplicate"]},
                "confidence_threshold": {"type": "number", "default": 0.0},
                "entity_priority": {"type": "list", "default": []},
                "custom_strategies": {"type": "object", "default": {}}
            }
        )

    def initialize(self):
        # No special initialization needed
        return True

    def is_available(self):
        return True

    def create_operator(self):
        return self.operator

    def apply(self, text, entities):
        return self.operator.apply(text, entities)

    def get_supported_entities(self):
        # This operator is agnostic to entity types
        return []

    def get_anonymization_method(self):
        return "sanitize" 