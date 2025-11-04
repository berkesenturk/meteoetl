from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from data_ingestion.download_seviri import query_and_download_seviri

BBOX = [4.3, 27.5, 22.4, 59.6]
DOWNLOAD_DIR = "data/raw"

def dl_task(**context):
    now = context['execution_date']  # Airflow passes DAG run time!
    query_and_download_seviri(now, BBOX, DOWNLOAD_DIR)

default_args = {
    'owner': 'berkesenturk',
    'depends_on_past': False,
    'retries': 2
}

dag = DAG(
    'download_seviri_query_dag',
    schedule_interval='*/15 * * * *',
    default_args=default_args,
    start_date=datetime(2025, 10, 1),
    catchup=False
)

dl_op = PythonOperator(
    task_id='query_and_download_seviri',
    python_callable=dl_task,
    provide_context=True,
    dag=dag
)
