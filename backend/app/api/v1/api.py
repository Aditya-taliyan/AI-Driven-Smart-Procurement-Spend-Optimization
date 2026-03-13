from fastapi import APIRouter

from app.api.v1.endpoints import (
    auth,
    users,
    suppliers,
    products,
    purchase_orders,
    invoices,
    contracts,
    analytics,
    ml_models,
    predictions,
    recommendations,
    optimization,
)

api_router = APIRouter()

# Authentication endpoints
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])

# User management
api_router.include_router(users.router, prefix="/users", tags=["users"])

# Core business entities
api_router.include_router(suppliers.router, prefix="/suppliers", tags=["suppliers"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
api_router.include_router(purchase_orders.router, prefix="/purchase-orders", tags=["purchase-orders"])
api_router.include_router(invoices.router, prefix="/invoices", tags=["invoices"])
api_router.include_router(contracts.router, prefix="/contracts", tags=["contracts"])

# Analytics and reporting
api_router.include_router(analytics.router, prefix="/analytics", tags=["analytics"])

# ML and AI endpoints
api_router.include_router(ml_models.router, prefix="/ml-models", tags=["ml-models"])
api_router.include_router(predictions.router, prefix="/predictions", tags=["predictions"])
api_router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
api_router.include_router(optimization.router, prefix="/optimization", tags=["optimization"])
