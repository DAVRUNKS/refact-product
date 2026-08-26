import os
import sqlite3

import pytest


TEST_DATABASE = "test_products.db"

os.environ["DATABASE"] = TEST_DATABASE


@pytest.fixture(autouse=True)
def setup_test_database():

    conn = sqlite3.connect(TEST_DATABASE)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()

    # Clear previous test data
    conn.execute("DELETE FROM products")
    conn.execute("DELETE FROM users")

    conn.commit()
    conn.close()

    yield

    # Clean up after the test
    conn = sqlite3.connect(TEST_DATABASE)

    conn.execute("DELETE FROM products")
    conn.execute("DELETE FROM users")

    conn.commit()
    conn.close()