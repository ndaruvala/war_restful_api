from src.resources.war import War
from src.resources.user import User
from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo, MongoClient
from flask_cors import CORS
import urllib
import os

USERNAME = os.environ['MONGO_USERNAME']
PASSWORD = os.environ['MONGO_PASSWORD']


def create_app(testing=False):
    app = Flask(__name__)
    api = Api(app)
    CORS(app)

    if not testing:
        app.config["DEBUG"] = True
        app.config["MONGO_DBNAME"] = "games"
        app.config["MONGO_URI"] = (
            "mongodb+srv://"
            + urllib.parse.quote_plus(USERNAME)
            + ":"
            + urllib.parse.quote_plus(PASSWORD)
            + "@cluster0.jtwfi.mongodb.net/games?retryWrites=true&w=majority"
        )
        mongo = PyMongo(app)
        users_collection = mongo.db.users
    else:
        app.config["MONGO_DBNAME"] = "testdatabase"
        app.config["MONGO_URI"] = "mongodb://localhost:27017"
        mongo = MongoClient()
        db = mongo["testdatabase"]
        users_collection = db["users"]

    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

    api.add_resource(
        War,
        "/war/start",
        endpoint="war_start_ep",
        resource_class_kwargs={"users_collection": users_collection},
    )

    api.add_resource(
        User,
        "/user/<int:user_id>",
        endpoint="user_ep",
        resource_class_kwargs={"users_collection": users_collection},
    )

    return app

app = create_app()
