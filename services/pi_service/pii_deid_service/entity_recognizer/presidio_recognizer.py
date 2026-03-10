"""
PresidioRecognizer wrapper for plugin system.

This class wraps presidio_analyzer.AnalyzerEngine for use as a plugin recognizer.
"""

from presidio_analyzer import AnalyzerEngine
from typing import List, Dict, Any

class PresidioRecognizer:
    def __init__(self, language: str = "en", entities: List[str] = None):
        self.language = language
        self.entities = entities or ["PERSON", "EMAIL", "PHONE_NUMBER"]
        self.engine = AnalyzerEngine()

    def recognize(self, text: str, language: str = None) -> List[Dict[str, Any]]:
        lang = language or self.language
        try:
            results = self.engine.analyze(text=text, language=lang, entities=self.entities)
            # Convert RecognizerResult objects to dicts
            entities = []
            for r in results:
                entity_dict = {
                    "start": r.start,
                    "end": r.end,
                    "entity_type": r.entity_type,
                    "score": r.score,
                    "text": text[r.start:r.end]
                }
                entities.append(entity_dict)
            return entities
        except Exception as e:
            print(f"Error in Presidio recognition: {e}")
            return [] 