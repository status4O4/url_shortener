from app.db.unit_of_work import UnitOfWork
from app.services.shortener import ShortenerService


def get_shortener_service():
    uow = UnitOfWork()
    return ShortenerService(uow)
