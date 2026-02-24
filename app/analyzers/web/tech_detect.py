import aiohttp
from typing import Dict


TECH_SIGNATURES = {
    "wordpress": "wp-content",
    "drupal": "drupal-settings-json",
    "laravel": "laravel_session",
    "react": "react",
    "vue": "vue"
}


async def detect_technologies(url: str) -> Dict:

    detected = []

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as resp:

                text = await resp.text(errors="ignore")
                headers = str(resp.headers).lower()

                for tech, sig in TECH_SIGNATURES.items():
                    if sig in text.lower() or sig in headers:
                        detected.append(tech)

    except Exception:
        pass

    return {
        "detected": detected
    }
