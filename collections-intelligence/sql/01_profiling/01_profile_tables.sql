-- SQL profiling script for raw collections tables
-- Purpose: establish schema shape, cardinality, null rates, and ID patterns
-- Run after loading raw CSVs into a staging schema.

SELECT 'accounts' AS table_name, COUNT(*) AS row_count FROM raw.accounts
UNION ALL
SELECT 'agents', COUNT(*) FROM raw.agents
UNION ALL
SELECT 'borrowers', COUNT(*) FROM raw.borrowers
UNION ALL
SELECT 'calls', COUNT(*) FROM raw.calls
UNION ALL
SELECT 'call_attempts', COUNT(*) FROM raw.call_attempts
UNION ALL
SELECT 'payments', COUNT(*) FROM raw.payments
UNION ALL
SELECT 'promises_to_pay', COUNT(*) FROM raw.promises_to_pay
UNION ALL
SELECT 'daily_targeting', COUNT(*) FROM raw.daily_targeting
UNION ALL
SELECT 'campaigns', COUNT(*) FROM raw.campaigns
UNION ALL
SELECT 'whatsapp_events', COUNT(*) FROM raw.whatsapp_events
UNION ALL
SELECT 'sms_events', COUNT(*) FROM raw.sms_events
UNION ALL
SELECT 'field_visits', COUNT(*) FROM raw.field_visits
UNION ALL
SELECT 'complaints', COUNT(*) FROM raw.complaints
UNION ALL
SELECT 'account_status_history', COUNT(*) FROM raw.account_status_history;

-- Example null-rate checks
SELECT 'payments' AS table_name, 'payment_reference' AS column_name, COUNT(*) - COUNT(payment_reference) AS nulls
FROM raw.payments
UNION ALL
SELECT 'accounts', 'borrower_id', COUNT(*) - COUNT(borrower_id) FROM raw.accounts
UNION ALL
SELECT 'calls', 'agent_id', COUNT(*) - COUNT(agent_id) FROM raw.calls;

-- Duplicate checks
SELECT 'payments' AS table_name, COUNT(*) AS dup_rows
FROM (
  SELECT payment_reference FROM raw.payments
  GROUP BY payment_reference
  HAVING COUNT(*) > 1
) d;
