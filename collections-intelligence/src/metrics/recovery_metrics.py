from __future__ import annotations

import pandas as pd


def compute_monthly_recovery(payments: pd.DataFrame, status_col: str = 'payment_status', amount_col: str = 'amount', event_col: str = 'event_at') -> pd.DataFrame:
    if status_col not in payments.columns:
        raise KeyError(f'{status_col} is required')
    if amount_col not in payments.columns:
        raise KeyError(f'{amount_col} is required')
    if event_col not in payments.columns:
        raise KeyError(f'{event_col} is required')

    df = payments.copy()
    df[event_col] = pd.to_datetime(df[event_col], errors='coerce')
    df[amount_col] = pd.to_numeric(df[amount_col], errors='coerce')
    success = df[df[status_col].astype(str).str.upper().eq('SUCCESS')].copy()
    success['month'] = success[event_col].dt.to_period('M').astype(str)
    return success.groupby('month', as_index=False)[amount_col].sum().rename(columns={amount_col: 'recovered_amount'})


def compute_recovery_growth(monthly: pd.DataFrame, amount_col: str = 'recovered_amount') -> pd.DataFrame:
    out = monthly.sort_values('month').copy()
    out['prev_amount'] = out[amount_col].shift(1)
    out['mom_growth'] = (out[amount_col] - out['prev_amount']) / out['prev_amount']
    out.loc[out['prev_amount'].isna(), 'mom_growth'] = pd.NA
    return out
