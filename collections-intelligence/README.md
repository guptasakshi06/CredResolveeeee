# Collections Intelligence & Recovery Reliability Platform

This project investigates whether the business claim that recovery improved by 11% month-on-month is supported by the underlying collections data.

## Business objective

The goal is to rebuild a trustworthy recovery view from noisy raw source data, reconcile duplicate and attribution issues, estimate the true performance trend, and present an executive-grade evidence base for collections investment decisions.

## Dataset

The project uses the Synthetic Collections Analytics Dataset, which contains intentionally imperfect operational data across borrower, account, agent, call, payment, promise-to-pay, WhatsApp, SMS, field-visit, telephony, and campaign tables.

Key data issues intentionally present in the raw data include:
- duplicate payment references
- duplicate event ingestion
- conflicting timestamps and timezone values
- entity-id drift between agent IDs and employee codes
- campaign and channel misattribution
- historical status overwrites
- legacy disposition codes
- missing/partial fields

## Architecture

Raw data -> staging -> data quality / forensics -> cleaned data -> entity resolution -> golden dataset -> feature engineering -> metrics layer -> statistical analysis -> investment / counterfactual analysis -> executive dashboard.

## Golden dataset

The golden layer creates a trusted ledger of account-level collections activity with traceability back to source tables. It captures payment, contact, promise-to-pay, agent-hours, campaign exposure, risk segment, and data-quality flags.

## Metrics

The analytical layer independently defines and documents core metrics:
- Contact rate
- RPC rate
- PTP rate
- PTP kept rate
- Recovery rate
- Recovery per account
- Recovery per agent hour
- Cost per ₹ recovered
- Channel conversion

Each metric includes denominator, numerator, exclusions, and source tables.

## Data-quality process

The project performs explicit detection and treatment for:
- exact and near-duplicate records
- payment deduplication and retry events
- attribution conflicts
- timestamp normalization
- entity resolution between agent IDs and employee codes
- low-confidence records and exclusion flags

## Statistical method

The analysis uses transparent methods: monthly recovery comparisons, stratified breakdowns, confidence intervals, proportion tests, and difference-in-differences style counterfactual analysis.

## Counterfactual method

A treatment/control comparison is used to estimate what recovery would have looked like if the targeting strategy had not shifted mid-year. This is framed as an observational analysis and presented with explicit assumptions and limitations.

## Dashboard

The platform produces an executive dashboard inspired by premium finance operations design, with KPI cards, recovery trends, funnel analysis, driver decomposition, data-quality panel, and investment scenarios.

## Key findings

The project is designed to determine whether the claimed 11% month-on-month improvement is real after correcting for duplicate payments, attribution detail, target shifts, and portfolio mix changes.

## How to reproduce

1. Create the PostgreSQL database using Docker Compose.
2. Load the raw CSV files into the staging area.
3. Run the SQL profiling scripts under `sql/`.
4. Execute the Python notebooks in `notebooks/`.
5. Build the dashboard in `dashboard/`.

## Limitations

This is a synthetic dataset with intentionally flawed data; it is suitable for forensic analytics training and evidence-based investigation but not for legal or financial reporting at scale.

## Future improvements

- Add full dbt layered transforms
- Add automated anomaly detection alerts
- Integrate with data quality metadata tables
- Add a richer causal design and uplift modeling layer
