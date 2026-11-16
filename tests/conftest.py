import pytest
import requests
import uuid

from config import BASE_URL, ADMIN_USER, ADMIN_PASS
from client import ApiClient


@pytest.fixture(scope="session")
def auth_headers():
    d = requests.post(f"{BASE_URL}/admin/login",
                      json={"username": ADMIN_USER, "password": ADMIN_PASS},
                      timeout=10).json()["data"]
    return {"Authorization": d["tokenHead"] + d["token"]}
@pytest.fixture
def brand(client):
    name = f"AUTOTEST_{uuid.uuid4().hex[:8]}"

    # 准备：创建
    r = client.post(f"/brand/create",
                      json={"name": name, "logo": "http://x/logo.png"}
                      )
    assert r.status_code == 200 and r.json()["code"] == 200

    # 准备：按名字查 id
    r = client.get(f"/brand/list",
                     params={"keyword": name, "pageNum": 1, "pageSize": 20}
                     )
    brand_id = r.json()["data"]["list"][0]["id"]

    yield {"id": brand_id, "name": name}

    client.get(f"/brand/delete/{brand_id}")
@pytest.fixture(scope="session")
def client(auth_headers):
    return ApiClient(headers=auth_headers)   