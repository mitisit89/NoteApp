from flask import Blueprint, jsonify, request
from app import app, db
from app.models import Recipe

rest = Blueprint('rest', __name__)


@app.route('/api/getData', methods=['GET'])
def get():
    posts = Recipe.query.all()
    data = []
    for post in posts:
        i = {'id': str(post.id), 'title': post.title, 'slug': post.slug, 'body': post.body,
             'time': str(post.time_stamp)}
        data.append(i)
    return jsonify(data)


@app.route('/api/postData', methods=['POST'])
def post():
    client_json = request.get_json()
    title = client_json['title']
    body = client_json['body']
    data = Recipe(title=title, body=body)
    db.session.add(data)
    db.session.commit()
    return 200
