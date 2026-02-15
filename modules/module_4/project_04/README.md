# Homework 4 Responses: Analytical Engineering with dbt

The objective was to create a dbt project that creates a data warehouse using the NYC Taxi green & yellow taxi data files from 2019-2020.

The following steps were taken

  - Set up dbt project following the dbt cloud setup guide
  - Loaded the Green and Yellow taxi data for 2019-2020 files into a Google Cloud Storage bucket (Used Docker and Kestra tool to orchestrate ETL)
  - Created data models within dbt that create the required dimensions, fact tables, macro functions, etc. All dbt models are located [here](../dbt_workshop/taxi_ny_data/).
  - Ran dbt build --target default to create all models and run tests

After a successful build, the following models were created: fct_trips, dim_zones, and fct_monthly_zone_revenue within the data warehouse.

The following questions test concepts learned from Analytical Engineering with dbt:

## Question 1. dbt Lineage and Execution

Given a dbt project with the following structure:

```
models/
├── staging/
│   ├── stg_green_tripdata.sql
│   └── stg_yellow_tripdata.sql
└── intermediate/
    └── int_trips_unioned.sql (depends on stg_green_tripdata & stg_yellow_tripdata)
```

If you run dbt run --select int_trips_unioned, what models will be built?

**ANSWER: `int_trips_unioned` only**

*Note: assumming stg_green_tripdata & stg_yellow_tripdata were already built

## Question 2. dbt Tests

You've configured a generic test like this in your schema.yml:

columns:
  - name: payment_type
    data_tests:
      - accepted_values:
          arguments:
            values: [1, 2, 3, 4, 5]
            quote: false

Your model fct_trips has been running successfully for months. A new value 6 now appears in the source data.

What happens when you run dbt test --select fct_trips?

**ANSWER: dbt will fail the test, returning a non-zero exit code**

*Note: making the assumption that the payment test is defined under model name: `fct_trips`



## Question 3. Counting Records in fct_monthly_zone_revenue

After running your dbt project, query the fct_monthly_zone_revenue model.

What is the count of records in the fct_monthly_zone_revenue model?

**ANSWER: 12,184**

SQL Query:

```sql
SELECT COUNT(*) FROM dbt_am_dev.fct_monthly_zone_revenue;
```


## Question 4. Best Performing Zone for Green Taxis (2020)

Using the fct_monthly_zone_revenue table, find the pickup zone with the highest total revenue (revenue_monthly_total_amount) for Green taxi trips in 2020.

Which zone had the highest revenue?

**ANSWER: East Harlem North**

SQL Query:
```sql
-- Highest Rev in Zone for Green Taxi Trips in 2020
with green_zone_rev as (
SELECT pickup_zone, revenue_month, revenue_monthly_total_amount FROM dbt_am_dev.fct_monthly_zone_revenue
where service_type = 'Green' and EXTRACT(year from revenue_month) = 2020
order by pickup_zone, revenue_month
)
, summ_tbl as (
select pickup_zone, SUM(revenue_monthly_total_amount) as rev_total
from green_zone_rev
group by pickup_zone
order by pickup_zone
)
select pickup_zone, summ_tbl.rev_total
from summ_tbl
where rev_total = (select max(rev_total) from summ_tbl)
;
```


## Question 5. Green Taxi Trip Counts (October 2019)
Using the fct_monthly_zone_revenue table, what is the total number of trips (total_monthly_trips) for Green taxis in October 2019?

**ANSWER: 384,624**

SQL Query:
```sql
--Total Trips for green taxi in October

SELECT revenue_month, sum(total_monthly_trips) FROM dbt_am_dev.fct_monthly_zone_revenue
where service_type = 'Green' and EXTRACT(year from revenue_month) = 2019 and EXTRACT(month from revenue_month) = 10
group by revenue_month
```


## Question 6. Build a Staging Model for FHV Data

Create a staging model for the For-Hire Vehicle (FHV) trip data for 2019.

  Load the FHV trip data for 2019 into your data warehouse
  Create a staging model stg_fhv_tripdata with these requirements (model defined [here](../dbt_workshop/taxi_ny_data/models/staging/)):
      Filter out records where dispatching_base_num IS NULL
      Rename fields to match your project's naming conventions (e.g., PUlocationID → pickup_location_id)

What is the count of records in stg_fhv_tripdata?

**ANSWER: 43,244,693**

SQL Query:
```
-- stg_fhv_tripdata record count
SELECT count(*) FROM `projectID.dbt_am_dev.stg_fhv_tripdata`;
```