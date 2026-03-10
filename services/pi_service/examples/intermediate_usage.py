#!/usr/bin/env python3
"""
Intermediate Usage Example - PII De-identification Service
=========================================================

This example shows how to process different types of data files and save results.
Perfect for users who want to process multiple files or different data formats.

Usage:
    python examples/intermediate_usage.py
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Add the project root to the path so we can import our modules
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from pii_deid_service.pipeline.builder import PluginBasedPipelineBuilder
from pii_deid_service.config_management.config_manager import config_manager
from pii_deid_service.pipeline import run_pipeline

def main():
    """Demonstrate intermediate usage with file processing."""
    
    print("🔒 INTERMEDIATE USAGE EXAMPLE")
    print("=" * 50)
    print("This example shows how to process different data files and save results.\n")
    
    # Step 1: Load pipeline configuration
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
    except Exception as e:
        print(f"❌ Error building pipeline: {e}")
        return
    
    # Step 3: Process different types of data files
    print("\n📝 Step 3: Processing different data files...")
    
    # Process sample texts
    print("\n--- Processing Sample Texts ---")
    process_texts_file(pipeline)
    
    # Process sample emails
    print("\n--- Processing Sample Emails ---")
    process_emails_file(pipeline)
    
    # Process sample ticket
    print("\n--- Processing Sample Ticket ---")
    process_ticket_file(pipeline)
    
    print("\n🎉 Intermediate usage example completed successfully!")
    print(f"📁 Check the 'examples/outputs/' directory for anonymized results")

def process_texts_file(pipeline):
    """Process the sample texts file."""
    try:
        # Load sample texts
        with open("examples/data/sample_texts.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        results = []
        for text_item in data["texts"]:
            print(f"\nProcessing: {text_item['title']}")
            print(f"Category: {text_item['category']}")
            
            # Anonymize the content
            anonymized_content = run_pipeline(pipeline, text_item["content"])
            
            # Create result
            result = {
                "id": text_item["id"],
                "title": text_item["title"],
                "category": text_item["category"],
                "original_content": text_item["content"],
                "anonymized_content": anonymized_content,
                "processed_at": datetime.now().isoformat()
            }
            results.append(result)
            
            print(f"✅ Anonymized successfully")
        
        # Save results
        output_file = "examples/outputs/anonymized_texts.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"results": results}, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Results saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error processing texts: {e}")

def process_emails_file(pipeline):
    """Process the sample emails file."""
    try:
        # Load sample emails
        with open("examples/data/sample_emails.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        
        results = []
        for email in data["emails"]:
            print(f"\nProcessing: {email['subject']}")
            print(f"From: {email['from']} To: {email['to']}")
            
            # Anonymize the email body
            anonymized_body = run_pipeline(pipeline, email["body"])
            
            # Create result
            result = {
                "id": email["id"],
                "subject": email["subject"],
                "from": email["from"],
                "to": email["to"],
                "original_body": email["body"],
                "anonymized_body": anonymized_body,
                "date": email["date"],
                "processed_at": datetime.now().isoformat()
            }
            results.append(result)
            
            print(f"✅ Anonymized successfully")
        
        # Save results
        output_file = "examples/outputs/anonymized_emails.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump({"results": results}, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Results saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error processing emails: {e}")

def process_ticket_file(pipeline):
    """Process the sample ticket file."""
    try:
        # Load sample ticket
        with open("examples/data/sample_ticket.json", "r", encoding="utf-8") as f:
            ticket = json.load(f)
        
        print(f"\nProcessing ticket: {ticket['ticket_id']}")
        print(f"Customer: {ticket['customer_name']}")
        
        # Anonymize different fields
        anonymized_ticket = ticket.copy()
        
        # Anonymize customer information
        anonymized_ticket["customer_name"] = run_pipeline(pipeline, ticket["customer_name"])
        anonymized_ticket["customer_email"] = run_pipeline(pipeline, ticket["customer_email"])
        anonymized_ticket["customer_phone"] = run_pipeline(pipeline, ticket["customer_phone"])
        anonymized_ticket["customer_address"] = run_pipeline(pipeline, ticket["customer_address"])
        anonymized_ticket["issue_description"] = run_pipeline(pipeline, ticket["issue_description"])
        
        # Anonymize assigned person
        anonymized_ticket["assigned_to"] = run_pipeline(pipeline, ticket["assigned_to"])
        anonymized_ticket["assigned_email"] = run_pipeline(pipeline, ticket["assigned_email"])
        
        # Anonymize conversations
        anonymized_conversations = []
        for conv in ticket["conversations"]:
            anonymized_conv = conv.copy()
            anonymized_conv["participant"] = run_pipeline(pipeline, conv["participant"])
            anonymized_conv["message"] = run_pipeline(pipeline, conv["message"])
            anonymized_conversations.append(anonymized_conv)
        
        anonymized_ticket["conversations"] = anonymized_conversations
        anonymized_ticket["processed_at"] = datetime.now().isoformat()
        
        print(f"✅ Ticket anonymized successfully")
        
        # Save results
        output_file = "examples/outputs/anonymized_ticket.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(anonymized_ticket, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Results saved to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error processing ticket: {e}")

if __name__ == "__main__":
    main() 