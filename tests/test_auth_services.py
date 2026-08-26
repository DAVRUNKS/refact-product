from app.services.auth_service import register_user
from app.database.connection import get_db_connection
from werkzeug.security import check_password_hash


def test_register_user():

    result = register_user(
        "testuser",
        "password123"
    )

    assert result is True


def test_password_is_hashed():

    register_user(
        "hashuser",
        "password123"
    )

    conn = get_db_connection()

    user = conn.execute(
        "SELECT * FROM users WHERE username = %s",
        ("hashuser",)
    ).fetchone()

    conn.close()

    assert user is not None
    assert user["password"] != "password123"

    assert check_password_hash(
        user["password"],
        "password123"
    )


def test_duplicate_username():

    register_user(
        "duplicate",
        "password123"
    )

    result = register_user(
        "duplicate",
        "anotherpassword"
    )

    assert result is False