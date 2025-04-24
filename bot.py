import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Menu principale sempre disponibile
def get_main_menu():
    return InlineKeyboardMarkup([[InlineKeyboardButton("📦 Acquista Pacchetti Prompt", callback_data="pacchetti")],
                                 [InlineKeyboardButton("🧠 Quiz Consulenza", callback_data="quiz")],
                                 [InlineKeyboardButton("💳 Integrazione Pagamenti", callback_data="pagamenti")],
                                 [InlineKeyboardButton("🚀 Branding e Social", callback_data="branding")]])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono Moty 🤖. Come posso aiutarti oggi?", reply_markup=get_main_menu())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    risposta = {
        "pacchetti": "📦 Pacchetti Prompt"

Scegli tra pacchetti pronti per creare contenuti unici, copywriting, marketing o idee business.
        "quiz": "🧠 Quiz Consulenza"

Uno strumento automatizzato per aiutare gli utenti a capire di cosa hanno bisogno.
        "pagamenti": "💳 Integrazione Pagamenti"

Possiamo collegare Stripe o attivare i pagamenti nativi di Telegram per automatizzare gli acquisti.
        "branding": "🚀 Branding e Social"

Contenuti visivi, tono di voce, nome brand, bio Instagram: creiamo tutto con Moty Assistant.
    }
    await query.edit_message_text(risposta[query.data], parse_mode="Markdown", reply_markup=get_main_menu())

def main():
    import os
    TOKEN = ("8087961436:AAGlF0kYCl8Fn-UAr3OclgUCJdke5yMeKUg")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
