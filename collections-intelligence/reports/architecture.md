# Architecture overview

Raw -> Staging -> Clean -> Golden -> Feature -> Metrics -> Dashboard

## Data contracts

- Account identifiers are treated as primary keys in the account layer.
- Borrower IDs are matched with account IDs at the account-borrower resolution layer.
- Agent IDs are harmonized to canonical agent IDs using employee code and vendor mapping.
- Payment records are deduplicated via payment reference and payment ID lineage.
- Every transformation retains raw lineage and an audit trail.

## Incremental processing

The pipeline supports daily loads and late-arriving event corrections via timestamp-sorted replays and backfill logs.

## Monitoring

The project includes automated checks for duplicate counts, null frequency, ID mismatch, payment volume anomalies, timezone drift, and late event spikes.
