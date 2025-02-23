import config
import psycopg2
from sqlalchemy import create_engine

def test_db_connection():
    conn = psycopg2.connect(
        host = config.DB_HOST,
        port = config.DB_PORT,
        database = config.DB_NAME,
        user = config.DB_USER,
        password = config.DB_PASSWORD
    )

    conn.cursor()

    print("PostgreSQL connection successful!")


def get_db_engine():
    DB_URL = "postgresql://" + config.DB_USER + ":" + config.DB_PASSWORD + "@" + config.DB_HOST + ":" + config.DB_PORT + "/" + config.DB_NAME
    engine = create_engine(DB_URL)

    return engine