import requests
from config import BASE_URL

def test_pytest_works():
    assert 1 + 1 == 2

def test_mall_admin_reachable():
    r = requests.get(f"{BASE_URL}/v3/api-docs/default", timeout=10)
    assert r.status_code == 200