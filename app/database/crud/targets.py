from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database.models import Target


async def create_target(
    db: AsyncSession,
    target: str,
    description=None,
    tags=None
):
    obj = Target(
        target=target,
        description=description,
        tags=tags or []
    )

    db.add(obj)
    await db.commit()
    await db.refresh(obj)

    return obj


async def get_target(db: AsyncSession, target_id: str):
    result = await db.execute(
        select(Target).where(Target.id == target_id)
    )
    return result.scalar_one_or_none()


async def list_targets(db: AsyncSession):
    result = await db.execute(select(Target))
    return result.scalars().all()


async def delete_target(db: AsyncSession, target_id: str):
    target = await get_target(db, target_id)

    if target:
        await db.delete(target)
        await db.commit()

    return target
