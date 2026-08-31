import os

import psycopg
import pytest


os.environ["DB_HOST"] = "localhost"
os.environ["DB_PORT"] = "5432"
os.environ["DB_NAME"] = "products_test_db"
os.environ["DB_USER"] = "postgres"
os.environ["DB_PASSWORD"] = "postgres"
os.environ["API_TOKEN"] = "testtoken"


@pytest.fixture(autouse=True)
def setup_test_database():

    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="products_test_db",
        user="postgres",
        password="postgres"
    )

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.execute("DELETE FROM products")
    conn.execute("DELETE FROM users")

    conn.commit()
    conn.close()

    yield

    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="products_test_db",
        user="postgres",
        password="postgres"
    )

    conn.execute("DELETE FROM products")
    conn.execute("DELETE FROM users")

    conn.commit()
    conn.close()