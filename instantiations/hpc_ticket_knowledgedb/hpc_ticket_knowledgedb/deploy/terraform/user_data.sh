#!/bin/bash
# User data script for HPC Knowledge Database VM initialization
# This script runs on first boot to set up the environment

set -e

# Log all output
exec > >(tee /var/log/user-data.log)
exec 2>&1

echo "=================================="
echo "HPC Knowledge Database VM Setup"
echo "=================================="
echo "Starting at: $(date)"

# Update system
echo "Updating system packages..."
apt-get update
apt-get upgrade -y

# Install required packages
echo "Installing Docker and dependencies..."
apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git \
    jq

# Install Docker
if ! command -v docker &> /dev/null; then
    echo "Installing Docker..."
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt-get update
    apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

    # Add ubuntu user to docker group
    usermod -aG docker ubuntu

    echo "Docker installed successfully"
else
    echo "Docker already installed"
fi

# Install Docker Compose V2
if ! docker compose version &> /dev/null; then
    echo "Installing Docker Compose..."
    mkdir -p /usr/local/lib/docker/cli-plugins
    curl -SL https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-linux-x86_64 -o /usr/local/lib/docker/cli-plugins/docker-compose
    chmod +x /usr/local/lib/docker/cli-plugins/docker-compose
    echo "Docker Compose installed"
fi

# Configure Elasticsearch volume (if attached)
DEVICE="/dev/vdb"
MOUNT_POINT="/var/lib/elasticsearch"

if [ -b "$DEVICE" ]; then
    echo "Configuring Elasticsearch data volume..."

    # Check if already formatted
    if ! blkid "$DEVICE" | grep -q "ext4"; then
        echo "Formatting volume..."
        mkfs.ext4 "$DEVICE"
    fi

    # Create mount point
    mkdir -p "$MOUNT_POINT"

    # Mount volume
    if ! grep -q "$DEVICE" /etc/fstab; then
        echo "$DEVICE $MOUNT_POINT ext4 defaults 0 2" >> /etc/fstab
    fi
    mount -a

    # Set permissions
    chmod 777 "$MOUNT_POINT"

    echo "Elasticsearch volume configured"
else
    echo "[!] No additional volume found for Elasticsearch data"
    mkdir -p "$MOUNT_POINT"
    chmod 777 "$MOUNT_POINT"
fi

# Create application directory
echo "Setting up application directory..."
APP_DIR="/opt/hpc-knowledge-db"
mkdir -p "$APP_DIR"
cd "$APP_DIR"

# Create docker-compose.yml
cat > docker-compose.yml <<'EOF'
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    container_name: hpc-kb-elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - ES_JAVA_OPTS=-Xms4g -Xmx4g
      - bootstrap.memory_lock=false
    ports:
      - "9200:9200"
    volumes:
      - /var/lib/elasticsearch:/usr/share/elasticsearch/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9200/_cluster/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  dr-api:
    image: ${docker_registry}/hpc-kb-dr-api:${dr_api_tag}
    container_name: hpc-kb-dr-api
    ports:
      - "8001:8000"
    environment:
      - LLM_BASE_URL=${llm_base_url}
      - LLM_API_KEY=dummy
      - LLM_MODEL=${llm_model}
      - ELASTIC_URL=http://elasticsearch:9200
      - DOCS_INDEX=docs
      - TICKETS_INDEX=tickets
    depends_on:
      - elasticsearch
    restart: unless-stopped
EOF

echo "Docker Compose configuration created"

# Pull Docker images
echo "Pulling Docker images..."
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.11.0
docker pull ${docker_registry}/hpc-kb-dr-api:${dr_api_tag}
echo "Docker images pulled"

# Start services
echo "Starting services..."
docker compose up -d

# Wait for services to be healthy
echo "Waiting for services to start..."
sleep 30

# Check service status
echo "Checking service status..."
docker compose ps

# Create systemd service for automatic startup
cat > /etc/systemd/system/hpc-kb.service <<'SYSTEMD_EOF'
[Unit]
Description=HPC Knowledge Database Services
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/opt/hpc-knowledge-db
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
SYSTEMD_EOF

systemctl daemon-reload
systemctl enable hpc-kb.service

echo "=================================="
echo "HPC Knowledge Database Setup Complete!"
echo "=================================="
echo "Services running:"
docker compose ps
echo ""
echo "To index data, SSH to the VM and run:"
echo "  cd /opt/hpc-knowledge-db"
echo "  docker compose --profile indexing up indexer"
echo ""
echo "Finished at: $(date)"
