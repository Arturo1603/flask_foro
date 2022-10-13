from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config_env

app = Flask(__name__)
app.config.from_object(config_env[getenv('FLASK_ENV')])

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)