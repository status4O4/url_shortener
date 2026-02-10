from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ShortLink:
    code: str
    url: str
    created_at: datetime
