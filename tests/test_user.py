from flask_pymongo import MongoClient
import os
import pytest
from ..app import create_app


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


def test_get_wins_1(client):
    response = client.get('/user/1')
    data = response.get_json()

    client = MongoClient()
    db = client["testdatabase"]
    user = db.users.find_one({"id": 1})

    assert data["id"] == user["id"]
    assert data["wins"] == user["wins"]


def test_get_wins_2(client):
    response = client.get('/user/2')
    data = response.get_json()

    client = MongoClient()
    db = client["testdatabase"]
    user = db.users.find_one({"id": 2})

    assert data["id"] == user["id"]
    assert data["wins"] == user["wins"]
