from flask import jsonify, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required

from app import app, db
from app.models import Recipe


@app.route('/api/getData', methods=['GET'])
@cross_origin()
@jwt_required(fresh=True)
def get():
    posts = Recipe.query.all()
    data = []
    for post in posts:
        i = {'id': str(post.id), 'title': post.title, 'slug': post.slug, 'body': post.body,
             'time': str(post.time_stamp)}
        data.append(i)
    return jsonify(data)


@app.route('/api/postData', methods=['POST'])
@cross_origin()
@jwt_required(fresh=True)
def post():
    client_json = request.get_json()
    print(client_json)
    data = Recipe(title=client_json['title'], body=client_json['body'])
    db.session.add(data)
    db.session.commit()
    return '200' # нужно возвращать строку


@app.route('/api/delData/<elem_id>', methods=['DELETE'])
@cross_origin()
@jwt_required(fresh=True)
def delete(elem_id):
    delete_item = Recipe.query.get(elem_id)
    db.session.delete(delete_item)
    db.session.commit()
    return '201'
    # посмотерть доки sql
