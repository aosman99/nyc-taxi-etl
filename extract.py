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

download_file(DATA_URL, DATA_DIR)