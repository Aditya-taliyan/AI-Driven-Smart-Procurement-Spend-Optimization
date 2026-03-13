from typing import List, Optional, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func, desc
from fastapi import HTTPException
import httpx
import logging

from app.models.supplier import Supplier, SupplierPerformance, SupplierRisk
from app.schemas.supplier import (
    SupplierCreate,
    SupplierUpdate,
    SupplierResponse,
    SupplierPerformanceResponse,
    SupplierRiskResponse,
    SupplierAnalyticsResponse,
    SupplierRecommendationResponse
)
from app.core.config import settings

logger = logging.getLogger(__name__)


class SupplierService:
    def __init__(self, db: Session):
        self.db = db
        self.ml_service_url = settings.SUPPLIER_RISK_SERVICE_URL

    async def get_suppliers(
        self,
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        category: Optional[str] = None,
        status: Optional[str] = None,
        risk_level: Optional[str] = None,
        is_preferred: Optional[bool] = None
    ) -> Dict[str, Any]:
        """Get suppliers with filtering and pagination."""
        query = self.db.query(Supplier)
        
        # Apply filters
        if search:
            query = query.filter(
                or_(
                    Supplier.name.ilike(f"%{search}%"),
                    Supplier.supplier_code.ilike(f"%{search}%"),
                    Supplier.email.ilike(f"%{search}%")
                )
            )
        
        if category:
            query = query.filter(Supplier.industry.ilike(f"%{category}%"))
        
        if status:
            query = query.filter(Supplier.risk_level == status)
        
        if risk_level:
            query = query.filter(Supplier.risk_level == risk_level)
        
        if is_preferred is not None:
            query = query.filter(Supplier.is_preferred == is_preferred)
        
        # Get total count
        total = query.count()
        
        # Apply pagination
        suppliers = query.offset(skip).limit(limit).all()
        
        return {
            "items": [SupplierResponse.from_orm(supplier) for supplier in suppliers],
            "total": total,
            "page": skip // limit + 1,
            "size": limit,
            "pages": (total + limit - 1) // limit
        }

    async def get_supplier(self, supplier_id: int) -> Optional[SupplierResponse]:
        """Get supplier by ID."""
        supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
        if not supplier:
            return None
        return SupplierResponse.from_orm(supplier)

    async def create_supplier(self, supplier_data: SupplierCreate) -> SupplierResponse:
        """Create new supplier."""
        # Check if supplier code already exists
        existing = self.db.query(Supplier).filter(
            Supplier.supplier_code == supplier_data.supplier_code
        ).first()
        if existing:
            raise HTTPException(status_code=400, detail="Supplier code already exists")
        
        supplier = Supplier(**supplier_data.dict())
        self.db.add(supplier)
        self.db.commit()
        self.db.refresh(supplier)
        
        # Trigger initial risk assessment
        await self.create_risk_assessment(supplier.id)
        
        return SupplierResponse.from_orm(supplier)

    async def update_supplier(self, supplier_id: int, supplier_data: SupplierUpdate) -> Optional[SupplierResponse]:
        """Update supplier."""
        supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
        if not supplier:
            return None
        
        # Update fields
        update_data = supplier_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(supplier, field, value)
        
        self.db.commit()
        self.db.refresh(supplier)
        
        return SupplierResponse.from_orm(supplier)

    async def delete_supplier(self, supplier_id: int) -> bool:
        """Delete supplier."""
        supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
        if not supplier:
            return False
        
        self.db.delete(supplier)
        self.db.commit()
        return True

    async def get_supplier_performance(self, supplier_id: int, period: Optional[str] = None) -> List[SupplierPerformanceResponse]:
        """Get supplier performance history."""
        query = self.db.query(SupplierPerformance).filter(SupplierPerformance.supplier_id == supplier_id)
        
        if period:
            query = query.filter(SupplierPerformance.period == period)
        
        performances = query.order_by(desc(SupplierPerformance.period)).all()
        return [SupplierPerformanceResponse.from_orm(perf) for perf in performances]

    async def get_supplier_risk(self, supplier_id: int) -> Optional[SupplierRiskResponse]:
        """Get latest supplier risk assessment."""
        risk = self.db.query(SupplierRisk).filter(
            SupplierRisk.supplier_id == supplier_id
        ).order_by(desc(SupplierRisk.assessment_date)).first()
        
        if not risk:
            return None
        
        return SupplierRiskResponse.from_orm(risk)

    async def create_risk_assessment(self, supplier_id: int) -> Dict[str, Any]:
        """Trigger risk assessment for supplier."""
        try:
            # Call ML service for risk assessment
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.ml_service_url}/assess",
                    json={"supplier_id": supplier_id},
                    timeout=30.0
                )
                response.raise_for_status()
                
                result = response.json()
                
                # Save risk assessment to database
                risk = SupplierRisk(
                    supplier_id=supplier_id,
                    financial_risk_score=result.get("financial_risk", 0.0),
                    operational_risk_score=result.get("operational_risk", 0.0),
                    compliance_risk_score=result.get("compliance_risk", 0.0),
                    reputational_risk_score=result.get("reputational_risk", 0.0),
                    geographic_risk_score=result.get("geographic_risk", 0.0),
                    overall_risk_score=result.get("overall_risk", 0.0),
                    risk_level=result.get("risk_level", "low"),
                    risk_factors=result.get("risk_factors", {}),
                    mitigation_strategies=result.get("mitigation_strategies", {})
                )
                
                self.db.add(risk)
                
                # Update supplier risk score
                supplier = self.db.query(Supplier).filter(Supplier.id == supplier_id).first()
                if supplier:
                    supplier.risk_score = result.get("overall_risk", 0.0)
                    supplier.risk_level = result.get("risk_level", "low")
                
                self.db.commit()
                
                return {
                    "message": "Risk assessment completed successfully",
                    "risk_score": result.get("overall_risk", 0.0),
                    "risk_level": result.get("risk_level", "low")
                }
                
        except httpx.HTTPError as e:
            logger.error(f"Failed to call risk assessment service: {e}")
            raise HTTPException(status_code=503, detail="Risk assessment service unavailable")
        except Exception as e:
            logger.error(f"Risk assessment failed: {e}")
            raise HTTPException(status_code=500, detail="Risk assessment failed")

    async def get_supplier_recommendations(self, supplier_id: int) -> List[SupplierRecommendationResponse]:
        """Get AI-powered recommendations for supplier optimization."""
        try:
            # Call recommendation service
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{settings.RECOMMENDATIONS_SERVICE_URL}/supplier/{supplier_id}",
                    timeout=30.0
                )
                response.raise_for_status()
                
                recommendations_data = response.json()
                recommendations = []
                
                for rec in recommendations_data.get("recommendations", []):
                    recommendations.append(SupplierRecommendationResponse(**rec))
                
                return recommendations
                
        except httpx.HTTPError as e:
            logger.error(f"Failed to call recommendation service: {e}")
            return []
        except Exception as e:
            logger.error(f"Failed to get recommendations: {e}")
            return []

    async def bulk_import_suppliers(self) -> Dict[str, Any]:
        """Bulk import suppliers from file."""
        # TODO: Implement file upload and bulk import logic
        return {
            "message": "Bulk import functionality not yet implemented",
            "status": "pending"
        }

    async def get_supplier_spend_analytics(self, supplier_id: Optional[int] = None, period: Optional[str] = None) -> List[SupplierAnalyticsResponse]:
        """Get supplier spending analytics."""
        # TODO: Implement spend analytics logic
        return []

    def _calculate_overall_score(self, supplier: Supplier) -> float:
        """Calculate overall supplier score."""
        weights = {
            "delivery": 0.3,
            "quality": 0.3,
            "price": 0.2,
            "compliance": 0.2
        }
        
        score = (
            supplier.on_time_delivery_rate * weights["delivery"] +
            supplier.quality_score * weights["quality"] +
            supplier.price_competitiveness * weights["price"] +
            supplier.compliance_score * weights["compliance"]
        )
        
        return round(score, 2)
