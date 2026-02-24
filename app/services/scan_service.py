from app.database.session import AsyncSessionLocal
from app.database.crud.targets import get_target
from app.database.crud.scans import create_scan, get_scan
from app.database.crud.results import list_results_by_scan
from app.scanner.engine import run_scan


class ScanService:

    # ---------------------------
    # Schedule scan via DB worker
    # ---------------------------
    async def schedule_scan(self, target_id: str):

        async with AsyncSessionLocal() as db:
            target = await get_target(db, target_id)

            if not target:
                raise ValueError("Target not found")

            scan = await create_scan(
                db=db,
                target_id=target_id
            )

            return {
                "scan_id": scan.id,
                "status": scan.status
            }

    # ---------------------------
    # Run scan immediately
    # ---------------------------
    async def run_immediate_scan(self, target: str):

        result = await run_scan(target)

        return {
            "status": "completed",
            "result": result
        }

    # ---------------------------
    # Get scan status
    # ---------------------------
    async def get_scan_status(self, scan_id: str):

        async with AsyncSessionLocal() as db:
            scan = await get_scan(db, scan_id)

            if not scan:
                raise ValueError("Scan not found")

            return {
                "scan_id": scan.id,
                "status": scan.status
            }

    # ---------------------------
    # Get scan results
    # ---------------------------
    async def get_scan_results(self, scan_id: str):

        async with AsyncSessionLocal() as db:
            results = await list_results_by_scan(db, scan_id)

            return [
                {
                    "result_id": r.id,
                    "data": r.data,
                    "severity": r.severity,
                    "created_at": r.created_at
                }
                for r in results
            ]
