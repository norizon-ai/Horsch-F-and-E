FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Create non-root user for security
RUN useradd -m -u 1000 proxyuser && \
    chown -R proxyuser:proxyuser /app
USER proxyuser

# Expose port
EXPOSE 5002

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD python -c "import httpx; httpx.get('http://localhost:5002/health', timeout=5)" || exit 1

# Run with optimized settings for production
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5002", "--workers", "4"]
