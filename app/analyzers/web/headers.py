import aiohttp
from typing import Dict


SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]


async def analyze_headers(url: str) -> Dict:

    result = {
        "server": None,
        "security_headers": {},
        "missing_security_headers": [],
        "all_headers": {}
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as resp:

                headers = dict(resp.headers)
                result["all_headers"] = headers
                result["server"] = headers.get("Server")

                for h in SECURITY_HEADERS:
                    if h in headers:
                        result["security_headers"][h] = headers[h]
                    else:
                        result["missing_security_headers"].append(h)

    except Exception:
        pass

    return result
