-- Duplicate detection and retention workflow
-- Document exact duplicates vs retry events versus ingestion duplicates.

WITH payment_refs AS (
  SELECT payment_reference, COUNT(*) AS cnt
  FROM raw.payments
  WHERE payment_reference IS NOT NULL
  GROUP BY payment_reference
)
SELECT *
FROM payment_refs
WHERE cnt > 1
ORDER BY cnt DESC;

-- Example: use row_number to flag duplicate payment references while retaining the best record.
-- SELECT *,
--        ROW_NUMBER() OVER (PARTITION BY payment_reference ORDER BY event_at, payment_id) AS rn
-- FROM raw.payments;
