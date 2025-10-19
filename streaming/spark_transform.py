from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

def run_spark_job(input_path='data/processed/seviri_metrics.csv', output_path='data/processed/spark_results'):
    spark = SparkSession.builder.appName('SEVIRI Transformer').getOrCreate()
    df = spark.read.option('header', True).csv(input_path)
    df = df.withColumn('mean_bt_celsius', col('mean_bt') - 273.15)
    agg = df.groupBy().agg(avg('mean_bt_celsius').alias('avg_bt_celsius'))
    agg.write.mode('overwrite').parquet(output_path)
    spark.stop()

if __name__ == '__main__':
    run_spark_job()