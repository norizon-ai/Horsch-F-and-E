FROM python:3.11-slim

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir mcp-atlassian

EXPOSE 8005

HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=15s \
    CMD curl -sf --max-time 2 http://localhost:8005/sse | head -1 | grep -q "event:" || exit 1

CMD ["mcp-atlassian", "--transport", "sse", "--port", "8005"]
