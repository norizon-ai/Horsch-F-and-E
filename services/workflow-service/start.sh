#!/bin/bash
set -e

echo "Running Alembic migrations against Azure PostgreSQL Flexible Server..."
alembic upgrade head

echo "Starting Gunicorn server..."
exec gunicorn app.main:app -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8001
