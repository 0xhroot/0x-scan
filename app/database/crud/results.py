from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.models import Result


async def create_result(
    db: AsyncSession,
    scan_id: str,
    data: dict,
    severity: str = "info"
):
    result = Result(
        scan_id=scan_id,
        data=data,
        severity=severity
    )

    db.add(result)
    await db.commit()
    await db.refresh(result)

    return result


async def get_result(db: AsyncSession, result_id: str):
    res = await db.execute(
        select(Result).where(Result.id == result_id)
    )
    return res.scalar_one_or_none()


async def list_results(db: AsyncSession):
    res = await db.execute(select(Result))
    return res.scalars().all()


async def list_results_by_scan(
    db: AsyncSession,
    scan_id: str
):
    res = await db.execute(
        select(Result).where(Result.scan_id == scan_id)
    )
    return res.scalars().all()
