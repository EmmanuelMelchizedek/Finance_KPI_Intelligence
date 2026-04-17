"""Airflow DAG template for orchestrating the KPI pipeline.
Replace the python callables with your own warehouse and model execution tasks.
"""
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_load():
    print("Load finance data into warehouse")


def run_transformations():
    print("Execute dbt or SQL transformations")


def refresh_dashboard_assets():
    print("Refresh downstream dashboard tables or exports")


with DAG(
    dag_id="finance_kpi_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@monthly",
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id="extract_load", python_callable=extract_load)
    t2 = PythonOperator(task_id="run_transformations", python_callable=run_transformations)
    t3 = PythonOperator(task_id="refresh_dashboard_assets", python_callable=refresh_dashboard_assets)
    t1 >> t2 >> t3
