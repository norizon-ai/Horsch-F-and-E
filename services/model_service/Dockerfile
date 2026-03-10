ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    TZ=UTC

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    wget \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Create model directory
RUN mkdir -p /models/embedding /models/ner /models/llm

# Set environment variables
ENV MODEL_DIR=/models \
    DOWNLOAD_MISSING=true \
    MODEL_CONFIG_PATH=/app/config/models.json \
    API_PORT=8000 \
    VLLM_PORT=8001

# Base stage complete
FROM base as cpu

# Install CPU-specific dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# NVIDIA CUDA stage
FROM base as cuda

# Install CUDA-specific dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Apple Metal stage - build vLLM from source
FROM base as metal

# Install Metal-specific dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir torch torchvision torchaudio && \
    pip install --no-cache-dir $(grep -v "vllm" requirements.txt | grep -v "^#")

# Clone and build vLLM from source
RUN git clone https://github.com/vllm-project/vllm.git /tmp/vllm && \
    cd /tmp/vllm && \
    pip install -r requirements/cpu.txt && \
    pip install -e . && \
    cd /app && \
    rm -rf /tmp/vllm

# Copy application code to all stages
COPY . /app/

# Final image - default to CPU
FROM cpu

# Expose ports
EXPOSE 8000 8001 8265

# Run the application
CMD ["python", "server.py"]
