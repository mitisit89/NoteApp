from app import app
from app.models import Recipe
from flask import Blueprint
from flask_restful import Api, reqparse, request, Resource
rest=Blueprint('rest',__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        posts = Recipe.query.all()
        data = []
        for post in posts:
            i = {'id': str(post.id), 'title': post.title, 'slug': post.slug, 'body': post.body, 'time': str(post.time_stamp)}
            data.append(i)
        return  data
        
api.add_resource(HelloWorld,  '/api/hello')
