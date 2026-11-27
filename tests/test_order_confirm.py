def test_confirm_order_uses_client_price(portal_client, cart_clean):
    r = portal_client.post("/cart/add", json={"productId": 1, "quantity": 1, "price": 100})
    assert r.status_code == 200
    assert r.json()["code"] == 200

    r = portal_client.get("/cart/list")
    items = r.json()["data"]
    assert len(items) == 1
    cid = items[0]["id"]

    r = portal_client.post("/order/generateConfirmOrder", json=[cid])
    assert r.status_code == 200
    body = r.json()
    assert body["code"] == 200
    assert body["data"]["calcAmount"]["payAmount"] == 100