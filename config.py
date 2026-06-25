import os
from pathlib import Path

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    load_dotenv = None

if load_dotenv is not None:
    load_dotenv()


class Settings:
    _base_dir = Path(__file__).resolve().parent
    _sqlite_db = _base_dir / "instance" / "calls.db"
    _sqlite_uri = _sqlite_db.as_posix()

    DATABASE_URL: str = os.getenv("DATABASE_URL") or os.getenv("DATA_BASE_URL")

    if not DATABASE_URL:
        if os.getenv("PORT"):
            raise RuntimeError(
                "DATABASE_URL is required in production. "
                "Set it to your Render Postgres internal URL."
            )

        DATABASE_URL = f"sqlite:///{_sqlite_uri}"

    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


settings = Settings()
