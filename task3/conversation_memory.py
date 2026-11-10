import json
from pathlib import Path

HISTORY_FILE = Path(__file__).parent / "conversation.json"

def save_message(role, content):
    history = []

    if HISTORY_FILE.exists():
        history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))

    history.append({
        "role": role,
        "content": content
    })

    HISTORY_FILE.write_text(
        json.dumps(history, indent=4),
        encoding="utf-8"
    )

def show_history():
    if HISTORY_FILE.exists():
        history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))
        for message in history:
            print(message["role"], ":", message["content"])
    else:
        print("No conversation history found.")

def main():
    save_message("user", "My name is Arun.")
    save_message("assistant", "Nice to meet you, Arun!")

    print("Conversation History:")
    show_history()

    print("\nNext question: What is my name?")
    history = json.loads(HISTORY_FILE.read_text(encoding="utf-8"))

    for message in history:
        if message["role"] == "user" and "My name is" in message["content"]:
            name = message["content"].replace("My name is", "").strip(". ")
            print("Your name is", name)

if __name__ == "__main__":
    main()