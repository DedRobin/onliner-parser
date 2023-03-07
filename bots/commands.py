import inspect
import os
from telegram import Update
from telegram.ext import ContextTypes

from bots.settings import logger


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_chat.first_name
    last_name = update.effective_chat.last_name
    username = update.effective_chat.username
    link = update.effective_chat.link
    chat_id = update.effective_chat.id
    command = inspect.currentframe().f_code.co_name

    data = first_name, last_name, username, link, chat_id, command

    logger.info(
        "{0} {1} - {2} ({3}), chat ID={4} used command '/{5}'".format(*data))

    if chat_id == os.environ.get("CHAT_ID"):
        await context.bot.send_message(
            chat_id=os.environ.get("CHAT_ID"),
            text="I'm a bot, please talk to me!"
        )
