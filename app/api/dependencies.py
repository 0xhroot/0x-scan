from fastapi import Request, HTTPException, Header, Depends
from typing import Optional
import uuid
import time
import os


# ==========================================
# CONFIG ACCESS
# ==========================================

class AppConfig:
    """
    Central configuration object.
    Replace with .env loader later.
    """

    API_KEY = os.getenv("API_KEY", "dev-secret")
    RATE_LIMIT = int(os.getenv("RATE_LIMIT", "60"))  # requests per minute


config = AppConfig()


def get_config() -> AppConfig:
    return config


# ==========================================
# REQUEST ID (for tracing)
# ==========================================

async def get_request_id() -> str:
    return str(uuid.uuid4())


# ==========================================
# CLIENT IP DETECTION
# ==========================================

async def get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()

    return request.client.host


# ==========================================
# API KEY AUTH (optional)
# ==========================================

async def verify_api_key(
    x_api_key: Optional[str] = Header(None),
    cfg: AppConfig = Depends(get_config)
):
    """
    Enable this dependency to protect routes.
    """

    if not x_api_key:
        raise HTTPException(
            status_code=401,
            detail="API key required"
        )

    if x_api_key != cfg.API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API key"
        )

    return True


# ==========================================
# SIMPLE RATE LIMITER (per IP)
# ==========================================

REQUEST_LOG = {}


async def rate_limiter(
    client_ip: str = Depends(get_client_ip),
    cfg: AppConfig = Depends(get_config)
):
    """
    Memory-based rate limiter.
    Replace with Redis for production.
    """

    now = time.time()

    if client_ip not in REQUEST_LOG:
        REQUEST_LOG[client_ip] = []

    # Remove old timestamps (>60s)
    REQUEST_LOG[client_ip] = [
        t for t in REQUEST_LOG[client_ip]
        if now - t < 60
    ]

    if len(REQUEST_LOG[client_ip]) >= cfg.RATE_LIMIT:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded"
        )

    REQUEST_LOG[client_ip].append(now)


# ==========================================
# DATABASE SESSION (Placeholder)
# ==========================================

async def get_db():
    """
    Placeholder for DB session.
    Replace with SQLAlchemy session later.
    """
    db = None
    try:
        yield db
    finally:
        pass


# ==========================================
# REQUEST CONTEXT BUNDLE
# ==========================================

class RequestContext:
    def __init__(self, request_id: str, client_ip: str):
        self.request_id = request_id
        self.client_ip = client_ip


async def get_request_context(
    request_id: str = Depends(get_request_id),
    client_ip: str = Depends(get_client_ip)
) -> RequestContext:

    return RequestContext(
        request_id=request_id,
        client_ip=client_ip
    )
