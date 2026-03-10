"""
Built-in model plugins.

This module provides plugin wrappers for the existing model components.
"""

from typing import Any, Dict, List, Optional
import logging

from ..base import ModelPlugin, PluginMetadata, PluginType
from ...entity_recognizer.flair_recognizer import FlairRecognizer
from ...entity_recognizer.transformers_recognizer import TransformersRecognizer

logger = logging.getLogger(__name__)


class FlairModelPlugin(ModelPlugin):
    """Plugin wrapper for Flair model."""
    
    def get_metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="flair_model",
            version="1.0.0",
            description="Flair sequence tagging model for NER",
            author="PII DeID Service",
            plugin_type=PluginType.MODEL,
            dependencies=["flair"],
            config_schema={
                "model_path": {"type": "string", "required": True},
                "language": {"type": "string", "default": "en"}
            }
        )
    
    def initialize(self) -> bool:
        try:
            model_path = self.config.get("model_path")
            if not model_path:
                logger.error("Flair model path not specified in config")
                return False
            
            # Create the configuration structure that FlairRecognizer expects
            model_config = {
                "SUPPORTED_LANGUAGE": self.config.get("language", "en"),
                "PRESIDIO_SUPPORTED_ENTITIES": ["PERSON", "LOCATION", "ORGANIZATION", "MISC"],
                "DEFAULT_EXPLANATION": "Identified as {} by Flair's Named Entity Recognition",
                "CHECK_LABEL_GROUPS": [
                    [["PERSON"], ["PER", "PERSON"]],
                    [["LOCATION"], ["LOC", "LOCATION"]],
                    [["ORGANIZATION"], ["ORG", "ORGANIZATION"]],
                    [["MISC"], ["MISC"]]
                ],
                "PRESIDIO_EQUIVALENCES": {
                    "PER": "PERSON",
                    "LOC": "LOCATION", 
                    "ORG": "ORGANIZATION",
                    "MISC": "MISC"
                }
            }
            
            self.model = FlairRecognizer(model_path, model_config)
            self.model.load()
            return True
        except Exception as e:
            logger.error(f"Failed to initialize Flair model: {e}")
            return False
    
    def is_available(self) -> bool:
        try:
            import flair
            return True
        except ImportError:
            return False
    
    def load_model(self) -> Any:
        return self.model
    
    def predict(self, text: str) -> List[Dict[str, Any]]:
        if not self.model:
            logger.error("Flair model not initialized")
            return []
        
        try:
            return self.model.predict(text)
        except Exception as e:
            logger.error(f"Error making prediction with Flair model: {e}")
            return []
    
    def get_supported_entities(self) -> List[str]:
        return ["PERSON", "LOCATION", "ORGANIZATION", "MISC"]


class SpacyModelPlugin(ModelPlugin):
    """Plugin wrapper for spaCy model."""
    
    def get_metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="spacy_model",
            version="1.0.0",
            description="spaCy model for NER",
            author="PII DeID Service",
            plugin_type=PluginType.MODEL,
            dependencies=["spacy"],
            config_schema={
                "model_name": {"type": "string", "default": "en_core_web_sm"},
                "language": {"type": "string", "default": "en"}
            }
        )
    
    def initialize(self) -> bool:
        try:
            model_name = self.config.get("model_name", "en_core_web_sm")
            # For now, we'll use a simple approach since we don't have a SpacyModel class
            import spacy
            self.model = spacy.load(model_name)
            return True
        except Exception as e:
            logger.error(f"Failed to initialize spaCy model: {e}")
            return False
    
    def is_available(self) -> bool:
        try:
            import spacy
            return True
        except ImportError:
            return False
    
    def load_model(self) -> Any:
        return self.model
    
    def predict(self, text: str) -> List[Dict[str, Any]]:
        if not self.model:
            logger.error("spaCy model not initialized")
            return []
        
        try:
            doc = self.model(text)
            entities = []
            for ent in doc.ents:
                entities.append({
                    "text": ent.text,
                    "start": ent.start_char,
                    "end": ent.end_char,
                    "label": ent.label_,
                    "confidence": 1.0
                })
            return entities
        except Exception as e:
            logger.error(f"Error making prediction with spaCy model: {e}")
            return []
    
    def get_supported_entities(self) -> List[str]:
        return ["PERSON", "ORG", "GPE", "LOC", "MISC"] 