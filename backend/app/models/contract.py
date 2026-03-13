from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class ContractType(enum.Enum):
    FIXED_PRICE = "fixed_price"
    TIME_MATERIAL = "time_material"
    RETAINER = "retainer"
    SERVICE_LEVEL = "service_level"
    FRAMEWORK = "framework"
    MASTER_SERVICE = "master_service"


class ContractStatus(enum.Enum):
    DRAFT = "draft"
    UNDER_REVIEW = "under_review"
    ACTIVE = "active"
    EXPIRED = "expired"
    TERMINATED = "terminated"
    SUSPENDED = "suspended"


class Contract(Base):
    __tablename__ = "contracts"
    
    id = Column(Integer, primary_key=True, index=True)
    contract_number = Column(String(50), unique=True, index=True, nullable=False)
    
    # Supplier Information
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    
    # Contract Details
    title = Column(String(255), nullable=False)
    description = Column(Text)
    contract_type = Column(Enum(ContractType), nullable=False)
    
    # Financial Information
    total_value = Column(Float, default=0.0)
    currency = Column(String(3), default="USD")
    
    # Contract Period
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=False)
    renewal_date = Column(DateTime(timezone=True))
    
    # Terms and Conditions
    payment_terms = Column(String(255))
    delivery_terms = Column(String(255))
    warranty_terms = Column(Text)
    penalty_clauses = Column(JSON)
    
    # Status
    status = Column(Enum(ContractStatus), default=ContractStatus.DRAFT)
    
    # Contract Management
    contract_owner_id = Column(Integer, ForeignKey("users.id"))
    legal_review_required = Column(Boolean, default=False)
    legal_review_date = Column(DateTime(timezone=True))
    legal_review_status = Column(String(50))
    
    # Performance Metrics
    total_spend = Column(Float, default=0.0)
    remaining_value = Column(Float, default=0.0)
    utilization_rate = Column(Float, default=0.0)
    
    # Risk Assessment
    risk_level = Column(String(20), default="low")
    risk_factors = Column(JSON)
    
    # Compliance
    compliance_requirements = Column(JSON)
    compliance_status = Column(String(50))
    
    # Renewal Information
    auto_renewal = Column(Boolean, default=False)
    renewal_notice_period = Column(Integer)  # Days before expiry
    renewal_terms = Column(JSON)
    
    # Additional Information
    notes = Column(Text)
    attachments = Column(JSON)  # List of file references
    tags = Column(JSON)  # List of tags
    
    # ML Features
    predicted_savings = Column(Float)
    optimization_potential = Column(Float)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    supplier = relationship("Supplier", back_populates="contracts")
    items = relationship("ContractItem", back_populates="contract", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Contract(id={self.id}, contract_number={self.contract_number}, status={self.status})>"


class ContractItem(Base):
    __tablename__ = "contract_items"
    
    id = Column(Integer, primary_key=True, index=True)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    
    # Item Details
    description = Column(String(500), nullable=False)
    specifications = Column(JSON)
    
    # Pricing
    unit_price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    
    # Quantity Limits
    min_quantity = Column(Float, default=0.0)
    max_quantity = Column(Float)
    
    # Delivery Information
    lead_time_days = Column(Integer, default=0)
    delivery_schedule = Column(JSON)
    
    # Quality Requirements
    quality_standards = Column(JSON)
    inspection_requirements = Column(JSON)
    
    # Additional Information
    notes = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    contract = relationship("Contract", back_populates="items")
    product = relationship("Product", back_populates="contract_items")
    
    def __repr__(self):
        return f"<ContractItem(id={self.id}, contract_id={self.contract_id}, product_id={self.product_id})>"
