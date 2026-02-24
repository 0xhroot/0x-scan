import subprocess
import platform
from typing import Dict


def detect_os_from_ttl(ttl: int) -> str:
    if ttl >= 128:
        return "Windows (likely)"
    if ttl >= 64:
        return "Linux / Unix (likely)"
    if ttl >= 255:
        return "Network device (Cisco/Router)"
    return "Unknown"


def get_ttl(ip: str) -> int:
    try:
        if platform.system().lower() == "windows":
            cmd = ["ping", "-n", "1", ip]
        else:
            cmd = ["ping", "-c", "1", ip]

        output = subprocess.check_output(
            cmd,
            stderr=subprocess.DEVNULL
        ).decode()

        for part in output.split():
            if "ttl=" in part.lower():
                return int(part.split("=")[1])

    except Exception:
        pass

    return -1


def fingerprint_os(
    ip: str,
    open_ports=None,
    banners=None
) -> Dict:

    ttl = get_ttl(ip)
    os_guess = detect_os_from_ttl(ttl)

    hints = []

    if open_ports:
        if 3389 in open_ports:
            hints.append("RDP detected → Windows likely")

        if 22 in open_ports:
            hints.append("SSH detected → Linux/Unix likely")

        if 445 in open_ports:
            hints.append("SMB detected → Windows")

    if banners:
        for b in banners:
            text = b.lower()

            if "ubuntu" in text:
                hints.append("Ubuntu detected")

            if "debian" in text:
                hints.append("Debian detected")

            if "microsoft" in text:
                hints.append("Windows service detected")

    return {
        "ttl": ttl,
        "os_guess": os_guess,
        "hints": hints
    }
