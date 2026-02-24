# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.logging import setup_logging

# API routes
from app.api.routes import (
    scan,
    targets,
    results,
    system
)

from app.database.session import engine, Base


# =============================
# App Setup
# =============================

settings = get_settings()

setup_logging("INFO")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="0x-Scan Recon Platform API"
)


# =============================
# CORS (for Web UI)
# =============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =============================
# Register Routes
# =============================

app.include_router(scan.router)
app.include_router(targets.router)
app.include_router(results.router)
app.include_router(system.router)


# =============================
# Root Endpoint
# =============================

@app.get("/")
async def root():
    return {
        "name": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running"
    }


# =============================
# Startup Event
# =============================

@app.on_event("startup")
async def startup_event():
    print("🚀 0x-Scan API starting...")

    # Create tables automatically
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✅ Database ready")


# =============================
# Shutdown Event
# =============================

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 0x-Scan API shutting down...")
