import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from app import app, add, subtract


def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_add_api():
    client = app.test_client()

    response = client.get("/add?a=10&b=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == 15


def test_subtract_api():
    client = app.test_client()

    response = client.get("/subtract?a=10&b=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["result"] == 5
