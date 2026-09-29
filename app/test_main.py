from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Microservice is online and operational."}

def test_health_check():
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "uptime_seconds" in data
    assert "memory_usage_percent" in data

def test_get_devices():
    response = client.get("/api/v1/devices")
    assert response.status_code == 200
    assert response.json()["count"] >= 2

def test_get_device_valid():
    response = client.get("/api/v1/devices/dev-101")
    assert response.status_code == 200
    assert response.json()["name"] == "Core-Gateway-01"

def test_get_device_not_found():
    response = client.get("/api/v1/devices/dev-999")
    assert response.status_code == 404