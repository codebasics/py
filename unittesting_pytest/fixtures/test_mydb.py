from fixtures.mydb import MyDB

import pytest

@pytest.fixture(scope="module")
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("closing DB")

def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789
