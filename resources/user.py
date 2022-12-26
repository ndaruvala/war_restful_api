from flask import jsonify
from flask_restful import Resource, abort


class User(Resource):
    """A class used to represent a User route."""

    def __init__(self, users_collection):
        self.users_collection = users_collection

    def get(self, user_id):
        user = self.users_collection.find_one({"id": user_id})

        if user is None:
            abort(404, message=f"User with id {user_id} does not exist.")
        else:
            return jsonify({"id": user_id, "wins": user["wins"]})
