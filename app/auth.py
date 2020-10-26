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
        status = {'login_status': 'true'}
        resp = make_response(jsonify(status), 201)
        return resp
    else:
        abort(401)


@app.route('/registration', methods=['POST'])
@cross_origin()
def create_new_user():
    new_user = request.json()
    check_email = User.query.filter_by(email=new_user['email']).first()
    if check_email is None:
        user_name = new_user['username']
        email = new_user['email']
        password = generate_password_hash(new_user['password'], "sha256")
        add_new_user = User(username=user_name, email=email, password=password)
        db.session.add(add_new_user)
        db.session.commit()
        return '200'
    else:
        return abort(404)
