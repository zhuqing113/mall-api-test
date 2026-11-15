import requests
from config import BASE_URL                


def test_get_brand_by_id(brand, auth_headers):
    r = requests.get(f"{BASE_URL}/brand/{brand['id']}", headers=auth_headers, timeout=10)
    assert r.status_code == 200
    body = r.json()
    assert body["code"] == 200
    assert body["data"]["id"] == brand["id"]
    assert body["data"]["name"] == brand["name"]