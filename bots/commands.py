import inspect
import logging
import os
from telegram import Update, ReplyKeyboardRemove
from telegram.ext import ContextTypes, ConversationHandler

from bots.buttons import markup_start
from db.tools import write_link, create_session

logger = logging.getLogger(__name__)

STATES = {
    "TRACK": 0,
    "BACK": 1
}


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

    if chat_id == int(os.environ.get("CHAT_ID")):
        await context.bot.send_message(
            chat_id=chat_id,
            reply_markup=markup_start,
            text="Бот запущен."
        )


async def track_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    if chat_id == int(os.environ.get("CHAT_ID")):
        await context.bot.send_message(
            chat_id=chat_id,
            reply_markup=ReplyKeyboardRemove(),
            text="Вставьте URL-адрес товара для отслеживания"
        )
    return STATES["TRACK"]


async def tack_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    username = update.effective_chat.username
    if chat_id == int(os.environ.get("CHAT_ID")):
        link = update.message.text
        session = create_session()
        await write_link(username=username, session=session, link=link)
        await context.bot.send_message(
            chat_id=chat_id,
            reply_markup=markup_start,
            text=f'Товар "{link}" отслеживается'
        )
        return ConversationHandler.END
