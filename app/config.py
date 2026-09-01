import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


class Config:

    @staticmethod
    def get_database():
        return os.getenv("DB_NAME", "products_db")

    @staticmethod
    def get_db_host():
        return os.getenv("DB_HOST", "localhost")

    @staticmethod
    def get_db_port():
        return int(os.getenv("DB_PORT", 5432))

    @staticmethod
    def get_db_user():
        return os.getenv("DB_USER", "postgres")

    @staticmethod
    def get_db_password():
        return os.getenv("DB_PASSWORD")

    @staticmethod
    def get_api_token():
        return os.getenv("API_TOKEN")

    @staticmethod
    def get_jwt_secret():
        return os.getenv("JWT_SECRET")

    @staticmethod
    def get_port():
        return int(os.getenv("PORT", 5000))

    @staticmethod
    def get_cors_origins():
        return [
            origin.strip()
            for origin in os.getenv(
                "CORS_ORIGINS",
                "http://localhost:5173"
            ).split(",")
            if origin.strip()
    ]