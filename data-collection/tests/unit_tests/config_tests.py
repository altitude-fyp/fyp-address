import os
import sys

here = sys.path[0]
home = here[:-len("/tests")]

def test_dotenv():
    """
    checks if .env file is present in data-collection directory
    """
    assert ".env" in os.listdir(home)

