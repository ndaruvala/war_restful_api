from src import create_app
from flask_pymongo import MongoClient
import os
import pytest


def setup_test_database():
    client = MongoClient()
    db = client["testdatabase"]
    users_collection = db["users"]

    users_collection.delete_many({})

    test_player1 = {"id": 1, "wins": 0}
    users_collection.insert_one(test_player1)

    test_player2 = {"id": 2, "wins": 0}
    users_collection.insert_one(test_player2)


@pytest.fixture
def client():
    app = create_app(testing=True)
    app.config['TESTING'] = True
    client = app.test_client()
    setup_test_database()
    yield client


def test_update_wins(client):
    response = client.post('/war/start')
    data = response.get_json()
    winner = data['winner']

    client = MongoClient()
    db = client["testdatabase"]

    player1 = db.users.find_one({"id": 1})
    player2 = db.users.find_one({"id": 2})

    if winner == "player1":
        assert player1["wins"] == 1 and player2["wins"] == 0
    else:
        assert player2["wins"] == 1 and player1["wins"] == 0
