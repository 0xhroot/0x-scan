import re
import asyncio
from datetime import datetime
from typing import List


# ==================================
# DOMAIN / IP VALIDATION
# ==================================

DOMAIN_REGEX = re.compile(
    r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
)

IP_REGEX = re.compile(
    r"^(?:\d{1,3}\.){3}\d{1,3}$"
)


def is_domain(value: str) -> bool:
    return bool(DOMAIN_REGEX.match(value))


def is_ip(value: str) -> bool:
    return bool(IP_REGEX.match(value))


def is_valid_target(value: str) -> bool:
    return is_domain(value) or is_ip(value)


# ==================================
# URL NORMALIZATION
# ==================================

def normalize_target(target: str) -> str:
    return target.strip().lower()


# ==================================
# TIME HELPERS
# ==================================

def now_iso() -> str:
    return datetime.utcnow().isoformat()


# ==================================
# ASYNC HELPERS
# ==================================

async def gather_limited(
    tasks: List,
    limit: int
):
    """
    Run async tasks with concurrency limit.
    """

    semaphore = asyncio.Semaphore(limit)

    async def sem_task(task):
        async with semaphore:
            return await task

    return await asyncio.gather(
        *(sem_task(t) for t in tasks)
    )


# ==================================
# CHUNKING
# ==================================

def chunk_list(data: List, size: int):
    for i in range(0, len(data), size):
        yield data[i:i + size]


# ==================================
# SAFE INT
# ==================================

def safe_int(value, default=0):
    try:
        return int(value)
    except Exception:
        return default
