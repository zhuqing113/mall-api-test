import time
import requests
import uuid

BASE = "http://localhost:8080"


def get_headers():
    d = requests.post(f"{BASE}/admin/login",
                      json={"username": "admin", "password": "macro123"},
                      timeout=10).json()["data"]
    return {"Authorization": d["tokenHead"] + d["token"]}


def test_create_and_delete_brand():
    h = get_headers()
    name = f"AUTOTEST_{uuid.uuid4().hex}" 
    brand_id = None  # 先设为 None，创建失败时 finally 里就知道没有 id 可删

    try:
        # 1. 创建
        r = requests.post(f"{BASE}/brand/create",
                          json={"name": name, "logo": "http://x/logo.png"},
                          headers=h, timeout=10)
        assert r.status_code == 200
        assert r.json()["code"] == 200
       

        # 2. 按关键字查 id
        r = requests.get(f"{BASE}/brand/list",
                         params={"keyword": name, "pageNum": 1, "pageSize": 20},
                         headers=h, timeout=10)
        data = r.json()["data"]
        assert data["total"] == 1
        brand_id = data["list"][0]["id"]
        assert data["list"][0]["name"] == name
        r = requests.get(f"{BASE}/brand/delete/{brand_id}", headers=h, timeout=10)
        # 填空5：断言删除的 HTTP 状态码和业务码都是 200
        assert r.status_code == 200
        assert r.json()["code"] == 200
        r = requests.get(f"{BASE}/brand/list",
                         params={"keyword": name, "pageNum": 1, "pageSize": 20},
                         headers=h, timeout=10)
        assert r.json()["data"]["total"] == 0
        brand_id = None

    finally:
        # 3. 清理：只有拿到 id 才删
        if brand_id is not None:
            try:
                requests.get(f"{BASE}/brand/delete/{brand_id}", headers=h, timeout=10)
            except Exception as e:
                print(f"清理测试数据失败，brand_id: {brand_id}, 错误: {e}")
