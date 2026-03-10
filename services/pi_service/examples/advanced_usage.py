#!/usr/bin/env python3
"""
Advanced Usage Example - PII De-identification Service
=====================================================

This example shows advanced features like custom pipeline configuration,
batch processing, and monitoring. Perfect for production use cases.

Usage:
    python examples/advanced_usage.py
"""

import json
import sys
from pathlib import Path
from datetime import datetime
import time

# Add the project root to the path so we can import our modules
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.config_manager import config_manager
from pii_deid_service.pipeline.monitor import PipelineMonitor
from pii_deid_service.config_management.plugin_schemas import PluginPipelineConfig, PluginComponentConfig
from pii_deid_service.pipeline import run_pipeline

def main():
    """Demonstrate advanced usage with custom configuration and monitoring."""
    
    print("🔒 ADVANCED USAGE EXAMPLE")
    print("=" * 50)
    print("This example shows advanced features for production use.\n")
    
    # Step 1: Create a custom pipeline configuration
    print("📋 Step 1: Creating custom pipeline configuration...")
    custom_config = create_custom_pipeline_config()
    
    # Step 2: Build the custom pipeline
    print("\n🔧 Step 2: Building custom pipeline...")
    try:
        builder = PluginBasedPipelineBuilder()
        builder.initialize()
        pipeline = builder.build_pipeline(custom_config)
        print("✅ Custom pipeline built successfully")
        print(f"   - Recognizers: {len(pipeline['recognizers'])}")
        print(f"   - Operators: {len(pipeline['operators'])}")
    except Exception as e:
        print(f"❌ Error building pipeline: {e}")
        return
    
    # Step 3: Set up monitoring
    print("\n📊 Step 3: Setting up monitoring...")
    monitor = PipelineMonitor("advanced_example")
    
    # Step 4: Batch process all data files
    print("\n📝 Step 4: Batch processing all data files...")
    batch_process_all_files(pipeline, monitor)
    
    # Step 5: Show monitoring results
    print("\n📈 Step 5: Processing summary...")
    show_processing_summary(monitor)
    
    print("\n🎉 Advanced usage example completed successfully!")
    print(f"📁 Check the 'examples/outputs/' directory for all results")

def create_custom_pipeline_config():
    """Create a custom pipeline configuration with specific settings."""
    
    # Create a custom pipeline with specific entity types and confidence thresholds
    custom_config = PluginPipelineConfig(
        name="custom_advanced_pipeline",
        description="Custom pipeline for advanced PII detection with high precision",
        models=[],  # No models for this example
        recognizers=[
            PluginComponentConfig(
                name="presidio_recognizer",
                config={
                    "language": "en",
                    "entities": [
                        "PERSON", 
                        "EMAIL", 
                        "PHONE_NUMBER", 
                        "LOCATION",
                        "CREDIT_CARD",
                        "IBAN_CODE",
                        "IP_ADDRESS"
                    ],
                    "confidence_threshold": 0.5  # Higher threshold for precision
                }
            )
        ],
        operators=[
            PluginComponentConfig(
                name="presidio_operator",
                config={
                    "anonymization_method": "replace",
                    "language": "en",
                    "analyzer_name": "presidio_analyzer"
                }
            )
        ]
    )
    
    # Save the custom configuration
    config_path = Path("user_configs/custom_advanced_pipeline.json")
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(custom_config.model_dump(), f, indent=2, ensure_ascii=False)
    
    print(f"✅ Custom configuration saved to: {config_path}")
    return custom_config

def batch_process_all_files(pipeline, monitor):
    """Process all data files in batch with monitoring."""
    
    # Define all data files to process
    data_files = [
        ("examples/data/sample_texts.json", "texts", process_texts_batch),
        ("examples/data/sample_emails.json", "emails", process_emails_batch),
        ("examples/data/sample_ticket.json", "ticket", process_ticket_batch)
    ]
    
    total_items = 0
    for file_path, data_type, processor in data_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if data_type == "ticket":
                item_count = 1  # Single ticket
            else:
                item_count = len(data.get(data_type, []))
            
            total_items += item_count
            
        except Exception as e:
            print(f"❌ Error reading {file_path}: {e}")
            continue
    
    # Start monitoring
    monitor.start_processing(total_items)
    
    # Process each file
    for file_path, data_type, processor in data_files:
        print(f"\n--- Processing {data_type.upper()} ---")
        try:
            processor(pipeline, monitor, file_path, data_type)
        except Exception as e:
            print(f"❌ Error processing {data_type}: {e}")
    
    # Complete monitoring
    monitor.complete_processing()

def process_texts_batch(pipeline, monitor, file_path, data_type):
    """Process texts in batch with monitoring."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    results = []
    for text_item in data["texts"]:
        start_time = time.time()
        
        # Anonymize the content
        anonymized_content = run_pipeline(pipeline, text_item["content"])
        
        processing_time = time.time() - start_time
        
        # Create result
        result = {
            "id": text_item["id"],
            "title": text_item["title"],
            "category": text_item["category"],
            "original_content": text_item["content"],
            "anonymized_content": anonymized_content,
            "processing_time": processing_time,
            "processed_at": datetime.now().isoformat()
        }
        results.append(result)
        
        # Update monitor
        entities_found = count_entities_in_text(text_item["content"], anonymized_content)
        monitor.update_progress(entities_found=entities_found)
        
        print(f"✅ {text_item['title']} - {entities_found} entities found")
    
    # Save results
    output_file = f"examples/outputs/batch_anonymized_{data_type}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"results": results, "metadata": {"total_items": len(results)}}, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Batch results saved to: {output_file}")

def process_emails_batch(pipeline, monitor, file_path, data_type):
    """Process emails in batch with monitoring."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    results = []
    for email in data["emails"]:
        start_time = time.time()
        
        # Anonymize the email body
        anonymized_body = run_pipeline(pipeline, email["body"])
        
        processing_time = time.time() - start_time
        
        # Create result
        result = {
            "id": email["id"],
            "subject": email["subject"],
            "from": email["from"],
            "to": email["to"],
            "original_body": email["body"],
            "anonymized_body": anonymized_body,
            "date": email["date"],
            "processing_time": processing_time,
            "processed_at": datetime.now().isoformat()
        }
        results.append(result)
        
        # Update monitor
        entities_found = count_entities_in_text(email["body"], anonymized_body)
        monitor.update_progress(entities_found=entities_found)
        
        print(f"✅ {email['subject']} - {entities_found} entities found")
    
    # Save results
    output_file = f"examples/outputs/batch_anonymized_{data_type}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"results": results, "metadata": {"total_items": len(results)}}, f, indent=2, ensure_ascii=False)
    
    print(f"💾 Batch results saved to: {output_file}")

def process_ticket_batch(pipeline, monitor, file_path, data_type):
    """Process ticket in batch with monitoring."""
    with open(file_path, "r", encoding="utf-8") as f:
        ticket = json.load(f)
    
    start_time = time.time()
    
    # Anonymize all fields
    anonymized_ticket = anonymize_ticket_completely(pipeline, ticket)
    
    processing_time = time.time() - start_time
    
    # Update monitor
    total_entities = count_entities_in_ticket(ticket, anonymized_ticket)
    monitor.update_progress(entities_found=total_entities)
    
    # Save results
    output_file = f"examples/outputs/batch_anonymized_{data_type}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(anonymized_ticket, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Ticket {ticket['ticket_id']} - {total_entities} entities found")
    print(f"💾 Batch results saved to: {output_file}")

def anonymize_ticket_completely(pipeline, ticket):
    """Anonymize all fields in a ticket."""
    anonymized_ticket = ticket.copy()
    
    # Fields to anonymize
    fields_to_anonymize = [
        "customer_name", "customer_email", "customer_phone", "customer_address",
        "issue_description", "assigned_to", "assigned_email"
    ]
    
    for field in fields_to_anonymize:
        if field in ticket:
            anonymized_ticket[field] = run_pipeline(pipeline, ticket[field])
    
    # Anonymize conversations
    anonymized_conversations = []
    for conv in ticket["conversations"]:
        anonymized_conv = conv.copy()
        anonymized_conv["participant"] = run_pipeline(pipeline, conv["participant"])
        anonymized_conv["message"] = run_pipeline(pipeline, conv["message"])
        anonymized_conversations.append(anonymized_conv)
    
    anonymized_ticket["conversations"] = anonymized_conversations
    anonymized_ticket["processed_at"] = datetime.now().isoformat()
    
    return anonymized_ticket

def count_entities_in_text(original_text, anonymized_text):
    """Count how many entities were found by comparing original and anonymized text."""
    # Simple heuristic: count the number of <ENTITY_TYPE> patterns
    import re
    entity_patterns = re.findall(r'<[^>]+>', anonymized_text)
    return len(entity_patterns)

def count_entities_in_ticket(original_ticket, anonymized_ticket):
    """Count total entities found in a ticket."""
    total_entities = 0
    
    # Count in main fields
    fields_to_check = [
        "customer_name", "customer_email", "customer_phone", "customer_address",
        "issue_description", "assigned_to", "assigned_email"
    ]
    
    for field in fields_to_check:
        if field in original_ticket and field in anonymized_ticket:
            total_entities += count_entities_in_text(original_ticket[field], anonymized_ticket[field])
    
    # Count in conversations
    for i, conv in enumerate(original_ticket["conversations"]):
        if i < len(anonymized_ticket["conversations"]):
            total_entities += count_entities_in_text(conv["participant"], anonymized_ticket["conversations"][i]["participant"])
            total_entities += count_entities_in_text(conv["message"], anonymized_ticket["conversations"][i]["message"])
    
    return total_entities

def show_processing_summary(monitor):
    """Show a summary of the processing results."""
    summary = monitor.get_summary()
    processed_items = summary['processed_items']
    print(f"\n📊 PROCESSING SUMMARY")
    print(f"  - Items processed: {processed_items}")
    print(f"  - Total entities detected: {summary['entities_detected']}")
    print(f"  - Total processing time: {summary['processing_time']:.2f}s")
    if processed_items > 0:
        print(f"  - Average time per item: {summary['processing_time'] / processed_items:.3f}s")
        print(f"  - Entities per item: {summary['entities_detected'] / processed_items:.1f}")
    else:
        print("  - Average time per item: N/A (no items processed)")
        print("  - Entities per item: N/A (no items processed)")
    print(f"  - Success rate: {summary['success_rate']:.1f}%")

if __name__ == "__main__":
    main() 