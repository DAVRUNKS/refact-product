from flask import Blueprint, jsonify, request

from app.services.auth_service import register_user
from app.utils.validators import validate_registration
from app.utils.errors import APIError


auth_bp = Blueprint("auth", __name__)


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