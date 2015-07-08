from .base import *


CORS_ORIGIN_ALLOW_ALL = True

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

JWT_AUTH = {
    "JWT_VERIFY_EXPIRATION": False,
}
