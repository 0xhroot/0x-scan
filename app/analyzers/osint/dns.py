import dns.resolver
from typing import Dict, List


RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"]


def query_record(domain: str, record_type: str) -> List[str]:
    results = []

    try:
        answers = dns.resolver.resolve(domain, record_type)

        for r in answers:
            results.append(str(r))

    except Exception:
        pass

    return results


def enumerate_dns(domain: str) -> Dict:

    data = {}

    for rtype in RECORD_TYPES:
        records = query_record(domain, rtype)
        if records:
            data[rtype] = records

    return {
        "domain": domain,
        "records": data
    }
