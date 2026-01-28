#! /usr/bin/env python
# coding: utf-8

import click
from io import BytesIO
import pandas as pd
import pyarrow.parquet as pq
import requests
from tqdm.auto import tqdm # tracks ingestion progress
from sqlalchemy import create_engine

dtype = {
    "VendorID": "int32",
    "store_and_fwd_flag": "object",
    "RatecodeID": "float64",
    "PULocationID": "int32",
    "DOLocationID": "int32",
    "passenger_count": "float64",
    "trip_distance": "float64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "payment_type": "float64",
    "trip_type": "float64",
    "congestion_surcharge": "float64",
    "cbd_congestion_fee": "float64"
}

parse_dates = [
    "lpep_pickup_datetime",
    "lpep_dropoff_datetime"
]


# Parameters for sql engine
@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='pgdatabase', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--year', default=2025, type=int, help='Year of the data')
@click.option('--month', default=11, type=int, help='Month of the data')
@click.option('--target-table', default='green_taxi_data_2025_11', help='Target table name')
@click.option('--chunksize', default=100000, type=int, help='Chunk size for reading CSV')

def ingest_data(pg_user, pg_pass, pg_host, pg_port, pg_db, year, month, target_table, chunksize):
    # Data source
    prefix = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
    url = f'{prefix}/green_tripdata_{year}-{month:02d}.parquet'

    # Download parquet file in memory
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        print("file downloaded!")
    except Exception as err:
        print(f"The following error occurred: {err}")

    # Read the Parquet file from bytes
    table = pq.read_table(BytesIO(response.content))

    # Define SQL engine
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # Convert table to batches and iterate
    first = True
    for batch in tqdm(table.to_batches(), desc="Processing batches"):
        df_chunk = batch.to_pandas()

        if first:
            # Create table schema (no data)
            df_chunk.head(0).to_sql(
                name=target_table,
                con=engine,
                if_exists="replace",
                index=False
            )
            first = False
            print("Table created")

        # Insert chunk
        df_chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            chunksize=chunksize,
            index=False
        )

        print(f"Inserted {len(df_chunk)} rows") 

def ingest_zone_data(pg_user='root', pg_pass='root', pg_host='pgdatabase', pg_port=5432, pg_db='ny_taxi'):
    # Download taxi zone file
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'

    try:
        # Define SQL engine
        engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

        df_zones = pd.read_csv(url)
        df_zones.to_sql(name='taxi_zones', con=engine, if_exists='replace')
        print('Taxi zone data loaded!')
    except Exception as err:
        print(f'The following error occurred: {err}')


if __name__== '__main__':
    try:
        ingest_data()
        ingest_zone_data()
    except Exception as e:
        print(f'An error has occurred: {e}')


