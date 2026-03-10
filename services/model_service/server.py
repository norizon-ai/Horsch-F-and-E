#!/usr/bin/env python3
"""
Model Service Server
===================

Main entry point for the model service that serves machine learning models:
- LLM and embedding models via vLLM's built-in OpenAI-compatible API server
- NER models via a custom FastAPI endpoint
"""

import os
import json
import logging
import subprocess
import threading
from typing import Dict, List, Optional, Union, Any
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from model_manager import ModelManager
from models.ner_model import NERModel

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("model-service")

# Load environment variables
# Use a local models directory if running locally, or /models if in Docker
MODEL_DIR = os.environ.get("MODEL_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "models"))
DOWNLOAD_MISSING = os.environ.get("DOWNLOAD_MISSING", "true").lower() == "true"
# Use a local config path if running locally, or /app/config if in Docker
MODEL_CONFIG_PATH = os.environ.get("MODEL_CONFIG_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "models.json"))
API_PORT = int(os.environ.get("API_PORT", "8000"))
VLLM_PORT = int(os.environ.get("VLLM_PORT", "8001"))
VLLM_MODEL = os.environ.get("VLLM_MODEL", None)
# Read default embedding model from config if available, otherwise use hardcoded default
VLLM_EMBEDDING_MODEL = os.environ.get("VLLM_EMBEDDING_MODEL", None)  # Will be read from config if not set
VLLM_TENSOR_PARALLEL_SIZE = int(os.environ.get("VLLM_TENSOR_PARALLEL_SIZE", "1"))
VLLM_MAX_MODEL_LEN = int(os.environ.get("VLLM_MAX_MODEL_LEN", "2048"))
VLLM_GPU_MEMORY_UTILIZATION = float(os.environ.get("VLLM_GPU_MEMORY_UTILIZATION", "0.9"))
VLLM_DEVICE = os.environ.get("VLLM_DEVICE", "cpu")  # Options: 'cuda', 'metal', 'cpu'

# Create FastAPI app
app = FastAPI(
    title="Model Service API",
    description="API for serving NER models. LLM and embedding models are served via vLLM's OpenAI-compatible API.",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model manager
model_manager = ModelManager(
    model_dir=MODEL_DIR,
    download_missing=DOWNLOAD_MISSING,
    config_path=MODEL_CONFIG_PATH,
)

# Define request/response models for our custom endpoints
class NERRequest(BaseModel):
    texts: List[str] = Field(..., description="List of texts for named entity recognition")
    model: str = Field(..., description="Model ID to use for NER")
    language: str = Field("en", description="Language of the texts")

class Entity(BaseModel):
    text: str = Field(..., description="Entity text")
    type: str = Field(..., description="Entity type")
    start: int = Field(..., description="Start position of entity in text")
    end: int = Field(..., description="End position of entity in text")
    score: float = Field(..., description="Confidence score for the entity")

class NERResponse(BaseModel):
    entities: List[List[Entity]] = Field(..., description="List of entities for each text")
    model: str = Field(..., description="Model ID used for NER")

# Define API endpoints
@app.get("/")
def root():
    """Return information about the service."""
    return {
        "name": "Model Service",
        "version": "1.0.0",
        "custom_api": f"http://localhost:{API_PORT}",
        "vllm_api": f"http://localhost:{VLLM_PORT}",
        "device": VLLM_DEVICE,
    }

@app.get("/models")
def list_models():
    """List all available models."""
    return {
        "models": model_manager.list_available_models()
    }

@app.post("/ner", response_model=NERResponse)
def perform_ner(request: NERRequest):
    """Perform named entity recognition on the provided texts."""
    try:
        logger.info(f"NER request received for model: {request.model}, language: {request.language}, texts: {len(request.texts)} items")
        
        # Get the model
        logger.info(f"Loading NER model: {request.model}")
        model = model_manager.get_model(request.model, "ner")
        logger.info(f"Model loaded successfully: {request.model}")
        
        # Perform recognition
        logger.info(f"Performing recognition with model: {request.model}")
        entities = model.recognize(request.texts, request.language)
        logger.info(f"Recognition completed successfully with {sum(len(e) for e in entities)} entities found")
        
        return {
            "entities": entities,
            "model": request.model,
        }
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        logger.error(f"Error performing NER with model {request.model}: {str(e)}")
        logger.error(f"Error trace: {error_trace}")
        raise HTTPException(status_code=500, detail=f"NER error: {str(e)}")

@app.get("/healthz")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

def start_vllm_server():
    """Start the vLLM OpenAI-compatible API server in a separate process."""
    # Try to get model from environment variables first
    model_to_use = VLLM_MODEL
    auto_load = True  # Default to auto_load if explicitly specified in env vars
    
    # If no LLM model specified, try to get embedding model from env or config
    if not model_to_use:
        if VLLM_EMBEDDING_MODEL:
            model_to_use = VLLM_EMBEDDING_MODEL
        else:
            # Try to read from config
            try:
                with open(MODEL_CONFIG_PATH, "r") as f:
                    model_config = json.load(f)
                
                # Check if vllm config exists and has embedding section
                if "vllm" in model_config and "embedding" in model_config["vllm"]:
                    # Get default embedding model from config
                    default_model = model_config["vllm"]["embedding"].get("default")
                    if default_model:
                        # Check if the model exists in the models list and get its auto_load setting
                        models_dict = model_config["vllm"]["embedding"].get("models", {})
                        if default_model in models_dict:
                            model_to_use = default_model
                            # Only auto-load if specified in config
                            auto_load = models_dict[default_model].get("auto_load", False)
                            logger.info(f"Using embedding model from config: {model_to_use} (auto_load: {auto_load})")
                        else:
                            model_to_use = default_model
                            logger.info(f"Using default embedding model: {model_to_use} (auto_load setting not found)")
            except Exception as e:
                logger.error(f"Error reading model config: {str(e)}")
                # Fall back to a hardcoded default if config reading fails
                model_to_use = "intfloat/multilingual-e5-base"
                logger.warning(f"Falling back to hardcoded default model: {model_to_use}")
    
    # Check if we should start the server based on auto_load setting
    if not model_to_use:
        logger.info("No VLLM model specified in environment or config, skipping vLLM server startup")
        return
    
    # Skip server startup if auto_load is False and no explicit model was requested via env vars
    if not auto_load and not VLLM_MODEL and not VLLM_EMBEDDING_MODEL:
        logger.info(f"Skipping vLLM server startup for model {model_to_use} as auto_load is set to False")
        return
    
    try:
        # Construct the model path
        model_path = os.path.join(MODEL_DIR, "llm", model_to_use.replace("/", "_"))
        
        # Check if the model exists, if not, try to download it
        if not os.path.exists(model_path) and DOWNLOAD_MISSING:
            logger.info(f"Model {model_to_use} not found, attempting to download")
            # Since we removed llm_model.py, we need to handle downloading differently
            os.makedirs(model_path, exist_ok=True)
            from huggingface_hub import snapshot_download
            snapshot_download(
                repo_id=model_to_use,
                local_dir=model_path,
                local_dir_use_symlinks=False,
            )
            logger.info(f"Downloaded model {model_to_use} to {model_path}")
        
        # Prepare the command to start vLLM's OpenAI API server
        cmd = [
            "python", "-m", "vllm.entrypoints.api_server",
            "--model", model_to_use,
            "--port", str(VLLM_PORT),
            "--host", "0.0.0.0",
        ]
        
        # Add device-specific arguments
        if VLLM_DEVICE == "cuda":
            cmd.extend([
                "--tensor-parallel-size", str(VLLM_TENSOR_PARALLEL_SIZE),
                "--gpu-memory-utilization", str(VLLM_GPU_MEMORY_UTILIZATION),
            ])
        elif VLLM_DEVICE == "metal":
            # Metal-specific settings for Apple Silicon
            cmd.extend([
                "--trust-remote-code",  # Often needed for newer models
                "--dtype", "float16",   # Use float16 for better performance on Metal
            ])
            # Set environment variable for Metal
            os.environ["VLLM_USE_METAL"] = "1"
        elif VLLM_DEVICE == "cpu":
            cmd.extend([
                "--cpu-only",  # Use CPU only
            ])
        
        logger.info(f"Starting vLLM API server with device {VLLM_DEVICE}")
        logger.info(f"Command: {' '.join(cmd)}")
        
        # Start the vLLM server process
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            env=os.environ.copy(),  # Pass current environment with any modifications
        )
        
        # Log the output from the vLLM server
        for line in process.stdout:
            logger.info(f"vLLM: {line.strip()}")
        
        process.wait()
        if process.returncode != 0:
            logger.error(f"vLLM server exited with code {process.returncode}")
    except Exception as e:
        logger.error(f"Error starting vLLM server: {str(e)}")
        logger.exception("vLLM server exception details:")

# Start the server
if __name__ == "__main__":
    logger.info(f"Starting Model Service on port {API_PORT}")
    logger.info(f"Model directory: {MODEL_DIR}")
    logger.info(f"Download missing models: {DOWNLOAD_MISSING}")
    logger.info(f"Model config path: {MODEL_CONFIG_PATH}")
    logger.info(f"Using device: {VLLM_DEVICE}")
    
    # Initialize models - pass the device from environment
    model_manager.initialize(device=VLLM_DEVICE)
    
    # Start vLLM server in a separate thread
    vllm_thread = threading.Thread(target=start_vllm_server, daemon=True)
    vllm_thread.start()
    
    # Start the FastAPI server directly with uvicorn
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)
