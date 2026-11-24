import pytest
import requests
import uuid

from config import BASE_URL, ADMIN_USER, ADMIN_PASS,TIMEOUT
from client import ApiClient
import pymysql
from config import DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
from config import PORTAL_URL,MEMBER_USER,MEMBER_PASS

@pytest.fixture(scope="session")
def auth_headers():
    d = requests.post(f"{BASE_URL}/admin/login",
                      json={"username": ADMIN_USER, "password": ADMIN_PASS},
                      timeout=TIMEOUT).json()["data"]
    return {"Authorization": d["tokenHead"] + d["token"]}
@pytest.fixture
def brand(client,db_guard):
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
@pytest.fixture
def db_guard():
    conn = pymysql.connect(host=DB_HOST, port=DB_PORT,
                           user=DB_USER, password=DB_PASS,
                           database=DB_NAME,
                           autocommit=True)
    cur = conn.cursor()
    cur.execute("SELECT COALESCE(MAX(id), 0) FROM pms_brand")
    max_before = cur.fetchone()[0]
    yield cur, max_before
    cur.execute("DELETE FROM pms_brand WHERE id > %s", (max_before,))
    conn.commit()
    conn.close()
@pytest.fixture(scope="session")
def portal_client():
    login = ApiClient(base_url=PORTAL_URL)
    r = login.post("/sso/login", params={"username": MEMBER_USER, "password": MEMBER_PASS})
    d = r.json()["data"]
    headers = {"Authorization": d["tokenHead"] + d["token"]}
    return ApiClient(headers=headers, base_url=PORTAL_URL)
@pytest.fixture
def cart_clean(db_guard):
    cur, _ = db_guard
    sql = "DELETE FROM oms_cart_item WHERE member_id = %s AND product_id = %s AND delete_status = 0"
    cur.execute(sql, (1, 1))
    yield
    sql = "DELETE FROM oms_cart_item WHERE member_id = %s AND product_id = %s AND delete_status = 0"
    cur.execute(sql, (1, 1))