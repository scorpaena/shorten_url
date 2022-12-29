from typing import Optional

from pydantic import BaseModel, Field, HttpUrl, conint
from settings import MAX_DAYS_AVAILABLE, MIN_DAYS_AVAILABLE


class UrlAndDaysDataInput(BaseModel):
    original_url: HttpUrl
    days_available: Optional[
        conint(ge=MIN_DAYS_AVAILABLE, le=MAX_DAYS_AVAILABLE)
    ] = Field(default=None)
