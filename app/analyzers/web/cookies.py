import aiohttp
from typing import List, Dict


async def analyze_cookies(url: str) -> List[Dict]:

    cookies_info = []

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as resp:

                for name, cookie in resp.cookies.items():

                    cookies_info.append({
                        "name": name,
                        "value": cookie.value,
                        "secure": cookie["secure"],
                        "httponly": cookie["httponly"],
                        "samesite": cookie.get("samesite"),
                        "expires": cookie.get("expires")
                    })

    except Exception:
        pass

    return cookies_info
