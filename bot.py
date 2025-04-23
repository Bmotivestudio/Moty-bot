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
    "prompt_instagram": """📱 *Pacchetto Instagram & TikTok*

🔥 Vuoi contenuti virali senza impazzire?

Con questo pacchetto di prompt ottieni:
✅ Caption ad effetto per Reels e post
✅ Idee video TikTok in trend
✅ Hook e call-to-action che convertono
✅ Prompt per commenti coinvolgenti
✅ Piano contenuti settimanale automatizzato

Perfetto per freelance, creator, piccoli brand.
📦 Formato: PDF scaricabile + prompt integrabili nel tuo AI Assistant

💰 Prezzo: 9€""",
    
    "prompt_vendita": """💼 *Pacchetto per vendere online*

💸 Vuoi vendere di più con l’AI?

Con questo pacchetto:
✅ Scrivi descrizioni prodotto persuasive
✅ Crea email automatiche che portano vendite
✅ Rispondi ai clienti indecisi con empatia
✅ Recuperi carrelli abbandonati con stile
✅ Costruisci offerte irresistibili

Ideale per chi ha un e-commerce o offre servizi online.
📦 Formato: PDF + accesso a prompt testabili nel bot

💰 Prezzo: 12€""",
    
    "prompt_assistente": """🤖 *Pacchetto: Crea il tuo AI Assistant*

⚙️ Vuoi un assistente AI che lavori per te?

Con questo pacchetto impari a:
✅ Creare un AI Assistant su misura per il tuo business
✅ Organizzare task, note vocali e messaggi automatici
✅ Personalizzare tono, obiettivi e stile
✅ Collegarlo a Telegram, Notion e Google Calendar

📦 Contenuto: Prompt pronti + guida interattiva

💰 Prezzo: 15€""",

    "prompt_free": """🎁 *Prompt gratuito*

👉 Agisci come un copywriter esperto e crea una caption accattivante per promuovere un nuovo prodotto ecologico.""",

    "acquista": """🛒 *Acquista pacchetti*

Per acquistare uno dei miei pacchetti, seleziona quello che ti interessa e riceverai il link al pagamento. (in arrivo)

Presto sarà attivo anche il pagamento direttamente in questa chat!"""
}

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

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    content = PROMPT_CONTENT.get(query.data, "❌ Selezione non valida.")
    await query.edit_message_text(text=content, parse_mode="Markdown")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_button))
    app.run_polling()

if __name__ == "__main__":
    main()
