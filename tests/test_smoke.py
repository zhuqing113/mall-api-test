import requests

def test_pytest_works():
    assert 1 + 1 == 2

def test_requests_works():
    resp = requests.get("https://httpbin.org/get", timeout=10)
    assert resp.status_code == 200