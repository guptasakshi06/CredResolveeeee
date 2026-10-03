from __future__ import annotations

import pandas as pd


def detect_duplicate_payment_references(payments: pd.DataFrame) -> pd.DataFrame:
    if 'payment_reference' not in payments.columns:
        raise KeyError('payment_reference column is required')
    payments = payments.copy()
    payments['duplicate_ref_flag'] = payments['payment_reference'].duplicated(keep=False)
    return payments.loc[payments['duplicate_ref_flag']].copy()


def drop_duplicate_payment_references(payments: pd.DataFrame, keep: str = 'first') -> pd.DataFrame:
    payments = payments.copy()
    if 'payment_reference' not in payments.columns:
        raise KeyError('payment_reference column is required')
    return payments.drop_duplicates(subset=['payment_reference'], keep=keep).copy()
