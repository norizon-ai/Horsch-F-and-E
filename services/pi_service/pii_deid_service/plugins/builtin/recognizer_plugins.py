"""
Built-in recognizer plugins.

This module provides plugin wrappers for the existing recognizer components.
"""

from typing import Any, Dict, List, Optional
import logging
import os

from ..base import RecognizerPlugin, PluginMetadata, PluginType
from ...entity_recognizer.presidio_recognizer import PresidioRecognizer
from ...entity_recognizer.user_id_recognizer import UserIdRecognizer
from ...entity_recognizer.court_reference_recognizer import CourtReferenceRecognizer
from ...entity_recognizer.currency_recognizer import CurrencyRecognizer
from ...entity_recognizer.file_number_recognizer import FileNumberRecognizer
from ...entity_recognizer.flair_recognizer import FlairRecognizer
from ...entity_recognizer.german_date_recognizer import GermanDateRecognizer
from ...entity_recognizer.reference_code_recognizer import ReferenceCodeRecognizer
from ...entity_recognizer.transformers_recognizer import TransformersRecognizer
from ...entity_recognizer.german_phone_recognizer import GermanPhoneRecognizer

logger = logging.getLogger(__name__)


class PresidioRecognizerPlugin(RecognizerPlugin):
    """Plugin wrapper for Presidio recognizer."""
    
    def get_metadata(self) -> PluginMetadata:
        return PluginMetadata(
            name="presidio_recognizer",
            version="1.0.0",
            description="Microsoft Presidio recognizer for PII detection",
            author="PII DeID Service",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=["presidio-analyzer"],
            config_schema={
                "language": {"type": "string", "default": "en"},
                "entities": {"type": "list", "default": ["PERSON", "EMAIL", "PHONE_NUMBER"]}
            }
        )
    
    def initialize(self) -> bool:
        try:
            language = self.config.get("language", "en")
            entities = self.config.get("entities", ["PERSON", "EMAIL", "PHONE_NUMBER"])
            
            # Create recognizer with proper configuration
            recognizer = PresidioRecognizer(language, entities)
            
            # Test the recognizer with a simple text to ensure it works
            test_text = "Hello world"
            test_result = recognizer.recognize(test_text)
            logger.info(f"Presidio recognizer initialized successfully. Test result: {len(test_result)} entities")
            
            # Store the recognizer
            self.recognizer = recognizer
            return True
        except Exception as e:
            logger.error(f"Failed to initialize Presidio recognizer: {e}")
            return False
    
    def is_available(self) -> bool:
        try:
            from presidio_analyzer import AnalyzerEngine
            return True
        except ImportError:
            return False
    
    def create_recognizer(self) -> Any:
        return self.recognizer
    
    def recognize(self, text: str, language: str = "en") -> List[Dict[str, Any]]:
        if not self.recognizer:
            logger.error("Presidio recognizer not initialized")
            return []
        
        try:
            return self.recognizer.recognize(text, language)
        except Exception as e:
            logger.error(f"Error recognizing entities with Presidio: {e}")
            return []
    
    def get_supported_entities(self) -> List[str]:
        return [
            "PERSON", "EMAIL", "PHONE_NUMBER", "CREDIT_CARD", 
            "IBAN_CODE", "IP_ADDRESS", "LOCATION", "DATE_TIME",
            "NRP", "MEDICAL_LICENSE", "US_SSN", "UK_NHS", "CA_SIN",
            "AU_TFN", "AU_ABN", "IN_PAN", "IN_AADHAAR", "ZA_ID"
        ]


class UserIdRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="user_id_recognizer",
            version="1.0.0",
            description="Detects user IDs like uc1234abcd",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        self.recognizer = UserIdRecognizer()
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="en"):
        # PatternRecognizer uses analyze()
        return self.recognizer.analyze(text, language=language, entities=["USER_ID"]) 


class CourtReferenceRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="court_reference_recognizer",
            version="1.0.0",
            description="Detects court references",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        self.recognizer = CourtReferenceRecognizer()
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="en"):
        return self.recognizer.analyze(text, language=language, entities=["COURT_REFERENCE"])


class CurrencyRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="currency_recognizer",
            version="1.0.0",
            description="Detects currency amounts",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        self.recognizer = CurrencyRecognizer()
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="en"):
        return self.recognizer.analyze(text, language=language, entities=["AMOUNT"])


class FileNumberRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="file_number_recognizer",
            version="1.0.0",
            description="Detects file numbers",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        self.recognizer = FileNumberRecognizer()
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="en"):
        return self.recognizer.analyze(text, language=language, entities=["FILE_NUMBER"])


class FlairRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="flair_recognizer",
            version="1.0.0",
            description="Detects entities using Flair NER",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        model_config = self.config
        model_path = model_config.get("MODEL_PATH")
        if not model_path:
            logging.error(f"MODEL_PATH missing in flair_recognizer config: {model_config}")
            raise ValueError("MODEL_PATH must be provided in flair_recognizer config")
        
        # Resolve relative path to user_configs/models/
        if not os.path.isabs(model_path):
            from pathlib import Path
            models_dir = Path("user_configs/models")
            model_path = str(models_dir / model_path)
        
        self.recognizer = FlairRecognizer(model_path=model_path, model_config=model_config)
        self.name = "Flair Analytics"
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self
    def recognize(self, text, language="en"):
        # FlairRecognizer expects analyze()
        return self.recognizer.analyze(text, self.recognizer.supported_entities)


class GermanDateRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="german_date_recognizer",
            version="1.0.0",
            description="Detects German date formats",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        self.recognizer = GermanDateRecognizer()
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="en"):
        return self.recognizer.analyze(text, language=language, entities=["DATE_TIME"])


class ReferenceCodeRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="reference_code_recognizer",
            version="1.0.0",
            description="Detects reference codes",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        self.recognizer = ReferenceCodeRecognizer()
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="en"):
        return self.recognizer.analyze(text, language=language, entities=["REFERENCE_CODE"])


class GermanPhoneRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="german_phone_recognizer",
            version="1.0.0",
            description="Detects German phone numbers using multiple regex patterns",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )
    def initialize(self):
        self.recognizer = GermanPhoneRecognizer()
        return True
    def is_available(self) -> bool:
        return True
    def create_recognizer(self):
        return self.recognizer
    def recognize(self, text, language="de"):
        return self.recognizer.recognize(text)


class TransformersRecognizerPlugin(RecognizerPlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="transformers_recognizer",
            version="1.0.0",
            description="Detects entities using Hugging Face Transformers NER",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=["transformers"],
            config_schema={}
        )
    def initialize(self):
        model_config = self.config or {}
        model_name = model_config.get("model")
        if not model_name:
            logging.error(f"'model' key missing in transformers_recognizer config: {model_config}")
            raise ValueError("'model' must be provided in transformers_recognizer config")
        self.recognizer = TransformersRecognizer(model_path=model_name, model_config=model_config)
        self.name = f"Transformer model {model_name}"
        return True
    def is_available(self) -> bool:
        try:
            import transformers
            return True
        except ImportError:
            return False
    def create_recognizer(self):
        return self
    def recognize(self, text, language="en"):
        return self.recognizer.analyze(text, self.recognizer.supported_entities)

# Register all recognizer plugins automatically
from pii_deid_service.plugins.registry import plugin_registry
from pii_deid_service.entity_recognizer.regex_phone_recognizer import RegexPhoneRecognizerPlugin

plugin_registry.register(PresidioRecognizerPlugin)
plugin_registry.register(UserIdRecognizerPlugin)
plugin_registry.register(CourtReferenceRecognizerPlugin)
plugin_registry.register(CurrencyRecognizerPlugin)
plugin_registry.register(FileNumberRecognizerPlugin)
plugin_registry.register(FlairRecognizerPlugin)
plugin_registry.register(GermanDateRecognizerPlugin)
plugin_registry.register(ReferenceCodeRecognizerPlugin)
plugin_registry.register(GermanPhoneRecognizerPlugin)
plugin_registry.register(TransformersRecognizerPlugin)
plugin_registry.register(RegexPhoneRecognizerPlugin) 