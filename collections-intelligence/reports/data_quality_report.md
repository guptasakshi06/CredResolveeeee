# Data quality report

| Issue | Detection | Treatment | Records affected | Financial impact |
|---|---|---|---:|---:|
| Duplicate payments | Duplicate `payment_reference` values | Deduplicate by canonical payment reference, retain earliest valid record | ~8,424 payment rows | Potential recovery inflation by large double-counting |
| Duplicate events | Repeated event IDs and retry records | Flag duplicates; keep one canonical record where exact retry is not business-valid | Multiple event tables | Distorted funnel counts |
| Inconsistent IDs | Agent and borrower identifiers drift across tables | Build canonical entity mappings | Material share of agent/account references | Misattributed productivity and recovery |
| Timestamp conflicts | Mixed UTC/Asia/Kolkata/Asia/Dubai values | Normalize to UTC and derive local business dates | Wide share of interaction events | Distorted daily and hourly trends |
| Timezone issues | Event time and recorded time differ across systems | Reconstruct by event timestamps and local timezone | High volume | Misleading claim timing |
| Legacy dispositions | Legacy codes in call disposition tables | Map to standardized disposition categories | Non-trivial subset | Misread contact and right-party outcomes |
| Attribution problems | Latest-campaign and varied attribution windows | Recompute with multi-window rules | High volume | Artificially improved or reduced attribution |
| Missing values | Null borrower IDs, vendor IDs, etc. | Label, exclude from strict metrics, retain for diagnostics | Moderate share | Understated denominator accuracy |
| Portfolio mix changes | Risk-segment and DPD mix shifts | Stratify monthly analyses | Material share | Simulated improvement due to easier portfolio |
| Denominator manipulation | Targeting and activity counts change over time | Use independent denominators and filters | Material share | Overstatement of conversion rates |
