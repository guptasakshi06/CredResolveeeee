# Executive memo

## What happened?

The raw collection dataset shows material operational noise. Duplicate payment references, campaign drift, inconsistent IDs, and timezone mismatch materially alter the performance story. A reconstructed monthly recovery trend differs from the topline business report because several data-quality issues inflate reported recovery.

## Why did it happen?

The main drivers are duplicate payment records, changes in targeting strategy, and attribution changes caused by campaign and channel definitions shifting over time. There are also differences between raw recorded timestamps and business-local dates, which affect the apparent month-of-performance for both calls and payments.

## Is the 11% claim supported?

The initial raw data pattern can appear to support an 11% improvement in some months, but once duplicate payments and attribution inconsistencies are corrected, the improvement is materially weaker and non-uniform. The claim cannot be accepted without qualification.

## How reliable is the data?

The data is moderately useful for forensic analysis but not yet suitable for finance-grade reporting without cleaning and reconciliation. The reliability score is lower than a production ledger due to duplicate events, mismatched identifiers, and inconsistent timestamps.

## What evidence is strongest?

The strongest evidence is the deduplicated payment ledger, the cross-table account and borrower reconciliation, and the comparison of reported versus independently reconstructed monthly recovery. These show where the raw reporting overstates recovery and how much of the apparent uplift is driven by measurement changes rather than true operational improvement.

## What remains uncertain?

The exact counterfactual impact of targeting changes and campaign redesign remains uncertain because the data is observational rather than randomized. Some unobserved borrower behavior and omitted operational context cannot be fully reconstructed.

## What financial impact does this have?

The financial impact is primarily in the overstated recovery and the misallocation of resources across channels and campaigns. The project provides a range of investment scenarios that should be used alongside operational judgment rather than as exact financial truth.

## What investment scenarios should leadership evaluate?

Leadership should compare targeted outreach strategy, telephony quality, AI voice automation, digital engagement, and field operations using scenario ranges with explicit assumptions. The output is intended to support a decision, not to replace business judgement.
