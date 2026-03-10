# based on https://github.com/microsoft/presidio/blob/main/presidio-analyzer/presidio_analyzer/predefined_recognizers/credit_card_recognizer.py

from typing import List, Optional
from presidio_analyzer import Pattern, PatternRecognizer

class ReferenceCodeRecognizer(PatternRecognizer):
    """
    Recognize common reference codes that are not file numbers or court references references using regex.

    :param patterns: List of patterns to be used by this recognizer
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "References Codes - Type I",
            r"\d{1,3}\/\d{1,2}\s?\/[\w\W]{1,2}(\/[a-zA-Z]{1,2})?", #CUSTOM_PATTERN based on data in column IhrZeichen or UnserZeichen
            0.3,
        ),
        Pattern(
            "Reference Codes - Type II",
            r"\d{1,6}\s?\/\s?\d{2}", # CUSTOM_PATTERN based on data in column IhrZeichen or UnserZeichen,
            0.3
        )
    ]
    
    

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        supported_language: str = "en",
        supported_entity: str = "REFERENCE_CODE",
    ):

        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            supported_language=supported_language,
        )

    def recognize(self, text, language="en"):
        return self.analyze(text, entities=["REFERENCE_CODE"])