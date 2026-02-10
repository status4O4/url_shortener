from fastapi import APIRouter, HTTPException, Depends

from app.schemas.link import ShortenRequest, ShortenResponse
from app.services.shortener import ShortenerService
from app.dependencies import get_shortener_service


router = APIRouter()


@router.post("/shorten", response_model=ShortenResponse)
def shorten(
    req: ShortenRequest, service: ShortenerService = Depends(get_shortener_service)
) -> ShortenResponse:
    url = str(req.url)
    code = service.shorten(url)
    return ShortenResponse(short_url=code)


@router.get("/{code}")
def redirect(code: str, service: ShortenerService = Depends(get_shortener_service)):
    url = service.resolve(code)
    if not url:
        raise HTTPException(status_code=404, detail="Not found")
    return {"redirect_to": url}
