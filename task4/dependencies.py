from fastapi import Header, HTTPException
from settings import settings


def verify_api_key(x_api_key: str = Header(default=None)):
    if x_api_key != settings.API_KEY:
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

    return True