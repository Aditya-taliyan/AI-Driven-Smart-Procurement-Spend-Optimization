from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class ProductStatus(enum.Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DISCONTINUED = "discontinued"
    UNDER_REVIEW = "under_review"


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True, index=True)
    code = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(Text)
    parent_id = Column(Integer, ForeignKey("categories.id"))
    
    # Category Hierarchy
    level = Column(Integer, default=0)
    path = Column(String(500))  # e.g., "Electronics > Computers > Laptops"
    
    # Category Attributes
    attributes = Column(JSON)  # Common attributes for products in this category
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    parent = relationship("Category", remote_side=[id])
    children = relationship("Category")
    products = relationship("Product", back_populates="category")
    
    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name}, code={self.code})>"


class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String(100), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False, index=True)
    description = Column(Text)
    
    # Classification
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    
    # Specifications
    brand = Column(String(100))
    model = Column(String(100))
    specifications = Column(JSON)  # Technical specifications
    attributes = Column(JSON)  # Custom attributes
    
    # Pricing
    unit_price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    min_order_quantity = Column(Integer, default=1)
    max_order_quantity = Column(Integer)
    
    # Inventory
    lead_time_days = Column(Integer, default=0)
    safety_stock = Column(Integer, default=0)
    reorder_point = Column(Integer, default=0)
    
    # Quality & Compliance
    quality_standards = Column(JSON)  # ISO, CE, etc.
    compliance_certifications = Column(JSON)
    
    # Status
    status = Column(Enum(ProductStatus), default=ProductStatus.ACTIVE)
    is_preferred = Column(Boolean, default=False)
    
    # Performance Metrics
    avg_rating = Column(Float, default=0.0)
    total_orders = Column(Integer, default=0)
    total_quantity = Column(Float, default=0.0)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    last_price_update = Column(DateTime(timezone=True))
    
    # Relationships
    category = relationship("Category", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")
    purchase_order_items = relationship("PurchaseOrderItem", back_populates="product")
    invoice_items = relationship("InvoiceItem", back_populates="product")
    contract_items = relationship("ContractItem", back_populates="product")
    
    def __repr__(self):
        return f"<Product(id={self.id}, sku={self.sku}, name={self.name})>"
