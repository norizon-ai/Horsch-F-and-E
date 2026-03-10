# Multi-stage Docker build for Intranet Connector Service

# Build Stage
FROM python:3.13-slim as builder

# Install system dependencies needed for building Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# Runtime Stage
FROM python:3.13-slim as runtime

# Install system dependencies needed for runtime
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser

# Set working directory
WORKDIR /app

# Copy Python packages from builder stage
COPY --from=builder /root/.local /home/appuser/.local

# Copy application source code
COPY src/ ./src/
COPY test_*.py ./
COPY *.md ./

# Set environment variables
ENV PYTHONPATH=/app
ENV PATH=/home/appuser/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Change ownership of app directory to appuser
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Note: Playwright installation skipped for Docker - 
# Set CRAWLER_USE_PLAYWRIGHT=false in environment to use basic HTTP client

# Expose port for FastAPI service
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command runs the FastAPI service
CMD ["python", "src/service.py"]
