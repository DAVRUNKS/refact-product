import os
import jwt
from psycopg.errors import UniqueViolation
from werkzeug.security import generate_password_hash

from werkzeug.security import check_password_hash

from app.database.connection import get_db_connection

def login_user(username, password):

    conn = get_db_connection()

    user = conn.execute(
        """
        SELECT * FROM users
        WHERE username = %s
        """,
        (username,)
    ).fetchone()

    conn.close()

    if user is None:
        return None

    if not check_password_hash(user["password"], password):
        return None

    token = jwt.encode(
        {
            "user_id": user["id"],
            "username": user["username"]
        },
        os.getenv("JWT_SECRET"),
        algorithm="HS256"
    )
    
    return token

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