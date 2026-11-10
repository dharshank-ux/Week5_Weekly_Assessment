# Week 5 - Task 4: Secured FastAPI Backend

## Completed Features

- FastAPI application
- API key authentication
- Settings management
- Dependency injection
- JSON database storage
- Create message endpoint
- Read messages endpoint
- Pytest test cases

## Security

- Valid API key allows access.
- Missing API key returns 401.
- Invalid API key returns 401.

## Run Application

py -m uvicorn main:app --reload

## Run Tests

py -m pytest -v