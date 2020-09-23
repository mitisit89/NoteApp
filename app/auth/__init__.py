from flask import Blueprint, request,make_response
from app import User, db
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)


@auth.route('api/login', methods=['GET'])
def check_current_user():
    current_user = {
        'email': request.json['email'],
        'password': request.json['password']
    }
    user = User.query.filter_by(email=current_user['email']).first()
    if user is None or check_password_hash(user.password, current_user['password']):
        return '404'


@auth.route('api/registation', methods=['POST'])
def create_new_user():
    new_user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'password': request.json['password']
    }
    check_email = User.query.filter_by(email=new_user['email']).first()
    if check_email is None:
        user_name = new_user['username']
        email = new_user['email']
        password = generate_password_hash(new_user['password'], "sha256")
        add_new_user = User(username=user_name, email=email, password=password)
        db.session.add(add_new_user)
        db.session.commit()
    else:
        return ''
