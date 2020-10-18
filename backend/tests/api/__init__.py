from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_main():
    """
    tests if fastapi app works
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "This is the backend for address-fyp"
