from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
from config import Configuration

app = Flask(__name__, static_folder='../client/dist', static_url_path='')
app.config.from_object(Configuration)
db = SQLAlchemy(app)

#migrate = Migrate(app, db)
from app.models import User, Recipe

from app.routes import rest

app.register_blueprint(rest)


@app.route('/')
def index():
    return send_file('../client/dist/index.html')
