from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

app = Flask(__name__)

def create_app(config_name):
	#app = Flask(__name__)
	app.config.from_object(config_by_name[config_name])
	db = SQLAlchemy(app)
	db.create_all()
	flask_bcrypt.init_app(app)

	return app
