import pytest

# 每行:(body, 期望库内一行 = (name, first_letter, logo, sort, show_status))
CASES = [
    # C-01 name 长64
    ({"name": "A" * 64, "logo": "x.png", "sort": 1, "showStatus": 1},
     ("A" * 64, "A", "x.png", 1, 1)),
    # C-07 firstLetter 长8
    ({"name": "AUTOTEST_fl8", "firstLetter": "B" * 8, "logo": "x.png", "sort": 1, "showStatus": 1},
     ("AUTOTEST_fl8", "B" * 8, "x.png", 1, 1)),
    # C-14 sort=0
    ({"name": "AUTOTEST_sort0", "logo": "x.png", "sort": 0, "showStatus": 1},
     ("AUTOTEST_sort0", "A", "x.png", 0, 1)),
    # C-15 showStatus=0
    ({"name": "AUTOTEST_show0", "logo": "x.png", "sort": 1, "showStatus": 0},
     ("AUTOTEST_show0", "A", "x.png", 1, 0)),
     ({"name": "ZAUTOTEST_fl", "logo": "x.png", "sort": 1, "showStatus": 1},
     ("ZAUTOTEST_fl", "Z", "x.png", 1, 1)),
]
IDS = ["name len64", "firstLetter len8", "sort=0", "showStatus=0","firstLetter default from name"]


@pytest.mark.parametrize("body, expected_row", CASES, ids=IDS)
def test_create_valid(client, db_guard, body, expected_row):
    cur, max_before = db_guard

    resp = client.post("/brand/create", json=body)  # 【填空3:抄 invalid 用例里发请求那一行,json= 指向 body】
    assert resp.status_code == 200
    assert resp.json()["code"] == 200

    cur.execute(
        "SELECT name, first_letter, logo, sort, show_status "
        "FROM pms_brand WHERE id > %s", (max_before,))
    rows = cur.fetchall()
    assert len(rows) == 1
    assert rows[0] == expected_row