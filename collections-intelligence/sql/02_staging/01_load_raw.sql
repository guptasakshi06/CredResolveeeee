-- Staging layer placeholder for raw ingestion into warehouse schema
-- This SQL is intentionally modular and designed to be parameterized by environment.

CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS clean;
CREATE SCHEMA IF NOT EXISTS golden;

-- Example raw table load pattern. Real warehouse loads should use COPY or a controlled ingestion job.
-- CREATE TABLE IF NOT EXISTS raw.payments (
--   payment_id TEXT,
--   account_id TEXT,
--   borrower_id TEXT,
--   event_at TIMESTAMP,
--   payment_reference TEXT,
--   amount NUMERIC,
--   payment_status TEXT,
--   payment_method TEXT,
--   provider_id TEXT
-- );
