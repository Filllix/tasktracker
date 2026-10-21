from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_visits_increments():
    first = client.get("/visits").json()["visits"]
    second = client.get("/visits").json()["visits"]
    assert second == first + 1