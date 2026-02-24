import aiohttp
import socket
from typing import Dict


CDN_SIGNATURES = {
    "cloudflare": ["cloudflare", "cf-ray"],
    "akamai": ["akamai", "akamaighost"],
    "fastly": ["fastly"],
    "amazon_cloudfront": ["cloudfront"],
    "google_cloud_cdn": ["google"],
    "azure_cdn": ["azureedge"]
}


async def detect_cdn(host: str) -> Dict:

    result = {
        "detected": False,
        "provider": None,
        "evidence": []
    }

    # --- Check DNS ---
    try:
        ip = socket.gethostbyname(host)

        if ip.startswith("104.") or ip.startswith("172."):
            result["evidence"].append("IP range suggests CDN")

    except Exception:
        pass

    # --- Check HTTP headers ---
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://{host}",
                timeout=5
            ) as resp:

                headers = str(resp.headers).lower()

                for provider, sigs in CDN_SIGNATURES.items():
                    for sig in sigs:
                        if sig in headers:
                            result["detected"] = True
                            result["provider"] = provider
                            result["evidence"].append(
                                f"Header contains '{sig}'"
                            )
                            return result

    except Exception:
        pass

    return result
