from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_api_analytics_top_countries():
    """
    tests for success status in /api/analytics/top_countries/{country_name} api
    """
    r = client.get("/api/analytics/top_countries/Singapore")
    assert r.status_code == 200
    
    data = r.json()
    assert data["status"] == "success"
    assert len(data["top3"]) == 3