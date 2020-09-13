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


@app.route('/api/postData', methods=['Get','POST'])
def post():
    client_json = {
        'title': request.json['title'],
        'body': request.json['body']
    }
    print(client_json)
    title = client_json['title']
    print(title)
    body = client_json['body']
    data = Recipe(title=title, body=body)
    db.session.add(data)
    db.session.commit()
    return '201'  # нужно возвращать строку


@app.route('/api/delData/<elem_id>', methods=['DELETE'])
def delete(elem_id):
    delete_item = Recipe.query.get(elem_id)
    db.session.delete(delete_item)
    db.session.commit()
    return '201'
    # посмотерть доки sql
