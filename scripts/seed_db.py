# scripts/seed_db.py

import asyncio

from app.database.session import AsyncSessionLocal
from app.database.crud.targets import create_target
from app.database.crud.scans import create_scan


SAMPLE_TARGETS = [
    ("example.com", "Demo site", ["prod", "web"]),
    ("testphp.vulnweb.com", "Test target", ["lab"]),
    ("scanme.nmap.org", "Public scan test", ["public"])
]


async def seed():

    print("🌱 Seeding database...")

    async with AsyncSessionLocal() as db:

        for target, desc, tags in SAMPLE_TARGETS:

            t = await create_target(
                db=db,
                target=target,
                description=desc,
                tags=tags
            )

            await create_scan(
                db=db,
                target_id=t.id
            )

            print(f"Added target: {target}")

    print("✅ Database seeded successfully")


if __name__ == "__main__":
    asyncio.run(seed())
