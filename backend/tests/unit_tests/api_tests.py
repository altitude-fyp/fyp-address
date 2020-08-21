import os
import sys

"""
Adding backend directory to path
"""
here = sys.path[0]
home = here[:-len("/tests")]
sys.path.append(home)

def test_sys_path():
    """
    checks that backend directory is in sys.path
    """
    backend_present = False
    for p in sys.path:
        p = p.split("/")[-1]
        if p == "backend":
            backend_present = True
    assert backend_present


from app import app

from fastapi.testclient import TestClient

client = TestClient(app)

def test_main():
    """
        placeholder: tests if fastapi works

    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "hello world"