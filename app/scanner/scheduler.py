import asyncio
from typing import Callable, Any


class Scheduler:
    def __init__(self, max_workers: int = 5):
        self.queue = asyncio.Queue()
        self.max_workers = max_workers
        self.workers = []

    async def worker(self):
        while True:
            func, args = await self.queue.get()

            try:
                await func(*args)
            except Exception as e:
                print(f"Worker error: {e}")

            self.queue.task_done()

    async def start(self):
        for _ in range(self.max_workers):
            task = asyncio.create_task(self.worker())
            self.workers.append(task)

    async def schedule(self, func: Callable, *args: Any):
        await self.queue.put((func, args))

    async def wait(self):
        await self.queue.join()
