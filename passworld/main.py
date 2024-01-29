import logging
import sys

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='[%(levelname)s][%(asctime)s] %(name)s :\n\t%(message)s',
    level=logging.INFO,
    #    filename='logs.txt'
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


async def add_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Мы могли бы добавить пароль...")

async def remove_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Мы могли бы удалить пароль...")

async def find_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Мы могли бы найти пароль...")

if __name__ == '__main__':
    application = ApplicationBuilder().token(sys.argv[1]).build()
    
    handlers = []
    handlers.append(CommandHandler('start', start))
    handlers.append(CommandHandler('add_password', add_password))
    handlers.append(CommandHandler('remove_password', remove_password))
    handlers.append(CommandHandler('find_password', find_password))

    for handler in handlers:
        application.add_handler(handler)
    
    application.run_polling()
