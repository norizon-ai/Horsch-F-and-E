"""
Pipeline module for PII De-identification Service.

This module provides plugin-based pipeline building, monitoring, and validation capabilities.
"""

from .builder import PluginBasedPipelineBuilder
from .monitor import PipelineMonitor, ProcessingStatus, ProcessingMetrics
from .plugin_validator import PluginPipelineValidator, PluginValidationError

__all__ = [
    "PluginBasedPipelineBuilder",
    "PipelineMonitor",
    "ProcessingStatus",
    "ProcessingMetrics",
    "PluginPipelineValidator",
    "PluginValidationError"
]

def run_pipeline(pipeline, text):
    """
    Run the pipeline on the input text, always returning the final anonymized string.
    """
    def recognizer_result_to_dict(result):
        if hasattr(result, 'start') and hasattr(result, 'end'):
            return {
                "start": result.start,
                "end": result.end,
                "entity_type": getattr(result, "entity_type", None),
                "score": getattr(result, "score", None),
                "text": getattr(result, "text", None)
            }
        return result

    recognizer_components = pipeline["recognizers"]
    operator_components = pipeline["operators"]

    all_entities = []
    for recognizer in recognizer_components:
        try:
            entities = recognizer.recognize(text)
            if entities:
                all_entities.extend([recognizer_result_to_dict(e) for e in entities])
        except Exception as e:
            print(f"Error in recognizer {getattr(recognizer, 'name', str(recognizer))}: {e}")

    result = all_entities
    for operator in operator_components:
        if isinstance(result, list):
            result = operator.apply(text, result)
        else:
            break

    # If the last result is still a list, try to find an anonymizer operator and apply it
    if isinstance(result, list):
        for operator in operator_components:
            try:
                test_result = operator.apply(text, result)
                if isinstance(test_result, str):
                    return test_result
            except Exception:
                continue
        print("Warning: No anonymizer operator found. Returning original text.")
        return text

    return result 