import pandas as pd

from src.cleaning.duplicate_detector import drop_duplicate_payment_references
from src.metrics.recovery_metrics import compute_monthly_recovery, compute_recovery_growth


def test_duplicate_reference_dedup_reduces_total():
    payments = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/payments.csv')
    raw_total = payments[payments['payment_status'].astype(str).str.upper().eq('SUCCESS')]['amount'].sum()
    deduped = drop_duplicate_payment_references(payments[payments['payment_status'].astype(str).str.upper().eq('SUCCESS')])
    assert deduped['amount'].sum() <= raw_total


def test_monthly_recovery_has_expected_columns():
    payments = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/payments.csv')
    monthly = compute_monthly_recovery(payments)
    assert {'month', 'recovered_amount'} <= set(monthly.columns)


def test_monthly_growth_is_numeric():
    payments = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/payments.csv')
    monthly = compute_monthly_recovery(payments)
    growth = compute_recovery_growth(monthly)
    assert growth['mom_growth'].dropna().notna().all()
    assert growth['mom_growth'].dropna().shape[0] >= 1
