import requests
from config import Config
from logger import logger


class UpdateHandler:

    @staticmethod
    def send_message(chat_id, text):
        url = f"{Config.TELEGRAM_API}/sendMessage"

        payload = {
            "chat_id": chat_id,
            "text": text
        }

        try:
            requests.post(url, json=payload, timeout=10)
        except Exception as e:
            logger.error(f"Failed to send message: {e}")

    @staticmethod
    def handle(update):
        logger.info(update)

        message = update.get("message")

        if not message:
            return

        chat_id = message["chat"]["id"]
        text = message.get("text", "")

        if text == "/start":
            UpdateHandler.send_message(
                chat_id,
                "👋 Welcome to TURNX AI Director V5!\n\nThe bot is now online."
            )
            return

        UpdateHandler.send_message(
            chat_id,
            f"You said:\n\n{text}"
      )
