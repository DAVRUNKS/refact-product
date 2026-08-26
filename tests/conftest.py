import os
import pytest
from dotenv import load_dotenv

load_dotenv()

os.environ["API_TOKEN"] = "testtoken"
os.environ["DB_HOST"] = "localhost"
os.environ["DB_PORT"] = "5432"
os.environ["DB_NAME"] = "products_test_db"
os.environ["DB_USER"] = "postgres"


@pytest.fixture(autouse=True)
def setup_test_database():

    from app.database.connection import get_db_connection

    conn = get_db_connection()

    try:
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

        conn.commit()

        yield

        conn.execute("DELETE FROM products")
        conn.execute("DELETE FROM users")

        conn.commit()

    finally:
        conn.close()


@pytest.fixture
def client():

    from app import create_app

    app = create_app()

    app.config["TESTING"] = True

    return app.test_client()