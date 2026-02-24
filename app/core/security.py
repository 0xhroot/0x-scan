import hashlib
import hmac
import secrets
from typing import Optional


# =============================
# API KEY HASHING
# =============================

def hash_api_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


def verify_api_key(key: str, hashed: str) -> bool:
    return hmac.compare_digest(
        hash_api_key(key),
        hashed
    )


# =============================
# PASSWORD HASHING
# =============================

def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    )
    return f"{salt}${hashed.hex()}"


def verify_password(password: str, stored: str) -> bool:
    salt, hashed = stored.split("$")
    new_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100000
    )
    return hmac.compare_digest(
        new_hash.hex(),
        hashed
    )


# =============================
# TOKEN GENERATION
# =============================

def generate_token(length: int = 32) -> str:
    return secrets.token_urlsafe(length)


# =============================
# RANDOM ID
# =============================

def generate_id() -> str:
    return secrets.token_hex(16)
