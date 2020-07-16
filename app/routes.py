
from flask import Blueprint,jsonify
from app import app
from app.models import Recipe

rest = Blueprint('rest', __name__)


@app.route('/api/', methods=['GET'])
def get():
    posts = Recipe.query.all()
    data =[]
    for post in posts:
        i = {'id': str(post.id), 'title': post.title, 'slug': post.slug, 'body': post.body,
             'time': str(post.time_stamp)}
        data.append(i)
    return jsonify(data)


def post():
    pass
