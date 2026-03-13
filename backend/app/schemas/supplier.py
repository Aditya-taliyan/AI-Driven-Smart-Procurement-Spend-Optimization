from typing import List, Optional, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr
from enum import Enum


class SupplierStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    UNDER_REVIEW = "under_review"
    BLACKLISTED = "blacklisted"


class SupplierCreate(BaseModel):
    supplier_code: str = Field(..., min_length=2, max_length=50)
    name: str = Field(..., min_length=2, max_length=255)
    legal_name: Optional[str] = Field(None, max_length=255)
    tax_id: Optional[str] = Field(None, max_length=50)
    registration_number: Optional[str] = Field(None, max_length=100)
    
    # Contact Information
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=50)
    website: Optional[str] = Field(None, max_length=500)
    
    # Address
    address_line1: Optional[str] = Field(None, max_length=255)
    address_line2: Optional[str] = Field(None, max_length=255)
    city: Optional[str] = Field(None, max_length=100)
    state: Optional[str] = Field(None, max_length=100)
    country: Optional[str] = Field(None, max_length=100)
    postal_code: Optional[str] = Field(None, max_length=20)
    
    # Business Details
    industry: Optional[str] = Field(None, max_length=100)
    business_type: Optional[str] = Field(None, max_length=100)
    year_established: Optional[int] = Field(None, ge=1800, le=2030)
    annual_revenue: Optional[float] = Field(None, ge=0)
    employee_count: Optional[int] = Field(None, ge=0)
    
    # Certification & Compliance
    certifications: Optional[List[str]] = []
    
    # Status
    is_active: bool = True
    is_preferred: bool = False


class SupplierUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=255)
    legal_name: Optional[str] = Field(None, max_length=255)
    tax_id: Optional[str] = Field(None, max_length=50)
    registration_number: Optional[str] = Field(None, max_length=100)
    
    # Contact Information
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, max_length=50)
    website: Optional[str] = Field(None, max_length=500)
    
    # Address
    address_line1: Optional[str] = Field(None, max_length=255)
    address_line2: Optional[str] = Field(None, max_length=255)
    city: Optional[str] = Field(None, max_length=100)
    state: Optional[str] = Field(None, max_length=100)
    country: Optional[str] = Field(None, max_length=100)
    postal_code: Optional[str] = Field(None, max_length=20)
    
    # Business Details
    industry: Optional[str] = Field(None, max_length=100)
    business_type: Optional[str] = Field(None, max_length=100)
    year_established: Optional[int] = Field(None, ge=1800, le=2030)
    annual_revenue: Optional[float] = Field(None, ge=0)
    employee_count: Optional[int] = Field(None, ge=0)
    
    # Certification & Compliance
    certifications: Optional[List[str]] = []
    
    # Performance Metrics
    on_time_delivery_rate: Optional[float] = Field(None, ge=0, le=100)
    quality_score: Optional[float] = Field(None, ge=0, le=100)
    price_competitiveness: Optional[float] = Field(None, ge=0, le=100)
    
    # Status
    is_active: Optional[bool] = None
    is_preferred: Optional[bool] = None


class SupplierResponse(BaseModel):
    id: int
    supplier_code: str
    name: str
    legal_name: Optional[str]
    tax_id: Optional[str]
    registration_number: Optional[str]
    
    # Contact Information
    email: Optional[str]
    phone: Optional[str]
    website: Optional[str]
    
    # Address
    address_line1: Optional[str]
    address_line2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    country: Optional[str]
    postal_code: Optional[str]
    
    # Business Details
    industry: Optional[str]
    business_type: Optional[str]
    year_established: Optional[int]
    annual_revenue: Optional[float]
    employee_count: Optional[int]
    
    # Certification & Compliance
    certifications: Optional[List[str]]
    compliance_score: float
    
    # Performance Metrics
    on_time_delivery_rate: float
    quality_score: float
    price_competitiveness: float
    overall_score: float
    
    # Risk Assessment
    risk_level: SupplierStatus
    risk_score: float
    
    # Status
    is_active: bool
    is_preferred: bool
    
    # Timestamps
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class SupplierListResponse(BaseModel):
    items: List[SupplierResponse]
    total: int
    page: int
    size: int
    pages: int


class SupplierPerformanceResponse(BaseModel):
    id: int
    supplier_id: int
    period: str
    
    # Performance Metrics
    on_time_delivery_rate: float
    quality_score: float
    price_competitiveness: float
    responsiveness_score: float
    innovation_score: float
    overall_score: float
    
    # Order Statistics
    total_orders: int
    total_value: float
    late_deliveries: int
    quality_issues: int
    
    # Additional Notes
    notes: Optional[str]
    
    # Timestamps
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class SupplierRiskResponse(BaseModel):
    id: int
    supplier_id: int
    
    # Risk Factors
    financial_risk_score: float
    operational_risk_score: float
    compliance_risk_score: float
    reputational_risk_score: float
    geographic_risk_score: float
    overall_risk_score: float
    
    # Risk Level Classification
    risk_level: SupplierStatus
    
    # Risk Factors Details
    risk_factors: Optional[Dict[str, Any]]
    mitigation_strategies: Optional[Dict[str, Any]]
    
    # Assessment Details
    assessment_date: datetime
    next_assessment_date: Optional[datetime]
    assessor_id: Optional[int]
    
    # Additional Notes
    notes: Optional[str]
    
    # Timestamps
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class SupplierAnalyticsResponse(BaseModel):
    supplier_id: int
    supplier_name: str
    
    # Spend Analytics
    total_spend: float
    order_count: int
    avg_order_value: float
    spend_trend: List[Dict[str, Any]]
    
    # Performance Trends
    performance_trend: List[SupplierPerformanceResponse]
    risk_trend: List[SupplierRiskResponse]
    
    # Recommendations
    recommendations: List[Dict[str, Any]]
    
    # Benchmarking
    industry_benchmarks: Dict[str, float]
    percentile_rankings: Dict[str, float]


class SupplierRecommendationResponse(BaseModel):
    supplier_id: int
    recommendation_type: str
    title: str
    description: str
    potential_savings: Optional[float]
    implementation_effort: str
    priority: str
    confidence_score: float
    action_items: List[str]
    
    class Config:
        from_attributes = True
