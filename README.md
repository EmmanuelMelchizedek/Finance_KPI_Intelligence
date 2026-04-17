# Finance KPI Intelligence Platform

## Business problem
Finance leaders need faster visibility into revenue, cost, profitability, customer trends, and forecast movement. This project simulates a modern analytics workflow that ingests monthly financial data, transforms it into business-ready KPI models, generates a forecast, and produces an executive dashboard with optional AI-written summaries.

## Why this project is valuable
This is not just a dashboard. It demonstrates:
- SQL-based KPI modeling
- ETL and pipeline orchestration patterns
- Forecasting with Python
- Executive reporting and narrative insights
- dbt-style transformation layers
- GitHub-ready engineering discipline

## Tech stack
Python, Pandas, NumPy, scikit-learn, SQL, Streamlit, Plotly, DuckDB, dbt-style SQL models, Airflow DAG template, Docker, GitHub Actions

## What the app does
- Loads financial transaction data
- Builds core KPIs such as revenue, cost, profit, margin, and complaint ratio
- Forecasts next-quarter revenue using time-based modeling
- Highlights best and worst performing segments
- Generates executive summary text
- Displays a dashboard suitable for business review meetings

## Repository structure
```text
project_1_finance_kpi_intelligence/
  app/
    streamlit_app.py
  data/
    financial_transactions.csv
  dags/
    finance_kpi_pipeline.py
  dbt_models/
    staging_financials.sql
    mart_finance_kpis.sql
  src/
    etl.py
    forecast.py
    kpi_summary.py
  sql/
    schema.sql
    analyst_queries.sql
  .github/workflows/
    ci.yml
  Dockerfile
  requirements.txt
```

## Local run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## Deploy
### Streamlit Community Cloud
- Push this folder to GitHub
- Set app path to `project_1_finance_kpi_intelligence/app/streamlit_app.py`
- Add any optional environment variables later if you connect LLM APIs

### Docker
```bash
docker build -t finance-kpi-app .
docker run -p 8501:8501 finance-kpi-app
```

## Resume-ready bullets
- Built a finance KPI intelligence platform using SQL, Python, and Streamlit to track revenue, cost, profitability, and customer trends, enabling faster executive decision-making through automated dashboards and forecasting.
- Designed ETL and dbt-style transformation workflows for monthly financial data, improving reporting reliability and demonstrating production-ready analytics engineering patterns for business performance monitoring.
- Developed time series forecasting and AI-generated executive summaries to surface trend changes, business risks, and segment-level performance drivers in a leadership-friendly format.
