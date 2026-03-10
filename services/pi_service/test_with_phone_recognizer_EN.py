#!/usr/bin/env python3
"""
User-Friendly Interface for Modular PII De-identification Service (Multi-Recognizer Demo)

This script demonstrates how using multiple recognizers in the pipeline
improves PII detection and anonymization, especially for formats missed by default recognizers.
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List

# Import pipeline components
from pii_deid_service.pipeline.monitor import PipelineMonitor
from pii_deid_service.config_management.plugin_schemas import PluginPipelineConfig
from pii_deid_service.pipeline import run_pipeline

def process_with_all_recognizers(pipeline, text):
    """Process text using all recognizers in the pipeline and combine results."""
    all_entities = []
    recognizer_results = []
    for recognizer in pipeline["recognizers"]:
        entities = recognizer.recognize(text)
        
        recognizer_results.append((recognizer.__class__.__name__, entities))
        
        all_entities.extend(entities)
        
    # Optionally deduplicate entities (by span/type)
    seen = set()
    deduped_entities = []
    for ent in all_entities:
        key = (ent["start"], ent["end"], ent["entity_type"])
        if key not in seen:
            deduped_entities.append(ent)
            seen.add(key)
    return deduped_entities, recognizer_results

def print_banner():
    print("=" * 70)
    print("🔒 MODULAR PII DE-IDENTIFICATION SERVICE (MULTI-RECOGNIZER DEMO)")
    print("=" * 70)
    print("Demonstrates the impact of using multiple recognizers in the pipeline.")
    print("=" * 70)

def build_and_run_pipeline(config_path):
    print("\n🚀 BUILDING AND RUNNING PIPELINE")
    print("-" * 40)
    try:
        from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
        with open(config_path, "r", encoding="utf-8") as f:
            config_data = json.load(f)
        config = PluginPipelineConfig(**config_data)
        builder = PluginBasedPipelineBuilder()
        if not builder.initialize():
            print("❌ Failed to initialize pipeline builder")
            return None
        pipeline = builder.build_pipeline(config)
        if not pipeline:
            print("❌ Failed to build pipeline")
            return None
        print("✅ Pipeline built successfully")
        print(f"  - Recognizers: {len(pipeline['recognizers'])}")
        print(f"  - Operators: {len(pipeline['operators'])}")
        return pipeline
    except Exception as e:
        print(f"❌ Error building pipeline: {e}")
        return None

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

def main():
    print_banner()
    config_path = "user_configs/pipelines/simple_pipeline.json"
    pipeline = build_and_run_pipeline(config_path)
    if not pipeline:
        return 1
    process_english_sample_data(pipeline)
    print("\n" + "=" * 70)
    print("🎉 DEMO COMPLETE! See above for the results using multiple recognizers.")
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main()) 