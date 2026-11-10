from fastapi import FastAPI, Depends
from pydantic import BaseModel
from settings import settings
from dependencies import verify_api_key
from store import save_message, get_messages

app = FastAPI(title=settings.APP_NAME)


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {"message": "Secure API is running"}


@app.post("/messages")
def create_message(
    request: MessageRequest,
    authenticated: bool = Depends(verify_api_key)
):
    saved = save_message(request.message)
    return {
        "success": True,
        "message": saved
    }


@app.get("/messages")
def read_messages(
    authenticated: bool = Depends(verify_api_key)
):
    return {"messages": get_messages()}