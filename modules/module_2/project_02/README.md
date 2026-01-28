# Homework 2 Responses

## Question 1.
ANSWER: 128.3 MiB

## Question 2.
ANSWER: green_tripdata_2020-04.csv

## Question 3.
ANSWER: 24,648,499

```sql
SELECT COUNT(*)  FROM `projectID.dataset.yellow_tripdata` 
WHERE filename like '%2020%' 
```

## Question 4.
ANSWER: 1,734,051

```sql
SELECT COUNT(*) FROM `projectID.dataset.green_tripdata` 
WHERE filename like '%2020%'
```

## Question 5.
ANSWER: 1,925,152


## Question 6.
ANSWER: Add a timezone property set to America/New_York in the Schedule trigger configuration