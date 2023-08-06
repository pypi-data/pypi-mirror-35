from flask import current_app
from itsdangerous import URLSafeSerializer, URLSafeTimedSerializer
from werkzeug.local import LocalProxy


timed_serializer = LocalProxy(lambda:
        URLSafeTimedSerializer(current_app.config['ITSDANGEROUS_SECRET']))


serializer = LocalProxy(lambda:
        URLSafeSerializer(current_app.config['ITSDANGEROUS_SECRET']))


def get_token(payload, salt):
    """Generic way of retrieving an untimed serializer for the current_app.
    """
    return serializer.dumps(payload, salt)


def decode_token(token, salt):
    """Generic way of decoding a token from an untimed serializer for the current_app.
    """
    return serializer.loads(token, salt)


def get_timed_token(payload, salt):
    """Generic way of retrieving a timed serializer for the current_app.
    """
    return timed_serializer.dumps(payload, salt)


def decode_timed_token(token, salt, max_age=None, return_timestamp=True):
    """Generic way of decoding a token from an untimed serializer for the current_app. Includes the
    timestamp on the response by default.
    """
    return timed_serializer.loads(token, max_age=max_age, return_timestamp=return_timestamp,
            salt=salt)

