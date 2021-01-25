from functools import wraps

import jwt
from flask import jsonify, request,Response

from app import app
from app.models import User


def check_token(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
        if not token:
            return jsonify({'msg': 'Token is missing'}),Response(status=401)
        try:
            data = jwt.decode(token, app.config['SECRET_KEYS'])
            current_user = User.qurey.fillter_by(public_id=data['public_id']).first()
        except:
            return Response(status=201)
        return func(current_user, *args, **kwargs)

    return decorator
