import logging
import sys

from telegram import (ReplyKeyboardMarkup, 
                      ReplyKeyboardRemove, 
                      Update,
                      InlineQueryResultArticle, 
                      KeyboardButton,
                      InputTextMessageContent)

from telegram.ext import (InlineQueryHandler, 
                          MessageHandler, 
                          CommandHandler,
                          ApplicationBuilder, 
                          ContextTypes, 
                          filters)

import commands

FIND_PASSWORD_MESSAGE = "🔎 Найти пароль"

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
    keyboard = [[KeyboardButton(text="Найти пароль")],
                [KeyboardButton(text="Добавить пароль")],
                [KeyboardButton(text="Изменить пароль")]]

    await update.message.reply_text(
            "Please choose:", 
            reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))

@with_buttons
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_start(update, context)

@with_buttons
async def add_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_add_password(update, context)

@with_buttons
async def change_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await commands.apply_change_password(update, context)

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
    handlers.append(CommandHandler('change_password', change_password))
    handlers.append(CommandHandler('🔎 Найти пароль', find_password))
    handlers.append(MessageHandler(filters.TEXT, default_answer))

    for handler in handlers:
        application.add_handler(handler)
    
    application.run_polling()
