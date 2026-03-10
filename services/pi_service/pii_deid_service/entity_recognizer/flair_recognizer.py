# Portions of this file are adapted from Microsoft Presidio, licensed under the MIT License.
# See https://github.com/microsoft/presidio for original source.
# based on https://github.com/microsoft/presidio/blob/main/docs/samples/python/flair_recognizer.py

import logging
from typing import Optional, List, Tuple, Set
import os

from presidio_analyzer import (
    RecognizerResult,
    EntityRecognizer,
    AnalysisExplanation,
)
from presidio_analyzer.nlp_engine import NlpArtifacts
from flair.data import Sentence
from flair.models import SequenceTagger


class FlairRecognizer(EntityRecognizer):
    """
    Wrapper for a flair model, if needed to be used within Presidio Analyzer.

    :example:
    >from presidio_analyzer import AnalyzerEngine, RecognizerRegistry

    >flair_recognizer = FlairRecognizer()

    >registry = RecognizerRegistry()
    >registry.add_recognizer(flair_recognizer)

    >analyzer = AnalyzerEngine(registry=registry)

    >results = analyzer.analyze(
    >    "My name is Christopher and I live in Irbid.",
    >    language="en",
    >    return_decision_process=True,
    >)
    >for result in results:
    >    print(result)
    >    print(result.analysis_explanation)
    """

    MODEL_LANGUAGES = {
        "en": "flair/ner-english-large",
        "es": "flair/ner-spanish-large",
        "de": "flair/ner-german-large",
        "nl": "flair/ner-dutch-large",
    }

    def __init__(
            self,
            model_path: str = None,
            model_config: dict = None,
    ):
        if model_path == "" or model_path is None:
            raise ValueError("model_path cannot be empty")
        if model_config == "" or model_config is None:
            raise ValueError("model_config cannot be empty")

        # If model_path is a .txt file, read the actual model path from the file
        if model_path.endswith('.txt') and os.path.isfile(model_path):
            with open(model_path, 'r', encoding='utf-8') as f:
                model_path = f.read().strip()

        # Error handling for missing model file
        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"Model file not found at {model_path}. Please download the required model and update your configuration file with the correct path."
            )

        supported_language = model_config["SUPPORTED_LANGUAGE"]
        supported_entities = model_config["PRESIDIO_SUPPORTED_ENTITIES"]
        self.default_explanation = model_config["DEFAULT_EXPLANATION"]
        self.check_label_groups = model_config["CHECK_LABEL_GROUPS"]
        self.presidio_equivalences = model_config["PRESIDIO_EQUIVALENCES"]

        self.model = SequenceTagger.load(model_path)

        super().__init__(
            supported_entities=supported_entities,
            supported_language=supported_language,
            name="Flair Analytics",
        )

    def load(self) -> None:
        """
        Load the model.

        Not used: Model is loaded during initialization.
        """
        pass

    def get_supported_entities(self) -> List[str]:
        """
        Return supported entities by this model.

        :return: List of the supported entities.
        """
        return self.supported_entities

    # Class to use Flair with Presidio as an external recognizer.
    def analyze(
            self, text: str, entities: List[str], nlp_artifacts: NlpArtifacts = None
    ) -> List[RecognizerResult]:
        """
        Analyze text using Text Analytics.

        :param text: The text for analysis.
        :param entities: Not working properly for this recognizer.
        :param nlp_artifacts: Not used by this recognizer.
        :param language: Text language. Supported languages in MODEL_LANGUAGES
        :return: The list of Presidio RecognizerResult constructed from the recognized
            Flair detections.
        """

        results = []

        sentences = Sentence(text)
        self.model.predict(sentences)

        # If there are no specific list of entities, we will look for all of it.
        if not entities:
            entities = self.supported_entities

        for entity in entities:
            if entity not in self.supported_entities:
                continue

            for ent in sentences.get_spans("ner"):
                if not self.__check_label(
                        entity, ent.labels[0].value, self.check_label_groups
                ):
                    continue
                textual_explanation = self.default_explanation.format(
                    ent.labels[0].value
                )
                explanation = self.build_flair_explanation(
                    round(ent.score, 2), textual_explanation
                )
                flair_result = self._convert_to_recognizer_result(ent, explanation)

                results.append(flair_result)

        return results

    def _convert_to_recognizer_result(self, entity, explanation) -> RecognizerResult:

        entity_type = self.presidio_equivalences.get(entity.tag, entity.tag)
        flair_score = round(entity.score, 2)

        flair_results = RecognizerResult(
            entity_type=entity_type,
            start=entity.start_position,
            end=entity.end_position,
            score=flair_score,
            analysis_explanation=explanation,
        )

        return flair_results

    def build_flair_explanation(
            self, original_score: float, explanation: str
    ) -> AnalysisExplanation:
        """
        Create explanation for why this result was detected.

        :param original_score: Score given by this recognizer
        :param explanation: Explanation string
        :return:
        """
        explanation = AnalysisExplanation(
            recognizer=self.__class__.__name__,
            original_score=original_score,
            textual_explanation=explanation,
        )
        return explanation

    @staticmethod
    def __check_label(
            entity: str, label: str, check_label_groups: List[Tuple[Set[str], Set[str]]]
    ) -> bool:
        return any(
            [entity in egrp and label in lgrp for egrp, lgrp in check_label_groups]
        )


if __name__ == "__main__":

    from presidio_analyzer import AnalyzerEngine, RecognizerRegistry

    flair_recognizer = (
        FlairRecognizer()
    )  # This would download a very large (+2GB) model on the first run

    registry = RecognizerRegistry()
    registry.add_recognizer(flair_recognizer)

    analyzer = AnalyzerEngine(registry=registry)

    results = analyzer.analyze(
        "My name is Christopher and I live in Irbid.",
        language="en",
        return_decision_process=True,
    )
    for result in results:
        print(result)
        print(result.analysis_explanation)
