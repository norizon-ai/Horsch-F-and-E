#!/usr/bin/env python3
"""
Basic Usage Example - PII De-identification Service
==================================================

This example shows the simplest way to use the modular PII de-identification system.
Perfect for beginners who want to quickly get started.

Usage:
    python examples/basic_usage.py
"""

import json
import sys
from pathlib import Path

# Add the project root to the path so we can import our modules
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.config_manager import config_manager
from pii_deid_service.pipeline import run_pipeline

def main():
    """Demonstrate basic usage of the PII de-identification system."""
    
    print("🔒 BASIC USAGE EXAMPLE")
    print("=" * 50)
    print("This example shows the simplest way to anonymize text with PII.\n")
    
    # Step 1: Load a simple pipeline configuration
    print("📋 Step 1: Loading pipeline configuration...")
    try:
        pipeline_config = config_manager.load_pipeline_config("user_configs/pipelines/anonymization_pipeline.json")
        print("✅ Pipeline configuration loaded successfully")
    except Exception as e:
        print(f"❌ Error loading configuration: {e}")
        return
    
    # Step 2: Build the pipeline
    print("\n🔧 Step 2: Building pipeline...")
    try:
        builder = PluginBasedPipelineBuilder()
        builder.initialize()
        pipeline = builder.build_pipeline(pipeline_config)
        print("✅ Pipeline built successfully")
        print(f"   - Recognizers: {len(pipeline['recognizers'])}")
        print(f"   - Operators: {len(pipeline['operators'])}")
    except Exception as e:
        print(f"❌ Error building pipeline: {e}")
        return
    
    # Step 3: Process sample text
    print("\n📝 Step 3: Processing sample text...")
    
    # Sample text with PII
    sample_text = "Hello, my name is John Doe and my email is john.doe@company.com. Please call me at +1-555-123-4567. I live in New York, NY."
    
    print(f"Original text: {sample_text}")
    
    try:
        # Process using the plugin-based pipeline
        result = run_pipeline(pipeline, sample_text)
        
        if result:
            print(f"✅ Anonymized text: {result}")
        else:
            print("❌ Failed to process text")
            
    except Exception as e:
        print(f"❌ Error processing text: {e}")
        return
    
    print("\n🎉 Basic usage example completed successfully!")
    print("\n💡 Next steps:")
    print("   - Try the intermediate_usage.py example for more features")
    print("   - Check the advanced_usage.py example for complex scenarios")
    print("   - Run 'python user_interface.py' for the interactive interface")

if __name__ == "__main__":
    main() 