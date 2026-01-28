# Homework 1 Responses

## Question 1.

Steps:
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

ANSWER: 25.3


## Question 2.
ANSWER: db:5432
db is listed as the service name; therefore it is the host. Port 5432 is the port that the postgres container uses; 5433 is the localhost port used to access the postgres.


## Question 3.
ANSWER: 8,007

```sql
select count(1)
from public.green_taxi_data_2025_11
where lpep_pickup_datetime >= date '2025-11-01' and lpep_pickup_datetime < date '2025-12-01'
and trip_distance <= 1 
```

## Question 4.
ANSWER: 2025-11-14

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

## Question 5.
ANSWER: East Harlem North

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

## Question 6.
ANSWER: Yorkville West

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

## Question 7.
ANSWER: terraform init, terraform apply -auto-approve, terraform destroy