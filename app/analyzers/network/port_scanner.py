import asyncio
from typing import List, Dict


DEFAULT_TIMEOUT = 3
DEFAULT_CONCURRENCY = 500


async def scan_port(ip: str, port: int, timeout: int = DEFAULT_TIMEOUT) -> Dict:
    result = {
        "port": port,
        "open": False,
        "banner": None
    }

    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port),
            timeout=timeout
        )

        result["open"] = True

        # Try banner grabbing
        try:
            writer.write(b"\r\n")
            await writer.drain()

            data = await asyncio.wait_for(
                reader.read(1024),
                timeout=1
            )

            if data:
                result["banner"] = data.decode(
                    errors="ignore"
                ).strip()

        except Exception:
            pass

        writer.close()
        await writer.wait_closed()

    except Exception:
        pass

    return result


async def scan_ports(
    ip: str,
    ports: List[int],
    concurrency: int = DEFAULT_CONCURRENCY
) -> List[Dict]:

    semaphore = asyncio.Semaphore(concurrency)

    async def sem_scan(port):
        async with semaphore:
            return await scan_port(ip, port)

    tasks = [sem_scan(p) for p in ports]
    results = await asyncio.gather(*tasks)

    return [r for r in results if r["open"]]
