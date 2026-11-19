import pandas as pd

def add_trip_duration(df):
    time_elapsed = df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]

    df["trip_duration_min"] = time_elapsed.dt.total_seconds() / 60

    return df


def flag_suspect_rows(df):
    negative_fare = df["fare_amount"] < 0
    bad_distance = (df["trip_distance"] <= 0) | (df["trip_distance"] > 100)
    bad_duration = df["trip_duration_min"] <= 0
    zero_passengers = df["passenger_count"] == 0

    df["is_suspect"] = negative_fare | bad_distance | bad_duration | zero_passengers

    return df


def fix_types(df):
    df["passenger_count"] = df["passenger_count"].astype("Int64")
    return df


def transform_trips(df):
    df = add_trip_duration(df)
    df = flag_suspect_rows(df)
    df = fix_types(df)
    return df

