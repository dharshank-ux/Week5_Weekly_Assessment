import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Week 5 Secure API"
    API_KEY = os.getenv("API_KEY", "my-secret-key")
    DATABASE_PATH = "task4_database.json"
    DEBUG = True

settings = Settings()