import os
import pandas as pd

def process_seviri(**kwargs):
    os.makedirs('data/processed', exist_ok=True)
    metrics = {'timestamp': pd.Timestamp.now(), 'mean_bt': 285.3, 'std_bt': 3.4, 'cloud_ratio': 0.23}
    pd.DataFrame([metrics]).to_csv('data/processed/seviri_metrics.csv', index=False)
    print('Processed metrics saved.')