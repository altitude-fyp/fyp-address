from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_post_api_charts():
    """
    tests if POST /api/charts is working as per normal
    """
    data = {
        "countries": ["Singapore"]
    }

    r = client.post(
        "/api/charts/",
        headers={},
        json=data
    )

    assert r.status_code == 200
    
    json = r.json()
    assert json["status"] == "success"
