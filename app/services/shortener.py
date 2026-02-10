import secrets
from datetime import datetime, timezone

from app.core.config import get_settings
from app.db.unit_of_work import UnitOfWork
from app.models.link import ShortLink

settings = get_settings()


class ShortenerService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def _generate_code(self) -> str:
        code = secrets.token_urlsafe(settings.short_code_length)
        return code

    def shorten(self, url: str) -> str:
        with self.uow as uow:
            existing = uow.repo.get_by_url(url)
            if existing:
                return existing.code

            code = self._generate_code()

            link = ShortLink(
                code=code,
                url=url,
                created_at=datetime.now(timezone.utc),
            )

            uow.repo.add(link)

            return code

    def resolve(self, code: str) -> str | None:
        with self.uow as uow:
            link = uow.repo.get_by_code(code)

        if link:
            return link.url

        return None
