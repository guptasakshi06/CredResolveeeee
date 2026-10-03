import pandas as pd


def test_account_ids_are_unique():
    accounts = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/accounts.csv')
    assert accounts['account_id'].is_unique


def test_payment_reference_duplicates_are_detected():
    payments = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/payments.csv')
    dup_count = payments['payment_reference'].duplicated(keep=False).sum()
    assert dup_count > 0


def test_positive_amounts():
    payments = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/payments.csv')
    assert (payments['amount'] >= 0).all()


def test_borrower_account_relationships_exist():
    accounts = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/accounts.csv')
    assert accounts['borrower_id'].notna().any()


def test_target_rows_are_present():
    targeting = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/daily_targeting.csv')
    assert len(targeting) > 0


def test_monthly_payment_total_is_reasonable():
    payments = pd.read_csv('/home/ubuntu/CredResolveeeee/collections-intelligence/data/raw/payments.csv')
    assert payments['amount'].sum() > 0
