import pytest
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient('127.0.0.1:8080')
db = client["db"]
col = db["employees"]


@pytest.fixture
def app_fixture():
    return app


@pytest.fixture
def client_fixture():
    client = app.test_client()
    yield client


# Test get route
def test_get_route(client_fixture):
    response = client_fixture.get('/api/v1/employees')
    assert response.status_code == 200


# Test post route
def test_post_route(client_fixture):
    response = client_fixture.post('/api/v1/employees')
    assert response.status_code == 200


# Test delete route
def test_delete_route(client_fixture):
    response = client_fixture.delete('/api/v1/employees/<int:employee_id>')
    assert response.status_code == 200


# Test put route
def test_put_route(client_fixture):
    response = client_fixture.put('/api/v1/employees/<int:employee_id>')
    assert response.status_code == 200
