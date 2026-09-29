import os
import time
from fastapi import FastAPI, HTTPException, status
import psutil

app = FastAPI(
    title="Device Provisioning Microservice",
    version="1.0.0",
    description="Lightweight microservice for network & IoT service telemetry."
)

START_TIME = time.time()

DEVICES_DB = {
    "dev-101": {"name": "Core-Gateway-01", "ip": "192.168.1.1", "status": "active"},
    "dev-102": {"name": "Edge-Switch-04", "ip": "192.168.1.254", "status": "maintenance"}
}

@app.get("/", tags=["Root"])
def root():
    return {"message": "Microservice is online and operational."}

@app.get("/healthz", status_code=status.HTTP_200_OK, tags=["Monitoring"])
def health_check():
    """Liveness probe used by Docker and orchestrators for zero-downtime updates."""
    uptime = time.time() - START_TIME
    memory_usage = psutil.virtual_memory().percent
    
    if memory_usage > 95.0:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE, 
            detail="High memory pressure"
        )

    return {
        "status": "healthy",
        "uptime_seconds": round(uptime, 2),
        "memory_usage_percent": memory_usage,
        "environment": os.getenv("APP_ENV", "production")
    }

@app.get("/api/v1/devices", tags=["Devices"])
def list_devices():
    return {"count": len(DEVICES_DB), "data": list(DEVICES_DB.values())}

@app.get("/api/v1/devices/{device_id}", tags=["Devices"])
def get_device(device_id: str):
    if device_id not in DEVICES_DB:
        raise HTTPException(status_code=404, detail="Device not found")
    return DEVICES_DB[device_id]