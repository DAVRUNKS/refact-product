from functools import wraps
from flask import request

from app.config import Config
from app.utils.responses import error_response


def require_token(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return error_response(
                "Authorization token required",
                401
            )

        if token != f"Bearer {Config.get_api_token()}":
            return error_response(
                "Invalid token",
                403
            )

        return f(*args, **kwargs)

    return decorated_function