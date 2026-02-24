import asyncio
import socket
from typing import List, Dict


async def udp_probe(ip: str, port: int, timeout: int = 2) -> Dict:
    result = {
        "port": port,
        "open_or_filtered": False,
        "response": None
    }

    loop = asyncio.get_event_loop()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setblocking(False)

        message = b"\x00"

        await loop.sock_sendto(sock, message, (ip, port))

        try:
            data, _ = await asyncio.wait_for(
                loop.sock_recvfrom(sock, 1024),
                timeout
            )

            result["open_or_filtered"] = True
            result["response"] = data.hex()

        except asyncio.TimeoutError:
            # No response — could still be open
            result["open_or_filtered"] = True

    except Exception:
        pass
    finally:
        sock.close()

    return result


async def scan_udp_ports(
    ip: str,
    ports: List[int]
) -> List[Dict]:

    tasks = [udp_probe(ip, p) for p in ports]
    results = await asyncio.gather(*tasks)

    return [r for r in results if r["open_or_filtered"]]
