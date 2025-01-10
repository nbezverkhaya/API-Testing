import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import requests
from utils.config import BASE_URL
from utils.schema_validator import validate_json

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "address": {"type": "object"},
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": {"type": "object"}
    },
    "required": ["id", "name", "username", "email"]
}

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    for user in users:
        assert validate_json(user, USER_SCHEMA)
