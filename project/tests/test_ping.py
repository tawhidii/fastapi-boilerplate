from app import main

def test_ping(test_app):
    res = test_app.get("/ping")
    assert res.status_code == 200
    assert res.json() == {"environment": "dev","testing": True,"ping": "pong!"}
    