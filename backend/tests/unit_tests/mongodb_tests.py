import os
import sys

"""
Adding backend directory to path
"""
here = sys.path[0]
home = here[:-len("/tests")]
sys.path.append(home)

from mongodb_helper import *

def test_path():
    """
    checks if backend directory is in path
    """
    out = False
    for path in sys.path:
        *_, path = path.split("/")
        if path == "backend":
            out = True
            
    assert out

def test_mongo_environment_variable():
    """
    checks if .env in backend has been loaded correctly
    """
    mongodb_connection_url = os.getenv("MONGODB_CONNECTION_URL")

    assert mongodb_connection_url is not None
    assert len(mongodb_connection_url) > 0
    assert "mongo" in mongodb_connection_url
    assert "fypaddress" in mongodb_connection_url

def test_mongo_find_one():
    """
    checks if mongo_find_one function can successfully read from mongodb atlas
        Note: pls don't delete the test collection on mongo
    """
    result = mongo_find_one("test", {"_id": "test_id"})

    assert type(result) == dict
    assert len(result) == 2
    assert result["hello"] == "world"