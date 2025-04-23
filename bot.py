import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Funzione per mostrare il menu principale
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("📦 Acquista pacchetti", callback_data="acquista_pacchetti")],
        [InlineKeyboardButton("🧠 Quiz consulenza", callback_data="quiz_consulenza")],
        [InlineKeyboardButton("💳 Pagamenti", callback_data="pagamenti")],
        [InlineKeyboardButton("🎨 Branding e Social", callback_data="branding")]
    ]
    return InlineKeyboardMarkup(keyboard)

# Avvio del bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono Moty 🤖", reply_markup=get_main_menu())

# Gestione dei pulsanti
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "acquista_pacchetti":
        text = "🎯 Scegli tra i pacchetti pronti:\n\n1. Business\n2. Creatività\n3. Crescita personale"
    elif query.data == "quiz_consulenza":
        text = "🧠 Avvia il quiz automatico per scoprire cosa ti serve davvero!"
    elif query.data == "pagamenti":
        text = "💳 Prossimamente potrai pagare direttamente qui!"
    elif query.data == "branding":
        text = "🎨 Servizi di branding, contenuti e crescita social!"

    # Rispondi con il contenuto + sempre il menu disponibile
    await query.edit_message_text(text=text, reply_markup=get_main_menu())

# Avvio del bot in modalità polling
def main():
    TOKEN = ("8087961436:AAGlF0kYCl8Fn-UAr3OclgUCJdke5yMeKUg")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Moty Assistant avviato (modalità polling)")
    app.run_polling()

if __name__ == "__main__":
    main()
