from app.database.session import AsyncSessionLocal
from app.database.crud.results import list_results_by_scan


class ReportService:

    # ---------------------------
    # Generate summary report
    # ---------------------------
    async def generate_scan_report(self, scan_id: str):

        async with AsyncSessionLocal() as db:
            results = await list_results_by_scan(db, scan_id)

            total = len(results)
            severity_count = {}

            for r in results:
                sev = r.severity or "info"
                severity_count[sev] = severity_count.get(sev, 0) + 1

            return {
                "scan_id": scan_id,
                "total_findings": total,
                "severity_breakdown": severity_count,
                "results": [
                    {
                        "id": r.id,
                        "data": r.data,
                        "severity": r.severity
                    }
                    for r in results
                ]
            }

    # ---------------------------
    # Risk score calculation
    # ---------------------------
    async def calculate_risk_score(self, scan_id: str):

        async with AsyncSessionLocal() as db:
            results = await list_results_by_scan(db, scan_id)

            score = 0

            severity_weights = {
                "critical": 10,
                "high": 7,
                "medium": 4,
                "low": 2,
                "info": 1
            }

            for r in results:
                score += severity_weights.get(r.severity, 1)

            return {
                "scan_id": scan_id,
                "risk_score": score
            }
