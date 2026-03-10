#!/bin/bash
# Helper script to run user ranking analysis

# Load config
source "$(dirname "$0")/config.sh"

# Export JWT token for Python script
export CLUSTERCOCKPIT_JWT="$JWT"

# Run the user ranking script
python3 rank_worst_users.py
