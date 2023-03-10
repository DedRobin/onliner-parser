import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from db.tools import create_session
from bots.commands import start, track_product

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":
    session = create_session()

    application = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()

    start_handler = CommandHandler("start", start)
    track_product_handler = MessageHandler(filters.Regex("^Добавить товар для отслеживания$"), track_product)

    application.add_handler(start_handler)
    application.add_handler(track_product_handler)

    application.run_polling()
