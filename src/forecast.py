import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def forecast_revenue(monthly_kpis: pd.DataFrame, periods: int = 3) -> pd.DataFrame:
    df = monthly_kpis.sort_values("month").copy()
    df["t"] = np.arange(len(df))
    model = LinearRegression()
    model.fit(df[["t"]], df["revenue"])

    future_t = np.arange(len(df), len(df) + periods)
    future_dates = pd.date_range(df["month"].max() + pd.offsets.MonthBegin(1), periods=periods, freq="MS")
    preds = model.predict(future_t.reshape(-1, 1))

    return pd.DataFrame({"month": future_dates, "forecast_revenue": preds.round(2)})
