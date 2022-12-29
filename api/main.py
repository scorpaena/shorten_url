from typing import Dict, Union

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, RedirectResponse
from models import UrlAndDaysDataInput
from utils import generate_url, get_url, save_url

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def value_error_exception_handler(
    request: Request, error: RequestValidationError
) -> JSONResponse:

    return JSONResponse(status_code=400, content={"message": str(error)})


@app.post("/api/generate")
async def generate_shortened_url(url: UrlAndDaysDataInput) -> Dict[str, str]:
    days_available = url.days_available
    original_url = url.original_url

    url_id, shortened_url = generate_url()

    await save_url(
        url_id=url_id, original_url=original_url, days_available=days_available
    )

    return {"shortened_url": shortened_url, "original_url": original_url}


@app.get("/{url_id}")
async def redirect_to_original_url(
    url_id: str,
) -> Union[HTTPException, RedirectResponse]:
    original_url = await get_url(url_id)

    if not original_url:
        raise HTTPException(status_code=404, detail="URL is not found")

    return RedirectResponse(original_url)
