from functools import wraps

import jwt
from flask import jsonify, request

from app import app
from app.models import User


def check_token(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'msg': 'Token is missing'})
        try:
            data = jwt.decode(token, app.config['SECRET_KEYS'])
            curent_user = User.qurey.fillter_by(public_id=data['public_id']).first()
        except:
            return jsonify(jsonify({'msg': 'Token is ok'}))
        return func(curent_user, *args, **kwargs)

    return decorator
