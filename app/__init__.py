from flask import Flask
from flask_pymongo import PyMongo
from .config import Config

from flask_jwt_extended import JWTManager

mongo = PyMongo()  
jwt = JWTManager()  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app) 
    jwt.init_app(app)     


    from .users.routes import api as user_api
    app.register_blueprint(user_api)
    
    from .users.models import User  # Adjust the import based on your structure
    # Call this during app initialization
    User.create_index()

    from .organizations.routes import api as org_api
    app.register_blueprint(org_api)

    return app

app = create_app() # for deployment on vercel 