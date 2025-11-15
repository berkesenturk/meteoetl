This is the place where I will note my development over the project.

15.11.2025
---------
why master worker for some?
should .env be used for security in docker compose env or sth else

download_seviri_query_dag: downloads the data and save it into a path. 
This is directly running a function from DAG, I am not sure how good it is.
Like emit_seviri_kafka_dag, maybe we should throw an event and it should work in somewhere else.

etl_seviri_dag: the dag we need. well ordered process line
etl_streaming_dag: I don't know whether it is useful.