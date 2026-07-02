from flask import Flask

from config import Config
from logger import logger
from telegram import register_telegram_routes

# Validate environment variables
Config.validate()

app = Flask(__name__)

# Register Telegram webhook route
register_telegram_routes(app)


@app.route("/", methods=["GET"])
def home():
    return {
        "status": "online",
        "bot": "TURNX AI Director V5"
    }, 200


if __name__ == "__main__":
    logger.info("TURNX AI Director V5 starting...")
    app.run(host="0.0.0.0", port=10000)
