import os
import sys

"""
Adding backend directory to path
"""
here = sys.path[0]
home = here[:-len("/tests")]

def test_dotenv():
    """
    checks if .env file is present in backend directory
    """
    assert ".env" in os.listdir(home)

def test_env():
    """
    checks if env folder is present in backend directory
    """
    assert "env" in os.listdir(home)

def test_pickled_folder():
    """
    checks if pickled folder is present in backend directory
    """
    assert "pickled" in os.listdir(home)

    pickled = home  + "/pickled"
    pdir = os.listdir(pickled)

    assert "constants.sav" in pdir
    assert "country_similarity_matrix.sav" in pdir
    assert "npl_binary_forecast.sav" in pdir
    