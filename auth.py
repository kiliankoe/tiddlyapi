import os
import hashlib
from datetime import datetime
from functools import wraps

from flask import request, Response

PASSPHRASE = os.environ['PASSPHRASE']

def gen_challenge():
    h = hashlib.new('sha256')
    h.update(datetime.today().strftime('%Y%m%d').encode('utf-8'))
    h.update('+'.encode('utf-8'))
    h.update(PASSPHRASE.encode('utf-8'))
    return h.hexdigest()

def challenge(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        challenge = gen_challenge()

        if not auth or auth != challenge:
            return Response(status=401)

        return func(*args, **kwargs)
    return decorated
