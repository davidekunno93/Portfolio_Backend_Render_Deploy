from flask import Flask
from flask_migrate import Migrate


app = Flask(__name__)

from app.models import db
db.init_app(app)
migrate = Migrate(app, db)

from app.auth.routes import auth
app.register_blueprint(auth)

from app.api.routes import api
app.register_blueprint(api)

import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config():
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_NOTIFICATION=False