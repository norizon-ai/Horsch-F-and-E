# HPC Knowledge Database: Scalability Implementation Guide

**Status:** Draft for Phase 1 Implementation
**Target Completion:** 4 weeks
**Owner:** DevOps/SRE Team

---

## PHASE 1 IMPLEMENTATION CHECKLIST

### Week 1: Elasticsearch Cluster Setup

#### 1.1 Provision VMs for ES Cluster

```bash
# Variables
REGION="DE-ERL"
FLAVOR="m4.xlarge"  # 8 vCPU, 32GB RAM
IMAGE="Ubuntu 22.04"

# Create master-only node
openstack server create \
  --flavor $FLAVOR \
  --image $IMAGE \
  --key-name hpc-kb-key \
  --security-group hpc_kb_secgroup \
  --nic net-id=<network-id> \
  hpc-kb-es-master

# Create data node 1
openstack server create \
  --flavor $FLAVOR \
  --image $IMAGE \
  --key-name hpc-kb-key \
  --security-group hpc_kb_secgroup \
  --nic net-id=<network-id> \
  hpc-kb-es-data-1

# Create data node 2
openstack server create \
  --flavor $FLAVOR \
  --image $IMAGE \
  --key-name hpc-kb-key \
  --security-group hpc_kb_secgroup \
  --nic net-id=<network-id> \
  hpc-kb-es-data-2

# Assign floating IPs for management (optional)
openstack floating ip create belwue | grep "floating_ip_address"
openstack server add floating ip hpc-kb-es-master <ip>
```

#### 1.2 Create Docker Compose for ES Cluster

**File: `/opt/hpc-kb/docker-compose-cluster.yml`**

```yaml
version: '3.8'

services:
  # ES Master Node (dedicated master, no data)
  es-master:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    container_name: es-master
    environment:
      - node.name=es-master
      - cluster.name=hpc-kb-cluster
      - discovery.seed_hosts=es-data-1,es-data-2
      - cluster.initial_master_nodes=es-master
      - node.master=true
      - node.data=false
      - node.ingest=false
      - xpack.security.enabled=false
      - ES_JAVA_OPTS=-Xms8g -Xmx8g
      - bootstrap.memory_lock=true
    ulimits:
      memlock:
        soft: -1
        hard: -1
    ports:
      - "9300:9300"  # Node communication
    networks:
      - hpc-kb-network
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9200/_cluster/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ES Data Node 1
  es-data-1:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    container_name: es-data-1
    environment:
      - node.name=es-data-1
      - cluster.name=hpc-kb-cluster
      - discovery.seed_hosts=es-master,es-data-2
      - cluster.initial_master_nodes=es-master
      - node.master=false
      - node.data=true
      - node.ingest=true
      - xpack.security.enabled=false
      - ES_JAVA_OPTS=-Xms16g -Xmx16g
      - bootstrap.memory_lock=true
      - indices.memory.index_buffer_size=40%
    ulimits:
      memlock:
        soft: -1
        hard: -1
    ports:
      - "9200:9200"
    volumes:
      - es-data-1:/usr/share/elasticsearch/data
    networks:
      - hpc-kb-network
    depends_on:
      - es-master
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9200/_cluster/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ES Data Node 2
  es-data-2:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    container_name: es-data-2
    environment:
      - node.name=es-data-2
      - cluster.name=hpc-kb-cluster
      - discovery.seed_hosts=es-master,es-data-1
      - cluster.initial_master_nodes=es-master
      - node.master=false
      - node.data=true
      - node.ingest=true
      - xpack.security.enabled=false
      - ES_JAVA_OPTS=-Xms16g -Xmx16g
      - bootstrap.memory_lock=true
      - indices.memory.index_buffer_size=40%
    ulimits:
      memlock:
        soft: -1
        hard: -1
    ports:
      - "9201:9200"
    volumes:
      - es-data-2:/usr/share/elasticsearch/data
    networks:
      - hpc-kb-network
    depends_on:
      - es-master
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9200/_cluster/health"]
      interval: 30s
      timeout: 10s
      retries: 3

networks:
  hpc-kb-network:
    driver: bridge

volumes:
  es-data-1:
    driver: local
  es-data-2:
    driver: local
```

#### 1.3 Validate ES Cluster Formation

```bash
# SSH to any ES node
ssh -i ~/.ssh/fau_openstack_key ubuntu@<floating-ip>

# Check cluster health
curl http://localhost:9200/_cluster/health?pretty

# Expected output:
{
  "cluster_name" : "hpc-kb-cluster",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 3,
  "number_of_data_nodes" : 2,
  "active_primary_shards" : XX,
  "active_shards" : XX,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0
}

# List nodes
curl http://localhost:9200/_cat/nodes?v

# Check indices
curl http://localhost:9200/_cat/indices?v
```

---

### Week 2: Data Migration to Cluster

#### 2.1 Reindex with Zero Downtime

```bash
# Step 1: Setup remote cluster on original ES
# SSH to original ES VM
ssh -i ~/.ssh/fau_openstack_key ubuntu@<original-es-ip>

# Stop indexer container (but keep API running)
docker-compose stop indexer

# Step 2: Configure remote cluster connection
curl -X PUT "localhost:9200/_cluster/settings" \
  -H 'Content-Type: application/json' \
  -d '{
    "persistent": {
      "search.remote.hpc-kb-cluster-old.seeds": ["<original-es-ip>:9200"]
    }
  }'

# Step 3: On new cluster, reindex from remote
curl -X POST "es-data-1:9200/_reindex?wait_for_completion=false" \
  -H 'Content-Type: application/json' \
  -d '{
    "source": {
      "remote": {
        "host": "http://<original-es-ip>:9200"
      },
      "index": "docs",
      "size": 5000
    },
    "dest": {
      "index": "docs",
      "op_type": "create"
    }
  }'

# Monitor reindexing progress
curl http://es-data-1:9200/_tasks?detailed=true | jq '.tasks[] | select(.action=="indices:data/write/reindex")'

# Once complete, verify data:
curl http://es-data-1:9200/docs/_count

# Step 4: Update API to use new cluster
# Update environment: ELASTIC_URL=http://es-data-1:9200 (or load balancer)
# Restart API containers

# Step 5: Decommission original ES
# Verify no traffic → Stop indexer → Backup data → Delete VM
```

#### 2.2 Update docker-compose.yml for Load-Balanced ES Access

```yaml
services:
  dr-api:
    environment:
      # Use load balancer hostname (not direct node)
      - ELASTIC_URL=http://es-lb:9200
    depends_on:
      - es-lb

  indexer:
    environment:
      - ELASTIC_URL=http://es-lb:9200
    depends_on:
      - es-lb

  # HAProxy for ES cluster (optional, for load balancing across data nodes)
  es-lb:
    image: haproxy:2.8-alpine
    container_name: es-lb
    ports:
      - "9200:9200"
    volumes:
      - ./haproxy-es.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    depends_on:
      - es-data-1
      - es-data-2
    networks:
      - hpc-kb-network
```

**File: `haproxy-es.cfg`**

```
global
  log stdout local0
  maxconn 65536
  daemon

defaults
  log     global
  mode    http
  option  httplog
  option  dontlognull
  timeout connect 5000
  timeout client  50000
  timeout server  50000

frontend es_front
  bind *:9200
  default_backend es_back

backend es_back
  balance roundrobin
  option httpchk GET /_cluster/health
  server es-data-1 es-data-1:9200 check inter 5s rise 2 fall 2
  server es-data-2 es-data-2:9200 check inter 5s rise 2 fall 2
```

---

### Week 3: API Scaling & HAProxy Load Balancer

#### 3.1 Deploy HAProxy Load Balancer

**File: `docker-compose-haproxy.yml`**

```yaml
version: '3.8'

services:
  haproxy:
    image: haproxy:2.8-alpine
    container_name: hpc-kb-lb
    ports:
      - "8001:8001"  # Public API endpoint
      - "8404:8404"  # Stats page (restrict access)
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
      - /var/run/docker.sock:/var/run/docker.sock
    networks:
      - hpc-kb-network
    restart: unless-stopped

networks:
  hpc-kb-network:
    external: true
```

**File: `haproxy.cfg`**

```
global
  log stdout local0 debug
  log stdout local1 notice
  maxconn 65536
  daemon
  stats socket /run/haproxy/admin.sock mode 660 level admin
  stats timeout 30s

defaults
  log     global
  mode    http
  option  httplog
  option  dontlognull
  option  http-server-close
  timeout connect 5000
  timeout client  50000
  timeout server  50000
  errorfile 400 /usr/local/etc/haproxy/errors/400.http
  errorfile 403 /usr/local/etc/haproxy/errors/403.http
  errorfile 408 /usr/local/etc/haproxy/errors/408.http
  errorfile 500 /usr/local/etc/haproxy/errors/500.http
  errorfile 502 /usr/local/etc/haproxy/errors/502.http
  errorfile 503 /usr/local/etc/haproxy/errors/503.http
  errorfile 504 /usr/local/etc/haproxy/errors/504.http

listen stats
  bind *:8404
  stats enable
  stats uri /stats
  stats refresh 30s
  stats admin if TRUE

frontend dr_api_front
  bind *:8001
  default_backend dr_api_back
  option httplog
  capture request header Host len 64
  capture request header User-Agent len 128
  log-format "%ci:%cp [%tr] %ft %b/%s %TR/%Tw/%Tc/%Tr/%Ta %ST %B %CC %CS %tsc %ac/%fc/%bc/%sc/%rc %sq/%bq %hr %hs %{+Q}r"

backend dr_api_back
  balance roundrobin
  option httpchk GET /health
  http-check expect status 200
  server api-1 api-1:8000 check inter 10s fall 3 rise 2
  server api-2 api-2:8000 check inter 10s fall 3 rise 2
  server api-3 api-3:8000 check inter 10s fall 3 rise 2 backup

  # Stickiness for long-running requests
  cookie SERVERID insert indirect nocache
  server api-1 api-1:8000 cookie api-1 check
  server api-2 api-2:8000 cookie api-2 check
  server api-3 api-3:8000 cookie api-3 check backup

  # Timeout for long queries
  timeout queue 30s
  timeout server 300s
```

#### 3.2 Update Main docker-compose.yml

```yaml
version: '3.8'

services:
  # Elasticsearch Load Balancer (points to cluster)
  es-proxy:
    image: haproxy:2.8-alpine
    container_name: es-proxy
    ports:
      - "9200:9200"
    volumes:
      - ./haproxy-es.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    networks:
      - hpc-kb-network
    restart: unless-stopped

  # API Instance 1
  dr-api-1:
    build:
      context: .
      dockerfile: Dockerfile.api
    container_name: hpc-kb-dr-api-1
    expose:
      - "8000"
    environment:
      - LLM_BASE_URL=${LLM_BASE_URL:-http://lme49.cs.fau.de:30000/v1}
      - LLM_API_KEY=${LLM_API_KEY:-dummy}
      - LLM_MODEL=${LLM_MODEL:-openai/gpt-oss-120b}
      - ELASTIC_URL=http://es-proxy:9200
      - DOCS_INDEX=${DOCS_INDEX:-docs}
      - TICKETS_INDEX=${TICKETS_INDEX:-tickets}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - es-proxy
      - redis
    networks:
      - hpc-kb-network
    restart: unless-stopped
    resources:
      limits:
        cpus: '1.0'
        memory: 4G
      reservations:
        cpus: '0.5'
        memory: 2G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # API Instance 2
  dr-api-2:
    build:
      context: .
      dockerfile: Dockerfile.api
    container_name: hpc-kb-dr-api-2
    expose:
      - "8000"
    environment:
      - LLM_BASE_URL=${LLM_BASE_URL:-http://lme49.cs.fau.de:30000/v1}
      - LLM_API_KEY=${LLM_API_KEY:-dummy}
      - LLM_MODEL=${LLM_MODEL:-openai/gpt-oss-120b}
      - ELASTIC_URL=http://es-proxy:9200
      - DOCS_INDEX=${DOCS_INDEX:-docs}
      - TICKETS_INDEX=${TICKETS_INDEX:-tickets}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - es-proxy
      - redis
    networks:
      - hpc-kb-network
    restart: unless-stopped
    resources:
      limits:
        cpus: '1.0'
        memory: 4G
      reservations:
        cpus: '0.5'
        memory: 2G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # API Instance 3 (optional, for surge capacity)
  dr-api-3:
    build:
      context: .
      dockerfile: Dockerfile.api
    container_name: hpc-kb-dr-api-3
    expose:
      - "8000"
    environment:
      - LLM_BASE_URL=${LLM_BASE_URL:-http://lme49.cs.fau.de:30000/v1}
      - LLM_API_KEY=${LLM_API_KEY:-dummy}
      - LLM_MODEL=${LLM_MODEL:-openai/gpt-oss-120b}
      - ELASTIC_URL=http://es-proxy:9200
      - DOCS_INDEX=${DOCS_INDEX:-docs}
      - TICKETS_INDEX=${TICKETS_INDEX:-tickets}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - es-proxy
      - redis
    networks:
      - hpc-kb-network
    restart: unless-stopped
    resources:
      limits:
        cpus: '1.0'
        memory: 4G
      reservations:
        cpus: '0.5'
        memory: 2G
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # HAProxy Load Balancer
  api-lb:
    image: haproxy:2.8-alpine
    container_name: hpc-kb-api-lb
    ports:
      - "8001:8001"
      - "8404:8404"
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    depends_on:
      - dr-api-1
      - dr-api-2
    networks:
      - hpc-kb-network
    restart: unless-stopped

  # Redis Cache
  redis:
    image: redis:7.2-alpine
    container_name: hpc-kb-redis
    expose:
      - "6379"
    command: redis-server --appendonly yes --maxmemory 4gb --maxmemory-policy allkeys-lru
    volumes:
      - redis-data:/data
    networks:
      - hpc-kb-network
    restart: unless-stopped
    resources:
      limits:
        cpus: '1.0'
        memory: 4.5G
      reservations:
        cpus: '0.5'
        memory: 2G
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 3

  # Data Indexer
  indexer:
    build:
      context: .
      dockerfile: Dockerfile.indexer
    container_name: hpc-kb-indexer
    environment:
      - ELASTIC_URL=http://es-proxy:9200
      - DOCS_INDEX=${DOCS_INDEX:-docs}
      - TICKETS_INDEX=${TICKETS_INDEX:-tickets}
      - EMBED_MODEL=${EMBED_MODEL:-sentence-transformers/all-MiniLM-L6-v2}
    depends_on:
      - es-proxy
    networks:
      - hpc-kb-network
    volumes:
      - ./ticketknowledgedb:/app/data:ro
    profiles:
      - indexing
    command: python index_all.py

networks:
  hpc-kb-network:
    driver: bridge

volumes:
  redis-data:
    driver: local
```

---

### Week 4: Monitoring & Alerting

#### 4.1 Prometheus Configuration

**File: `prometheus.yml`**

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: 'hpc-kb'
    environment: 'production'

alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - 'alertmanager:9093'

rule_files:
  - 'alerts.yml'

scrape_configs:
  # Elasticsearch cluster metrics
  - job_name: 'elasticsearch'
    static_configs:
      - targets: ['es-data-1:9200', 'es-data-2:9200', 'es-master:9200']
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance

  # API instances
  - job_name: 'api'
    static_configs:
      - targets: ['dr-api-1:8000', 'dr-api-2:8000', 'dr-api-3:8000']
    relabel_configs:
      - source_labels: [__address__]
        target_label: instance

  # Redis
  - job_name: 'redis'
    static_configs:
      - targets: ['redis:6379']

  # HAProxy stats
  - job_name: 'haproxy'
    static_configs:
      - targets: ['api-lb:8404/stats;csv']

  # Docker metrics (via cadvisor)
  - job_name: 'docker'
    static_configs:
      - targets: ['cadvisor:8080']
```

**File: `alerts.yml`**

```yaml
groups:
  - name: hpc_kb_alerts
    interval: 30s
    rules:
      # Elasticsearch alerts
      - alert: ESClusterRed
        expr: elasticsearch_cluster_health_status{color="red"} == 1
        for: 2m
        annotations:
          summary: "ES cluster status is RED"
          description: "Cluster {{ $labels.cluster }} health is RED"

      - alert: ESHighDiskUsage
        expr: (elasticsearch_filesystem_data_used_bytes / elasticsearch_filesystem_data_size_bytes) > 0.8
        for: 5m
        annotations:
          summary: "ES disk usage > 80%"
          description: "Node {{ $labels.node }} disk usage: {{ $value | humanizePercentage }}"

      - alert: ESHighJVMMemory
        expr: (elasticsearch_jvm_memory_used_bytes / elasticsearch_jvm_memory_max_bytes) > 0.85
        for: 5m
        annotations:
          summary: "ES JVM memory > 85%"
          description: "Node {{ $labels.node }} JVM: {{ $value | humanizePercentage }}"

      # API alerts
      - alert: APIHighErrorRate
        expr: (rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])) > 0.01
        for: 5m
        annotations:
          summary: "API error rate > 1%"
          description: "Error rate: {{ $value | humanizePercentage }}"

      - alert: APIHighLatency
        expr: histogram_quantile(0.99, http_request_duration_seconds_bucket) > 5
        for: 5m
        annotations:
          summary: "API p99 latency > 5s"
          description: "p99 latency: {{ $value }}s"

      - alert: APIInstanceDown
        expr: up{job="api"} == 0
        for: 2m
        annotations:
          summary: "API instance down"
          description: "Instance {{ $labels.instance }} is down"

      # Redis alerts
      - alert: RedisHighMemoryUsage
        expr: (redis_memory_used_bytes / redis_memory_max_bytes) > 0.85
        for: 5m
        annotations:
          summary: "Redis memory > 85%"
          description: "Memory usage: {{ $value | humanizePercentage }}"

      - alert: RedisLowHitRate
        expr: redis_keyspace_hits_total / (redis_keyspace_hits_total + redis_keyspace_misses_total) < 0.5
        for: 10m
        annotations:
          summary: "Redis hit rate < 50%"
          description: "Hit rate: {{ $value | humanizePercentage }}"

      # HAProxy alerts
      - alert: APIBackendDown
        expr: count(haproxy_backend_up{backend="dr_api_back"}) < 2
        for: 2m
        annotations:
          summary: "Less than 2 API backends healthy"
          description: "Available backends: {{ $value }}"
```

#### 4.2 Docker Compose for Monitoring Stack

**File: `docker-compose-monitoring.yml`**

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - ./alerts.yml:/etc/prometheus/alerts.yml:ro
      - prometheus-data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'
    networks:
      - hpc-kb-network
    restart: unless-stopped

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_PASSWORD:-admin}
      - GF_USERS_ALLOW_SIGN_UP=false
    volumes:
      - grafana-data:/var/lib/grafana
      - ./grafana-datasources.yml:/etc/grafana/provisioning/datasources/datasources.yml:ro
      - ./grafana-dashboards.yml:/etc/grafana/provisioning/dashboards/dashboards.yml:ro
    depends_on:
      - prometheus
    networks:
      - hpc-kb-network
    restart: unless-stopped

  alertmanager:
    image: prom/alertmanager:latest
    container_name: alertmanager
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager.yml:/etc/alertmanager/alertmanager.yml:ro
      - alertmanager-data:/alertmanager
    command:
      - '--config.file=/etc/alertmanager/alertmanager.yml'
      - '--storage.path=/alertmanager'
    networks:
      - hpc-kb-network
    restart: unless-stopped

  cadvisor:
    image: gcr.io/cadvisor/cadvisor:latest
    container_name: cadvisor
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker/:/var/lib/docker:ro
    networks:
      - hpc-kb-network
    restart: unless-stopped

networks:
  hpc-kb-network:
    external: true

volumes:
  prometheus-data:
    driver: local
  grafana-data:
    driver: local
  alertmanager-data:
    driver: local
```

---

## DEPLOYMENT COMMANDS (Quick Reference)

```bash
# Week 1: Start ES cluster
docker-compose -f docker-compose-cluster.yml up -d

# Week 2: Verify ES cluster
curl http://localhost:9200/_cluster/health?pretty

# Week 3: Start main stack with LB and Redis
docker-compose -f docker-compose.yml up -d

# Week 4: Start monitoring
docker-compose -f docker-compose-monitoring.yml up -d

# Verify all services
docker-compose ps
docker-compose logs -f api-lb
curl http://localhost:8001/health
curl http://localhost:3000 (Grafana)
curl http://localhost:8404/stats (HAProxy stats)
```

---

## TESTING CHECKLIST

- [ ] Elasticsearch cluster consensus (3 nodes visible)
- [ ] API responds through HAProxy load balancer
- [ ] Health checks passing (ES, API, Redis)
- [ ] Redis caching working (check hit rates)
- [ ] Prometheus scraping all targets
- [ ] Grafana dashboards displaying metrics
- [ ] Alert rules evaluating without errors
- [ ] Single API instance failure = traffic redirects to others
- [ ] Single ES node failure = cluster remains green
- [ ] Backup snapshots working

---

**Next Steps:** Review and approve by Week 1, execute deployment by Week 4
