# Module Assignment 1: Docker, Terraform & SQL

In this homework I prepared the environment and practiced Docker and SQL. This repository contains the code for solving the assignment questions.

## Question 1. Understanding Docker images
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?

Steps: \
a. Created a Dockerfile with a base image of python3.13.11-slim

b. Created a docker image called homework_test:python13 using:
```
docker build -t homework_test:python13
```
c. Ran the following command:
```
docker run -it homework_test:python13
```
d. Once inside the docker container typed:
```
pip -version
```

>ANSWER: 25.3


## Question 2. Understanding Docker networking and docker-compose
Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

>ANSWER: db:5432 \
**Note**: db is listed as the service name; therefore it is the host. Port 5432 is the port that the postgres container uses; 5433 is the localhost port used to access the postgres.


For questions 3-6, I needed to prepare the data. \
Steps: 
- I download the green taxi trips data for November 2025: \
`wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet`

- I also downloaded a CSV file to get the dataset with zones: \
`wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv`


## Question 3. Counting short trips
For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile? 
>ANSWER: 8,007

SQL snippet:
```sql
select count(1)
from public.green_taxi_data_2025_11
where lpep_pickup_datetime >= date '2025-11-01' and lpep_pickup_datetime < date '2025-12-01'
and trip_distance <= 1 
```

## Question 4. Longest trip for each day

Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

Use the pick up time for your calculations.


>ANSWER: 2025-11-14

SQL snippet:
```sql
WITH t1 AS (
    SELECT trip_distance, lpep_pickup_datetime
    FROM public.green_taxi_data_2025_11
    WHERE trip_distance < 100
	ORDER BY trip_distance desc
)
SELECT lpep_pickup_datetime, trip_distance
FROM t1
limit 1
;
```

## Question 5. Biggest pickup zone
Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

>ANSWER: East Harlem North

SQL snippet:
```sql
/*Join zone data*/
with t1 as (
select * from
public.green_taxi_data_2025_11 as gtd
where date(gtd.lpep_pickup_datetime) = date '2025-11-18'
)
, t2 as (
select "PULocationID", "LocationID", "Borough", "Zone", service_zone, total_amount 
from t1
left join public.taxi_zones tz
on t1."PULocationID" = tz."LocationID"
)
/*sum amount by zone*/
, t3 as (
select "Zone", sum(total_amount) as tot_amt
from t2
group by "Zone"
order by tot_amt desc
)
select *
from t3
limit 1
```

## Question 6. Largest tip

For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

Note: it's tip , not trip. We need the name of the zone, not the ID.

>ANSWER: Yorkville West

SQL snippet:
```sql
with t1 as (
select "PULocationID", tz1."LocationID" as pickup_id, tz1."Zone" as pickup_zone
,"DOLocationID", tz2."LocationID" as dropoff_id, tz2."Zone" as dropoff_zone
, tip_amount, lpep_pickup_datetime
from public.green_taxi_data_2025_11 as gtd
left join public.taxi_zones tz1
on gtd."PULocationID" = tz1."LocationID"
left join public.taxi_zones tz2
on gtd."DOLocationID" = tz2."LocationID"
where gtd.lpep_pickup_datetime >= date '2025-11-01' and gtd.lpep_pickup_datetime < '2025-12-01'
and tz1."Zone" = 'East Harlem North'
order by tip_amount desc
)
select pickup_zone, dropoff_zone, tip_amount
from t1
limit 1
```

## Terraform

In this section I prepared the environment by creating resources in GCP with Terraform. Files can be reviewed here: [terraform_hmk](/modules/module_1/project_01/terraform_hmk/)

Terraform was installed and files were modified as necessary to create a GCP Bucket and Big Query Dataset.

## Question 7. Terraform Workflow
Which of the following sequences, respectively, describes the workflow for:

    - Downloading the provider plugins and setting up backend,
    - Generating proposed changes and auto-executing the plan
    - Remove all resources managed by terraform`

ANSWER: terraform init, terraform apply -auto-approve, terraform destroy