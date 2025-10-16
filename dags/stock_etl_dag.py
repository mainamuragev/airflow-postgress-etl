from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import pandas as pd
import sqlalchemy
import requests

default_args = {
    "owner": "airflow",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="stock_market_etl",
    start_date=datetime(2025, 10, 15),
    schedule_interval="@daily",  # or use `schedule=` for Airflow 2.8+
    catchup=False,
    default_args=default_args,
    tags=["etl", "stocks"],
) as dag:

    def extract_data(ti):
        url = "https://api.polygon.io/v3/reference/tickers"
        params = {
            "limit": "100",
            "sort": "ticker",
            "apiKey": Variable.get("POLYGON_API_KEY")
        }
        response = requests.get(url, params=params)
        data = response.json().get("results", [])
        ti.xcom_push(key='raw_data', value=data)

    def transform_data(ti):
        raw_data = ti.xcom_pull(key='raw_data', task_ids='extract_data')
        df = pd.DataFrame(raw_data)
        df = df[["ticker", "name", "primary_exchange", "currency_name"]].fillna("N/A")
        ti.xcom_push(key='clean_data', value=df.to_dict(orient="records"))

    def load_data(ti):
        clean_data = ti.xcom_pull(key='clean_data', task_ids='transform_data')
        df = pd.DataFrame(clean_data)
        engine = sqlalchemy.create_engine(Variable.get("POSTGRES_CONN"))
        df.to_sql('fund_tickers', engine, if_exists='append', index=False)

    extract = PythonOperator(task_id='extract_data', python_callable=extract_data)
    transform = PythonOperator(task_id='transform_data', python_callable=transform_data)
    load = PythonOperator(task_id='load_data', python_callable=load_data)

    extract >> transform >> load
