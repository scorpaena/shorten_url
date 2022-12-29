from typing import Optional, Tuple
from urllib.parse import urljoin

import redis.asyncio as aioredis
from settings import HOST, REDIS_URL, SHORTENED_URL_LIFE_PERIOD
from shortuuid import ShortUUID


async def get_redis() -> aioredis.Redis:
    redis_object = await aioredis.from_url(REDIS_URL, decode_responses=True)
    return redis_object


async def save_url(
    url_id: str, original_url: str, days_available: Optional[int] = None
) -> None:

    seconds_available = (days_available or SHORTENED_URL_LIFE_PERIOD) * 3600 * 24

    redis = await get_redis()

    await redis.setex(
        name=url_id,
        time=seconds_available,
        value=original_url,
    )


async def get_url(url_id: str) -> Optional[str]:
    redis = await get_redis()
    original_url = await redis.get(url_id)
    return original_url


def generate_url() -> Tuple[str, str]:
    uuid = ShortUUID().random(length=8)
    return (uuid, urljoin(HOST, uuid))
