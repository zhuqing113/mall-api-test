import pytest
import requests
import uuid

BASE = "http://localhost:8080"


@pytest.fixture(scope="session")
def auth_headers():
    d = requests.post(f"{BASE}/admin/login",
                      json={"username": "admin", "password": "macro123"},
                      timeout=10).json()["data"]
    return {"Authorization": d["tokenHead"] + d["token"]}
@pytest.fixture
def brand(auth_headers):
    name = f"AUTOTEST_{uuid.uuid4().hex[:8]}"

    # 准备：创建
    r = requests.post(f"{BASE}/brand/create",
                      json={"name": name, "logo": "http://x/logo.png"},
                      headers=auth_headers, timeout=10)
    assert r.status_code == 200 and r.json()["code"] == 200

    # 准备：按名字查 id
    r = requests.get(f"{BASE}/brand/list",
                     params={"keyword": name, "pageNum": 1, "pageSize": 20},
                     headers=auth_headers, timeout=10)
    brand_id = r.json()["data"]["list"][0]["id"]

    yield {"id": brand_id, "name": name}

    requests.get(f"{BASE}/brand/delete/{brand_id}", headers=auth_headers, timeout=10)
   