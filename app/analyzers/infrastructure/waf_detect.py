import aiohttp
from typing import Dict


WAF_SIGNATURES = {
    "cloudflare": ["cf-ray", "cloudflare"],
    "aws_waf": ["aws", "awselb"],
    "akamai": ["akamai"],
    "imperva": ["imperva", "incapsula"],
    "f5_big_ip": ["bigip", "f5"],
    "sucuri": ["sucuri"]
}


async def detect_waf(host: str) -> Dict:

    result = {
        "detected": False,
        "provider": None,
        "evidence": []
    }

    test_url = f"https://{host}/?test_waf=1"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(test_url, timeout=5) as resp:

                headers = str(resp.headers).lower()

                for provider, sigs in WAF_SIGNATURES.items():
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
