import socket
import re
from typing import Dict


DOMAIN_REGEX = re.compile(
    r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
)

IP_REGEX = re.compile(
    r"^(?:\d{1,3}\.){3}\d{1,3}$"
)


class Target:
    def __init__(self, raw: str):
        self.raw = raw.strip().lower()
        self.ip = None
        self.hostname = None

    def validate(self) -> bool:
        return bool(
            DOMAIN_REGEX.match(self.raw)
            or IP_REGEX.match(self.raw)
        )

    def resolve(self) -> Dict:
        if not self.validate():
            raise ValueError("Invalid target")

        if IP_REGEX.match(self.raw):
            self.ip = self.raw
            try:
                self.hostname = socket.gethostbyaddr(self.raw)[0]
            except Exception:
                self.hostname = None
        else:
            self.hostname = self.raw
            self.ip = socket.gethostbyname(self.raw)

        return {
            "raw": self.raw,
            "ip": self.ip,
            "hostname": self.hostname
        }
