import asyncio
from typing import Dict, List
from datetime import datetime

from app.scanner.target import Target
from app.scanner.scheduler import Scheduler
from app.scanner.rate_limiter import RateLimiter

# Simple TCP scan
COMMON_PORTS = [
    21, 22, 25, 53, 80, 110,
    143, 443, 3306, 8080
]

rate_limiter = RateLimiter(limit_per_minute=120)
scheduler = Scheduler(max_workers=10)


# ======================================
# Port Scan
# ======================================

async def scan_port(ip: str, port: int) -> bool:
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port),
            timeout=3
        )
        writer.close()
        await writer.wait_closed()
        return True
    except Exception:
        return False


async def port_scan(ip: str, ports: List[int]) -> List[int]:
    tasks = [scan_port(ip, p) for p in ports]
    results = await asyncio.gather(*tasks)
    return [p for p, open_ in zip(ports, results) if open_]


# ======================================
# HTTP Probe
# ======================================

async def http_probe(host: str) -> Dict:
    import aiohttp

    result = {}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"http://{host}",
                timeout=5
            ) as resp:

                result["status"] = resp.status
                result["headers"] = dict(resp.headers)

                text = await resp.text()

                if "<title>" in text:
                    start = text.find("<title>")
                    end = text.find("</title>")
                    result["title"] = text[start+7:end]

    except Exception:
        pass

    return result


# ======================================
# MAIN SCAN FUNCTION
# ======================================

async def run_scan(
    target_raw: str,
    full_scan: bool = True,
    ports_mode: str = "common"
) -> Dict:

    # Rate limit per target
    if not rate_limiter.allow(target_raw):
        return {
            "error": "Rate limit exceeded"
        }

    target = Target(target_raw)

    resolved = target.resolve()
    ip = resolved["ip"]
    hostname = resolved["hostname"]

    # Choose port set
    if ports_mode == "common":
        ports = COMMON_PORTS
    else:
        ports = COMMON_PORTS

    open_ports = await port_scan(ip, ports)

    http_data = {}
    if 80 in open_ports or 8080 in open_ports:
        http_data = await http_probe(hostname or ip)

    result = {
        "target": target_raw,
        "resolved_ip": ip,
        "hostname": hostname,
        "timestamp": datetime.utcnow().isoformat(),
        "open_ports": open_ports,
        "http": http_data
    }

    return result


# ======================================
# BACKGROUND EXECUTION
# ======================================

async def background_scan(
    target: str,
    full_scan: bool,
    ports: str
):
    result = await run_scan(target, full_scan, ports)

    print("\n=== SCAN RESULT ===")
    print(result)

