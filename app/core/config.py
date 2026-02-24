import os
from functools import lru_cache


class Settings:
    # =========================
    # Application
    # =========================
    APP_NAME: str = "0x-scan"
    VERSION: str = "0.1.0"
    ENV: str = os.getenv("ENV", "development")

    # =========================
    # Server
    # =========================
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))

    # =========================
    # Security
    # =========================
    API_KEY: str = os.getenv("API_KEY", "dev-secret")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change-me")

    # =========================
    # Rate Limiting
    # =========================
    RATE_LIMIT: int = int(os.getenv("RATE_LIMIT", "60"))

    # =========================
    # Database (future)
    # =========================
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://user:pass@localhost:5432/recon"
    )

    # =========================
    # Redis (future)
    # =========================
    REDIS_URL: str = os.getenv(
        "REDIS_URL",
        "redis://localhost:6379"
    )

    # =========================
    # Scanner
    # =========================
    DEFAULT_TIMEOUT: int = int(os.getenv("SCAN_TIMEOUT", "5"))
    MAX_CONCURRENT_SCANS: int = int(
        os.getenv("MAX_CONCURRENT_SCANS", "100")
    )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
