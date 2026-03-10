# based on https://github.com/microsoft/presidio/blob/main/presidio-analyzer/presidio_analyzer/predefined_recognizers/credit_card_recognizer.py

from typing import List, Optional
from presidio_analyzer import Pattern, PatternRecognizer

class FileNumberRecognizer(PatternRecognizer):
    """
    Recognize common file numbers (Aktenzeichen) using regex.

    :param patterns: List of patterns to be used by this recognizer
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "File Numbers",
            r"\d{1,6}-(19|20)\d{2}\/\d{3}:\d{2}",  # see 01_data-visualization.ipynb
            0.3,
        ),
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        supported_language: str = "en",
        supported_entity: str = "FILE_NUMBER",
    ):

        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            supported_language=supported_language,
        )

    def recognize(self, text, language="en"):
        return self.analyze(text, entities=["FILE_NUMBER"])
