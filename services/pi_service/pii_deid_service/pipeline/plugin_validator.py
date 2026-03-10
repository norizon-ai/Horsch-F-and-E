"""
Plugin-based Pipeline Validator for PII De-identification Service.

This module validates plugin-based pipeline configurations before execution.
"""

import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)


class PluginValidationError(Exception):
    """Raised when plugin pipeline validation fails."""
    pass


class PluginPipelineValidator:
    """Validates plugin-based pipeline configurations before execution."""

    @staticmethod
    def validate_pipeline(pipeline: Dict[str, Any]) -> List[str]:
        """Validate a plugin-based pipeline configuration.
        
        Args:
            pipeline: Plugin-based pipeline dictionary to validate
            
        Returns:
            List of validation warnings (empty if all valid)
            
        Raises:
            PluginValidationError: If validation fails
        """
        warnings = []
        
        try:
            # Validate pipeline structure
            structure_warnings = PluginPipelineValidator._validate_pipeline_structure(pipeline)
            warnings.extend(structure_warnings)
            
            # Validate models
            if "models" in pipeline:
                model_warnings = PluginPipelineValidator._validate_plugin_models(pipeline["models"])
                warnings.extend(model_warnings)
            
            # Validate recognizers
            if "recognizers" in pipeline:
                recognizer_warnings = PluginPipelineValidator._validate_plugin_recognizers(pipeline["recognizers"])
                warnings.extend(recognizer_warnings)
            
            # Validate operators
            if "operators" in pipeline:
                operator_warnings = PluginPipelineValidator._validate_plugin_operators(pipeline["operators"])
                warnings.extend(operator_warnings)
            
            logger.info(f"Plugin pipeline validation completed with {len(warnings)} warnings")
            return warnings
            
        except Exception as e:
            logger.error(f"Plugin pipeline validation failed: {e}")
            raise PluginValidationError(f"Plugin pipeline validation failed: {e}")

    @staticmethod
    def _validate_pipeline_structure(pipeline: Dict[str, Any]) -> List[str]:
        """Validate the basic pipeline structure."""
        warnings = []
        
        # Check required fields
        required_fields = ["name"]
        for field in required_fields:
            if field not in pipeline:
                warnings.append(f"Missing required field: {field}")
        
        # Check that at least one component type is present
        component_types = ["models", "recognizers", "operators"]
        if not any(comp_type in pipeline for comp_type in component_types):
            warnings.append("Pipeline must contain at least one component type (models, recognizers, or operators)")
        
        return warnings

    @staticmethod
    def _validate_plugin_models(models: List[Any]) -> List[str]:
        """Validate plugin model components."""
        warnings = []
        
        if not models:
            warnings.append("No models configured in pipeline")
            return warnings
        
        # Check that models are properly instantiated
        for i, model in enumerate(models):
            if model is None:
                warnings.append(f"Model at index {i} is None")
            elif not hasattr(model, 'predict'):
                warnings.append(f"Model at index {i} does not have required 'predict' method")
        
        return warnings

    @staticmethod
    def _validate_plugin_recognizers(recognizers: List[Any]) -> List[str]:
        """Validate plugin recognizer components."""
        warnings = []
        
        if not recognizers:
            warnings.append("No recognizers configured in pipeline")
            return warnings
        
        # Check that recognizers are properly instantiated
        for i, recognizer in enumerate(recognizers):
            if recognizer is None:
                warnings.append(f"Recognizer at index {i} is None")
            elif not hasattr(recognizer, 'recognize'):
                warnings.append(f"Recognizer at index {i} does not have required 'recognize' method")
        
        return warnings

    @staticmethod
    def _validate_plugin_operators(operators: List[Any]) -> List[str]:
        """Validate plugin operator components."""
        warnings = []
        
        if not operators:
            warnings.append("No operators configured in pipeline")
            return warnings
        
        # Check that operators are properly instantiated
        for i, operator in enumerate(operators):
            if operator is None:
                warnings.append(f"Operator at index {i} is None")
            elif not hasattr(operator, 'apply'):
                warnings.append(f"Operator at index {i} does not have required 'apply' method")
        
        return warnings

    @staticmethod
    def validate_plugin_component(component: Any, component_type: str) -> List[str]:
        """Validate a single plugin component."""
        warnings = []
        
        if component is None:
            warnings.append(f"{component_type} component is None")
            return warnings
        
        # Check for required methods based on component type
        required_methods = {
            "model": ["predict"],
            "recognizer": ["recognize"],
            "operator": ["apply"]
        }
        
        if component_type in required_methods:
            for method in required_methods[component_type]:
                if not hasattr(component, method):
                    warnings.append(f"{component_type} component missing required method: {method}")
        
        return warnings 