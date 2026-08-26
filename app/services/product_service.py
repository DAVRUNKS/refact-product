from app.database.connection import get_db_connection


def get_all_products():
    conn = get_db_connection()

    try:
        products = conn.execute(
            "SELECT * FROM products"
        ).fetchall()

        return products

    finally:
        conn.close()


def get_product_by_id(product_id):
    conn = get_db_connection()

    try:
        product = conn.execute(
            """
            SELECT *
            FROM products
            WHERE id = %s
            """,
            (product_id,)
        ).fetchone()

        return product

    finally:
        conn.close()


def create_product(name, price):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO products (name, price)
            VALUES (%s, %s)
            RETURNING id
            """,
            (name, price)
        )

        product_id = cursor.fetchone()["id"]

        conn.commit()

        return product_id

    finally:
        conn.close()


def update_product(product_id, name, price):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE products
            SET name = %s, price = %s
            WHERE id = %s
            """,
            (name, price, product_id)
        )

        conn.commit()

        return cursor.rowcount

    finally:
        conn.close()


def delete_product(product_id):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            DELETE FROM products
            WHERE id = %s
            """,
            (product_id,)
        )

        conn.commit()

        return cursor.rowcount

    finally:
        conn.close()