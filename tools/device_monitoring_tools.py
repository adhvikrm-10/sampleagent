import random
from datetime import datetime, timedelta

# Simulated device database
DEVICE_DATABASE = { ... }  # prepopulated dictionary

def get_device_info(device_id: str):
    # Return metadata for device or error if not found
    return DEVICE_DATABASE.get(device_id, {"status": "error", "message": "Device not found"})

def get_sensor_readings(device_id: str, sensor_type: str, hours: int = 1):
    # Simulate 5-min interval sensor data over specified hours
    readings = []
    now = datetime.utcnow()
    for i in range(hours*12):
        timestamp = now - timedelta(minutes=5*i)
        value = random.gauss(25, 2) if sensor_type == "temperature" else random.random()*100
        readings.append({"timestamp": timestamp.isoformat(), "value": round(value, 2), "unit": "Celsius"})
    return {"device_id": device_id, "sensor_type": sensor_type, "readings": list(reversed(readings))}

def analyze_device_health(device_id: str):
    # Simple heuristic combining uptime, firmware version, anomalies
    info = get_device_info(device_id)
    health_score = 100
    issues = []
    # logic to adjust score and issues
    return {"device_id": device_id, "health_score": health_score, "status": "healthy", "issues": issues}
