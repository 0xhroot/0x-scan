import asyncio

from app.database.session import AsyncSessionLocal
from app.database.crud.scans import list_scans, update_scan_status
from app.database.crud.results import create_result
from app.database.models import Scan, Target

from sqlalchemy import select

from app.scanner.engine import run_scan


POLL_INTERVAL = 5  # seconds


async def process_scan(db, scan: Scan):

    # Fetch associated target
    result = await db.execute(
        select(Target).where(Target.id == scan.target_id)
    )
    target = result.scalar_one_or_none()

    if not target:
        await update_scan_status(db, scan.id, "failed")
        return

    await update_scan_status(db, scan.id, "running")

    try:
        scan_data = await run_scan(target.target)

        await create_result(
            db=db,
            scan_id=scan.id,
            data=scan_data,
            severity="info"
        )

        await update_scan_status(db, scan.id, "completed")

    except Exception as e:
        await update_scan_status(db, scan.id, "failed")
        print(f"Scan failed: {e}")


async def scan_worker():

    print("🛰️ Scan worker started")

    while True:
        async with AsyncSessionLocal() as db:

            scans = await list_scans(db)

            pending_scans = [
                s for s in scans if s.status == "pending"
            ]

            for scan in pending_scans:
                await process_scan(db, scan)

        await asyncio.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    asyncio.run(scan_worker())
