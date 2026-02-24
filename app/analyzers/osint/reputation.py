import socket
from typing import Dict


PRIVATE_RANGES = [
    ("10.", "Private network"),
    ("192.168.", "Private network"),
    ("172.16.", "Private network"),
    ("172.17.", "Private network"),
    ("127.", "Loopback")
]


def check_private_ip(ip: str):
    for prefix, label in PRIVATE_RANGES:
        if ip.startswith(prefix):
            return label
    return None


def check_exposed_services(open_ports):
    risky_ports = {
        21: "FTP",
        23: "Telnet",
        445: "SMB",
        3389: "RDP",
        3306: "MySQL",
        6379: "Redis",
        27017: "MongoDB"
    }

    exposed = []

    for p in open_ports or []:
        if p in risky_ports:
            exposed.append(risky_ports[p])

    return exposed


def assess_reputation(
    host: str,
    open_ports=None
) -> Dict:

    result = {
        "ip": None,
        "private_network": False,
        "risk_level": "unknown",
        "exposed_services": []
    }

    try:
        ip = socket.gethostbyname(host)
        result["ip"] = ip

        private = check_private_ip(ip)
        if private:
            result["private_network"] = True
            result["risk_level"] = "internal"
            return result

        exposed = check_exposed_services(open_ports)
        result["exposed_services"] = exposed

        if exposed:
            result["risk_level"] = "medium"
        else:
            result["risk_level"] = "low"

    except Exception:
        pass

    return result
