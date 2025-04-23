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

# Dizionario risposte
PROMPT_CONTENT = {
    "prompt_instagram": "📱 Pacchetto Instagram & TikTok:\nPrompt per contenuti virali e caption perfette.\n💰 Prezzo: 9",
    "prompt_vendita": "💼 Pacchetto per vendere online:\nPrompt per vendere di più con l'AI.\n💰 Prezzo: 12",
    "prompt_assistente": "🤖 Crea il tuo AI Assistant:\nPrompt per costruire un assistente AI personalizzato.\n💰 Prezzo: 15",
    "prompt_free": "🎁 Prompt gratuito:\n👉 Agisci come un copywriter esperto e crea una caption accattivante per promuovere un nuovo prodotto ecologico.",
    "acquista": "🛒 Scegli un pacchetto da acquistare:",
    "acquista_ig": "Per acquistare il Pacchetto Instagram & TikTok clicca qui sotto.\n📦 Dopo il pagamento riceverai il PDF:\n👉 [LINK PAGAMENTO]",
    "acquista_vendita": "Per acquistare il Pacchetto Vendita clicca qui sotto.\n📦 Dopo il pagamento riceverai il PDF:\n👉 [LINK PAGAMENTO]",
    "acquista_ai": "Per acquistare il Pacchetto Assistant clicca qui sotto.\n📦 Dopo il pagamento riceverai il PDF:\n👉 [LINK PAGAMENTO]"
}

# Menu principale
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📱 Prompt Instagram & TikTok", callback_data="prompt_instagram")],
        [InlineKeyboardButton("💼 Prompt per vendere online", callback_data="prompt_vendita")],
        [InlineKeyboardButton("🤖 Crea il tuo AI Assistant", callback_data="prompt_assistente")],
        [InlineKeyboardButton("🎁 Prompt gratuito", callback_data="prompt_free")],
        [InlineKeyboardButton("🛒 Acquista pacchetti", callback_data="acquista")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(WELCOME_TEXT, reply_markup=reply_markup)

# Gestione pulsanti
async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "acquista":
        keyboard = [
            [InlineKeyboardButton("📱 Acquista Instagram", callback_data="acquista_ig")],
            [InlineKeyboardButton("💼 Acquista Vendita", callback_data="acquista_vendita")],
            [InlineKeyboardButton("🤖 Acquista Assistant", callback_data="acquista_ai")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=PROMPT_CONTENT["acquista"], reply_markup=reply_markup)
    else:
        content = PROMPT_CONTENT.get(query.data, "❌ Selezione non valida.")
        await query.edit_message_text(text=content, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.run_polling()

if __name__ == "__main__":
    main()
