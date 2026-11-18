import pandas as pd
from pathlib import Path
from urllib.request import urlretrieve

# Public NYC TLC yellow taxi trips for January 2024 (Parquet)
DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

# Local folder for downloaded files (git-ignored)
DATA_DIR = Path("data")


def download_file(url, dest_dir):
    # Create the target folder if it does not exist yet
    dest_dir.mkdir(exist_ok=True)

    # Local path = folder + the file name at the end of the URL
    dest_path = dest_dir / url.split("/")[-1]

    # Skip the download if we already have the file
    if dest_path.exists():
        print(f"Already downloaded: {dest_path}")
        return dest_path

    # Fetch the file from the internet and save it to disk
    print(f"Downloading {url}")
    urlretrieve(url, dest_path)
    return dest_path


def read_trips(file_path):
    # Load the Parquet file into an in-memory DataFrame
    return pd.read_parquet(file_path)


def inspect_trips(df):
    # Row and column counts
    print("Shape:", df.shape)

    # Column names and the type pandas assigned to each
    print("\nColumn types:")
    print(df.dtypes)

    # Count of missing values per column
    print("\nMissing values per column:")
    print(df.isna().sum())
    
    # Summary statistics (min, max, mean...) for key numeric columns
    print("\nSummary statistics:")
    print(df[["passenger_count", "trip_distance", "fare_amount", "total_amount"]].describe())


path = download_file(DATA_URL, DATA_DIR)
df = read_trips(path)
inspect_trips(df)
print(df.head(3).T)