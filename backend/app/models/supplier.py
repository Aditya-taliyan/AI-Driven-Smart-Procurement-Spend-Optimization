from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class SupplierStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    UNDER_REVIEW = "under_review"
    BLACKLISTED = "blacklisted"


class Supplier(Base):
    __tablename__ = "suppliers"
    
    id = Column(Integer, primary_key=True, index=True)
    supplier_code = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False, index=True)
    legal_name = Column(String(255))
    tax_id = Column(String(50))
    registration_number = Column(String(100))
    
    # Contact Information
    email = Column(String(255))
    phone = Column(String(50))
    website = Column(String(500))
    
    # Address
    address_line1 = Column(String(255))
    address_line2 = Column(String(255))
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    postal_code = Column(String(20))
    
    # Business Details
    industry = Column(String(100))
    business_type = Column(String(100))  # Manufacturer, Distributor, Service Provider
    year_established = Column(Integer)
    annual_revenue = Column(Float)
    employee_count = Column(Integer)
    
    # Certification & Compliance
    certifications = Column(JSON)  # ISO, CE, etc.
    compliance_score = Column(Float, default=0.0)
    
    # Performance Metrics
    on_time_delivery_rate = Column(Float, default=0.0)
    quality_score = Column(Float, default=0.0)
    price_competitiveness = Column(Float, default=0.0)
    overall_score = Column(Float, default=0.0)
    
    # Risk Assessment
    risk_level = Column(Enum(SupplierStatus), default=SupplierStatus.ACTIVE)
    risk_score = Column(Float, default=0.0)
    
    # Status
    is_active = Column(Boolean, default=True)
    is_preferred = Column(Boolean, default=False)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    products = relationship("Product", back_populates="supplier")
    purchase_orders = relationship("PurchaseOrder", back_populates="supplier")
    contracts = relationship("Contract", back_populates="supplier")
    performance_records = relationship("SupplierPerformance", back_populates="supplier")
    risk_assessments = relationship("SupplierRisk", back_populates="supplier")
    
    def __repr__(self):
        return f"<Supplier(id={self.id}, name={self.name}, code={self.supplier_code})>"


class SupplierPerformance(Base):
    __tablename__ = "supplier_performance"
    
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    
    # Performance Metrics
    period = Column(String(20), nullable=False)  # e.g., "2024-Q1"
    on_time_delivery_rate = Column(Float, default=0.0)
    quality_score = Column(Float, default=0.0)
    price_competitiveness = Column(Float, default=0.0)
    responsiveness_score = Column(Float, default=0.0)
    innovation_score = Column(Float, default=0.0)
    overall_score = Column(Float, default=0.0)
    
    # Order Statistics
    total_orders = Column(Integer, default=0)
    total_value = Column(Float, default=0.0)
    late_deliveries = Column(Integer, default=0)
    quality_issues = Column(Integer, default=0)
    
    # Additional Notes
    notes = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    supplier = relationship("Supplier", back_populates="performance_records")
    
    def __repr__(self):
        return f"<SupplierPerformance(id={self.id}, supplier_id={self.supplier_id}, period={self.period})>"


class SupplierRisk(Base):
    __tablename__ = "supplier_risk"
    
    id = Column(Integer, primary_key=True, index=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    
    # Risk Factors
    financial_risk_score = Column(Float, default=0.0)
    operational_risk_score = Column(Float, default=0.0)
    compliance_risk_score = Column(Float, default=0.0)
    reputational_risk_score = Column(Float, default=0.0)
    geographic_risk_score = Column(Float, default=0.0)
    overall_risk_score = Column(Float, default=0.0)
    
    # Risk Level Classification
    risk_level = Column(Enum(SupplierStatus), default=SupplierStatus.ACTIVE)
    
    # Risk Factors Details
    risk_factors = Column(JSON)  # Detailed risk factors and scores
    mitigation_strategies = Column(JSON)  # Recommended mitigation strategies
    
    # Assessment Details
    assessment_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    next_assessment_date = Column(DateTime(timezone=True))
    assessor_id = Column(Integer, ForeignKey("users.id"))
    
    # Additional Notes
    notes = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    supplier = relationship("Supplier", back_populates="risk_assessments")
    
    def __repr__(self):
        return f"<SupplierRisk(id={self.id}, supplier_id={self.supplier_id}, risk_level={self.risk_level})>"
