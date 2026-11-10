# Week 5 - Task 2: Reliability and Async

## Exponential Backoff - 4 Lines

1. Exponential backoff retries failed API requests after waiting.
2. Each retry increases the waiting time.
3. Jitter adds a random delay to avoid simultaneous retries.
4. It helps reduce server overload and API rate limits.

## Completed
- Tenacity retry
- Retry on 429 and 5xx errors
- No retry on 401 errors
- Sequential async calls
- Parallel async calls
- Semaphore concurrency limit of 3
- Partial failure handling