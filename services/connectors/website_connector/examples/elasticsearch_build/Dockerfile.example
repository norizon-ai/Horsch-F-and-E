FROM docker.elastic.co/elasticsearch/elasticsearch:8.11.0

# Disable security for easier local development
ENV xpack.security.enabled=false
ENV discovery.type=single-node

# Copy the indexed data (will be populated during build)
COPY es_data/ /usr/share/elasticsearch/data/

# Set permissions
USER root
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/data
USER elasticsearch

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 \
    CMD curl -f http://localhost:9200/_cluster/health || exit 1
