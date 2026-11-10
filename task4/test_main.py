from fastapi.testclient import TestClient
from main import app
from settings import settings

client = TestClient(app)

headers = {"x-api-key": settings.API_KEY}


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_create_message():
    response = client.post(
        "/messages",
        json={"message": "Hello"},
        headers=headers
    )
    assert response.status_code == 200
    assert response.json()["success"] is True


def test_read_messages():
    response = client.get("/messages", headers=headers)
    assert response.status_code == 200


def test_missing_api_key():
    response = client.get("/messages")
    assert response.status_code == 401


def test_invalid_api_key():
    response = client.get(
        "/messages",
        headers={"x-api-key": "wrong-key"}
    )
    assert response.status_code == 401