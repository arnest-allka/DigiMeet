from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from bson import ObjectId

# Initialize extensions
mongo = PyMongo()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app
    mongo.init_app(app)
    bcrypt.init_app(app)
    
    # Import Blueprints and register them
    from .auth import auth as auth_blueprint
    from .routes import routes as routes_blueprint

    app.register_blueprint(auth_blueprint, url_prefix='/')
    app.register_blueprint(routes_blueprint, url_prefix='/')

    from .models import User

    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    @login_manager.user_loader
    def load_user(user_id):
        user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user_data:
            return User(user_data)
        return None
    return app
