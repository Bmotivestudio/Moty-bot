import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = ("8087961436:AAGlF0kYCl8Fn-UAr3OclgUCJdke5yMeKUg")

WELCOME_TEXT = """Ciao! Sono Moty, il tuo assistente AI personale.

Scopri i miei pacchetti di prompt per:
- creare contenuti virali
- vendere di più online
- costruire il tuo AI Assistant

Scegli un'opzione qui sotto:
"""

PROMPT_CONTENT = {
    "prompt_instagram": "📱 Pacchetto Instagram & TikTok:\nPrompt per creare contenuti virali, caption perfette e piani editoriali.",
    "prompt_vendita": "💼 Pacchetto Vendita:\nPrompt per vendere di più con l'AI, scrivere descrizioni persuasive ed email che convertono.",
    "prompt_assistente": "🤖 Crea il tuo AI Assistant:\nPrompt per costruire un assistente AI su misura per il tuo lavoro.",
    "prompt_free": "🎁 Ecco il tuo prompt gratuito:\n👉 Agisci come un copywriter esperto e crea una caption accattivante per promuovere un nuovo prodotto ecologico.",
    "acquista": "🛒 Per acquistare uno dei miei pacchetti, visita la pagina ufficiale o scegli un pacchetto e riceverai il link al pagamento. (link in arrivo)"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 Prompt Instagram & TikTok", callback_data="prompt_instagram")],
        [InlineKeyboardButton("💼 Prompt per vendere online", callback_data="prompt_vendita")],
        [InlineKeyboardButton("🤖 Crea il tuo AI Assistant", callback_data="prompt_assistente")],
        [InlineKeyboardButton("🎁 Ricevi un prompt gratuito", callback_data="prompt_free")],
        [InlineKeyboardButton("🛒 Acquista pacchetti", callback_data="acquista")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    content = PROMPT_CONTENT.get(query.data, "❌ Selezione non valida.")
    await query.edit_message_text(text=content)

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.run_polling()

if __name__ == "__main__":
    main()
