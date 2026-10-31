import sys
sys.path.insert(0, "backend")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "healthy"}
