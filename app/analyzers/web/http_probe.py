import aiohttp
import asyncio
import time
from typing import Dict


async def probe_url(url: str, timeout: int = 5) -> Dict:

    result = {
        "url": url,
        "status": None,
        "title": None,
        "server": None,
        "content_type": None,
        "redirected": False,
        "final_url": None,
        "response_time_ms": None
    }

    start = time.time()

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url,
                timeout=timeout,
                allow_redirects=True
            ) as resp:

                result["status"] = resp.status
                result["server"] = resp.headers.get("Server")
                result["content_type"] = resp.headers.get("Content-Type")
                result["final_url"] = str(resp.url)
                result["redirected"] = str(resp.url) != url

                text = await resp.text(errors="ignore")

                if "<title>" in text.lower():
                    s = text.lower().find("<title>")
                    e = text.lower().find("</title>")
                    result["title"] = text[s+7:e].strip()

    except Exception:
        pass

    result["response_time_ms"] = int((time.time() - start) * 1000)

    return result


async def probe_host(host: str) -> Dict:

    http = await probe_url(f"http://{host}")
    https = await probe_url(f"https://{host}")

    return {
        "http": http,
        "https": https
    }
