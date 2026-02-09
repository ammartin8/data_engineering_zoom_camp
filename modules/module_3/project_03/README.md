# Homework 3 Responses
Note: Using projectID and dataset labels instead of actual names.

## Question 1.
What is count of records for the 2024 Yellow Taxi Data?

ANSWER: 20,332,093

Query:
```sql
SELECT COUNT(*)
FROM `projectID.dataset.yellow_tripdata_2024_ext`
;
```

## Question 2.
Write a query to count the distinct number of PULocationIDs for the entire dataset on both the tables.
What is the estimated amount of data that will be read when this query is executed on the External Table and the Table?

ANSWER: 0 MB for the External Table and 155.12 MB for the Materialized Table

Query:
```sql
-- Distinct Number of PULocationIDs from both datasets: 262
-- External: Estimated 0B Processed
SELECT COUNT(DISTINCT(PULocationID)) as unique_locations
FROM `projectID.dataset.yellow_tripdata_2024_ext`
;

-- Materialized: Estimated 155.12MB Processed
SELECT COUNT(DISTINCT(PULocationID)) as unique_locations
FROM `projectID.dataset.yellow_tripdata_2024`
;
```

## Question 3.
Write a query to retrieve the PULocationID from the table (not the external table) in BigQuery. Now write a query to retrieve the PULocationID and DOLocationID on the same table. Why are the estimated number of Bytes different?

ANSWER: BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

Query:
```sql
-- Column Review Comparsion
-- One column: Estimated 155.12 MB Processed
SELECT PULocationID
FROM `projectID.dataset.yellow_tripdata_2024`
;

-- Two column: Estimated 310.24 MB Processed
SELECT PULocationID, DOLocationID
FROM `projectID.dataset.yellow_tripdata_2024`
;
```

## Question 4.
How many records have a fare_amount of 0?

ANSWER: 8,333

Query:
```sql
-- Fare Amount
SELECT COUNT(*)
FROM `projectID.dataset.yellow_tripdata_2024_ext`
WHERE fare_amount = 0
;
```

Question 5.
What is the best strategy to make an optimized table in Big Query if your query will always filter based on tpep_dropoff_datetime and order the results by VendorID (Create a new table with this strategy)

ANSWER: Partition by tpep_dropoff_datetime and Cluster on VendorID

Query:
```sql
-- Partition/Cluster Strategy
CREATE OR REPLACE TABLE `projectID.dataset.yellow_tripdata_2024_ext`
PARTITION BY DATE(tpep_pickup_datetime)
CLUSTER BY VendorID AS
SELECT * FROM projectID.dataset.yellow_tripdata_2024_ext
;
```

## Question 6.
Write a query to retrieve the distinct VendorIDs between tpep_dropoff_datetime 2024-03-01 and 2024-03-15 (inclusive)

Use the materialized table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 5 and note the estimated bytes processed. What are these values?

Choose the answer which most closely matches.
ANSWER: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7.
Where is the data stored in the External Table you created?

ANSWER: GCP Bucket


## Question 8.
It is best practice in Big Query to always cluster your data:

ANSWER: FALSE


## Question 9.
No Points: Write a SELECT count(*) query FROM the materialized table you created. How many bytes does it estimate will be read? Why?

ANSWER: Due to the fact that the query result has been ran and is already cached.