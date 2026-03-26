from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
import logging
import os

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.api import api_router

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Starting Demand Forecasting Service...")
    
    # Initialize ML models
    from app.services.model_service import ModelService
    model_service = ModelService()
    await model_service.initialize_models()
    
    yield
    
    # Shutdown
    logger.info("Shutting down Demand Forecasting Service...")


# Create FastAPI application
app = FastAPI(
    title="Demand Forecasting Service",
    description="AI-powered demand forecasting for procurement optimization",
    version="1.0.0",
    lifespan=lifespan
)

# Include API router
app.include_router(api_router, prefix="/api/v1")


# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Demand Forecasting Service",
        "version": "1.0.0"
    }


# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Demand Forecasting Service",
        "docs": "/api/v1/docs",
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
