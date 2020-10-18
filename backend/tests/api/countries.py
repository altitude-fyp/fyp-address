from app import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_api_countries_metadata():
    """
    tests GET /api/countries/metadata/{countries}
    """
    r = client.get("/api/countries/metadata/Singapore")
    assert r.status_code == 200

    data = r.json()
    assert "Singapore" in data
    
    for key in ["code", "lat", "lon", "flag"]:
        assert key in data["Singapore"]


def test_api_countries_metadata_multiple_countries():
    """
    tests GET /api/countries/metadata/{countries} for multiple countries
    """
    r = client.get("/api/countries/metadata/Singapore,Malaysia,China")
    assert r.status_code == 200

    data = r.json()
    assert len(data) == 3

    for key in ["Singapore", "Malaysia", "China"]:
        assert key in data
    
    for key in ["code", "lat", "lon", "flag"]:
        assert key in data["Singapore"]


def test_api_countries_selectableFeatures():
    """
    tests GET /api/countries/selectableFeatures
    """
    r = client.get("/api/countries/selectableFeatures")
    assert r.status_code == 200

    data = r.json()
    assert len(data) == 4
    

def test_api_countries_statistics():
    """
    tests GET /api/countries/statistics
    """
    r = client.get("/api/countries/statistics/Singapore")
    assert r.status_code == 200

    data = r.json()
    assert "Singapore" in data


def test_api_countries_statistics_multiple_countries():
    """
    tests GET /api/countries/statistics for multiple countries
    """
    r = client.get("/api/countries/statistics/Singapore,Malaysia,China")
    assert r.status_code == 200

    data = r.json()
    assert "Singapore" in data
    assert "Malaysia" in data
    assert "China" in data


def test_api_countries_list():
    """
    tests GET /api/countries/list
    """
    r = client.get("/api/countries/list")
    assert r.status_code == 200

    data = r.json()
    assert data["status"] == "success"


def test_api_countries_csv():
    """
    tests GET /api/countries/csv
    """
    r = client.get("/api/countries/csv/Singapore,Malaysia,China,United States")
    assert r.status_code == 200

    data = r.json()
    assert len(data) == 4

    countries = [i["country"] for i in data]
    for k in ["Singapore", "Malaysia", "China", "United States"]:
        assert k in countries


        