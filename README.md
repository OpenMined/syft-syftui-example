# Syft SyftUI Example

A minimal example SyftUI application demonstrating a simple setup with:

- **Frontend**: Next.js app that displays "Hello World"
- **Backend**: FastAPI server with a simple API endpoint
- **Cron Job**: Background task that logs periodically

## Quick Start

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

- `backend/` - FastAPI server
- `frontend/` - Next.js React app
- `src/syft_syftui_example/` - Python cron job component
- `justfile` - Build and run commands

## Development

- `just dev` - Run both frontend and backend in development mode
- `just install` - Install all dependencies
- `just build` - Build the frontend
- `just cron` - Run the cron job component

This is a minimal template for SyftUI applications. 