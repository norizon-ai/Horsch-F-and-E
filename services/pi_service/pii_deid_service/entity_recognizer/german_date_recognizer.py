# based on https://github.com/microsoft/presidio/blob/main/presidio-analyzer/presidio_analyzer/predefined_recognizers/credit_card_recognizer.py

from typing import List, Optional
from presidio_analyzer import Pattern, PatternRecognizer

class GermanDateRecognizer(PatternRecognizer):
    """
    Recognize common german date formats using regex.

    :param patterns: List of patterns to be used by this recognizer
    :param supported_language: Language this recognizer supports
    :param supported_entity: The entity this recognizer can detect
    """

    PATTERNS = [
        Pattern(
            "Day (Full)",
            r"Montag|Dienstag|Mittwoch|Donnerstag|Freitag|Samstag|Sonntag",
            1.0,
        ),
        
        Pattern(
            "Day (Short)",
            r"(Mo|M0|Di|Dl|D1|Mi|Ml|M1|Do|D0|Fr|Sa|So|S0)(?=[\.\,])",
            0.3,
        ),
        
        # https://stackoverflow.com/questions/69695218/capture-german-date-formats-using-regex
        Pattern(
            "Date",
            r"""(?x)(?<!d)(?:(?:(?:0?[1-9]|[12]\d)|3[01])\s?[./:-][\s.]?(?:0?[13578]|1[02]|J(?:an(?:uar)?|uli?)|M(?:ärz?|ai)|Aug(?:ust)?|Dez(?:ember)?|(O|0)kt(?:ober)?)\s?(?:[./:-][\s.]?)?[1-9]\d\d\d|(?:(?:0?[1-9]|[12]\d)|30)\s?[./:-][\s.]?(?:0?[13-9]|1[012]|J(?:an(?:uar)?|u[nl]i?)|M(?:ärz?|ai)|A(?:pr(?:il)?|ug(?:ust)?)|Sep(?:tember)?|(?:Nov|Dez)(?:ember)?|(O|0)kt(?:ober)?)\s?(?:[./:-][\s.]?)?[1-9]\d\d\d|(?:0?[1-9]|[12]\d)\s?[./:-][\s.]?(?:0?2|Fe(?:b(?:ruar)?)?)\s?(?:[./:-][\s.]?)?[1-9]\d(?:[02468][048]|[13579][26])|(?:0?[1-9]|[12][0-8])\s?[./:-][\s.]?(?:0?2|Fe(?:b(?:ruar)?)?)\s?(?:[./:-][\s.]?)?[1-9]\d\d\d
)(?!\d)""",

            0.2,
        ),
        
        Pattern(
            "Time of Day",
            r"(?<=\s)([012]?[0-9])[\.\:]([0-5][0-9])(?=\s)",
            0.3,
        ),
        
        Pattern(
            "Date without Day",
            r"""(Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)\s{0,}(([12]\d{3})|(\d{2}))""",
            0.5
        )
    ]

    CONTEXT = [
        "am",
        "uhr",
        "datum",
        "-",
        "den",
        "dem",
        "bis"
    ]

    def __init__(
        self,
        patterns: Optional[List[Pattern]] = None,
        supported_language: str = "en",
        supported_entity: str = "DATE_TIME",
    ):

        patterns = patterns if patterns else self.PATTERNS
        super().__init__(
            supported_entity=supported_entity,
            patterns=patterns,
            supported_language=supported_language,
        )

    def recognize(self, text, language="en"):
        return self.analyze(text, entities=["DATE_TIME"])
