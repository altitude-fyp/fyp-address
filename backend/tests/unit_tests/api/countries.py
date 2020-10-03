from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_get_api_countries():
    """
    test that GET api/countries runs successfully
    """
    r = client.get("/api/countries")
    assert r.status_code == 200
    assert r.json()["status"] == "success"

def test_post_api_countries():
    """
    test that POST api/countries runs successfully
    """
    data = {
        "countries": ["Singapore"]
    }

    r = client.post(
        "/api/countries/",
        headers={},
        json=data
    )
    assert r.status_code == 200
    assert r.json()["status"] == "success"