import uuid

from flask import request, jsonify
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token
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
        token = create_access_token(identity=current_user)
        print(token)
        return jsonify({'token': token}), 201
    else:
        return jsonify({'error': 'неверный логин или пароль'}), 401


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
