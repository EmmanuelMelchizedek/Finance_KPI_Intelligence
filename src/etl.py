import pandas as pd
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "financial_transactions.csv"


def load_financial_data(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["month"])
    df["complaint_ratio"] = (df["complaints"] / df["customers"]).round(4)
    return df


def build_monthly_kpis(df: pd.DataFrame) -> pd.DataFrame:
    monthly = (
        df.groupby("month", as_index=False)
        .agg(
            revenue=("revenue", "sum"),
            cost=("cost", "sum"),
            profit=("profit", "sum"),
            customers=("customers", "sum"),
            complaints=("complaints", "sum"),
        )
    )
    monthly["margin_pct"] = (monthly["profit"] / monthly["revenue"] * 100).round(2)
    monthly["complaint_ratio"] = (monthly["complaints"] / monthly["customers"]).round(4)
    return monthly


def build_segment_kpis(df: pd.DataFrame) -> pd.DataFrame:
    seg = (
        df.groupby(["region", "product"], as_index=False)
        .agg(revenue=("revenue", "sum"), cost=("cost", "sum"), profit=("profit", "sum"), customers=("customers", "sum"))
    )
    seg["margin_pct"] = (seg["profit"] / seg["revenue"] * 100).round(2)
    return seg.sort_values(["profit", "revenue"], ascending=False)
