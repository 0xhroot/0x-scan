import asyncio
import json
import aiohttp


class NotificationService:

    # ---------------------------
    # Console notification
    # ---------------------------
    async def notify_console(self, message: str):

        print(f"[ALERT] {message}")

    # ---------------------------
    # Webhook notification
    # ---------------------------
    async def notify_webhook(self, url: str, payload: dict):

        try:
            async with aiohttp.ClientSession() as session:
                await session.post(
                    url,
                    json=payload,
                    timeout=5
                )
        except Exception as e:
            print(f"Webhook failed: {e}")

    # ---------------------------
    # Notify scan completion
    # ---------------------------
    async def scan_completed(self, scan_id: str):

        message = f"Scan {scan_id} completed"

        await self.notify_console(message)

    # ---------------------------
    # Notify high-risk finding
    # ---------------------------
    async def high_risk_alert(self, scan_id: str, details: dict):

        message = f"High risk finding in scan {scan_id}: {details}"

        await self.notify_console(message)
