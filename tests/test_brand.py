import time
import requests
import uuid
from config import BASE_URL



def test_create_and_delete_brand(client):
    name = f"AUTOTEST_{uuid.uuid4().hex}" 
    brand_id = None  # 先设为 None，创建失败时 finally 里就知道没有 id 可删

    try:
        # 1. 创建
        r = client.post("/brand/create",
                          json={"name": name, "logo": "http://x/logo.png"}
                          )
        assert r.status_code == 200
        assert r.json()["code"] == 200
       

        # 2. 按关键字查 id
        r = client.get("/brand/list",
                         params={"keyword": name, "pageNum": 1, "pageSize": 20}
                         )
        data = r.json()["data"]
        assert data["total"] == 1
        brand_id = data["list"][0]["id"]
        assert data["list"][0]["name"] == name
        r = client.get(f"/brand/delete/{brand_id}")
        assert r.status_code == 200
        assert r.json()["code"] == 200
        r = client.get("/brand/list",
                         params={"keyword": name, "pageNum": 1, "pageSize": 20},
                         )
        assert r.json()["data"]["total"] == 0
        brand_id = None

    finally:
        # 3. 清理：只有拿到 id 才删
        if brand_id is not None:
            try:
                client.get(f"/brand/delete/{brand_id}")
            except Exception as e:
                print(f"清理测试数据失败，brand_id: {brand_id}, 错误: {e}")
