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

def test_pickled_folder_exist():
    """
    checks if pickled folder is present in backend directory
    """
    assert "pickled" in os.listdir(home)

    pickled = home  + "/pickled"

    assert "all_countries.sav" in os.listdir(pickled)
    assert "top_countries_cossim_matrix.sav" in os.listdir(pickled)