from flask import Blueprint, request, jsonify

from handlers import UpdateHandler
from logger import logger

telegram_bp = Blueprint("telegram", __name__)


@telegram_bp.route("/webhook", methods=["POST"])
def webhook():
    try:
        update = request.get_json(force=True)

        logger.info(f"Incoming update: {update}")

        UpdateHandler.handle(update)

        return jsonify({"ok": True})

    except Exception as e:
        logger.exception(f"Webhook error: {e}")
        return jsonify({"ok": False}), 500


def register_telegram_routes(app):
    app.register_blueprint(telegram_bp)
