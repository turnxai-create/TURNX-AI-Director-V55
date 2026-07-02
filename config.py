import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "").strip()

    TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

    @staticmethod
    def validate():
        if not Config.BOT_TOKEN:
            raise ValueError("BOT_TOKEN is missing!")

        if not Config.WEBHOOK_URL:
            raise ValueError("WEBHOOK_URL is missing!")
