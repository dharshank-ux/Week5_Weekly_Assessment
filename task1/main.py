import json
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from llm_client import ask_openai
from cost_tracker import count_tokens, log_usage, get_today_usage

app = FastAPI(title="Week 5 Weekly Assessment")

TOKEN_LIMIT = 3000


class ChatRequest(BaseModel):
    prompt: str


@app.get("/")
def home():
    return {"message": "LLM Chat API is running"}


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    prompt = request.prompt

    input_tokens = count_tokens([prompt])

    if input_tokens > TOKEN_LIMIT:
        raise HTTPException(
            status_code=413,
            detail="Token limit exceeded"
        )

    result = ask_openai(prompt)

    answer = result["answer"]

    usage = result["usage"]

    log_usage(
        usage["input_tokens"],
        usage["output_tokens"]
    )

    async def generate():
        for word in answer.split():
            data = json.dumps({"token": word + " "})
            yield f"data: {data}\n\n"
            await asyncio.sleep(0.1)

        yield "data: [DONE]\n\n"

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )


@app.get("/usage")
def usage():
    return get_today_usage()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)