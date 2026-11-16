def test_get_brand_by_id(brand, client):
    r = client.get(f"/brand/{brand['id']}")
    assert r.status_code == 200
    body = r.json()
    assert body["code"] == 200
    assert body["data"]["id"] == brand["id"]
    assert body["data"]["name"] == brand["name"]