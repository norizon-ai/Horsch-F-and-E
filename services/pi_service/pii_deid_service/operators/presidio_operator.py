"""
PresidioOperator wrapper for plugin system.

This class wraps presidio_anonymizer.AnonymizerEngine for use as a plugin operator.
"""

from presidio_anonymizer import AnonymizerEngine
from typing import List, Dict, Any

class PresidioOperator:
    def __init__(self, language: str = "en", anonymization_method: str = "replace"):
        self.language = language
        self.anonymization_method = anonymization_method
        self.engine = AnonymizerEngine()

    def apply(self, text: str, entities: List[Dict[str, Any]]) -> str:
        # entities: list of dicts with start, end, entity_type, etc.
        try:
            # Convert our entity format to Presidio's RecognizerResult format
            from presidio_analyzer import RecognizerResult
            analyzer_results = []
            for ent in entities:
                result = RecognizerResult(
                    entity_type=ent["entity_type"],
                    start=ent["start"],
                    end=ent["end"],
                    score=ent.get("score", 1.0)
                )
                analyzer_results.append(result)
            
            # Create anonymization operators in the correct format
            from presidio_anonymizer.entities import OperatorConfig
            operators = {}
            for ent in entities:
                entity_type = ent["entity_type"]
                if entity_type not in operators:
                    operators[entity_type] = OperatorConfig(self.anonymization_method)
            
            result = self.engine.anonymize(
                text=text,
                analyzer_results=analyzer_results,
                operators=operators
            )
            return result.text
        except Exception as e:
            print(f"Error in Presidio anonymization: {e}")
            return text 