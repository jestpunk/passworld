import logging
import sys

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler, filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

import commands

logging.basicConfig(
    format='[%(levelname)s][%(asctime)s] %(name)s :\n\t%(message)s',
    level=logging.INFO,
    #    filename='logs.txt'
)

def with_buttons(handler_cmd):
    async def wrapped_handler_cmd(update, context):
        await handler_cmd(update, context)
        await print_buttons(update, context)
    return wrapped_handler_cmd


async def print_buttons(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="BUTTONS")

@with_buttons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_start(update, context)


@with_buttons
async def add_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_add_password(update, context)


@with_buttons
async def remove_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_remove_password(update, context)


@with_buttons
async def find_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_find_password(update, context)


@with_buttons
async def default_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_default_answer(update, context)


if __name__ == '__main__':
    application = ApplicationBuilder().token(sys.argv[1]).build()
    
    handlers = []

    handlers.append(CommandHandler('start', start))
    handlers.append(CommandHandler('add_password', add_password))
    handlers.append(CommandHandler('remove_password', remove_password))
    handlers.append(CommandHandler('find_password', find_password))
    handlers.append(MessageHandler(filters.TEXT, default_answer))

    for handler in handlers:
        application.add_handler(handler)
    
    application.run_polling()
