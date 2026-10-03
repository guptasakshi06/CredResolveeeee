from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd


@dataclass
class DatasetProfile:
    name: str
    rows: int
    columns: int
    duplicate_rows: int
    null_pct: dict
    dt_min: str | None
    dt_max: str | None


def profile_csv(path: str | Path) -> DatasetProfile:
    df = pd.read_csv(path)
    dt_candidates = [
        c for c in df.columns if 'at' in c.lower() or c in {'target_date', 'opened_at', 'joined_at', 'updated_at'}
    ]
    dt_min = None
    dt_max = None
    if dt_candidates:
        dt_col = dt_candidates[0]
        s = pd.to_datetime(df[dt_col], errors='coerce')
        if s.notna().any():
            dt_min = s.min().isoformat()
            dt_max = s.max().isoformat()
    return DatasetProfile(
        name=Path(path).stem,
        rows=len(df),
        columns=len(df.columns),
        duplicate_rows=int(df.duplicated().sum()),
        null_pct=df.isna().mean().mul(100).round(3).to_dict(),
        dt_min=dt_min,
        dt_max=dt_max,
    )


def profile_directory(dir_path: str | Path) -> dict[str, DatasetProfile]:
    profiles: dict[str, DatasetProfile] = {}
    for csv_file in sorted(Path(dir_path).glob('*.csv')):
        profiles[csv_file.stem] = profile_csv(csv_file)
    return profiles
