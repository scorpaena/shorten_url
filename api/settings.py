import os

REDIS_URL = os.getenv("REDIS_URL", default="redis://localhost:6379")

SHORTENED_URL_LIFE_PERIOD = os.getenv("SHORTENED_URL_LIFE_PERIOD", default=90)

HOST = os.getenv("HOST", default="http://0.0.0.0:8080")

MIN_DAYS_AVAILABLE = os.getenv("MIN_DAYS_AVAILABLE", default=1)

MAX_DAYS_AVAILABLE = os.getenv("MAX_DAYS_AVAILABLE", default=365)
