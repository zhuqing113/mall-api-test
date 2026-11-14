import pytest
import requests

BASE = "http://localhost:8080"


@pytest.fixture(scope="session")
def auth_headers():
    d = requests.post(f"{BASE}/admin/login",
                      json={"username": "admin", "password": "macro123"},
                      timeout=10).json()["data"]
    return {"Authorization": d["tokenHead"] + d["token"]}