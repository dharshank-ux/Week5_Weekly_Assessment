import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic

load_dotenv()


def ask_openai(prompt):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return {
            "answer": f"Mock OpenAI response: {prompt}",
            "model": "gpt-4o-mini (mock)",
            "usage": {
                "input_tokens": 10,
                "output_tokens": 15
            }
        }

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.choices[0].message.content,
        "model": response.model,
        "usage": {
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens
        }
    }


def ask_claude(prompt, system):
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        return {
            "answer": f"Mock Claude response: {prompt}",
            "model": "claude-sonnet (mock)",
            "usage": {
                "input_tokens": 10,
                "output_tokens": 15
            }
        }

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=500,
        system=system,
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.content[0].text,
        "model": response.model,
        "usage": {
            "input_tokens": response.usage.input_tokens,
            "output_tokens": response.usage.output_tokens
        }
    }


if __name__ == "__main__":
    result = ask_openai("Hello")
    print("OpenAI:", result)

    result = ask_claude("Hello", "You are helpful.")
    print("Claude:", result)