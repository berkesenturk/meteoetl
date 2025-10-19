import pandas as pd

def load_to_database(**kwargs):
    df = pd.read_csv('data/processed/seviri_metrics.csv')
    print('Loading metrics to DB simulation:')
    print(df.head())
    # Extend with psycopg2/SQLAlchemy for TimescaleDB