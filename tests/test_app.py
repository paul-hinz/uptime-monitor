import pytest
from app import app, check_url
from unittest.mock import patch, Mock

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Uptime Monitor" in response.data

@patch("app.requests.get")
def test_index_post(client, mock_get):
    mock_response = Mock()
    mock_response.ok = True
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    response = client.post("/", data={"url": "https://example.com"})
    assert response.status_code == 200
    assert b"https://example.com" in response.data
    assert b"UP" in response.data