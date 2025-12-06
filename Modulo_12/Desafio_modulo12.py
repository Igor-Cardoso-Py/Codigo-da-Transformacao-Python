import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_soma(client):
    response = client.get("/soma?a=3&b=2")
    assert response.status_code == 200
    assert response.json["resultado"] == 5

def test_dividir(client):
    response = client.get("/dividir?a=10&b=2")
    assert response.status_code == 200
    assert response.json["resultado"] == 5

def test_divisao_por_zero(client):
    response = client.get("/dividir?a=10&b=0")
    assert response.status_code == 400
    assert response.json["erro"] == "Divisão por zero"