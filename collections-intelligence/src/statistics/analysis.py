from __future__ import annotations

import pandas as pd


def evidence_summary(payments: pd.DataFrame) -> dict:
    raw_success = payments[payments['payment_status'].astype(str).str.upper().eq('SUCCESS')].copy()
    deduped = raw_success.drop_duplicates(subset='payment_reference', keep='first')
    inflation = raw_success['amount'].sum() - deduped['amount'].sum()
    return {
        'raw_success_total': float(raw_success['amount'].sum()),
        'deduped_success_total': float(deduped['amount'].sum()),
        'inflation': float(inflation),
        'inflat_pct': float((inflation / raw_success['amount'].sum()) * 100) if raw_success['amount'].sum() else 0.0,
    }
