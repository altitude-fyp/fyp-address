from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_api_charts():
    """
    tests if GET /api/charts is working as per normal
    """

    r = client.get("/api/charts/Singapore")

    assert r.status_code == 200
    
    data = r.json()
    assert data["status"] == "success"
