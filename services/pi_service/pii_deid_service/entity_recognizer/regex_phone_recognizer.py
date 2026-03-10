import re
from pii_deid_service.plugins.base import RecognizerPlugin, PluginMetadata, PluginType

class RegexPhoneRecognizer:
    """
    Recognizer for international phone numbers with support for various formats.
    """
    def __init__(self, config=None):
        self.config = config or {}
        # Improved pattern to handle various international formats
        # Supports: +49-30-123-4567, +1-555-123-4567, +44-20-7946-0958, etc.
        self.pattern = re.compile(r"\+\d{1,3}[-.\s]?\d{1,5}[-.\s]?\d{3,4}[-.\s]?\d{3,4}")

    def recognize(self, text):
        matches = []
        for match in self.pattern.finditer(text):
            matches.append({
                "entity_type": "PHONE_NUMBER",
                "start": match.start(),
                "end": match.end(),
                "score": 1.0
            })
        return matches

class RegexPhoneRecognizerPlugin(RecognizerPlugin):
    """
    Plugin wrapper for RegexPhoneRecognizer.
    """
    def get_metadata(self):
        return PluginMetadata(
            name="regex_phone_recognizer",
            version="1.0.0",
            description="Detects international phone numbers using regex.",
            author="Your Name",
            plugin_type=PluginType.RECOGNIZER,
            dependencies=[],
            config_schema={}
        )

    def initialize(self):
        self.recognizer = RegexPhoneRecognizer(self.config)
        return True

    def is_available(self):
        return True

    def create_recognizer(self):
        return self.recognizer

    def recognize(self, text, language="en"):
        return self.recognizer.recognize(text) 