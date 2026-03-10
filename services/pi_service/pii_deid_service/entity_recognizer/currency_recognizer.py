# based on https://github.com/microsoft/presidio/blob/main/presidio-analyzer/presidio_analyzer/predefined_recognizers/credit_card_recognizer.py

from typing import List, Optional
from presidio_analyzer import Pattern, PatternRecognizer

class CurrencyRecognizer(PatternRecognizer):
    """
    Recognize common currency formats (euro and usd) using regex.

    :param patterns: List of patterns to be used by this recognizer
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "EURO",
            r"((\d{1,}(([\.\,])?\d{3}){0,}))([\,\.]\d{0,2})?\s?(€|EURO|EUR)",
            1.0,
        ),
    ]

    CONTEXT = [
        "EURO",
        "EUR",
        "€",
        "$",
        "USD",
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        supported_language: str = "en",
        supported_entity: str = "AMOUNT",
    ):

        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            supported_language=supported_language,
        )

    def recognize(self, text, language="en"):
        return self.analyze(text, entities=["AMOUNT"])
