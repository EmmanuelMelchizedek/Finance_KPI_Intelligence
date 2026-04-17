import streamlit as st
import plotly.express as px
from src.etl import load_financial_data, build_monthly_kpis, build_segment_kpis
from src.forecast import forecast_revenue
from src.kpi_summary import generate_exec_summary

st.set_page_config(page_title="Finance KPI Intelligence Platform", layout="wide")
st.title("Finance KPI Intelligence Platform")
st.caption("Executive KPI monitoring, forecasting, and business narrative generation")

df = load_financial_data()
monthly = build_monthly_kpis(df)
segments = build_segment_kpis(df)
forecast = forecast_revenue(monthly)
summary = generate_exec_summary(monthly, segments, forecast)

col1, col2, col3, col4 = st.columns(4)
latest = monthly.iloc[-1]
col1.metric("Revenue", f"${latest['revenue']:,.0f}")
col2.metric("Profit", f"${latest['profit']:,.0f}")
col3.metric("Margin %", f"{latest['margin_pct']:.1f}%")
col4.metric("Customers", f"{int(latest['customers']):,}")

st.subheader("Executive summary")
st.info(summary)

rev_fig = px.line(monthly, x="month", y="revenue", title="Monthly Revenue Trend", markers=True)
st.plotly_chart(rev_fig, use_container_width=True)

forecast_fig = px.line(forecast, x="month", y="forecast_revenue", title="Forecasted Revenue", markers=True)
st.plotly_chart(forecast_fig, use_container_width=True)

seg_fig = px.bar(segments, x="region", y="profit", color="product", barmode="group", title="Profit by Region and Product")
st.plotly_chart(seg_fig, use_container_width=True)

st.subheader("Segment KPI table")
st.dataframe(segments, use_container_width=True)
