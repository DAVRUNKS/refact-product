import os
import jwt

from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash
from app.services.auth_service import register_user
from app.utils.validators import validate_registration
from app.utils.errors import APIError
from app.database.connection import get_db_connection


auth_bp = Blueprint("auth", __name__)

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

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    if not data:
        raise APIError(
            "JSON data required",
            400
        )

    username = data.get("username")
    password = data.get("password")

    error = validate_registration(
        username,
        password
    )

    if error:
        raise APIError(
            error,
            400
        )

    success = register_user(
        username,
        password
    )

    if not success:
        raise APIError(
            "Username already exists",
            409
        )

    return jsonify({
        "message": "User registered successfully"
    }), 201