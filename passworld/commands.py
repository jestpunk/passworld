from telegram import Update
from telegram.ext import ContextTypes

async def apply_add_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("Applying add password")

async def apply_default_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    default_answer = "DEFAULT ANSWER"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=default_answer)

async def apply_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="CMD START")

async def apply_add_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="CMD ADD PASSWORD")

async def apply_remove_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="CMD REMOVE PASSWORD")

async def apply_find_password(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="CMD FIND PASSWORD")


