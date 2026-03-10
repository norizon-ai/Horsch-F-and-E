#!/bin/bash
# Load config
source "$(dirname "$0")/config.sh"

# Get current timestamp
END_TIME=$(date +%s)
START_TIME=$((END_TIME - 86400))  # 24 hours ago

echo "Querying Alex cluster jobs from $START_TIME to $END_TIME"
curl -s -X "GET" "${API_BASE_URL}/userapi/jobs/?state=running&cluster=alex&start-time=${START_TIME}-${END_TIME}" \
  -H "X-Auth-Token: $JWT" | jq '.'