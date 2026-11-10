import logging
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception,
    before_sleep_log
)

logging.basicConfig(level=logging.INFO, format="%(message)s")


class APIError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"HTTP {status_code}")


def should_retry(error):
    return (
        isinstance(error, APIError)
        and (
            error.status_code == 429
            or 500 <= error.status_code <= 599
        )
    )


attempts = 0


@retry(
    retry=retry_if_exception(should_retry),
    wait=wait_exponential(multiplier=1, min=1, max=8),
    stop=stop_after_attempt(5),
    before_sleep=before_sleep_log(logging.getLogger(), logging.WARNING),
    reraise=True
)
def mock_api_call():
    global attempts
    attempts += 1

    if attempts <= 2:
        print(f"Attempt {attempts} failed (429)")
        raise APIError(429)

    print(f"Attempt {attempts} succeeded")
    return "Success!"


print("TEST 1: Retry 429 errors")

try:
    result = mock_api_call()
    print("Result:", result)
except APIError as error:
    print("Failed:", error)


print("\nTEST 2: 401 error (No Retry)")

attempts = 0


@retry(
    retry=retry_if_exception(should_retry),
    wait=wait_exponential(multiplier=1),
    stop=stop_after_attempt(5),
    before_sleep=before_sleep_log(logging.getLogger(), logging.WARNING),
    reraise=True
)
def unauthorized_call():
    global attempts
    attempts += 1
    print(f"Attempt {attempts} failed (401)")
    raise APIError(401)


try:
    unauthorized_call()
except APIError as error:
    print("401 not retried:", error)