from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World !!!"}

def test_read_test():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "cool !"}

def test_read_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Beeee freeeeeeeeeeeee !"}
