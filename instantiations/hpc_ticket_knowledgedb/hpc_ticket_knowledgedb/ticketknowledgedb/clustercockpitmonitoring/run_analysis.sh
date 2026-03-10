#!/bin/bash
# Helper script to run GPU utilization analysis

# Load config
source "$(dirname "$0")/config.sh"

# Export JWT token for Python script
export CLUSTERCOCKPIT_JWT="$JWT"

# Run the Python analysis script
python find_underutilized_gpu_jobs.py
