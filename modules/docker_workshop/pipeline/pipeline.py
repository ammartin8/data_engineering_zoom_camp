import pandas as pd
import sys

# sample pipeline
print("arguments", sys.argv)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

df = pd.DataFrame({"day": [1, 2], "B": [3, 4]})
df['day'] = day
print(df.head())

df.to_parquet(f"output_day_{day}.parquet")

print(f'hello pipeline, day={day}')