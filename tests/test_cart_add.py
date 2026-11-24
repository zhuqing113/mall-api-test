def test_add_twice_accumulates(portal_client, cart_clean, db_guard):
    cur, _ = db_guard
    q = "SELECT COUNT(*), COALESCE(SUM(quantity), 0) FROM oms_cart_item WHERE member_id = 1 AND product_id = 1 AND delete_status = 0"
    body = {"productId": 1, "quantity": 1}

    r = portal_client.post("/cart/add", json=body)
    assert r.status_code == 200 and r.json()["code"] == 200
    cur.execute(q)
    assert cur.fetchone() == (1, 1)

    r = portal_client.post("/cart/add", json=body)
    assert r.status_code == 200 and r.json()["code"] == 200
    cur.execute(q)
    assert cur.fetchone() == (1, 2)