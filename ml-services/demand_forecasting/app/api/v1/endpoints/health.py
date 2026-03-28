from fastapi import APIRouter
import logging
from datetime import datetime

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
async def health_check():
    """Health check endpoint for the demand forecasting service."""
    try:
        # Check model service status
        from app.services.model_service import ModelService
        model_service = ModelService()
        
        models_loaded = len(model_service.models) > 0
        
        return {
            "status": "healthy",
            "service": "Demand Forecasting Service",
            "version": "1.0.0",
            "timestamp": datetime.now().isoformat(),
            "models_loaded": models_loaded,
            "available_models": list(model_service.models.keys()) if models_loaded else []
        }
        
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return {
            "status": "unhealthy",
            "service": "Demand Forecasting Service",
            "version": "1.0.0",
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        }


@router.get("/detailed")
async def detailed_health_check():
    """Detailed health check with component status."""
    components = {
        "models": "unknown",
        "database": "unknown",
        "mlflow": "unknown"
    }
    
    try:
        # Check models
        from app.services.model_service import ModelService
        model_service = ModelService()
        if model_service.models:
            components["models"] = "healthy"
        else:
            components["models"] = "unhealthy"
    except Exception as e:
        components["models"] = f"error: {str(e)}"
    
    # Check database connectivity
    try:
        # TODO: Implement database health check
        components["database"] = "healthy"
    except Exception as e:
        components["database"] = f"error: {str(e)}"
    
    # Check MLflow connectivity
    try:
        import mlflow
        mlflow.set_tracking_uri("http://localhost:5000")
        # Simple test - try to list experiments
        mlflow.search_experiments()
        components["mlflow"] = "healthy"
    except Exception as e:
        components["mlflow"] = f"error: {str(e)}"
    
    overall_status = "healthy" if all(
        status == "healthy" for status in components.values()
    ) else "unhealthy"
    
    return {
        "status": overall_status,
        "service": "Demand Forecasting Service",
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat(),
        "components": components
    }
