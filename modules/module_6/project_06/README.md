# Module 6 - Batch Processing with PySpark

In this assignment we'll put what we learned about Spark in practice.

I used the Yellow 2025-11 data from the official website:

`wget https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet`

To prepare the data I did the following:
- Created a [download_zone_data.py](./download_scripts/download_zone_data.py) script to download zone data
- Created a [download_taxi_trip_data.py](./download_scripts/download_taxi_trip_data.py) script to download yellow_tripdata_2025-11 data


Further analysis and pyspark code references can be in the following notebook here: [project_06_batch_spark_processing.ipynb](./project_06_batch_spark_processing.ipynb)

## Question 1: Install Spark and PySpark

- Install Spark
- Run PySpark
- Create a local spark session
- Execute spark.version.

What's the output?
> ANSWER: Spark version: 4.1.1

Python code:
```python
import pyspark
from pyspark.sql import SparkSession
import os

# Initialize Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

print(f"Spark version: {spark.version}")
```


## Question 2: Yellow November 2025

Read the November 2025 Yellow into a Spark Dataframe.

Repartition the Dataframe to 4 partitions and save it to parquet.

What is the average size of the Parquet (ending with .parquet extension) Files that were created (in MB)? Select the answer which most closely matches.

>ANSWER: 25MB

Python code:
```python
# Read parquet data file
df_yellow = spark.read \
    .option("header", "true") \
        .parquet('download_scripts/data/yellow_tripdata_2025-11.parquet')

# Repartition data
year = 2025
month = 11
output_path = f'download_scripts/data/pq/yellow/{year}/{month:02d}/'

df_yellow \
    .repartition(4) \
    .write.parquet(output_path)

# Reading file sizes
path = "download_scripts/data/pq/yellow/2025/11"

def list_files_with_size(path):
    for entry in os.scandir(path):
        if entry.is_file() and entry.name.lower().endswith(".parquet"):
            size = entry.stat().st_size
            unit = 'bytes'
            if size > 1024:
                size /= 1024
                unit = 'KB'
            if size > 1024:
                size /= 1024
                unit = 'MB'
            if size > 1024:
                size /= 1024
                unit = 'GB'
            print(f"{entry.name} → {size:.2f} {unit}")

size = list_files_with_size(path)
```


## Question 3: Count records

How many taxi trips were there on the 15th of November?

Consider only trips that started on the 15th of November.

> ANSWER: 162,604

Pyspark code:

```python
df_yellow.filter(to_date(df_yellow.tpep_pickup_datetime) == '2025-11-15').count()
```


## Question 4: Longest trip
What is the length of the longest trip in the dataset in hours?

>ANSWER: 90.6

Pyspark code:

```python
df_with_days = df_yellow.withColumn(
    "trip_time_hours", (unix_timestamp(col("tpep_dropoff_datetime")) - unix_timestamp(col("tpep_pickup_datetime"))) / 3600)

df_with_days.select("tpep_dropoff_datetime", "tpep_pickup_datetime", "trip_time_hours").show()

df_with_days.agg(max("trip_time_hours").alias("max_trip_time_hours")).show()
```


## Question 5: User Interface
Spark's User Interface which shows the application's dashboard runs on which local port?

>ANSWER: 4040

## Question 6: Least frequent pickup location zone

Using the zone lookup data and the Yellow November 2025 data, what is the name of the LEAST frequent pickup location Zone?

>ANSWER: Governor's Island/Ellis Island/Liberty Island

Pyspark code:
```python
# Importing zone data
df_zones = spark.read.parquet('download_scripts/data/zones/')

# join zone data with yellow trip data
df_result = df_yellow.join(df_zones, df_yellow.PULocationID == df_zones.LocationID)

df_pickup_report = df_result.select("tpep_pickup_datetime", "PULocationID", "LocationID", "Borough", "Zone", "service_zone")

df_pickup_report.groupBy("Zone").count().show()
```