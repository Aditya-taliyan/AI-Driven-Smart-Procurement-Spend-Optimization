-- PostgreSQL initialization script for Smart Procurement Platform

-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
CREATE EXTENSION IF NOT EXISTS "btree_gin";

-- Create schemas
CREATE SCHEMA IF NOT EXISTS procurement;
CREATE SCHEMA IF NOT EXISTS ml;
CREATE SCHEMA IF NOT EXISTS analytics;

-- Set default schema
SET search_path TO procurement, public;

-- Create custom types
CREATE TYPE procurement.order_status AS ENUM ('pending', 'approved', 'rejected', 'completed', 'cancelled');
CREATE TYPE procurement.payment_status AS ENUM ('pending', 'paid', 'overdue', 'cancelled');
CREATE TYPE procurement.risk_level AS ENUM ('low', 'medium', 'high', 'critical');
CREATE TYPE procurement.contract_type AS ENUM ('fixed_price', 'time_material', 'retainer', 'service_level');

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_suppliers_name ON suppliers USING gin(name gin_trgm_ops);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_purchase_orders_date ON purchase_orders(order_date);
CREATE INDEX IF NOT EXISTS idx_invoices_due_date ON invoices(due_date);

-- Create audit trigger function
CREATE OR REPLACE FUNCTION procurement.update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.modified_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Grant permissions
GRANT USAGE ON SCHEMA procurement TO PUBLIC;
GRANT USAGE ON SCHEMA ml TO PUBLIC;
GRANT USAGE ON SCHEMA analytics TO PUBLIC;
