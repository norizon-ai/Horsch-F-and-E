#!/usr/bin/env python3
"""
NER Model Test Script
====================

This script tests the Named Entity Recognition (NER) functionality of the model service.
It includes tests for both German and English NER models, with various test cases
to verify entity recognition capabilities.
"""

import os
import sys
import json
import argparse
import requests
from typing import Dict, List, Any, Optional

# Default service URL
DEFAULT_MODEL_SERVICE_URL = "http://localhost:8000"

def print_banner():
    """Print the test banner."""
    print("\n" + "=" * 80)
    print("NER MODEL TEST SCRIPT".center(80))
    print("=" * 80)
    print("Testing Named Entity Recognition capabilities of the model service")
    print("=" * 80 + "\n")

def test_available_models(base_url: str) -> Dict:
    """Test the models endpoint to get available NER models."""
    print("\n=== Checking Available NER Models ===")
    try:
        response = requests.get(f"{base_url}/models")
        response.raise_for_status()
        response_data = response.json()
        
        # Print the full response for debugging
        print(f"API Response: {json.dumps(response_data, indent=2)}")
        
        # Check if 'models' key exists in the response
        if "models" in response_data:
            models = response_data["models"]
            
            # Check if 'ner' key exists in the models dictionary
            if "ner" in models:
                print(f"✅ Found {len(models['ner'])} NER models:")
                for model_id in models["ner"]:
                    print(f"  - {model_id}")
                return models
            else:
                print("❌ No NER models found in the service (no 'ner' key in models)")
                return {}
        else:
            print("❌ Unexpected API response format (no 'models' key)")
            return {}
    except Exception as e:
        print(f"❌ Error accessing models endpoint: {str(e)}")
        return {}

def test_german_ner(base_url: str, model_id: str = "flair/ner-german-large") -> None:
    """Test German NER model with various German text examples."""
    print(f"\n=== Testing German NER with model {model_id} ===")
    
    # Test cases for German NER
    test_texts = [
        "Angela Merkel ist eine deutsche Politikerin und war von 2005 bis 2021 Bundeskanzlerin der Bundesrepublik Deutschland.",
        "Die Firma BMW hat ihren Hauptsitz in München, Bayern.",
        "Thomas Müller spielt Fußball für den FC Bayern München und die deutsche Nationalmannschaft.",
        "Die Berliner Mauer fiel am 9. November 1989.",
        "Die Deutsche Bank hat eine Filiale in Frankfurt am Main eröffnet."
    ]
    
    try:
        response = requests.post(
            f"{base_url}/ner",
            json={
                "texts": test_texts,
                "model": model_id,
                "language": "de"
            }
        )
        response.raise_for_status()
        result = response.json()
        
        print("✅ German NER test successful")
        print("\nRecognized entities in German texts:")
        
        for i, entities in enumerate(result['entities']):
            print(f"\nText {i+1}: {test_texts[i]}")
            if entities:
                for entity in entities:
                    entity_text = entity['text']
                    entity_type = entity['type']
                    entity_score = entity['score']
                    print(f"  - {entity_text} ({entity_type}) [score: {entity_score:.4f}]")
            else:
                print("  No entities found")
                
        # Verify some expected entities
        expected_entities = {
            "Angela Merkel": "PERSON",
            "Deutschland": "LOCATION",
            "BMW": "ORGANIZATION",
            "München": "LOCATION",
            "Bayern": "LOCATION",
            "Thomas Müller": "PERSON",
            "FC Bayern München": "ORGANIZATION",
            "Berliner Mauer": "LOCATION",
            "Deutsche Bank": "ORGANIZATION",
            "Frankfurt am Main": "LOCATION"
        }
        
        # Check if expected entities were found
        found_entities = {}
        for entities_list in result['entities']:
            for entity in entities_list:
                found_entities[entity['text']] = entity['type']
        
        print("\nVerifying expected entities:")
        for entity_text, expected_type in expected_entities.items():
            if entity_text in found_entities:
                if found_entities[entity_text] == expected_type:
                    print(f"  ✅ Found {entity_text} as {expected_type}")
                else:
                    print(f"  ⚠️ Found {entity_text} as {found_entities[entity_text]}, expected {expected_type}")
            else:
                print(f"  ❌ Missing expected entity: {entity_text} ({expected_type})")
                
    except Exception as e:
        print(f"❌ Error testing German NER: {str(e)}")

def test_english_ner(base_url: str, model_id: str = "dslim/bert-base-NER") -> None:
    """Test English NER model with various English text examples."""
    print(f"\n=== Testing English NER with model {model_id} ===")
    
    # Test cases for English NER
    test_texts = [
        "Apple Inc. was founded by Steve Jobs and Steve Wozniak in Cupertino, California.",
        "Microsoft CEO Satya Nadella announced a new partnership with OpenAI in Seattle.",
        "The Eiffel Tower in Paris, France attracts millions of tourists every year.",
        "NASA launched the James Webb Space Telescope in December 2021.",
        "The United Nations headquarters is located in New York City."
    ]
    
    try:
        response = requests.post(
            f"{base_url}/ner",
            json={
                "texts": test_texts,
                "model": model_id,
                "language": "en"
            }
        )
        response.raise_for_status()
        result = response.json()
        
        print("✅ English NER test successful")
        print("\nRecognized entities in English texts:")
        
        for i, entities in enumerate(result['entities']):
            print(f"\nText {i+1}: {test_texts[i]}")
            if entities:
                for entity in entities:
                    entity_text = entity['text']
                    entity_type = entity['type']
                    entity_score = entity['score']
                    print(f"  - {entity_text} ({entity_type}) [score: {entity_score:.4f}]")
            else:
                print("  No entities found")
                
        # Verify some expected entities
        expected_entities = {
            "Apple Inc.": "ORGANIZATION",
            "Steve Jobs": "PERSON",
            "Steve Wozniak": "PERSON",
            "Cupertino": "LOCATION",
            "California": "LOCATION",
            "Microsoft": "ORGANIZATION",
            "Satya Nadella": "PERSON",
            "OpenAI": "ORGANIZATION",
            "Seattle": "LOCATION",
            "Eiffel Tower": "LOCATION",
            "Paris": "LOCATION",
            "France": "LOCATION",
            "NASA": "ORGANIZATION",
            "James Webb Space Telescope": "MISC",
            "United Nations": "ORGANIZATION",
            "New York City": "LOCATION"
        }
        
        # Check if expected entities were found
        found_entities = {}
        for entities_list in result['entities']:
            for entity in entities_list:
                found_entities[entity['text']] = entity['type']
        
        print("\nVerifying expected entities:")
        for entity_text, expected_type in expected_entities.items():
            if entity_text in found_entities:
                if found_entities[entity_text] == expected_type:
                    print(f"  ✅ Found {entity_text} as {expected_type}")
                else:
                    print(f"  ⚠️ Found {entity_text} as {found_entities[entity_text]}, expected {expected_type}")
            else:
                print(f"  ❌ Missing expected entity: {entity_text} ({expected_type})")
                
    except Exception as e:
        print(f"❌ Error testing English NER: {str(e)}")

def test_ner_performance(base_url: str, model_id: str, language: str) -> None:
    """Test NER model performance with a longer text."""
    print(f"\n=== Testing NER Performance with model {model_id} ({language}) ===")
    
    # Longer text for performance testing
    if language == "de":
        long_text = """
        Die Deutsche Bank AG ist eine deutsche Universalbank mit Sitz in Frankfurt am Main. 
        Als Kreditinstitut betreibt sie Bankgeschäfte aller Art und deckt die Bedürfnisse 
        von Privat-, Geschäfts- und Investmentbanking-Kunden ab. Sie ist die größte deutsche Bank, 
        gemessen an der Bilanzsumme die viertgrößte Europas und weltweit die 21.-größte Bank. 
        Die Bank unterhält Niederlassungen in zahlreichen Ländern und beschäftigt weltweit 84.659 Mitarbeiter. 
        Der Vorstandsvorsitzende ist seit April 2018 Christian Sewing, Aufsichtsratsvorsitzender ist seit Mai 2017 Paul Achleitner.
        """
    else:  # English
        long_text = """
        Google LLC is an American multinational technology company focusing on search engine technology, 
        online advertising, cloud computing, computer software, quantum computing, e-commerce, 
        artificial intelligence, and consumer electronics. It has been referred to as "the most powerful 
        company in the world" and one of the world's most valuable brands due to its market dominance, 
        data collection, and technological advantages in the area of artificial intelligence. 
        Google's parent company Alphabet Inc. is one of the Big Five American information technology 
        companies, alongside Amazon, Apple, Meta, and Microsoft. Google was founded on September 4, 1998, 
        by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University in California.
        """
    
    try:
        response = requests.post(
            f"{base_url}/ner",
            json={
                "texts": [long_text],
                "model": model_id,
                "language": language
            }
        )
        response.raise_for_status()
        result = response.json()
        
        print("✅ NER performance test successful")
        print("\nRecognized entities in long text:")
        
        entities = result['entities'][0]
        if entities:
            # Group entities by type
            entities_by_type = {}
            for entity in entities:
                entity_type = entity['type']
                if entity_type not in entities_by_type:
                    entities_by_type[entity_type] = []
                entities_by_type[entity_type].append(entity['text'])
            
            # Print entities by type
            for entity_type, entity_texts in entities_by_type.items():
                print(f"\n{entity_type} entities:")
                for text in sorted(set(entity_texts)):
                    print(f"  - {text}")
        else:
            print("  No entities found")
                
    except Exception as e:
        print(f"❌ Error testing NER performance: {str(e)}")

def test_ner_throughput(base_url: str, model_id: str = "flair/ner-german-large") -> None:
    """Test NER model throughput with multiple texts."""
    print(f"\n=== Testing NER Throughput with model {model_id} ===")
    
    import time
    
    # Generate multiple German texts for throughput testing
    test_texts = [
        "Die Deutsche Bank AG ist eine deutsche Universalbank mit Sitz in Frankfurt am Main.",
        "BMW hat seinen Hauptsitz in München und produziert Autos und Motorräder.",
        "Die Berliner Mauer fiel am 9. November 1989.",
        "Angela Merkel war von 2005 bis 2021 Bundeskanzlerin der Bundesrepublik Deutschland.",
        "Die Firma Siemens wurde 1847 in Berlin gegründet und hat heute ihren Hauptsitz in München.",
        "Der Kölner Dom ist eine römisch-katholische Kirche in Köln unter dem Patrozinium des Heiligen Petrus.",
        "Die Universität Heidelberg wurde im Jahr 1386 gegründet und ist die älteste Universität Deutschlands.",
        "Das Oktoberfest in München ist das größte Volksfest der Welt.",
        "Die Zugspitze ist mit 2962 Metern der höchste Berg Deutschlands.",
        "Hamburg ist die zweitgrößte Stadt Deutschlands und einer der wichtigsten Häfen Europas."
    ]
    
    # Duplicate the texts to create a larger dataset (50 texts total)
    all_texts = test_texts * 5
    
    try:
        start_time = time.time()
        
        response = requests.post(
            f"{base_url}/ner",
            json={
                "texts": all_texts,
                "model": model_id,
                "language": "de"
            }
        )
        response.raise_for_status()
        result = response.json()
        
        end_time = time.time()
        duration = end_time - start_time
        
        # Calculate throughput metrics
        total_texts = len(all_texts)
        total_chars = sum(len(text) for text in all_texts)
        total_entities = sum(len(entities) for entities in result['entities'])
        
        # Calculate bytes per character (assuming UTF-8 encoding where each char is ~1-4 bytes)
        # Using 1.5 as a conservative average for European languages
        bytes_per_char = 1.5
        total_bytes = total_chars * bytes_per_char
        bytes_per_second = total_bytes / duration
        
        # Calculate time to process 1GB of text
        one_gb_bytes = 1024 * 1024 * 1024  # 1GB in bytes
        seconds_for_1gb = one_gb_bytes / bytes_per_second
        
        # Convert to more readable time format
        hours, remainder = divmod(seconds_for_1gb, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        print("✅ NER throughput test successful")
        print(f"\nProcessed {total_texts} texts with {total_chars} characters in {duration:.2f} seconds")
        print(f"Throughput: {total_texts/duration:.2f} texts/second")
        print(f"Character throughput: {total_chars/duration:.2f} chars/second")
        print(f"Byte throughput: {bytes_per_second:.2f} bytes/second")
        print(f"Found {total_entities} entities ({total_entities/duration:.2f} entities/second)")
        
        print("\nEstimated time to process 1GB of text:")
        print(f"  {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds")
        print(f"  (approximately {seconds_for_1gb/3600:.2f} hours)")
        
    except Exception as e:
        print(f"❌ Error testing NER throughput: {str(e)}")

def main():
    """Main function to run the NER model tests."""
    parser = argparse.ArgumentParser(description="Test NER models in the model service")
    parser.add_argument("--url", default=DEFAULT_MODEL_SERVICE_URL, help="Base URL of the model service")
    parser.add_argument("--german-model", default="flair/ner-german-large", help="German NER model to test")
    parser.add_argument("--english-model", default="dslim/bert-base-NER", help="English NER model to test")
    parser.add_argument("--skip-english", action="store_true", help="Skip English NER tests")
    parser.add_argument("--skip-german", action="store_true", help="Skip German NER tests")
    parser.add_argument("--throughput-only", action="store_true", help="Run only throughput tests")
    args = parser.parse_args()
    
    # Check if the model service is running
    try:
        requests.get(f"{args.url}/healthz").raise_for_status()
    except Exception as e:
        print(f"❌ Error: Model service not available at {args.url}")
        print(f"   {str(e)}")
        sys.exit(1)
    
    print_banner()
    
    # Check available models
    models = test_available_models(args.url)
    
    if not models or "ner" not in models:
        print("❌ No NER models available in the service")
        sys.exit(1)
    
    # Test German NER if not skipped and model is available
    if not args.skip_german and "ner" in models and args.german_model in models["ner"]:
        if not args.throughput_only:
            test_german_ner(args.url, args.german_model)
            test_ner_performance(args.url, args.german_model, "de")
        test_ner_throughput(args.url, args.german_model)
    elif not args.skip_german:
        print(f"\n⚠️ German NER model {args.german_model} not available, skipping German tests")
    
    # Test English NER if not skipped and model is available
    if not args.skip_english and "ner" in models and args.english_model in models["ner"]:
        if not args.throughput_only:
            test_english_ner(args.url, args.english_model)
            test_ner_performance(args.url, args.english_model, "en")
    elif not args.skip_english:
        print(f"\n⚠️ English NER model {args.english_model} not available, skipping English tests")
    
    print("\n" + "=" * 80)
    print("NER MODEL TESTS COMPLETED".center(80))
    print("=" * 80)

if __name__ == "__main__":
    main()
