"""
Client for communicating with the model service to generate embeddings.
"""
import requests
from typing import List, Optional
import json


class ModelServiceClient:
    """
    Client for the model service to generate embeddings.
    """
    
    def __init__(self, model_service_url: str = "http://localhost:8000"):
        """
        Initialize the model service client.
        
        Args:
            model_service_url: Base URL of the model service
        """
        self.base_url = model_service_url.rstrip('/')
        self.embedding_endpoint = f"{self.base_url}/embeddings"
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        })
    
    def generate_embeddings(self, texts: List[str], model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> Optional[List[List[float]]]:
        """
        Generate embeddings for a list of texts.
        
        Args:
            texts: List of text strings to embed
            model_name: Name of the embedding model to use
        
        Returns:
            List of embedding vectors or None if failed
        """
        if not texts:
            return []
        
        payload = {
            "texts": texts,
            "model_name": model_name
        }
        
        try:
            response = self.session.post(
                self.embedding_endpoint,
                json=payload,
                timeout=60  # Longer timeout for embedding generation
            )
            
            if response.status_code == 200:
                result = response.json()
                embeddings = result.get('embeddings', [])
                
                if len(embeddings) != len(texts):
                    print(f"Warning: Expected {len(texts)} embeddings, got {len(embeddings)}")
                
                return embeddings
            else:
                print(f"Model service error {response.status_code}: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with model service: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error parsing model service response: {e}")
            return None
    
    def generate_embedding_batch(self, texts: List[str], batch_size: int = 32, 
                                model_name: str = "sentence-transformers/all-MiniLM-L6-v2") -> Optional[List[List[float]]]:
        """
        Generate embeddings for a large list of texts in batches.
        
        Args:
            texts: List of text strings to embed
            batch_size: Number of texts to process in each batch
            model_name: Name of the embedding model to use
        
        Returns:
            List of embedding vectors or None if failed
        """
        if not texts:
            return []
        
        all_embeddings = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            print(f"Processing embedding batch {i//batch_size + 1}/{(len(texts) + batch_size - 1)//batch_size}")
            
            batch_embeddings = self.generate_embeddings(batch, model_name)
            
            if batch_embeddings is None:
                print(f"Failed to generate embeddings for batch starting at index {i}")
                return None
            
            all_embeddings.extend(batch_embeddings)
        
        return all_embeddings
    
    def health_check(self) -> bool:
        """
        Check if the model service is healthy and accessible.
        
        Returns:
            bool: True if healthy, False otherwise
        """
        try:
            # Try a simple embedding request
            test_embedding = self.generate_embeddings(["test"])
            return test_embedding is not None and len(test_embedding) > 0
            
        except Exception as e:
            print(f"Model service health check failed: {e}")
            return False
    
    def get_available_models(self) -> Optional[List[str]]:
        """
        Get list of available embedding models from the service.
        
        Returns:
            List of model names or None if failed
        """
        try:
            response = self.session.get(f"{self.base_url}/models")
            
            if response.status_code == 200:
                result = response.json()
                return result.get('models', [])
            else:
                print(f"Error getting models: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error getting available models: {e}")
            return None
