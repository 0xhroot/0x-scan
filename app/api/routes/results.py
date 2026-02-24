from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
import uuid
from datetime import datetime


router = APIRouter(prefix="/results", tags=["Results"])


# =====================================
# In-Memory Result Store (Replace with DB later)
# =====================================

RESULT_STORE = {}


# =====================================
# Helper — Create Result (used by scanner later)
# =====================================

def store_result(target: str, data: dict) -> str:
    result_id = str(uuid.uuid4())

    RESULT_STORE[result_id] = {
        "id": result_id,
        "target": target,
        "data": data,
        "created_at": datetime.utcnow().isoformat()
    }

    return result_id


# =====================================
# List All Results
# =====================================

@router.get("/", response_model=List[dict])
async def list_results(
    target: Optional[str] = Query(None, description="Filter by target")
):

    if target:
        return [
            r for r in RESULT_STORE.values()
            if r["target"] == target.lower()
        ]

    return list(RESULT_STORE.values())


# =====================================
# Get Single Result
# =====================================

@router.get("/{result_id}")
async def get_result(result_id: str):

    result = RESULT_STORE.get(result_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Result not found"
        )

    return result


# =====================================
# Delete Result
# =====================================

@router.delete("/{result_id}")
async def delete_result(result_id: str):

    if result_id not in RESULT_STORE:
        raise HTTPException(
            status_code=404,
            detail="Result not found"
        )

    deleted = RESULT_STORE.pop(result_id)

    return {
        "status": "deleted",
        "id": result_id,
        "target": deleted["target"]
    }
