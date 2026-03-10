import re
from presidio_analyzer import Pattern, PatternRecognizer

class UserIdRecognizer(PatternRecognizer):
    PATTERNS = [
        Pattern("User ID", r"[a-z]{2}\d{4}[a-z]{4}", 0.5)
    ]
    def __init__(self):
        super().__init__(
            supported_entity="USER_ID",
            patterns=self.PATTERNS,
            supported_language="en"
        )

    def recognize(self, text, language="en"):
        return self.analyze(text, entities=["USER_ID"]) 