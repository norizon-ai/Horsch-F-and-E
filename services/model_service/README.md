# Model Service

This directory contains the implementation of the model service for the tier-zero application, which serves machine learning models using Ray and vLLM.

## Overview

The model service is responsible for serving various machine learning models, including:
- LLM models for text generation and embeddings via vLLM's OpenAI-compatible API
- NER models for named entity recognition via custom endpoints

The service uses Ray and vLLM for efficient model serving, providing a scalable and high-performance solution for model inference.

## Architecture

The model service follows a microservice architecture:
- **vLLM Server**: OpenAI-compatible API server that handles LLM and embedding requests
- **Custom API Server**: FastAPI server that handles NER requests
- **Model Manager**: Handles model discovery, downloading, and lifecycle management

### Key Components

- `server.py`: Main entry point that starts both vLLM and custom API servers
- `model_manager.py`: Handles model discovery, downloading, and management
- `models/`: Directory containing model implementations and wrappers
- `config/`: Configuration files for different model types

## Setup and Configuration

The model service can be configured through environment variables in the `docker-compose.yml` file:

- `MODEL_DIR`: Directory where models are stored (default: `/models`)
- `DOWNLOAD_MISSING`: Whether to download missing models (default: `true`)
- `MODEL_CONFIG_PATH`: Path to the model configuration file (default: `/config/models.json`)
- `RAY_NUM_GPUS`: Number of GPUs to use for Ray (default: `0`)
- `API_PORT`: Port for the custom API server (default: `8000`)
- `VLLM_PORT`: Port for the vLLM OpenAI-compatible API server (default: `8001`)
- `VLLM_MODEL`: Model ID for vLLM to serve (default: None)
- `VLLM_DEVICE`: Device to use for vLLM (`cuda`, `metal`, or `cpu`) (default: `cpu`)
- `VLLM_TENSOR_PARALLEL_SIZE`: Tensor parallelism size for vLLM (default: `1`)
- `VLLM_MAX_MODEL_LEN`: Maximum model sequence length (default: `2048`)
- `VLLM_GPU_MEMORY_UTILIZATION`: GPU memory utilization factor (default: `0.9`)

## Usage

### Starting the Service

```bash
docker-compose up model-service
```

### API Endpoints

- `POST /v1/embeddings`: Generate embeddings for input text
- `POST /v1/ner`: Perform named entity recognition
- `POST /v1/generate`: Generate text using a language model

## Model Storage

Models can be stored in two ways:
1. **Local Storage**: Models are stored locally in the `MODEL_DIR` directory
2. **Remote Download**: Models are downloaded from HuggingFace or other sources when needed

The service will check if a requested model exists locally before attempting to download it.

## Integration with Other Services

The model service is designed to integrate with other tier-zero services, particularly:
- **PI Service**: For named entity recognition models
- **Ingestion Worker**: For embedding models used in document processing

## Development

To add support for a new model type:
1. Create a new model wrapper in the `models/` directory
2. Update the model configuration in `config/models.json`
3. Implement the necessary API endpoints in `server.py`

## Running the Model Service on Different Platforms

### Hardware Support

The model service supports multiple hardware platforms:
- NVIDIA GPUs (CUDA)
- Apple Silicon (Metal)
- CPU-only environments

### Running the Service

#### Prerequisites

- Docker and Docker Compose
- For NVIDIA GPUs: NVIDIA Container Toolkit
- For Apple Silicon: Python 3.10+ and pip

#### Option 1: Using Docker (NVIDIA or CPU)

For NVIDIA GPUs or CPU-only environments, you can use Docker directly:

```bash
# For NVIDIA GPUs
VLLM_DEVICE=cuda RAY_NUM_GPUS=1 docker-compose up --build

# For CPU-only
VLLM_DEVICE=cpu docker-compose up --build
```

#### Option 2: Local Setup for Apple Silicon (Metal)

For Apple Silicon with Metal support, we recommend running the service locally:

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install vLLM from source:
```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -r requirements/cpu.txt
pip install -e .
cd ..
```

4. Run the service:
```bash
VLLM_DEVICE=metal RAY_NUM_GPUS=1 python server.py
```

### Configuration

The service can be configured using environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| MODEL_DIR | Directory for model storage | /models |
| DOWNLOAD_MISSING | Download missing models automatically | true |
| MODEL_CONFIG_PATH | Path to model configuration JSON | /app/config/models.json |
| API_PORT | Port for custom FastAPI server | 8000 |
| VLLM_PORT | Port for vLLM OpenAI API server | 8001 |
| RAY_DASHBOARD_PORT | Port for Ray dashboard | 8265 |
| RAY_NUM_GPUS | Number of GPUs to use (0 for CPU-only) | 0 |
| VLLM_MODEL | Model ID for vLLM | meta-llama/Llama-2-7b-chat-hf |
| VLLM_DEVICE | Device to use (cuda, metal, cpu) | cpu |
| VLLM_TENSOR_PARALLEL_SIZE | Tensor parallelism size for vLLM | 1 |
| VLLM_GPU_MEMORY_UTILIZATION | GPU memory utilization for vLLM | 0.9 |

### API Endpoints

#### Custom API (port 8000)

- `GET /`: Service information
- `GET /models`: List available models
- `POST /embeddings`: Generate embeddings
- `POST /ner`: Perform named entity recognition

#### vLLM OpenAI API (port 8001)

- `POST /v1/completions`: Text completions
- `POST /v1/chat/completions`: Chat completions
- `GET /v1/models`: List available models

### Testing

Use the included test script to verify functionality:

```bash
python test_model_service.py
