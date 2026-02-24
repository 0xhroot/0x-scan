import asyncio
from datetime import datetime, timedelta

from app.database.session import AsyncSessionLocal
from app.database.crud.targets import list_targets
from app.database.crud.scans import create_scan


MONITOR_INTERVAL = 3600  # seconds (1 hour)


last_run = {}


async def monitor_targets():

    print("🔁 Monitor worker started")

    while True:
        async with AsyncSessionLocal() as db:

            targets = await list_targets(db)

            for t in targets:

                last = last_run.get(t.id)

                if last and datetime.utcnow() - last < timedelta(seconds=MONITOR_INTERVAL):
                    continue

                print(f"Scheduling monitoring scan for {t.target}")

                await create_scan(
                    db=db,
                    target_id=t.id
                )

                last_run[t.id] = datetime.utcnow()

        await asyncio.sleep(60)  # check every minute


if __name__ == "__main__":
    asyncio.run(monitor_targets())
