import pyspark
from pyspark.sql import SparkSession
import os

# Initialize Spark Session
spark = SparkSession.builder \
    .master("local[*]") \
    .appName('test') \
    .getOrCreate()

print(f"Spark version: {spark.version}")

# Download the file (if not already present)
file_path = "taxi_zone_lookup.csv"
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

# Show first few lines (optional, but useful for debugging)
with open(file_path, 'r') as f:
    print("\n--- First 5 lines of the file ---")
    for i, line in enumerate(f):
        if i >= 5:
            break
        print(line.strip())

# Read CSV into DataFrame
df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(file_path)

# Show DataFrame
df.show(5)  # Show first 5 rows

# Write to Parquet
df.write.mode("overwrite").parquet("zones")

# List files in directory
print("\n--- Files in current directory ---")
for f in os.listdir('.'):
    print(f)

# Stop Spark Session
spark.stop()
