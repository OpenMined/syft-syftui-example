#!/bin/bash

echo "INFO	[syftbox] Script PID: $$"
echo "INFO	[syftbox] Start time: $(date)"
echo "INFO	[syftbox] App ID: com.github.openmined.syft-syftui-example"
echo "INFO	[syftbox] App Dir: $(pwd)"
echo "INFO	[syftbox] App Port: ${SYFTBOX_ASSIGNED_PORT:-8001}"
echo "INFO	[syftbox] Client Config Path: $HOME/.syftbox/config.json"
echo "INFO	[syftbox] PATH: $PATH"
echo "INFO	[syftbox] ==========STARTING APP=========="

# Clean up old virtual environment
rm -rf .venv

# Create virtual environment with uv
uv venv -p 3.12
uv pip install -r requirements.txt

# Set default port if not provided
SYFTBOX_ASSIGNED_PORT=${SYFTBOX_ASSIGNED_PORT:-8001}

# Build frontend
echo "INFO	[syftbox] Building frontend..."
cd frontend
bun install
bun run build
cd ..

# Start the SyftUI Example app
echo "INFO	[syftbox] Starting SyftUI Example on port $SYFTBOX_ASSIGNED_PORT"
uv run uvicorn backend.main:app --host 0.0.0.0 --port $SYFTBOX_ASSIGNED_PORT 