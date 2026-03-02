# Homework: Build Your Own dlt Pipeline

## The Challenge
For this homework, build a dlt pipeline that loads NYC taxi trip data from a custom API into DuckDB and then answer some questions using the loaded data.


## Data Source

You'll be working with **NYC Yellow Taxi trip data** from a custom API (not available as a dlt scaffold). This dataset contains records of individual taxi trips in New York City.

| Property | Value |
|----------|-------|
| Base URL | `https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api` |
| Format | Paginated JSON |
| Page Size | 1,000 records per page |
| Pagination | Stop when an empty page is returned |


## Question 1: What is the start date and end date of the dataset?
ANSWER: 2009-06-01 to 2009-07-01

Python Query:
```python
print(df.trip_pickup_date_time.describe())
print(df.trip_dropoff_date_time.describe())
```


## Question 2: What proportion of trips are paid with credit card?
ANSWER: 26.66%

Python Query:
```
df.payment_type.value_counts(normalize=True)
```

## Question 3: What is the total amount of money generated in tips?
ANSWER: $6,063.41

Python Query:
```python
df.tip_amt.sum()
```

