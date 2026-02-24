from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Optional
import re

# Scanner engine import (will implement later)
from app.scanner.engine import run_scan


router = APIRouter(prefix="/scan", tags=["Scanning"])


# ================================
# Request / Response Models
# ================================

class ScanRequest(BaseModel):
    target: str = Field(..., example="example.com")
    full_scan: Optional[bool] = Field(default=True)
    ports: Optional[str] = Field(
        default="common",
        description="common | top100 | full | custom list (e.g., 80,443,8080)"
    )


class ScanResponse(BaseModel):
    status: str
    target: str
    message: str


# ================================
# Utility — Target Validation
# ================================

DOMAIN_REGEX = re.compile(
    r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
)

IP_REGEX = re.compile(
    r"^(?:\d{1,3}\.){3}\d{1,3}$"
)


def validate_target(target: str) -> bool:
    if DOMAIN_REGEX.match(target):
        return True
    if IP_REGEX.match(target):
        return True
    return False


# ================================
# Start Scan Endpoint
# ================================

@router.post("/start", response_model=ScanResponse)
async def start_scan(
    req: ScanRequest,
    background_tasks: BackgroundTasks
):

    target = req.target.strip().lower()

    # Validate target
    if not validate_target(target):
        raise HTTPException(
            status_code=400,
            detail="Invalid target. Provide valid domain or IP."
        )

    # Launch scan in background
    background_tasks.add_task(
        run_scan,
        target,
        req.full_scan,
        req.ports
    )

    return ScanResponse(
        status="accepted",
        target=target,
        message="Scan started in background"
    )


# ================================
# Quick Scan Endpoint
# ================================

@router.post("/quick")
async def quick_scan(req: ScanRequest):
    """
    Runs scan synchronously (for testing / small scans)
    """

    target = req.target.strip().lower()

    if not validate_target(target):
        raise HTTPException(
            status_code=400,
            detail="Invalid target"
        )

    result = await run_scan(
        target,
        req.full_scan,
        req.ports
    )

    return {
        "status": "completed",
        "target": target,
        "result": result
    }
