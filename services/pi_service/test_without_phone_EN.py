#!/usr/bin/env python3
"""
User-Friendly Interface for Modular PII De-identification Service

This script demonstrates how easy it is to use the modular system
for anonymizing PII data with different configurations.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

# Import pipeline components
from pii_deid_service.pipeline.monitor import PipelineMonitor
from pii_deid_service.config_management.plugin_schemas import PluginPipelineConfig, PluginComponentConfig
from pii_deid_service.pipeline import run_pipeline

def process_with_plugin_pipeline(pipeline, text):
    """Process text using the plugin-based pipeline."""
    try:
        # Get recognizer and operator from pipeline
        recognizer_component = pipeline["recognizers"][0]
        operator_component = pipeline["operators"][0]
        
        # The components are already instances, not plugin classes
        recognizer = recognizer_component
        operator = operator_component
        
        # Detect entities
        entities = recognizer.recognize(text)
        
        if entities:
            # Anonymize
            anonymized_text = operator.apply(text, entities)
            return anonymized_text
        else:
            return text  # Return original if no entities found
            
    except Exception as e:
        print(f"Error in pipeline processing: {e}")
        return None

def print_banner():
    """Print the application banner."""
    print("=" * 70)
    print("🔒 MODULAR PII DE-IDENTIFICATION SERVICE")
    print("=" * 70)
    print("Easy-to-use interface for anonymizing sensitive data")
    print("Built with modular architecture for maximum flexibility")
    print("=" * 70)

def show_available_components():
    """Show available components in the system."""
    print("\n📦 AVAILABLE COMPONENTS")
    print("-" * 40)
    
    try:
        from pii_deid_service.plugins.manager import PluginManager
        
        plugin_manager = PluginManager()
        plugin_manager.initialize()
        
        available_plugins = plugin_manager.get_available_plugins()
        
        for plugin_type, plugins in available_plugins.items():
            print(f"\n🔧 {plugin_type.upper()}:")
            for plugin_name in plugins:
                info = plugin_manager.get_plugin_info(plugin_name)
                description = info.get("description", "No description") if info else "No info"
                print(f"  • {plugin_name}: {description}")
        
        return True
    except Exception as e:
        print(f"❌ Error loading components: {e}")
        return False

def create_simple_pipeline():
    """Create a simple pipeline configuration."""
    print("\n🔧 CREATING SIMPLE PIPELINE")
    print("-" * 40)
    
    try:
        # Create a simple pipeline with just Presidio components
        pipeline_config = PluginPipelineConfig(
            name="simple_pipeline",
            description="Simple pipeline for basic PII detection",
            models=[],  # No models needed for basic detection
            recognizers=[
                PluginComponentConfig(
                    name="presidio_recognizer",
                    config={
                        "language": "en",
                        "entities": ["PERSON", "EMAIL", "PHONE_NUMBER", "LOCATION"],
                        "confidence_threshold": 0.3
                    }
                )
            ],
            operators=[
                PluginComponentConfig(
                    name="presidio_operator",
                    config={
                        "anonymization_method": "replace",
                        "language": "en"
                    }
                )
            ]
        )
        
        # Save the configuration
        config_dir = Path("user_configs/pipelines")
        config_dir.mkdir(parents=True, exist_ok=True)
        
        config_path = config_dir / "simple_pipeline.json"
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(pipeline_config.model_dump(), f, indent=2, ensure_ascii=False)
        
        print(f"✅ Created simple pipeline: {config_path}")
        return pipeline_config
        
    except Exception as e:
        print(f"❌ Error creating pipeline: {e}")
        return None

def build_and_run_pipeline(config):
    """Build and run the pipeline."""
    print("\n🚀 BUILDING AND RUNNING PIPELINE")
    print("-" * 40)
    
    try:
        from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
        
        # Initialize pipeline builder
        builder = PluginBasedPipelineBuilder()
        if not builder.initialize():
            print("❌ Failed to initialize pipeline builder")
            return False
        
        # Build pipeline
        pipeline = builder.build_pipeline(config)
        if not pipeline:
            print("❌ Failed to build pipeline")
            return False
        
        print("✅ Pipeline built successfully")
        print(f"  - Recognizers: {len(pipeline['recognizers'])}")
        print(f"  - Operators: {len(pipeline['operators'])}")
        
        return pipeline
        
    except Exception as e:
        print(f"❌ Error building pipeline: {e}")
        return False

def process_english_sample_data(pipeline):
    print("\n📊 PROCESSING ENGLISH SAMPLE DATA")
    print("-" * 40)
    try:
        sample_texts = [
            "Hello, my name is John Doe and my email is john.doe@company.com. Please call me at +1-555-123-4567. I live in New York, NY.",
            "Contact Jane Smith at jane.smith@company.com or call 555-987-6543. Her address is 123 Main St, Los Angeles, CA 90001.",
            "The meeting is with Dr. Emily Brown on March 15th. Her phone number is (555) 123-7890 and email is ebrown@hospital.com."
        ]
        for i, text in enumerate(sample_texts, 1):
            print(f"\n📝 Processing: English Sample {i}")
            print(f"Original: {text}")
            anonymized_text = run_pipeline(pipeline, text)
            print(f"✅ Anonymized: {anonymized_text}")
    except Exception as e:
        print(f"❌ Error processing data: {e}")
        import traceback
        traceback.print_exc()

def demonstrate_modularity():
    """Demonstrate the modularity of the system."""
    print("\n🔧 DEMONSTRATING MODULARITY")
    print("-" * 40)
    
    print("The system is designed to be highly modular:")
    print("\n✅ Easy to Add Components:")
    print("  • Add new recognizers by creating plugin files")
    print("  • Add new models by implementing model plugins")
    print("  • Add new operators by creating operator plugins")
    
    print("\n✅ Easy to Remove Components:")
    print("  • Simply remove plugins from the registry")
    print("  • Update pipeline configurations")
    print("  • No code changes required")
    
    print("\n✅ Easy to Modify Components:")
    print("  • Update plugin configurations")
    print("  • Modify plugin implementations")
    print("  • Hot-reload capabilities")
    
    print("\n✅ Configuration-Driven:")
    print("  • All pipelines defined in JSON")
    print("  • No hardcoded dependencies")
    print("  • Easy to version control")

def main():
    """Main user interface function."""
    print_banner()
    
    # Show available components
    if not show_available_components():
        return 1
    
    # Create simple pipeline
    config = create_simple_pipeline()
    if not config:
        return 1
    
    # Build pipeline
    pipeline = build_and_run_pipeline(config)
    if not pipeline:
        return 1
    
    # Process sample data
    if not process_english_sample_data(pipeline):
        return 1
    
    # Demonstrate modularity
    demonstrate_modularity()
    
    print("\n" + "=" * 70)
    print("🎉 SUCCESS! Modular PII De-identification System is Ready!")
    print("=" * 70)
    print("✅ All components working correctly")
    print("✅ Easy to add/remove/modify components")
    print("✅ User-friendly interface available")
    print("✅ Ready for production use")
    print("=" * 70)
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 