from typing import Optional, Dict, Any
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field
import logging

from app.services.model_service import ModelService

router = APIRouter()
logger = logging.getLogger(__name__)

# Global model service instance
model_service = ModelService()


class ForecastRequest(BaseModel):
    product_id: int = Field(..., description="Product ID to forecast")
    horizon: int = Field(default=90, ge=1, le=365, description="Forecast horizon in days")
    model_type: str = Field(default="ensemble", description="Model type: lstm, prophet, xgboost, ensemble")
    historical_data: Optional[Dict[str, Any]] = Field(None, description="Historical data (optional)")


class ForecastResponse(BaseModel):
    product_id: int
    forecast_horizon: int
    model_type: str
    predictions: Dict[str, Any]
    confidence_intervals: Dict[str, Any]
    model_metadata: Dict[str, Any]
    generated_at: str


@router.post("/", response_model=ForecastResponse)
async def create_forecast(request: ForecastRequest):
    """Generate demand forecast for a product."""
    try:
        # Ensure model service is initialized
        if not model_service.models:
            await model_service.initialize_models()
        
        # Convert historical data if provided
        historical_data = None
        if request.historical_data:
            import pandas as pd
            historical_data = pd.DataFrame(request.historical_data)
        
        # Generate forecast
        result = await model_service.predict_demand(
            product_id=request.product_id,
            horizon=request.horizon,
            model_type=request.model_type,
            historical_data=historical_data
        )
        
        return ForecastResponse(**result)
        
    except Exception as e:
        logger.error(f"Forecast generation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Forecast generation failed: {str(e)}")


@router.get("/product/{product_id}", response_model=ForecastResponse)
async def get_product_forecast(
    product_id: int,
    horizon: int = Query(default=90, ge=1, le=365),
    model_type: str = Query(default="ensemble", regex="^(lstm|prophet|xgboost|ensemble)$")
):
    """Get demand forecast for a specific product."""
    try:
        # Ensure model service is initialized
        if not model_service.models:
            await model_service.initialize_models()
        
        # Generate forecast
        result = await model_service.predict_demand(
            product_id=product_id,
            horizon=horizon,
            model_type=model_type
        )
        
        return ForecastResponse(**result)
        
    except Exception as e:
        logger.error(f"Forecast retrieval failed: {e}")
        raise HTTPException(status_code=500, detail=f"Forecast retrieval failed: {str(e)}")


@router.post("/batch")
async def create_batch_forecasts(
    product_ids: list[int],
    horizon: int = Query(default=90, ge=1, le=365),
    model_type: str = Query(default="ensemble", regex="^(lstm|prophet|xgboost|ensemble)$")
):
    """Generate demand forecasts for multiple products."""
    try:
        # Ensure model service is initialized
        if not model_service.models:
            await model_service.initialize_models()
        
        forecasts = []
        errors = []
        
        for product_id in product_ids:
            try:
                result = await model_service.predict_demand(
                    product_id=product_id,
                    horizon=horizon,
                    model_type=model_type
                )
                forecasts.append(ForecastResponse(**result))
            except Exception as e:
                logger.error(f"Forecast failed for product {product_id}: {e}")
                errors.append({
                    "product_id": product_id,
                    "error": str(e)
                })
        
        return {
            "forecasts": forecasts,
            "errors": errors,
            "total_requested": len(product_ids),
            "successful": len(forecasts),
            "failed": len(errors)
        }
        
    except Exception as e:
        logger.error(f"Batch forecast generation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Batch forecast generation failed: {str(e)}")


@router.get("/models/available")
async def get_available_models():
    """Get list of available forecasting models."""
    try:
        if not model_service.models:
            await model_service.initialize_models()
        
        return {
            "available_models": list(model_service.models.keys()),
            "model_metadata": model_service.model_metadata,
            "default_model": "ensemble"
        }
        
    except Exception as e:
        logger.error(f"Failed to get available models: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get available models")


@router.post("/retrain/{product_id}")
async def retrain_product_models(product_id: int):
    """Retrain forecasting models for a specific product."""
    try:
        # TODO: Implement actual retraining with new data
        result = await model_service.retrain_models(product_id, None)
        
        return {
            "message": f"Model retraining initiated for product {product_id}",
            "status": "in_progress",
            "result": result
        }
        
    except Exception as e:
        logger.error(f"Model retraining failed: {e}")
        raise HTTPException(status_code=500, detail=f"Model retraining failed: {str(e)}")
