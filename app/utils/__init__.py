import os
from functools import wraps

from flask import jsonify, request


API_TOKEN = os.getenv("API_TOKEN")


def require_token(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({
                "error": "Authorization token required"
            }), 401

        if token != f"Bearer {API_TOKEN}":
            return jsonify({
                "error": "Invalid token"
            }), 403

        return f(*args, **kwargs)

    return decorated_function