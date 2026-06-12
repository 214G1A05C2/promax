import os
from pathlib import Path


class Config:
    _base_dir = Path(__file__).resolve().parent
    _sqlite_db = _base_dir / "instance" / "calls.db"
    _sqlite_uri = _sqlite_db.as_posix()

    _database_url = (
        os.getenv("DATABASE_URL")
        or os.getenv("DATA_BASE_URL")
        or f"sqlite:///{_sqlite_uri}"
    )

    if _database_url.startswith("postgres://"):
        _database_url = _database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = _database_url

    SQLALCHEMY_TRACK_MODIFICATIONS = False
