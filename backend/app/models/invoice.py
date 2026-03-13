from sqlalchemy import Column, Integer, String, Float, DateTime, Text, Boolean, ForeignKey, Enum, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.core.database import Base


class PaymentStatus(enum.Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    PAID = "paid"
    OVERDUE = "overdue"
    CANCELLED = "cancelled"
    DISPUTED = "disputed"


class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String(50), unique=True, index=True, nullable=False)
    
    # Related Documents
    purchase_order_id = Column(Integer, ForeignKey("purchase_orders.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=False)
    
    # Invoice Details
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
    invoice_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    due_date = Column(DateTime(timezone=True), nullable=False)
    paid_date = Column(DateTime(timezone=True))
    
    # Payment Information
    payment_terms = Column(String(255))
    payment_method = Column(String(100))
    payment_reference = Column(String(100))
    
    # Status
    status = Column(Enum(PaymentStatus), default=PaymentStatus.PENDING)
    
    # Validation Information
    is_validated = Column(Boolean, default=False)
    validation_date = Column(DateTime(timezone=True))
    validated_by = Column(Integer, ForeignKey("users.id"))
    validation_notes = Column(Text)
    
    # Duplicate Detection
    duplicate_score = Column(Float, default=0.0)
    potential_duplicates = Column(JSON)  # List of potential duplicate invoice IDs
    
    # Anomaly Detection
    anomaly_score = Column(Float, default=0.0)
    anomaly_reasons = Column(JSON)
    
    # Additional Information
    notes = Column(Text)
    attachments = Column(JSON)  # List of file references
    tags = Column(JSON)  # List of tags
    
    # Supplier Invoice Reference
    supplier_invoice_number = Column(String(100))
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    purchase_order = relationship("PurchaseOrder", back_populates="invoices")
    supplier = relationship("Supplier")
    items = relationship("InvoiceItem", back_populates="invoice", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Invoice(id={self.id}, invoice_number={self.invoice_number}, status={self.status})>"


class InvoiceItem(Base):
    __tablename__ = "invoice_items"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"))
    
    # Item Details
    description = Column(String(500))
    specifications = Column(JSON)
    
    # Quantity and Pricing
    quantity = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    total_price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    
    # Matching with Purchase Order
    po_item_id = Column(Integer, ForeignKey("purchase_order_items.id"))
    quantity_variance = Column(Float, default=0.0)  # Difference from PO quantity
    price_variance = Column(Float, default=0.0)  # Difference from PO price
    
    # Additional Information
    notes = Column(Text)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    
    # Relationships
    invoice = relationship("Invoice", back_populates="items")
    product = relationship("Product", back_populates="invoice_items")
    
    def __repr__(self):
        return f"<InvoiceItem(id={self.id}, invoice_id={self.invoice_id}, product_id={self.product_id})>"
