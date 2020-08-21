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