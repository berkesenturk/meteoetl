from kafka import KafkaConsumer
import json
import eumdac
import os
from datetime import datetime

KAFKA_BOOTSTRAP = 'localhost:9092'
TOPIC = 'seviri_ingest'
COLLECTION_ID = "EO:EUM:DAT:MSG:HRSEVIRI"
DOWNLOAD_DIR = "data/raw"

def download_for_event(event):
    client = eumdac.Client(os.getenv("EUMETSAT_USERNAME"), os.getenv("EUMETSAT_PASSWORD"))
    coll = client.get_collection(COLLECTION_ID)
    ts = event['timestamp']
    bbox = event['bbox']
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)
    products = coll.search(start=ts, end=ts, bbox=bbox)
    for prod in products:
        file_path = os.path.join(DOWNLOAD_DIR, prod.name)
        if not os.path.exists(file_path):
            print(f"Downloading {prod.name} for {ts} ...")
            prod.download(file_path)
            print(f"Saved to {file_path}")

def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_BOOTSTRAP,
        value_deserializer=lambda v: json.loads(v.decode('utf-8')),
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='seviri_download'
    )
    print("Started SEVIRI API Kafka consumer.")
    for msg in consumer:
        event = msg.value
        print("Received ingest event:", event)
        download_for_event(event)

if __name__ == "__main__":
    main()
