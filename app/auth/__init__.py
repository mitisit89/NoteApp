from  flask import  Blueprint,request
from  app import  User,db
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth',__name__)

@auth.route('/registation',methods=['POST'])
def create_new_user():
    new_user=request.get_json()
    username=new_user['username']
    email=new_user['email']
    password=generate_password_hash(new_user['password'],"sha256")
    add_new_user=User(username=username,email=email,password=password)
    db.session.add(add_new_user)
    db.session.commit()