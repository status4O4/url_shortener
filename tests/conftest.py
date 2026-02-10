from pathlib import Path

import pytest

from app.db.unit_of_work import UnitOfWork
from app.services.shortener import ShortenerService


@pytest.fixture
def tmp_db(tmp_path: Path) -> str:
    db_file = tmp_path / "test.db"
    return str(db_file)


@pytest.fixture
def uow(tmp_db: str) -> UnitOfWork:
    return UnitOfWork(tmp_db)


@pytest.fixture
def service(uow: UnitOfWork) -> ShortenerService:
    return ShortenerService(uow)
