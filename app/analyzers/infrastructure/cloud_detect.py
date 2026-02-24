import socket
from typing import Dict


CLOUD_PATTERNS = {
    "aws": ["amazonaws.com", "compute.amazonaws"],
    "gcp": ["googleusercontent.com"],
    "azure": ["cloudapp.azure.com"],
    "digitalocean": ["digitalocean.com"],
    "linode": ["linode.com"],
    "vultr": ["vultr.com"],
    "ovh": ["ovh.net"]
}


def detect_cloud(host: str) -> Dict:

    result = {
        "detected": False,
        "provider": None,
        "evidence": []
    }

    try:
        ip = socket.gethostbyname(host)

        try:
            reverse = socket.gethostbyaddr(ip)[0].lower()
        except Exception:
            reverse = ""

        for provider, patterns in CLOUD_PATTERNS.items():
            for p in patterns:
                if p in reverse:
                    result["detected"] = True
                    result["provider"] = provider
                    result["evidence"].append(
                        f"Reverse DNS contains '{p}'"
                    )
                    return result

    except Exception:
        pass

    return result
