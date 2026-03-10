#!/bin/bash
# Load config
source "$(dirname "$0")/config.sh"

# Get current timestamp (October 8, 2025 ≈ 1760000000)
# Query for running jobs in the last 24 hours
END_TIME=$(date +%s)
START_TIME=$((END_TIME - 86400))  # 24 hours ago

echo "Querying jobs from $START_TIME to $END_TIME"
curl -X "GET" "${API_BASE_URL}/userapi/jobs/?state=running&cluster=helma&start-time=${START_TIME}-${END_TIME}" -H "X-Auth-Token: $JWT"

curl -X "GET" "${API_BASE_URL}/userapi/jobs/?cluster=helma&start-time=${START_TIME}-${END_TIME}" -H "X-Auth-Token: $JWT"
