from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import json
from kafka import KafkaProducer

# Kafka settings
KAFKA_BOOTSTRAP = 'localhost:9092'
TOPIC = 'seviri_ingest'
BBOX = [4.3, 27.5, 22.4, 59.6]


def produce_ingest_event(**context):
    ts = context['execution_date'].strftime("%Y-%m-%dT%H:%M:%S")
    event = {
        'timestamp': ts,
        'bbox': BBOX
    }
    producer = KafkaProducer(bootstrap_servers=KAFKA_BOOTSTRAP,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    producer.send(TOPIC, event)
    producer.flush()
    print("Kafka ingest event sent:", event)

default_args = {
    'owner': 'berkesenturk',
    'depends_on_past': False,
    'retries': 2
}

dag = DAG(
    'emit_seviri_kafka_dag',
    schedule_interval='*/15 * * * *',
    default_args=default_args,
    start_date=datetime(2025, 10, 1),
    catchup=False
)

op = PythonOperator(
    task_id='emit_seviri_ingest_event',
    python_callable=produce_ingest_event,
    provide_context=True,
    dag=dag
)
