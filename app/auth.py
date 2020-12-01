import uuid
import jwt
import datetime
from flask import request, make_response, jsonify
from flask_cors import cross_origin
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash

from app import app, db
from app.models import User

"""
Если я правильно понял ,то авторизация по кукам работает только если приложение работает на одном домене
"""


@app.route('/api/auth/login', methods=['POST', 'GET'])
@cross_origin(supports_credentials=True)
def check_current_user():
    current_user = request.get_json()
    print(current_user)
    user = User.query.filter_by(email=current_user['email']).first()

    if user and check_password_hash(user.password, current_user['password']):
        token = jwt.encode(
            {'user': current_user['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8'), 'pub_id': user.public_id}), 201
    else:
        abort(401)


@app.route('/api/auth/registration', methods=['POST'])
@cross_origin()
def create_new_user():
    new_user = request.get_json()
    check_email = User.query.filter_by(email=new_user['email']).first()
    if check_email is None:
        password = generate_password_hash(new_user['password'], "sha256")
        add_new_user = User(public_id=str(uuid.uuid4()), username=new_user['username'], email=new_user['email'],
                            password=password)
        db.session.add(add_new_user)
        db.session.commit()
        return jsonify({'msg': 'The new user created'}), 201
    else:
        return jsonify({'msg': 'The username/email are exist'}), 403
