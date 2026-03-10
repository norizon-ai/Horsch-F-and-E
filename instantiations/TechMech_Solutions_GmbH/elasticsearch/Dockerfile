FROM docker.elastic.co/elasticsearch/elasticsearch:8.11.0

# Single-node cluster, security disabled for local dev
ENV discovery.type=single-node \
    xpack.security.enabled=false \
    ES_JAVA_OPTS="-Xms2g -Xmx2g" \
    bootstrap.memory_lock=false \
    cluster.routing.allocation.disk.threshold_enabled=false

EXPOSE 9200
