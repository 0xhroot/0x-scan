from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
import re


router = APIRouter(prefix="/targets", tags=["Targets"])


# =====================================
# In-Memory Storage (replace with DB later)
# =====================================

TARGET_STORE = {}


# =====================================
# Validation Regex
# =====================================

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


# =====================================
# Models
# =====================================

class TargetCreate(BaseModel):
    target: str = Field(..., example="example.com")
    description: Optional[str] = None
    tags: Optional[List[str]] = []


class TargetResponse(BaseModel):
    id: str
    target: str
    description: Optional[str]
    tags: List[str]


# =====================================
# Add New Target
# =====================================

@router.post("/", response_model=TargetResponse)
async def add_target(data: TargetCreate):

    target = data.target.strip().lower()

    if not validate_target(target):
        raise HTTPException(
            status_code=400,
            detail="Invalid domain or IP address"
        )

    # Prevent duplicates
    for t in TARGET_STORE.values():
        if t["target"] == target:
            raise HTTPException(
                status_code=409,
                detail="Target already exists"
            )

    target_id = str(uuid.uuid4())

    TARGET_STORE[target_id] = {
        "id": target_id,
        "target": target,
        "description": data.description,
        "tags": data.tags or []
    }

    return TARGET_STORE[target_id]


# =====================================
# List All Targets
# =====================================

@router.get("/", response_model=List[TargetResponse])
async def list_targets():
    return list(TARGET_STORE.values())


# =====================================
# Get Single Target
# =====================================

@router.get("/{target_id}", response_model=TargetResponse)
async def get_target(target_id: str):

    target = TARGET_STORE.get(target_id)

    if not target:
        raise HTTPException(
            status_code=404,
            detail="Target not found"
        )

    return target


# =====================================
# Delete Target
# =====================================

@router.delete("/{target_id}")
async def delete_target(target_id: str):

    if target_id not in TARGET_STORE:
        raise HTTPException(
            status_code=404,
            detail="Target not found"
        )

    deleted = TARGET_STORE.pop(target_id)

    return {
        "status": "deleted",
        "target": deleted["target"],
        "id": target_id
    }
