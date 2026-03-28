from fastapi import APIRouter

from app.api.v1.endpoints import forecasting, models, health

api_router = APIRouter()

# Include endpoints
api_router.include_router(forecasting.router, prefix="/forecast", tags=["forecasting"])
api_router.include_router(models.router, prefix="/models", tags=["models"])
api_router.include_router(health.router, prefix="/health", tags=["health"])
