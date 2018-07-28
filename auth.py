import os
from datetime import datetime
from functools import wraps

from flask import request, Response

PASSPHRASE = os.environ['PASSPHRASE']

def require_auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')

        if not auth or auth != PASSPHRASE:
            return Response(status=401)

        return func(*args, **kwargs)
    return decorated
