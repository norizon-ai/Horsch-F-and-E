#!/usr/bin/env python3
"""
Model Service Test Script
========================

This script tests the model service by making requests to both the custom endpoints
and the vLLM OpenAI-compatible API.
"""

import os
import sys
import json
import argparse
import requests
from typing import Dict, List, Any, Optional

# Default service URLs
DEFAULT_MODEL_SERVICE_URL = "http://localhost:8000"
DEFAULT_VLLM_SERVICE_URL = "http://localhost:8001"

def test_root_endpoint(base_url: str) -> None:
    """Test the root endpoint of the model service."""
    print("\n=== Testing Root Endpoint ===")
    try:
        response = requests.get(f"{base_url}/")
        response.raise_for_status()
        print("✅ Root endpoint is working")
        print(f"Service info: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Error accessing root endpoint: {str(e)}")
        sys.exit(1)

def test_models_endpoint(base_url: str) -> None:
    """Test the models endpoint of the model service."""
    print("\n=== Testing Models Endpoint ===")
    try:
        response = requests.get(f"{base_url}/models")
        response.raise_for_status()
        print("✅ Models endpoint is working")
        print(f"Available models: {json.dumps(response.json(), indent=2)}")
        return response.json()
    except Exception as e:
        print(f"❌ Error accessing models endpoint: {str(e)}")
        return None

def test_embedding_endpoint(base_url: str, model_id: str) -> None:
    """Test the embedding endpoint of the model service."""
    print(f"\n=== Testing Embedding Endpoint with model {model_id} ===")
    
    test_texts = [
        "This is a test sentence for embeddings.",
        "Another example to test the embedding model."
    ]
    
    try:
        response = requests.post(
            f"{base_url}/embeddings",
            json={
                "texts": test_texts,
                "model": model_id
            }
        )
        response.raise_for_status()
        result = response.json()
        
        print("✅ Embedding endpoint is working")
        print(f"Generated {len(result['embeddings'])} embeddings")
        print(f"Embedding dimensions: {result['dimensions']}")
        
        # Print a sample of the first embedding
        first_embedding = result['embeddings'][0][:5]
        print(f"Sample of first embedding: {first_embedding}...")
    except Exception as e:
        print(f"❌ Error generating embeddings: {str(e)}")

def test_ner_endpoint(base_url: str, model_id: str) -> None:
    """Test the NER endpoint of the model service."""
    print(f"\n=== Testing NER Endpoint with model {model_id} ===")
    
    test_texts = [
        "John Smith works at Google in Mountain View.",
        "Apple Inc. was founded by Steve Jobs in Cupertino, California."
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
        
        print("✅ NER endpoint is working")
        print("Recognized entities:")
        
        for i, entities in enumerate(result['entities']):
            print(f"\nText: {test_texts[i]}")
            for entity in entities:
                print(f"  - {entity['text']} ({entity['type']}) [score: {entity['score']:.4f}]")
    except Exception as e:
        print(f"❌ Error performing NER: {str(e)}")

def test_vllm_models_endpoint(base_url: str) -> None:
    """Test the models endpoint of the vLLM OpenAI-compatible API."""
    print("\n=== Testing vLLM Models Endpoint ===")
    try:
        response = requests.get(f"{base_url}/v1/models")
        response.raise_for_status()
        print("✅ vLLM models endpoint is working")
        print(f"Available models: {json.dumps(response.json(), indent=2)}")
        return response.json()
    except Exception as e:
        print(f"❌ Error accessing vLLM models endpoint: {str(e)}")
        return None

def test_vllm_completions_endpoint(base_url: str, model_id: str) -> None:
    """Test the completions endpoint of the vLLM OpenAI-compatible API."""
    print(f"\n=== Testing vLLM Completions Endpoint with model {model_id} ===")
    
    prompt = "Write a short poem about artificial intelligence."
    
    try:
        response = requests.post(
            f"{base_url}/v1/completions",
            json={
                "model": model_id,
                "prompt": prompt,
                "max_tokens": 100,
                "temperature": 0.7
            }
        )
        response.raise_for_status()
        result = response.json()
        
        print("✅ vLLM completions endpoint is working")
        print(f"Prompt: {prompt}")
        print(f"Generated text: {result['choices'][0]['text']}")
    except Exception as e:
        print(f"❌ Error generating completions: {str(e)}")

def test_vllm_chat_completions_endpoint(base_url: str, model_id: str) -> None:
    """Test the chat completions endpoint of the vLLM OpenAI-compatible API."""
    print(f"\n=== Testing vLLM Chat Completions Endpoint with model {model_id} ===")
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the benefits of using Ray and vLLM for model serving?"}
    ]
    
    try:
        response = requests.post(
            f"{base_url}/v1/chat/completions",
            json={
                "model": model_id,
                "messages": messages,
                "max_tokens": 150,
                "temperature": 0.7
            }
        )
        response.raise_for_status()
        result = response.json()
        
        print("✅ vLLM chat completions endpoint is working")
        print(f"User message: {messages[1]['content']}")
        print(f"Assistant response: {result['choices'][0]['message']['content']}")
    except Exception as e:
        print(f"❌ Error generating chat completions: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Test the model service")
    parser.add_argument("--model-service-url", default=DEFAULT_MODEL_SERVICE_URL, help="URL of the model service")
    parser.add_argument("--vllm-service-url", default=DEFAULT_VLLM_SERVICE_URL, help="URL of the vLLM service")
    parser.add_argument("--embedding-model", help="ID of the embedding model to test")
    parser.add_argument("--ner-model", help="ID of the NER model to test")
    parser.add_argument("--llm-model", help="ID of the LLM model to test")
    
    args = parser.parse_args()
    
    # Test model service
    test_root_endpoint(args.model_service_url)
    models = test_models_endpoint(args.model_service_url)
    
    # Test embedding endpoint if a model is specified or available
    embedding_model = args.embedding_model
    if not embedding_model and models and "embedding" in models.get("models", {}):
        embedding_models = models["models"]["embedding"]
        if embedding_models:
            embedding_model = embedding_models[0]
    
    if embedding_model:
        test_embedding_endpoint(args.model_service_url, embedding_model)
    else:
        print("\n⚠️ No embedding model specified or available, skipping embedding test")
    
    # Test NER endpoint if a model is specified or available
    ner_model = args.ner_model
    if not ner_model and models and "ner" in models.get("models", {}):
        ner_models = models["models"]["ner"]
        if ner_models:
            ner_model = ner_models[0]
    
    if ner_model:
        test_ner_endpoint(args.model_service_url, ner_model)
    else:
        print("\n⚠️ No NER model specified or available, skipping NER test")
    
    # Test vLLM OpenAI-compatible API
    vllm_models = test_vllm_models_endpoint(args.vllm_service_url)
    
    # Test completions endpoint if a model is specified or available
    llm_model = args.llm_model
    if not llm_model and vllm_models and "data" in vllm_models:
        vllm_model_list = vllm_models["data"]
        if vllm_model_list:
            llm_model = vllm_model_list[0]["id"]
    
    if llm_model:
        test_vllm_completions_endpoint(args.vllm_service_url, llm_model)
        test_vllm_chat_completions_endpoint(args.vllm_service_url, llm_model)
    else:
        print("\n⚠️ No LLM model specified or available, skipping vLLM tests")
    
    print("\n=== Test Summary ===")
    print("Model Service: " + ("✅ Working" if models else "❌ Not working"))
    print("vLLM Service: " + ("✅ Working" if vllm_models else "❌ Not working"))

if __name__ == "__main__":
    main()
