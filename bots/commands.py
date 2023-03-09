import inspect
import logging
import os
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    username = update.effective_chat.username
    link = update.effective_chat.link
    chat_id = update.effective_chat.id
    command = inspect.currentframe().f_code.co_name

    data = first_name, last_name, username, link, chat_id, command

    logger = logging.getLogger(__name__)
    logger.info(
        "{0} {1} - {2} ({3}), chat ID={4} used command '/{5}'".format(*data))

    if chat_id == int(os.environ.get("CHAT_ID")):
        await context.bot.send_message(
            chat_id=os.environ.get("CHAT_ID"),
            text="Бот запущен."
        )
