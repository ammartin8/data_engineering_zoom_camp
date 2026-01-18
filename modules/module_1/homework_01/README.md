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
