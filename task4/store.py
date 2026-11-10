import json
from pathlib import Path

DATABASE_FILE = Path(__file__).parent / "task4_database.json"


def load_data():
    if DATABASE_FILE.exists():
        return json.loads(DATABASE_FILE.read_text(encoding="utf-8"))
    return {"messages": []}


def save_message(message):
    data = load_data()
    data["messages"].append(message)

    DATABASE_FILE.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )

    return message


def get_messages():
    return load_data()["messages"]