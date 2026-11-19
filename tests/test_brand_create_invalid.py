import pytest

LOGO = "http://x/logo.png"

CASES = [
    ({"logo": LOGO}, 404),                                              # name 缺失
    ({"name": "", "logo": LOGO}, 404),                                  # name 空串
    ({"name": "AUTOTEST_p1"}, 404),                                    # 填空1：logo 缺失，预期码？依据？
    ({"name": "AUTOTEST_p2", "logo": LOGO, "sort": -1}, 404),          # 填空2：sort=-1
    ({"name": "AUTOTEST_p3", "logo": LOGO, "showStatus": 2}, 404),  
]

IDS = ["name missing", "name empty", "logo missing", "sort=-1", "showStatus=2"]

@pytest.mark.parametrize("body, expected_code", CASES, ids=IDS)
def test_create_invalid(client, body, expected_code, db_guard):
    r = client.post("/brand/create", json=body)
    assert r.status_code == 200
    assert r.json()["code"] == expected_code