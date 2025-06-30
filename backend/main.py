"""
Minimal FastAPI backend for SyftUI Example
"""

from datetime import datetime
from typing import Dict, Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from loguru import logger
from pydantic import BaseModel


class HelloResponse(BaseModel):
    message: str
    timestamp: datetime
    status: str


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime


app = FastAPI(
    title="SyftUI Example API",
    description="Minimal API for SyftUI Example",
    version="0.1.0",
)

# Add CORS middleware for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now()
    )


@app.get("/api/hello", response_model=HelloResponse)
async def hello_world():
    """Simple hello world endpoint."""
    logger.info("Hello world endpoint called")
    return HelloResponse(
        message="Hello World from SyftUI Example!",
        timestamp=datetime.now(),
        status="success"
    )


@app.get("/api/status")
async def get_status() -> Dict[str, Any]:
    """Get application status."""
    return {
        "app": "SyftUI Example",
        "version": "0.1.0",
        "timestamp": datetime.now(),
        "components": {
            "backend": "running",
            "frontend": "available",
            "cron": "available"
        }
    }


# Serve static files (for production)
try:
    app.mount("/", StaticFiles(directory="frontend/out", html=True, check_dir=False))
except RuntimeError:
    # Frontend not built yet, skip static files
    logger.warning("Frontend not built - static files not available")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 