#!/usr/bin/env python3
"""
Embedding Model
==============

Implementation of the embedding model class for generating text embeddings.
"""

import os
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path

import torch
import numpy as np
from sentence_transformers import SentenceTransformer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("embedding-model")


class EmbeddingModel:
    """
    Wrapper for embedding models that generate vector representations of text.
    """

    def __init__(
        self,
        model_id: str,
        model_path: Path,
        model_config: Dict,
    ):
        """
        Initialize the embedding model.

        Args:
            model_id: ID of the model
            model_path: Path to the model directory
            model_config: Configuration for the model
        """
        self.model_id = model_id
        self.model_path = model_path
        self.model_config = model_config
        self.model = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.batch_size = model_config.get("batch_size", 32)
        self.normalize = model_config.get("normalize", True)
        
        self._load_model()

    def _load_model(self) -> None:
        """
        Load the embedding model.
        """
        try:
            logger.info(f"Loading embedding model {self.model_id} on {self.device}")
            
            # Load the model using sentence-transformers
            self.model = SentenceTransformer(str(self.model_path))
            self.model.to(self.device)
            
            logger.info(f"Loaded embedding model {self.model_id}")
        except Exception as e:
            logger.error(f"Failed to load embedding model {self.model_id}: {str(e)}")
            raise

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a batch of texts.

        Args:
            texts: List of texts to embed

        Returns:
            List of embeddings, one for each input text
        """
        if not self.model:
            raise RuntimeError(f"Model {self.model_id} not loaded")
        
        if not texts:
            return []
        
        try:
            # Generate embeddings in batches
            embeddings = []
            for i in range(0, len(texts), self.batch_size):
                batch = texts[i:i + self.batch_size]
                batch_embeddings = self.model.encode(batch, convert_to_numpy=True)
                
                # Normalize if required
                if self.normalize:
                    batch_embeddings = batch_embeddings / np.linalg.norm(batch_embeddings, axis=1, keepdims=True)
                
                # Convert to Python list for JSON serialization
                batch_embeddings = batch_embeddings.tolist()
                embeddings.extend(batch_embeddings)
            
            return embeddings
        except Exception as e:
            logger.error(f"Error generating embeddings with model {self.model_id}: {str(e)}")
            raise
    
    def embed(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.

        Args:
            text: Text to embed

        Returns:
            Embedding vector
        """
        embeddings = self.embed_batch([text])
        return embeddings[0] if embeddings else []
