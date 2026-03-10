import re

class GermanPhoneRecognizer:
    """
    Specialized recognizer for German phone numbers with support for various formats.
    """
    def __init__(self, config=None):
        self.config = config or {}
        # Multiple patterns for different German phone formats
        self.patterns = [
            # International format: +49-30-123-4567
            re.compile(r"\+\d{1,3}[-.\s]?\d{1,5}[-.\s]?\d{3,4}[-.\s]?\d{3,4}"),
            # Local format: 030-123-4567
            re.compile(r"\b0\d{1,4}[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b"),
            # Mobile format: 0176-123-4567
            re.compile(r"\b01[567]\d[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b"),
            # With parentheses: (030) 123-4567
            re.compile(r"\(\d{1,4}\)[-.\s]?\d{3,4}[-.\s]?\d{3,4}"),
            # Space separated: 030 123 4567
            re.compile(r"\b0\d{1,4}\s\d{3,4}\s\d{3,4}\b"),
            # Mobile space separated: 0176 123 4567
            re.compile(r"\b01[567]\d\s\d{3,4}\s\d{3,4}\b")
        ]

    def recognize(self, text, language="de"):
        matches = []
        seen_positions = set()  # Avoid duplicate matches
        
        for pattern in self.patterns:
            for match in pattern.finditer(text):
                start, end = match.start(), match.end()
                
                # Check if this position overlaps with existing matches
                overlap = False
                for existing_start, existing_end in seen_positions:
                    if (start < existing_end and end > existing_start):
                        overlap = True
                        break
                
                if not overlap:
                    matches.append({
                        "entity_type": "PHONE_NUMBER",
                        "start": start,
                        "end": end,
                        "score": 1.0
                    })
                    seen_positions.add((start, end))
        
        return matches 