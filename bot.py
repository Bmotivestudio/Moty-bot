from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup\
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
# Inserisci il tuo token qui (non condividerlo mai pubblicamente!)\
BOT_TOKEN = "8152725037:AAFPPLVStK6GwmU1qHR7QKq1X_msQHUg6Mo"
\
# Messaggio di benvenuto\
WELCOME_MESSAGE = """\
Ciao, sono Moty, l'assistente AI di Bmotive!\
\
Posso aiutarti a:\
- Trovare prompt e automazioni gi\'e0 pronti\
- Creare il tuo assistente personale\
- Ricevere una consulenza su misura per il tuo business\
\
Cosa vuoi fare oggi?\
"""\
\
# Comando /start\
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    keyboard = [\
        [InlineKeyboardButton("Pacchetti Prompt", callback_data="prompt")],\
        [InlineKeyboardButton("Quiz + Consulenza", callback_data="quiz")],\
        [InlineKeyboardButton("I miei acquisti", callback_data="acquisti")],\
        [InlineKeyboardButton("Contatta Moty", url="https://t.me/Bmotiveagencybot")]\
    ]\
    reply_markup = InlineKeyboardMarkup(keyboard)\
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup)\
\
# Gestione pulsanti\
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    query = update.callback_query\
    await query.answer()\
\
    if query.data == "prompt":\
        await query.edit_message_text("Ecco i pacchetti disponibili! (presto online)")\
    elif query.data == "quiz":\
        await query.edit_message_text("Inizia il quiz per ricevere la tua consulenza AI personalizzata. (prossimamente!)")\
    elif query.data == "acquisti":\
        await query.edit_message_text("Qui troverai i tuoi pacchetti acquistati. (in arrivo!)")\
\
# Avvio del bot\
def main():\
    app = ApplicationBuilder().token(BOT_TOKEN).build()\
\
    app.add_handler(CommandHandler("start", start))\
    app.add_handler(CallbackQueryHandler(button_handler))\
\
    print("Moty \'e8 online!")\
    app.run_polling()\
\
if __name__ == '__main__':\
    main()
