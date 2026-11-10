import time
from llm_client import ask_openai


prompt = "Explain artificial intelligence in simple words."

# Non-streaming measurement
start = time.time()

result = ask_openai(prompt)

non_stream_time = time.time() - start

print("Non-streaming answer:", result["answer"])
print("Non-streaming time:", round(non_stream_time, 3), "seconds")


# Streaming simulation measurement
start = time.time()

answer = result["answer"]

first_token_time = None

for word in answer.split():
    if first_token_time is None:
        first_token_time = time.time() - start

    print(word, end=" ", flush=True)
    time.sleep(0.1)

print("\nFirst token time:", round(first_token_time, 3), "seconds")
print("Streaming simulation completed.")