from flask import Flask
# from flask_migrate import Migrate
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
CORS(app, supports_credentials=True, withCredentials=True)
db = SQLAlchemy(app)

# migrate = Migrate(app, db)
from app.models import User, Recipe
from app import auth
from app import routes
