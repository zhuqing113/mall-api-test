import requests
from conftest import BASE


def test_get_brand_by_id(brand, auth_headers):
    r = requests.get(f"{BASE}/brand/{brand['id']}", headers=auth_headers, timeout=10)
    print(r.json())
    assert r.status_code == 200
    assert r.json()["code"] == 200
    assert body["data"]["id"] == brand      # 填：从哪个对象取
    assert body["data"]["name"] == brand 