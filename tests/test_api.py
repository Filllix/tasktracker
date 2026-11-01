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

def test_ready_when_db_up():
    r = client.get("/ready")
    assert r.status_code == 200
    assert r.json() == {"status": "ready"}


def test_ready_when_db_down(monkeypatch):
    monkeypatch.setattr(
        "app.main.DB_URL",
        "postgresql://x:y@127.0.0.1:1/z?connect_timeout=1",
    )
    r = client.get("/ready")
    assert r.status_code == 503