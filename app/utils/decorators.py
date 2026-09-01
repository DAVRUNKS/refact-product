from functools import wraps

import jwt
from flask import request

from app.config import Config
from app.utils.responses import error_response


def require_token(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return error_response(
                "Authorization token required",
                401
            )

        if not auth_header.startswith("Bearer "):
            return error_response(
                "Invalid authorization format",
                401
            )

        token = auth_header.split(" ", 1)[1]

        try:
            payload = jwt.decode(
                token,
                Config.get_jwt_secret(),
                algorithms=["HS256"]
            )

            request.user = payload

        except jwt.ExpiredSignatureError:
            return error_response(
                "Token has expired",
                401
            )

        except jwt.InvalidTokenError:
            return error_response(
                "Invalid token",
                403
            )

        return f(*args, **kwargs)

    return decorated_function

