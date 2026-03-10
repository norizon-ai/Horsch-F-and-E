#!/usr/bin/env python3
"""
NER Model
=========

Implementation of the named entity recognition model class for identifying entities in text.
"""

import os
import logging
from typing import Dict, List, Optional, Any
from pathlib import Path
import concurrent.futures
from typing import List, Dict, Tuple, Any
import time

import torch
from flair.data import Sentence
from flair.models import SequenceTagger
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("ner-model")


class NERModel:
    """
    Wrapper for named entity recognition models that identify entities in text.
    """

    def __init__(
        self,
        model_id: str,
        model_path: Path,
        model_config: Dict,
        device: str = "cpu",
    ):
        """
        Initialize the NER model.

        Args:
            model_id: ID of the model
            model_path: Path to the model directory
            model_config: Configuration for the model
            device: Device to use for model loading (default: cpu)
        """
        self.model_id = model_id
        self.model_path = model_path
        self.model_config = model_config
        self.model = None
        
        # Map device string to torch device
        if device == "metal":
            # Force CPU for all NER models due to MPS compatibility issues
            self.device = "cpu"
            logger.warning(f"Forcing CPU usage for NER model {model_id} due to MPS compatibility issues")
        elif device == "cuda" and torch.cuda.is_available():
            self.device = "cuda"
            logger.info(f"Using CUDA device for NER model {model_id}")
        else:
            self.device = "cpu"
            logger.info(f"Using CPU device for NER model {model_id}")
        
        self.model_type = model_config.get("model_type", "flair")
        self.batch_size = model_config.get("batch_size", 8)
        self.entity_mapping = model_config.get("entity_mapping", {})
        
        self._load_model()

    def _load_model(self) -> None:
        """
        Load the NER model based on its type.
        """
        try:
            logger.info(f"Loading NER model {self.model_id} of type {self.model_type} on {self.device}")
            
            if self.model_type == "flair":
                # Look for the .pt file in the model directory
                model_name = self.model_id.split('/')[-1]
                model_file = self.model_path / f"{model_name}.pt"
                
                # Patch torch.load to handle PyTorch 2.6 weights_only compatibility
                import torch
                original_torch_load = torch.load
                
                def patched_torch_load(*args, **kwargs):
                    # Set weights_only=False for compatibility with older models
                    kwargs['weights_only'] = False
                    return original_torch_load(*args, **kwargs)
                
                # Temporarily patch torch.load
                torch.load = patched_torch_load
                
                try:
                    if model_file.exists():
                        logger.info(f"Loading Flair model from file: {model_file}")
                        self.model = SequenceTagger.load(str(model_file))
                    else:
                        # Fallback to loading from model ID directly
                        logger.info(f"No .pt file found, loading from model ID: {self.model_id}")
                        self.model = SequenceTagger.load(self.model_id)
                finally:
                    # Restore original torch.load
                    torch.load = original_torch_load
                
                self.model.to(self.device)
            elif self.model_type == "transformers":
                tokenizer = AutoTokenizer.from_pretrained(str(self.model_path))
                model = AutoModelForTokenClassification.from_pretrained(str(self.model_path))
                self.model = pipeline(
                    "ner",
                    model=model,
                    tokenizer=tokenizer,
                    device=0 if self.device == "cuda" else -1,
                    aggregation_strategy="simple",
                )
            else:
                raise ValueError(f"Unsupported model type: {self.model_type}")
            
            logger.info(f"Loaded NER model {self.model_id}")
        except Exception as e:
            logger.error(f"Failed to load NER model {self.model_id}: {str(e)}")
            raise

    def recognize(self, texts: List[str], language: str = "en") -> List[List[Dict]]:
        """
        Perform named entity recognition on the provided texts.

        Args:
            texts: List of texts to analyze
            language: Language of the texts

        Returns:
            List of lists of entities, one list for each input text
        """
        if not self.model:
            raise RuntimeError(f"Model {self.model_id} not loaded")
        
        if not texts:
            return []
        
        try:
            if self.model_type == "flair":
                return self._recognize_with_flair(texts, language)
            elif self.model_type == "transformers":
                return self._recognize_with_transformers(texts)
            else:
                raise ValueError(f"Unsupported model type: {self.model_type}")
        except Exception as e:
            logger.error(f"Error performing NER with model {self.model_id}: {str(e)}")
            raise

    def _recognize_with_flair(self, texts: List[str], language: str) -> List[List[Dict]]:
        """
        Perform named entity recognition using a Flair model.

        Args:
            texts: List of texts to analyze
            language: Language of the texts

        Returns:
            List of lists of entities, one list for each input text
        """
        all_entities = []
        
        # Create batches of sentences
        batches = []
        current_batch = []
        current_batch_size = 0
        batch_size = self.batch_size
        
        # Group texts into batches
        for i, text in enumerate(texts):
            current_batch.append((i, Sentence(text)))
            current_batch_size += 1
            
            if current_batch_size >= batch_size or i == len(texts) - 1:
                batches.append(current_batch)
                current_batch = []
                current_batch_size = 0
        
        # Initialize results array
        all_entities = [[] for _ in range(len(texts))]
        
        # Process each batch
        for batch in batches:
            # Extract just the sentences for prediction
            sentences = [item[1] for item in batch]
            
            # Run NER model on the batch of sentences
            # Use a larger mini_batch_size for better performance
            # Set verbose=False to reduce overhead
            self.model.predict(sentences, mini_batch_size=min(32, len(sentences)), verbose=False)
            
            # Process results for each sentence in the batch
            for idx, sentence in batch:
                entities = []
                for entity in sentence.get_spans('ner'):
                    entity_type = entity.tag
                    
                    # Apply entity mapping if available
                    if entity_type in self.entity_mapping:
                        entity_type = self.entity_mapping[entity_type]
                    
                    entities.append({
                        "text": entity.text,
                        "type": entity_type,
                        "start": entity.start_position,
                        "end": entity.end_position,
                        "score": entity.score,
                    })
                
                all_entities[idx] = entities
        
        return all_entities

    def _recognize_with_transformers(self, texts: List[str]) -> List[List[Dict]]:
        """
        Perform named entity recognition using a Transformers model.

        Args:
            texts: List of texts to analyze

        Returns:
            List of lists of entities, one list for each input text
        """
        all_entities = []
        
        # Process texts in batches
        batch_size = self.batch_size
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i+batch_size]
            
            # Run NER pipeline on the batch of texts
            # The pipeline automatically handles batching internally
            batch_results = self.model(batch_texts)
            
            # If only one text was processed, wrap the result in a list
            if len(batch_texts) == 1:
                batch_results = [batch_results]
            
            # Process and format entities for each text in the batch
            for raw_entities in batch_results:
                entities = []
                for entity in raw_entities:
                    entity_type = entity["entity_group"]
                    
                    # Apply entity mapping if available
                    if entity_type in self.entity_mapping:
                        entity_type = self.entity_mapping[entity_type]
                    
                    entities.append({
                        "text": entity["word"],
                        "type": entity_type,
                        "start": entity["start"],
                        "end": entity["end"],
                        "score": entity["score"],
                    })
                
                all_entities.append(entities)
        
        return all_entities
