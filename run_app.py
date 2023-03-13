import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, filters

from db.tools import create_session
from bots.commands import start, track_menu, tack_product, STATES

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

if __name__ == "__main__":

    application = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()

    start_handler = CommandHandler("start", start)
    track_product_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^Добавить товар для отслеживания$"), track_menu)],
        states={
            STATES["TRACK"]: [MessageHandler(filters.TEXT, tack_product)],
        },
        fallbacks=[CommandHandler("back", track_menu)]
    )

    application.add_handler(start_handler)
    application.add_handler(track_product_handler)

    application.run_polling()
