import pyspark
from pyspark.sql import SparkSession
import os

# Initialize Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

print(f"Spark version: {spark.version}")

# Define the data directory
data_dir = "data"

# Download the file (if not already present)

file_path = os.path.join(data_dir, "taxi_zone_lookup.csv")

# Ensure the data directory exists
os.makedirs(data_dir, exist_ok=True)

if not os.path.exists(file_path):
    try:
        print("Downloading taxi_zone_lookup.csv...")
        # Use urllib instead of !wget for better portability
        import urllib.request
        url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
        urllib.request.urlretrieve(url, file_path)
        print("Download complete.")
    except Exception as e:
        print(f"Failed to download: {e}")
else:
    print("File already exists.")

# Read CSV into DataFrame
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(file_path)

# Show DataFrame
df.show(5)  # Show first 5 rows

# Write to Parquet
output_dir = os.path.join(data_dir, "zones")
os.makedirs(output_dir, exist_ok=True)
df.write.mode("overwrite").parquet(output_dir)

# List files in directory
print("\n--- Files in current directory ---")
for f in os.listdir('.'):
    print(f)

# Stop Spark Session
spark.stop()