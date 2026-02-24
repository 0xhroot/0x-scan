import ssl
import socket
from datetime import datetime
from typing import Dict


def analyze_tls(host: str, port: int = 443) -> Dict:

    result = {
        "supported": False,
        "subject": None,
        "issuer": None,
        "expires": None,
        "days_remaining": None,
        "tls_version": None,
        "cipher": None
    }

    try:
        ctx = ssl.create_default_context()

        with ctx.wrap_socket(
            socket.socket(),
            server_hostname=host
        ) as s:

            s.settimeout(5)
            s.connect((host, port))

            cert = s.getpeercert()

            result["supported"] = True
            result["tls_version"] = s.version()
            result["cipher"] = s.cipher()[0]

            if cert:

                subject = dict(x[0] for x in cert["subject"])
                issuer = dict(x[0] for x in cert["issuer"])

                result["subject"] = subject.get("commonName")
                result["issuer"] = issuer.get("commonName")

                expires = cert["notAfter"]
                expiry_date = datetime.strptime(
                    expires,
                    "%b %d %H:%M:%S %Y %Z"
                )

                result["expires"] = expiry_date.isoformat()
                result["days_remaining"] = (
                    expiry_date - datetime.utcnow()
                ).days

    except Exception:
        pass

    return result
