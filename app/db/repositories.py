from datetime import datetime
from sqlite3 import Connection

from app.models.link import ShortLink


class ShortLinkRepository:
    def __init__(self, conn: Connection):
        self.conn = conn

    def add(self, link: ShortLink) -> None:
        self.conn.execute(
            "INSERT INTO links (code, url, created_at) VALUES (?, ?, ?)",
            (link.code, link.url, link.created_at.isoformat()),
        )

    def get_by_code(self, code: str) -> ShortLink | None:
        row = self.conn.execute(
            "SELECT code, url, created_at FROM links WHERE code = ?",
            (code,),
        ).fetchone()

        if not row:
            return None

        link = self._row_to_model(row)
        return link

    def get_by_url(self, url: str) -> ShortLink | None:
        row = self.conn.execute(
            "SELECT code, url, created_at FROM links WHERE url = ?",
            (url,),
        ).fetchone()

        if not row:
            return None

        link = self._row_to_model(row)
        return link

    @staticmethod
    def _row_to_model(row):
        if not row:
            return None

        return ShortLink(
            code=row[0],
            url=row[1],
            created_at=datetime.fromisoformat(row[2]),
        )
