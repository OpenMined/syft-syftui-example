# SyftUI Example Build Commands

set dotenv-load := true

_green := '\033[1;32m'
_nc := '\033[0m'

@default:
    just --list

# Install all dependencies
install:
    @echo "${_green}Installing backend dependencies...${_nc}"
    uv sync
    @echo "${_green}Installing frontend dependencies...${_nc}"
    bun install --cwd frontend

# Run development server (frontend + backend)
dev:
    @echo "${_green}Starting development servers...${_nc}"
    bunx concurrently --names "backend,frontend" --prefix-colors "red,green" \
        "uv run uvicorn backend.main:app --reload --port 8001" \
        "NEXT_PUBLIC_API_URL=http://localhost:8001 bun run --cwd frontend dev"

# Build frontend
build:
    @echo "${_green}Building frontend...${_nc}"
    bun run --cwd frontend build

# Run backend only
backend:
    uv run uvicorn backend.main:app --reload --port 8001

# Run frontend only  
frontend:
    NEXT_PUBLIC_API_URL=http://localhost:8001 bun run --cwd frontend dev

# Run cron job component
cron:
    uv run python -m syft_syftui_example.cron

# Production build and run
prod:
    just build
    uv run uvicorn backend.main:app --port 8001

# Clean build artifacts
clean:
    rm -rf frontend/.next
    rm -rf frontend/out
    rm -rf .venv
    rm -rf __pycache__ 