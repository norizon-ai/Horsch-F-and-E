FROM docker.elastic.co/elasticsearch/elasticsearch:8.11.0

USER root

ENV TZ=Europe \
    DEBIAN_FRONTEND=noninteractive

# Install Python and dependencies
RUN apt-get update && \
    apt-get install -y python3.9 python3-pip curl && \
    python3.9 -m pip install --upgrade pip setuptools wheel && \
    python3.9 -m pip install \
        elasticsearch==7.17.9 \
        sentence-transformers==3.0.1 \
        beautifulsoup4==4.12.2 \
        html2text==2020.1.16 \
        langchain-text-splitters==0.2.0 \
        tqdm==4.66.1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy Confluence export data (will be added during build)
COPY confluence_export /data/confluence_export

# Copy indexing script
COPY index_confluence.py /usr/share/elasticsearch/

# Copy startup scripts
COPY index_during_build.sh /usr/share/elasticsearch/
COPY entrypoint.sh /usr/share/elasticsearch/

# Make scripts executable
RUN chmod +x /usr/share/elasticsearch/index_during_build.sh && \
    chmod +x /usr/share/elasticsearch/entrypoint.sh

# Environment variables for Elasticsearch
ENV discovery.type=single-node \
    xpack.security.enabled=false \
    ES_JAVA_OPTS="-Xms2g -Xmx2g" \
    bootstrap.memory_lock=false \
    cluster.routing.allocation.disk.threshold_enabled=false

# Set ownership
RUN chown -R elasticsearch:elasticsearch /usr/share/elasticsearch /data

# Switch to elasticsearch user and index data during build
USER elasticsearch
RUN /usr/share/elasticsearch/index_during_build.sh

# Expose Elasticsearch port
EXPOSE 9200

# Use custom entrypoint
ENTRYPOINT ["/usr/share/elasticsearch/entrypoint.sh"]
