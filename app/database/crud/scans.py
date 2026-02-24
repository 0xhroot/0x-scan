from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.models import Scan


async def create_scan(
    db: AsyncSession,
    target_id: str
):
    scan = Scan(target_id=target_id)

    db.add(scan)
    await db.commit()
    await db.refresh(scan)

    return scan


async def get_scan(db: AsyncSession, scan_id: str):
    result = await db.execute(
        select(Scan).where(Scan.id == scan_id)
    )
    return result.scalar_one_or_none()


async def update_scan_status(
    db: AsyncSession,
    scan_id: str,
    status: str
):
    scan = await get_scan(db, scan_id)

    if scan:
        scan.status = status
        await db.commit()

    return scan


async def list_scans(db: AsyncSession):
    result = await db.execute(select(Scan))
    return result.scalars().all()
