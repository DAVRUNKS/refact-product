from psycopg.errors import UniqueViolation
from werkzeug.security import generate_password_hash

from app.database.connection import get_db_connection


def register_user(username, password):

    hashed_password = generate_password_hash(password)

    conn = get_db_connection()

    try:
        conn.execute(
            """
            INSERT INTO users (username, password)
            VALUES (%s, %s)
            """,
            (username, hashed_password)
        )

        conn.commit()
        return True

    except UniqueViolation:
        conn.rollback()
        return False

    finally:
        conn.close()