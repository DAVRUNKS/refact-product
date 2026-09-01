import os
import jwt
import psycopg
import pytest

JWT_SECRET = os.getenv("JWT_SECRET")

os.getenv("DB_HOST")
os.getenv("DB_PORT")
os.getenv("DB_NAME")
os.getenv("DB_USER")
os.getenv("DB_PASSWORD")
os.getenv("JWT_SECRET")
os.getenv("CORS_ORIGINS")
os.getenv("PORT")

@pytest.fixture
def auth_headers():
    token = jwt.encode(
        {
            "user_id": 1,
            "username": "testuser"
        },
        os.getenv("JWT_SECRET"),
        algorithm="HS256"
    )

    return {
        "Authorization": f"Bearer {token}"
    }
    
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