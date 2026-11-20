import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


def make_engine():
    load_dotenv()
    user = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    database = os.environ["POSTGRES_DB"]
    host = "localhost"
    port = 5432

    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
    return create_engine(url)


def load_trips(df, engine):
    with engine.begin() as connection:
        df.to_sql(
            "trips",
            connection,
            if_exists="replace",
            index=False,
            chunksize=50_000,
        )