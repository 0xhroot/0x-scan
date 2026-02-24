import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import asyncio

from app.database.session import engine, Base

# 🔥 IMPORTANT — import models so SQLAlchemy registers tables
from app.database import models


async def init():
    print("📦 Creating database tables...")

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✅ Tables created successfully")


if __name__ == "__main__":
    asyncio.run(init())
