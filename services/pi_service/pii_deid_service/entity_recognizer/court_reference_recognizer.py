# based on https://github.com/microsoft/presidio/blob/main/presidio-analyzer/presidio_analyzer/predefined_recognizers/credit_card_recognizer.py

from typing import List, Optional
from presidio_analyzer import Pattern, PatternRecognizer

class CourtReferenceRecognizer(PatternRecognizer):
    """
    Recognize common court references (Gerichtzeichen) using regex.

    :param patterns: List of patterns to be used by this recognizer
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "Court References",
            r"\d{1,3}\s([a-zA-Z]{1,2}|(M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})))\s\d{1,6}\/(19|20)?\d{2}(\s?\(\d{1,4}\))?",  # see 01_data-visualization.ipynb
            0.3,
        ),
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        supported_language: str = "en",
        supported_entity: str = "COURT_REFERENCE",
    ):

        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            supported_language=supported_language
        )

    def recognize(self, text, language="en"):
        return self.analyze(text, entities=["COURT_REFERENCE"])