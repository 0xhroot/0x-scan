from fastapi import APIRouter
import platform
import psutil
from datetime import datetime


router = APIRouter(prefix="/system", tags=["System"])


# =====================================
# Health Check
# =====================================

@router.get("/health")
async def health():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }


# =====================================
# System Info
# =====================================

@router.get("/info")
async def system_info():
    return {
        "platform": platform.system(),
        "platform_release": platform.release(),
        "architecture": platform.machine(),
        "python_version": platform.python_version(),
        "hostname": platform.node()
    }


# =====================================
# Resource Usage
# =====================================

@router.get("/resources")
async def resources():

    memory = psutil.virtual_memory()
    cpu = psutil.cpu_percent(interval=0.5)
    disk = psutil.disk_usage("/")

    return {
        "cpu_percent": cpu,
        "memory": {
            "total": memory.total,
            "available": memory.available,
            "used": memory.used,
            "percent": memory.percent
        },
        "disk": {
            "total": disk.total,
            "used": disk.used,
            "free": disk.free,
            "percent": disk.percent
        }
    }


# =====================================
# Uptime (Process Level)
# =====================================

START_TIME = datetime.utcnow()

@router.get("/uptime")
async def uptime():

    delta = datetime.utcnow() - START_TIME

    return {
        "uptime_seconds": int(delta.total_seconds()),
        "started_at": START_TIME.isoformat()
    }
