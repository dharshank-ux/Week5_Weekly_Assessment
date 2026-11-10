import asyncio
import time


async def mock_api_call(question):
    await asyncio.sleep(1)

    if question == "Question 5":
        raise Exception("Mock API error")

    return f"{question}: Success"


async def sequential_calls():
    print("\n--- Sequential Execution ---")

    start = time.time()

    results = []

    for i in range(1, 11):
        try:
            result = await mock_api_call(f"Question {i}")
            results.append(result)
            print(result)
        except Exception as error:
            print(f"Question {i} failed: {error}")

    print("Sequential time:", round(time.time() - start, 2), "seconds")


async def parallel_calls():
    print("\n--- Parallel Execution ---")

    start = time.time()

    semaphore = asyncio.Semaphore(3)

    async def limited_call(i):
        async with semaphore:
            try:
                result = await mock_api_call(f"Question {i}")
                print(result)
                return result
            except Exception as error:
                print(f"Question {i} failed: {error}")
                return None

    tasks = [
        limited_call(i)
        for i in range(1, 11)
    ]

    results = await asyncio.gather(*tasks)

    print("Successful calls:", sum(r is not None for r in results))
    print("Parallel time:", round(time.time() - start, 2), "seconds")


async def main():
    await sequential_calls()
    await parallel_calls()


asyncio.run(main())