from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
CORS(app, supports_credentials=True, withCredentials=True)
db = SQLAlchemy(app)
jwt = JWTManager(app)
from app.models import User, Recipe
migrate = Migrate(app, db)
from app import auth, routes
