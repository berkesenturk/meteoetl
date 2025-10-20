# MeteoETL: Meteosat SEVIRI Data Engineering Pipeline

A professional portfolio project demonstrating batch, streaming, and real-time ETL for Meteosat SEVIRI satellite data. Includes Airflow, Kafka, Spark, Flink, PostgreSQL/TimescaleDB, Docker.

Author: Berke Sentürk

## Architecture Overview

- Ingestion: Airflow, Python, Kafka streaming
- Processing: Batch (Xarray/Pandas/Spark), Streaming (Flink)
- Storage: PostgreSQL/TimescaleDB
- Visualization: Grafana/Kibana (setup optional)
- Deployment: Kubernetes, Docker Compose microservice stack

firstly ensure that meteoetl works in terms of downloading data /raw (will be s3 in future)
