import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler

from db.tools import create_session
from bots.commands import start

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
    )
    session = create_session()

    application = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()

    start_handler = CommandHandler("start", start)

    application.add_handler(start_handler)

    application.run_polling()
