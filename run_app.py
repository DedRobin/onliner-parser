import os

from telegram.ext import ApplicationBuilder, CommandHandler

from bots.create_db_session import create_session
from bots.commands import start
from bots import settings

if __name__ == "__main__":
    session = create_session()

    application = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()

    start_handler = CommandHandler("start", start)

    application.add_handler(start_handler)

    application.run_polling()
