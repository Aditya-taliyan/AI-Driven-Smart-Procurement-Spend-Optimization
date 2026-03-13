from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class OrderStatus(enum.Enum):
    DRAFT = "draft"
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    SENT_TO_SUPPLIER = "sent_to_supplier"
    CONFIRMED = "confirmed"
    PARTIALLY_RECEIVED = "partially_received"
    RECEIVED = "received"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    order_number = Column(String(50), unique=True, index=True, nullable=False)
    
    # Supplier Information
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    
    # User Information
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    approved_by = Column(Integer, ForeignKey("users.id"))
    
    # Order Details
    title = Column(String(255), nullable=False)
    description = Column(Text)
    
    # Financial Information
    subtotal = Column(Float, default=0.0)
    tax_amount = Column(Float, default=0.0)
    shipping_cost = Column(Float, default=0.0)
    discount_amount = Column(Float, default=0.0)
    total_amount = Column(Float, default=0.0)
    currency = Column(String(3), default="USD")
    
    # Dates
    order_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    approval_date = Column(DateTime(timezone=True))
    expected_delivery_date = Column(DateTime(timezone=True))
    actual_delivery_date = Column(DateTime(timezone=True))
    
    # Delivery Information
    delivery_address = Column(JSON)  # Address object
    delivery_instructions = Column(Text)
    
    # Payment Terms
    payment_terms = Column(String(255))
    payment_method = Column(String(100))
    
    # Status
    status = Column(Enum(OrderStatus), default=OrderStatus.DRAFT)
    priority = Column(String(20), default="normal")  # low, normal, high, urgent
    
    # Approval Workflow
    approval_workflow = Column(JSON)  # Approval chain and status
    rejection_reason = Column(Text)
    
    # Additional Information
    notes = Column(Text)
    attachments = Column(JSON)  # List of file references
    tags = Column(JSON)  # List of tags
    
    # ML Features
    predicted_delivery_date = Column(DateTime(timezone=True))
    confidence_score = Column(Float)
    anomaly_score = Column(Float)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    supplier = relationship("Supplier", back_populates="purchase_orders")
    created_by_user = relationship("User", foreign_keys=[created_by], back_populates="purchase_orders")
    approved_by_user = relationship("User", foreign_keys=[approved_by], back_populates="approved_purchase_orders")
    items = relationship("PurchaseOrderItem", back_populates="purchase_order", cascade="all, delete-orphan")
    invoices = relationship("Invoice", back_populates="purchase_order")
    
    def __repr__(self):
        return f"<PurchaseOrder(id={self.id}, order_number={self.order_number}, status={self.status})>"


class PurchaseOrderItem(Base):
    __tablename__ = "purchase_order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    purchase_order_id = Column(Integer, ForeignKey("purchase_orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    
    # Item Details
    description = Column(String(500))
    specifications = Column(JSON)
    
    # Quantity and Pricing
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    
    # Delivery Information
    expected_quantity = Column(Float)  # Expected to receive
    received_quantity = Column(Float, default=0.0)
    
    # Quality Information
    quality_notes = Column(Text)
    inspection_required = Column(Boolean, default=False)
    inspection_date = Column(DateTime(timezone=True))
    inspection_result = Column(JSON)
    
    # Additional Information
    notes = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    purchase_order = relationship("PurchaseOrder", back_populates="items")
    product = relationship("Product", back_populates="purchase_order_items")
    
    def __repr__(self):
        return f"<PurchaseOrderItem(id={self.id}, po_id={self.purchase_order_id}, product_id={self.product_id})>"
