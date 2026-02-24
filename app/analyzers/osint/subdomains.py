import socket
from typing import List


COMMON_SUBDOMAINS = [
    "www", "mail", "api", "dev", "test",
    "staging", "admin", "portal", "beta",
    "blog", "shop", "m", "cdn", "static",
    "secure", "vpn", "app"
]


def resolve_subdomain(sub: str, domain: str):
    fqdn = f"{sub}.{domain}"

    try:
        ip = socket.gethostbyname(fqdn)
        return {"subdomain": fqdn, "ip": ip}
    except Exception:
        return None


def discover_subdomains(domain: str) -> List[dict]:

    found = []

    for sub in COMMON_SUBDOMAINS:
        result = resolve_subdomain(sub, domain)
        if result:
            found.append(result)

    return found
