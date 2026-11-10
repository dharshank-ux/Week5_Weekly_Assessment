import json
from datetime import date
from pathlib import Path

LOG_FILE = Path(__file__).parent / "usage_log.json"

INPUT_PRICE = 1.0
OUTPUT_PRICE = 2.0


def count_tokens(messages):
    try:
        import tiktoken
        encoding = tiktoken.get_encoding("cl100k_base")
        text = " ".join(str(message) for message in messages)
        return len(encoding.encode(text))
    except Exception:
        return len(" ".join(map(str, messages)).split())


def calculate_cost(input_tokens, output_tokens):
    input_cost = (input_tokens / 1_000_000) * INPUT_PRICE
    output_cost = (output_tokens / 1_000_000) * OUTPUT_PRICE
    return round(input_cost + output_cost, 8)


def log_usage(input_tokens, output_tokens):
    cost = calculate_cost(input_tokens, output_tokens)

    record = {
        "date": str(date.today()),
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "cost": cost
    }

    logs = []

    if LOG_FILE.exists():
        logs = json.loads(LOG_FILE.read_text(encoding="utf-8"))

    logs.append(record)

    LOG_FILE.write_text(
        json.dumps(logs, indent=4),
        encoding="utf-8"
    )

    return record


def get_today_usage():
    if not LOG_FILE.exists():
        return {"total_tokens": 0, "total_cost": 0}

    logs = json.loads(LOG_FILE.read_text(encoding="utf-8"))

    today = str(date.today())

    today_logs = [item for item in logs if item["date"] == today]

    return {
        "total_tokens": sum(item["total_tokens"] for item in today_logs),
        "total_cost": round(sum(item["cost"] for item in today_logs), 8)
    }