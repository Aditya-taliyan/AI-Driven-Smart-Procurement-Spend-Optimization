from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.supplier import (
    SupplierCreate,
    SupplierUpdate,
    SupplierResponse,
    SupplierListResponse,
    SupplierPerformanceResponse,
    SupplierRiskResponse
)
from app.services.supplier_service import SupplierService

router = APIRouter()


@router.get("/", response_model=SupplierListResponse)
async def get_suppliers(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    search: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    risk_level: Optional[str] = Query(None),
    is_preferred: Optional[bool] = Query(None),
    db: Session = Depends(get_db)
):
    """Get list of suppliers with filtering and pagination."""
    service = SupplierService(db)
    return await service.get_suppliers(
        skip=skip,
        limit=limit,
        search=search,
        category=category,
        status=status,
        risk_level=risk_level,
        is_preferred=is_preferred
    )


@router.get("/{supplier_id}", response_model=SupplierResponse)
async def get_supplier(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    """Get supplier by ID."""
    service = SupplierService(db)
    supplier = await service.get_supplier(supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


@router.post("/", response_model=SupplierResponse)
async def create_supplier(
    supplier: SupplierCreate,
    db: Session = Depends(get_db)
):
    """Create new supplier."""
    service = SupplierService(db)
    return await service.create_supplier(supplier)


@router.put("/{supplier_id}", response_model=SupplierResponse)
async def update_supplier(
    supplier_id: int,
    supplier_update: SupplierUpdate,
    db: Session = Depends(get_db)
):
    """Update supplier."""
    service = SupplierService(db)
    supplier = await service.update_supplier(supplier_id, supplier_update)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


@router.delete("/{supplier_id}")
async def delete_supplier(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    """Delete supplier."""
    service = SupplierService(db)
    success = await service.delete_supplier(supplier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return {"message": "Supplier deleted successfully"}


@router.get("/{supplier_id}/performance", response_model=List[SupplierPerformanceResponse])
async def get_supplier_performance(
    supplier_id: int,
    period: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """Get supplier performance history."""
    service = SupplierService(db)
    performance = await service.get_supplier_performance(supplier_id, period)
    return performance


@router.get("/{supplier_id}/risk", response_model=SupplierRiskResponse)
async def get_supplier_risk(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    """Get supplier risk assessment."""
    service = SupplierService(db)
    risk = await service.get_supplier_risk(supplier_id)
    if not risk:
        raise HTTPException(status_code=404, detail="Risk assessment not found")
    return risk


@router.post("/{supplier_id}/risk-assessment")
async def create_risk_assessment(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    """Trigger risk assessment for supplier."""
    service = SupplierService(db)
    return await service.create_risk_assessment(supplier_id)


@router.get("/{supplier_id}/recommendations")
async def get_supplier_recommendations(
    supplier_id: int,
    db: Session = Depends(get_db)
):
    """Get AI-powered recommendations for supplier optimization."""
    service = SupplierService(db)
    return await service.get_supplier_recommendations(supplier_id)


@router.post("/bulk-import")
async def bulk_import_suppliers(
    db: Session = Depends(get_db)
):
    """Bulk import suppliers from file."""
    service = SupplierService(db)
    return await service.bulk_import_suppliers()


@router.get("/analytics/supplier-spend")
async def get_supplier_spend_analytics(
    supplier_id: Optional[int] = Query(None),
    period: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    """Get supplier spending analytics."""
    service = SupplierService(db)
    return await service.get_supplier_spend_analytics(supplier_id, period)
