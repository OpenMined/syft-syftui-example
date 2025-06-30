#!/bin/bash
set -e

echo "INFO	[syftbox] Script PID: $$"
echo "INFO	[syftbox] Start time: $(date)"
echo "INFO	[syftbox] App ID: com.github.openmined.syft-syftui-example"
echo "INFO	[syftbox] App Dir: $(pwd)"
echo "INFO	[syftbox] App Port: ${SYFTBOX_ASSIGNED_PORT:-8001}"
echo "INFO	[syftbox] Client Config Path: $HOME/.syftbox/config.json"
echo "INFO	[syftbox] PATH: $PATH"
echo "INFO	[syftbox] ==========STARTING APP=========="

# Disable interactive prompts and shell customizations for non-interactive environments
export ZSH_DISABLE_COMPFIX=true
export NONINTERACTIVE=1

# Clean up old virtual environment
echo "INFO	[syftbox] Setting up virtual environment with uv..."
rm -rf .venv

# Let uv handle Python version management - it will download Python 3.12 if needed
echo "INFO	[syftbox] Creating virtual environment with Python 3.12..."
uv venv --python 3.12

# Set the virtual environment path for uv to use
export VIRTUAL_ENV="$(pwd)/.venv"
export PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies using requirements.txt
echo "INFO	[syftbox] Installing Python dependencies..."
uv pip install -r requirements.txt

# Set default port if not provided
SYFTBOX_ASSIGNED_PORT=${SYFTBOX_ASSIGNED_PORT:-8001}

# Install bun if not available
if ! command -v bun &> /dev/null; then
    echo "INFO	[syftbox] Installing bun..."
    curl -fsSL https://bun.sh/install | bash
    export PATH="$HOME/.bun/bin:$PATH"
fi

# Build frontend using bun's runtime
echo "INFO	[syftbox] Building frontend..."
cd frontend
"$HOME/.bun/bin/bun" install
"$HOME/.bun/bin/bun" run build
cd ..

# Start the SyftUI Example app
echo "INFO	[syftbox] Starting SyftUI Example on port $SYFTBOX_ASSIGNED_PORT"
uv run uvicorn backend.main:app --host 0.0.0.0 --port $SYFTBOX_ASSIGNED_PORT 