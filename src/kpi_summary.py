import pandas as pd


def generate_exec_summary(monthly: pd.DataFrame, segments: pd.DataFrame, forecast: pd.DataFrame) -> str:
    latest = monthly.sort_values("month").iloc[-1]
    prev = monthly.sort_values("month").iloc[-2]
    growth = ((latest["revenue"] - prev["revenue"]) / prev["revenue"]) * 100
    best_segment = segments.iloc[0]
    weakest_segment = segments.sort_values("margin_pct").iloc[0]
    avg_forecast = forecast["forecast_revenue"].mean()

    return (
        f"Latest monthly revenue reached ${latest['revenue']:,.0f}, with a month-over-month change of {growth:.1f}%. "
        f"Overall margin stands at {latest['margin_pct']:.1f}%. The strongest segment is {best_segment['region']} - {best_segment['product']} "
        f"with ${best_segment['profit']:,.0f} in profit, while the lowest margin segment is {weakest_segment['region']} - {weakest_segment['product']} "
        f"at {weakest_segment['margin_pct']:.1f}%. The next-quarter average forecasted monthly revenue is ${avg_forecast:,.0f}, "
        f"which helps frame budget planning and leadership review."
    )
