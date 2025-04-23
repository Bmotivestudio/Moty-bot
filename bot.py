import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

BOT_TOKEN = os.getenv("8087961436:AAGlF0kYCl8Fn-UAr3OclgUCJdke5yMeKUg")

WELCOME_MESSAGE = """Ciao, sono Moty, l'assistente AI di Bmotive!

Posso aiutarti a:
- Trovare prompt e automazioni già pronti
- Creare il tuo assistente personale
- Ricevere una consulenza su misura per il tuo business

Cosa vuoi fare oggi?
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Pacchetti Prompt", callback_data="prompt")],
        [InlineKeyboardButton("Quiz + Consulenza", callback_data="quiz")],
        [InlineKeyboardButton("I miei acquisti", callback_data="acquisti")],
        [InlineKeyboardButton("Contatta Moty", url="https://t.me/Bmotiveagencybot")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "prompt":
        await query.edit_message_text("Ecco i pacchetti disponibili! (presto online)")
    elif query.data == "quiz":
        await query.edit_message_text("Inizia il quiz per ricevere la tua consulenza AI personalizzata. (prossimamente!)")
    elif query.data == "acquisti":
        await query.edit_message_text("Qui troverai i tuoi pacchetti acquistati. (in arrivo!)")

application = ApplicationBuilder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CallbackQueryHandler(button_handler))

if __name__ == "__main__":
    application.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        url_path=BOT_TOKEN,
        webhook_url=f"{os.environ.get('WEBHOOK_BASE_URL')}/{BOT_TOKEN}"
    )
