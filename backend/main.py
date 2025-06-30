"""
Minimal FastAPI backend for SyftUI Example with SyftBox integration
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
    user_email: str = "unknown"


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime


# Initialize SyftBox connection
syftbox_client = None
try:
    from syft_core import Client
    syftbox_client = Client.load()
    logger.info(f"✅ SyftBox filesystem accessible — logged in as: {syftbox_client.email}")
    logger.info(f"✅ SyftBox app running at {syftbox_client.config.client_url}")
except Exception as e:
    logger.warning(f"⚠️  SyftBox not available: {e}")
    logger.info("Running in standalone mode")


app = FastAPI(
    title="SyftUI Example API",
    description="Minimal API for SyftUI Example with SyftBox integration",
    version="0.1.0",
)

# Add CORS middleware for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:*",
        "http://127.0.0.1:*"
    ],
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
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
    """Simple hello world endpoint with SyftBox integration."""
    logger.info("Hello world endpoint called")
    
    user_email = "unknown"
    if syftbox_client:
        user_email = syftbox_client.email
    
    return HelloResponse(
        message="Hello World from SyftUI Example!",
        timestamp=datetime.now(),
        status="success",
        user_email=user_email
    )


@app.get("/api/status")
async def get_status() -> Dict[str, Any]:
    """Get application status."""
    syftbox_status = "connected" if syftbox_client else "disconnected"
    user_email = syftbox_client.email if syftbox_client else "unknown"
    
    return {
        "app": "SyftUI Example",
        "version": "0.1.0",
        "timestamp": datetime.now(),
        "syftbox": {
            "status": syftbox_status,
            "user_email": user_email
        },
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