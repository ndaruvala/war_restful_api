from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo, MongoClient
from flask_cors import CORS
import urllib
import war_restful_api.resources.war
import war_restful_api.resources.user
import os


def create_app(testing=False):
    app = Flask(__name__)
    api = Api(app)
    CORS(app)

    if not testing:
        username = os.environ['MONGO_USERNAME']
        password = os.environ['MONGO_PASSWORD']
        app.config["MONGO_DBNAME"] = "games"
        app.config["MONGO_URI"] = (
            "mongodb+srv://"
            + urllib.parse.quote_plus(username)
            + ":"
            + urllib.parse.quote_plus(password)
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

    api.add_resource(
        war.War,
        "/war/start",
        endpoint="war_start_ep",
        resource_class_kwargs={"users_collection": users_collection},
    )

    api.add_resource(
        user.User,
        "/user/<int:user_id>",
        endpoint="user_ep",
        resource_class_kwargs={"users_collection": users_collection},
    )

    return app


if "__name__" == "__main__":
    create_app()
