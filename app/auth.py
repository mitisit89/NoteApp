from flask import Blueprint, request, make_response, abort
import uuid
from app import app
from app.models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import cross_origin


@app.route('/api/auth/login', methods=['POST'])
@cross_origin()
def check_current_user():
    current_user = request.get_json()
    print(current_user)
    user = User.query.filter_by(email=current_user['email']).first()
    if user and check_password_hash(user.password, current_user['password']):
        return 'ok'
    else:
        return abort(401)


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
