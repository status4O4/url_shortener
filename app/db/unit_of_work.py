import sqlite3
from app.db.repositories import ShortLinkRepository
from app.core.config import get_settings

settings = get_settings()


class UnitOfWork:
    def __init__(self, db_path: str = settings.database_path):
        self._db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self._db_path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS links (
                code TEXT PRIMARY KEY,
                url TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL
            )
        """)
        self.repo = ShortLinkRepository(self.conn)
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc:
            self.conn.rollback()
        else:
            self.conn.commit()
        self.conn.close()
