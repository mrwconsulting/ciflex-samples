from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    resp = client.get('/')
    assert resp.status_code == 200
