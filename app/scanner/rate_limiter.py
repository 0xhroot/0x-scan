import time
from collections import defaultdict


class RateLimiter:
    def __init__(self, limit_per_minute: int = 60):
        self.limit = limit_per_minute
        self.requests = defaultdict(list)

    def allow(self, key: str) -> bool:
        now = time.time()

        timestamps = self.requests[key]

        # Remove entries older than 60 sec
        self.requests[key] = [
            t for t in timestamps if now - t < 60
        ]

        if len(self.requests[key]) >= self.limit:
            return False

        self.requests[key].append(now)
        return True
