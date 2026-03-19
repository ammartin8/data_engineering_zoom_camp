# Module 2 Responses: Kestra Orchestration

For this assignment, I worked with the green taxi dataset located here:

`https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/`

Assignment \
So far in the course, we processed data for the year 2019 and 2020. The task is to extend the existing flows to include data for the year 2021.

In order to include data for year 2021, I leveraged the backfill functionality in the kestra scheduled flow (you can see the workflow here: [09_gcp_taxi_scheduled.yaml](/modules/module_2/project_02/flows/09_gcp_taxi_scheduled.yaml))

## Question 1.

Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size (i.e. the output file yellow_tripdata_2020-12.csv of the extract task)? \

>ANSWER: 128.3 MiB

## Question 2.

What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

>ANSWER: green_tripdata_2020-04.csv

## Question 3.

How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

>ANSWER: 24,648,499

SQL Snippet:
```sql
SELECT COUNT(*)  FROM `projectID.dataset.yellow_tripdata` 
WHERE filename like '%2020%' 
```

## Question 4.

How many rows are there for the Green Taxi data for all CSV files in the year 2020?

>ANSWER: 1,734,051

SQL snippet:
```sql
SELECT COUNT(*) FROM `projectID.dataset.green_tripdata` 
WHERE filename like '%2020%'
```

## Question 5.

How many rows are there for the Yellow Taxi data for the March 2021 CSV file?

>ANSWER: 1,925,152


## Question 6.

How would you configure the timezone to New York in a Schedule trigger?

>ANSWER: Add a timezone property set to America/New_York in the Schedule trigger configuration