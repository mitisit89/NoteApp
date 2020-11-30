from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id=db.Column(db.String(50),unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))
    posts = db.relationship('Recipe', backref='author', lazy='dynamic')
    #avatar=db.Column(db.BLOB)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140))
    body = db.Column(db.Text)
    time_stamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.String, db.ForeignKey('user.public_id'))
