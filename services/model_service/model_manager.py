#!/usr/bin/env python3
"""
Model Manager
============

Manages the lifecycle of machine learning models including discovery, downloading,
and loading.
"""

import os
import json
import logging
import shutil
import datetime
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
import urllib.request
import tempfile

import torch
from huggingface_hub import hf_hub_download, snapshot_download

from models.ner_model import NERModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("model-manager")


class ModelManager:
    """
    Manages the lifecycle of machine learning models.
    """

    def __init__(
        self,
        model_dir: str,
        download_missing: bool = True,
        config_path: Optional[str] = None,
    ):
        """
        Initialize the model manager.

        Args:
            model_dir: Directory to store models
            download_missing: Whether to download missing models
            config_path: Path to model configuration JSON
        """
        self.model_dir = Path(model_dir)
        self.download_missing = download_missing
        self.config_path = config_path
        self.model_config = {}
        self.models = {}
        self.model_load_times = {}  # Track when models are loaded
        self.device = "cpu"  # Default device
        
        # Create model directories if they don't exist
        os.makedirs(self.model_dir / "ner", exist_ok=True)
        os.makedirs(self.model_dir / "llm", exist_ok=True)
        
        # Load model configuration if provided
        if config_path:
            self._load_config()
    
    def _load_config(self) -> None:
        """
        Load model configuration from JSON file.
        """
        try:
            with open(self.config_path, "r") as f:
                self.model_config = json.load(f)
            logger.info(f"Loaded model configuration from {self.config_path}")
        except Exception as e:
            logger.error(f"Error loading model configuration: {str(e)}")
            self.model_config = {}
    
    def initialize(self, device: str = "cpu") -> None:
        """
        Initialize models based on configuration.

        Args:
            device: Device to use for model loading (default: cpu)
        """
        self.device = device
        logger.info(f"Initializing model manager with device: {device}")
        
        if not self.model_config:
            logger.warning("No model configuration loaded, skipping initialization")
            return
        
        # Initialize NER models
        if "ner" in self.model_config:
            logger.info(f"Found {len(self.model_config['ner'])} NER models in configuration")
            for model_id, config in self.model_config["ner"].items():
                try:
                    model_path = self.model_dir / "ner" / model_id
                    if model_path.exists():
                        # Get modification time of model directory
                        mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(model_path))
                        logger.info(f"NER model {model_id} found at {model_path} (last modified: {mod_time.isoformat()})")
                    else:
                        logger.info(f"NER model {model_id} not found locally, will be downloaded if needed")
                    
                    if config.get("auto_load", False):
                        logger.info(f"Auto-loading NER model {model_id} on device {device}")
                        self.get_model(model_id, "ner", device=device)
                except Exception as e:
                    logger.error(f"Error auto-loading NER model {model_id}: {str(e)}")
        
        # Log summary of loaded models
        if self.models:
            logger.info("=== Loaded Models Summary ===")
            for model_key, model in self.models.items():
                model_type, model_id = model_key.split(":", 1)
                load_time = self.model_load_times.get(model_key, "unknown")
                model_path = self.model_dir / model_type / model_id
                logger.info(f"Model: {model_id} (Type: {model_type}, Path: {model_path}, Loaded at: {load_time})")
        else:
            logger.info("No models loaded at startup")
    
    def get_model(self, model_id: str, model_type: str, device: str = "cpu") -> Any:
        """
        Get a model by ID and type, loading it if necessary.

        Args:
            model_id: ID of the model
            model_type: Type of the model (ner)
            device: Device to use for model loading (default: cpu)

        Returns:
            The requested model
        """
        model_key = f"{model_type}:{model_id}"
        
        # Return cached model if available
        if model_key in self.models:
            return self.models[model_key]
        
        # Check if model exists in configuration
        if model_type not in self.model_config or model_id not in self.model_config[model_type]:
            raise ValueError(f"Model {model_id} of type {model_type} not found in configuration")
        
        # Get model configuration
        model_config = self.model_config[model_type][model_id]
        
        # Check if model exists locally
        model_path = self.model_dir / model_type / model_id
        if not model_path.exists():
            if self.download_missing:
                self.download_model(model_id, model_type)
            else:
                raise FileNotFoundError(f"Model {model_id} not found locally and download_missing is False")
        
        # Load the model
        logger.info(f"Loading {model_type} model: {model_id} from {model_path} on device {device}")
        model = self._load_model(model_id, model_type, model_path, model_config, device=device)
        self.models[model_key] = model
        self.model_load_times[model_key] = datetime.datetime.now().isoformat()
        logger.info(f"Successfully loaded {model_type} model: {model_id}")
        
        return model
    
    def download_model(self, model_id: str, model_type: str) -> None:
        """
        Download a model by ID and type.

        Args:
            model_id: ID of the model
            model_type: Type of the model (ner)
        """
        if model_type not in self.model_config or model_id not in self.model_config[model_type]:
            raise ValueError(f"Model {model_id} of type {model_type} not found in configuration")
        
        model_config = self.model_config[model_type][model_id]
        model_path = self.model_dir / model_type / model_id
        
        # Create model directory
        os.makedirs(model_path, exist_ok=True)
        
        try:
            # Download from Hugging Face Hub
            if "hf_repo" in model_config:
                logger.info(f"Downloading model {model_id} from Hugging Face Hub: {model_config['hf_repo']}")
                
                # For Flair models, download and save as .pt file
                if model_type == "ner" and model_config.get("model_type") == "flair":
                    # Save the model directly as a .pt file
                    model_file = model_path / f"{model_id.split('/')[-1]}.pt"
                    
                    # Check if model file already exists
                    if not model_file.exists():
                        logger.info(f"Downloading Flair model to {model_file}")
                        
                        # Import here to avoid circular imports
                        from flair.models import SequenceTagger
                        import torch
                        
                        # Patch torch.load to handle PyTorch 2.6 weights_only compatibility
                        original_torch_load = torch.load
                        
                        def patched_torch_load(*args, **kwargs):
                            # Set weights_only=False for compatibility with older models
                            kwargs['weights_only'] = False
                            return original_torch_load(*args, **kwargs)
                        
                        # Temporarily patch torch.load
                        torch.load = patched_torch_load
                        
                        try:
                            # Download and save the model
                            model = SequenceTagger.load(model_config["hf_repo"])
                            model.save(str(model_file))
                            logger.info(f"Saved Flair model to {model_file}")
                        finally:
                            # Restore original torch.load
                            torch.load = original_torch_load
                    else:
                        logger.info(f"Flair model already exists at {model_file}")
                    
                    return
                
                # Download specific files if specified
                if "hf_files" in model_config:
                    for file in model_config["hf_files"]:
                        hf_hub_download(
                            repo_id=model_config["hf_repo"],
                            filename=file,
                            local_dir=model_path,
                            local_dir_use_symlinks=False,
                        )
                # Otherwise download the entire repository
                else:
                    snapshot_download(
                        repo_id=model_config["hf_repo"],
                        local_dir=model_path,
                        local_dir_use_symlinks=False,
                    )
            
            # Download from URL
            elif "url" in model_config:
                logger.info(f"Downloading model {model_id} from URL: {model_config['url']}")
                
                # Download to temporary file
                with tempfile.NamedTemporaryFile() as temp_file:
                    urllib.request.urlretrieve(model_config["url"], temp_file.name)
                    
                    # Extract if it's an archive
                    if model_config.get("archive", False):
                        import tarfile
                        import zipfile
                        
                        if model_config["url"].endswith(".tar.gz") or model_config["url"].endswith(".tgz"):
                            with tarfile.open(temp_file.name, "r:gz") as tar:
                                tar.extractall(path=model_path)
                        elif model_config["url"].endswith(".zip"):
                            with zipfile.ZipFile(temp_file.name, "r") as zip_ref:
                                zip_ref.extractall(path=model_path)
                        else:
                            raise ValueError(f"Unsupported archive format for model {model_id}")
                    # Otherwise copy the file directly
                    else:
                        output_file = model_path / os.path.basename(model_config["url"])
                        shutil.copy(temp_file.name, output_file)
            
            else:
                raise ValueError(f"No download source specified for model {model_id}")
            
            logger.info(f"Downloaded model {model_id} to {model_path}")
        except Exception as e:
            logger.error(f"Error downloading model {model_id}: {str(e)}")
            raise
    
    def _load_model(self, model_id: str, model_type: str, model_path: Path, model_config: Dict, device: str = "cpu") -> Any:
        """
        Load a model based on its type.

        Args:
            model_id: ID of the model
            model_type: Type of the model
            model_path: Path to the model directory
            model_config: Configuration for the model
            device: Device to use for model loading (default: cpu)

        Returns:
            The loaded model
        """
        try:
            if model_type == "ner":
                return NERModel(model_id, model_path, model_config, device=device)
            else:
                raise ValueError(f"Unsupported model type: {model_type}")
        except Exception as e:
            logger.error(f"Error loading model {model_id}: {str(e)}")
            raise
    
    def list_available_models(self) -> Dict[str, List[str]]:
        """
        List all available models by type.

        Returns:
            Dictionary of model types to lists of model IDs
        """
        available_models = {}
        
        # List models from configuration
        for model_type, models in self.model_config.items():
            available_models[model_type] = list(models.keys())
        
        return available_models
