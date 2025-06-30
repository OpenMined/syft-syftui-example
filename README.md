# Syft SyftUI Example

A minimal example SyftUI application demonstrating a simple setup with:

- **Frontend**: Next.js app that displays "Hello World"
- **Backend**: FastAPI server with SyftBox integration
- **Cron Job**: Background task that logs periodically
- **SyftBox Integration**: Proper `run.sh` and SyftBox client connection

## Quick Start

### For SyftBox (Production)

1. Copy this directory to your SyftBox apps folder
2. SyftBox will automatically run `./run.sh` to start the app
3. Visit the assigned port in your browser

### For Development

1. Install dependencies:
```bash
just install
```

2. Run the development server:
```bash
just dev
```

3. Open your browser to http://localhost:3000

## Architecture

- `run.sh` - SyftBox app entry point (called by SyftBox)
- `requirements.txt` - Dependencies for SyftBox deployment
- `backend/` - FastAPI server with SyftBox client integration
- `frontend/` - Next.js React app
- `src/syft_syftui_example/` - Python cron job component
- `justfile` - Build and run commands for development

## SyftBox Integration

This app properly integrates with SyftBox by:

- **`run.sh`**: Main entry point with proper SyftBox logging format
- **Port handling**: Uses `SYFTBOX_ASSIGNED_PORT` environment variable
- **SyftBox client**: Connects to SyftBox filesystem and shows user email
- **Virtual environment**: Sets up clean Python environment with `uv`
- **Frontend building**: Builds Next.js app as part of startup

## Development Commands

- `just dev` - Run both frontend and backend in development mode
- `just install` - Install all dependencies
- `just build` - Build the frontend
- `just cron` - Run the cron job component
- `./run.sh` - Run as SyftBox would (for testing)

## SyftBox Deployment

1. Ensure SyftBox is installed and you're logged in
2. Copy this directory to your SyftBox apps folder
3. SyftBox will handle the rest via `run.sh`

This is a minimal but complete template for SyftUI applications. 