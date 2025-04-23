import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN ="8087961436:AAGlF0kYCl8Fn-UAr3OclgUCJdke5yMeKUg"
WEBHOOK_BASE_URL = os.getenv("https://moty-bot.onrender.com")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono Moty, l'assistente di Bmotive Studio!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=f"{WEBHOOK_BASE_URL}/webhook"
    )

if __name__ == "__main__":
    main()
