from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from .auth import auth
from .routes import routes

app = Flask(__name__)
app.config.from_object('config.Config')

mongo = PyMongo(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'

app.register_blueprint(routes, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')
