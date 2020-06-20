from functools import wraps

import jwt
from flask import request
from helpers.configs import key


def validate(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        message = request.get_json()
        message_keys = (
            "sender",
            "receiver",
            "message",
            "subject"
        )
        if not all(key in message_keys for key in message):
            return "Wrong fields in message"
        return f(*args, **kwargs)

    return wrap


def validate_token(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            payload = jwt.decode(request.headers.get("Authorization")[7:], key, algorithms="HS256")
            kwargs["user"] = payload["username"]
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

        return f(*args, **kwargs)
    return wrap
