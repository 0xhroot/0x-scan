# scripts/run_worker.py

import asyncio

from app.workers.scan_worker import scan_worker
from app.workers.monitor_worker import monitor_targets


async def main():

    print("🚀 Starting background workers...")

    await asyncio.gather(
        scan_worker(),
        monitor_targets()
    )


if __name__ == "__main__":
    asyncio.run(main())
