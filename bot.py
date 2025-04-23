import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = ("8087961436:AAGlF0kYCl8Fn-UAr3OclgUCJdke5yMeKUg")
# ——— MENU PRINCIPALE ———
def get_main_menu():
    keyboard = [
        [InlineKeyboardButton("💡 Acquista pacchetti prompt", callback_data="acquista_pacchetti")],
        [InlineKeyboardButton("🤖 Quiz automatico", callback_data="quiz_consulenza")],
        [InlineKeyboardButton("💳 Acquista con Stripe", callback_data="pagamenti")],
        [InlineKeyboardButton("✨ Branding & Social", callback_data="branding")]
    ]
    return InlineKeyboardMarkup(keyboard)

def add_menu_button(keyboard):
    keyboard.append([InlineKeyboardButton("🔙 Menu", callback_data="menu")])
    return InlineKeyboardMarkup(keyboard)

# ——— START ———
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono Moty 🤖", reply_markup=get_main_menu())

# ——— CALLBACKS ———
async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "menu":
        await query.edit_message_text("Menu principale:", reply_markup=get_main_menu())

    elif data == "acquista_pacchetti":
        keyboard = [
            [InlineKeyboardButton("📦 Starter", callback_data="starter")],
            [InlineKeyboardButton("🚀 Pro", callback_data="pro")],
            [InlineKeyboardButton("🏆 Master", callback_data="master")]
        ]
        await query.edit_message_text("Scegli un pacchetto:", reply_markup=add_menu_button(keyboard))

    elif data == "starter":
        text = "📦 **Starter Pack**:\n5 prompt originali + guida PDF per iniziare a vendere. Prezzo: 5€"
        await query.edit_message_text(text, reply_markup=add_menu_button([]))

    elif data == "pro":
        text = "🚀 **Pro Pack**:\n15 prompt avanzati + strategie di vendita + supporto Telegram. Prezzo: 15€"
        await query.edit_message_text(text, reply_markup=add_menu_button([]))

    elif data == "master":
        text = "🏆 **Master Pack**:\nTutti i prompt + 1 consulenza + accesso aggiornamenti. Prezzo: 30€"
        await query.edit_message_text(text, reply_markup=add_menu_button([]))

    elif data == "quiz_consulenza":
        await query.edit_message_text("🧠 Il quiz automatico è in sviluppo!", reply_markup=add_menu_button([]))

    elif data == "pagamenti":
        await query.edit_message_text("💳 Supporto Stripe e Telegram Payments in arrivo!", reply_markup=add_menu_button([]))

    elif data == "branding":
        await query.edit_message_text("📱 Consulenza su branding e social media disponibile presto!", reply_markup=add_menu_button([]))

# ——— AVVIO APP ———
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))

    app.run_webhook(
        listen="0.0.0.0",
        port=10000,
        webhook_url=f"{WEBHOOK_BASE_URL}/webhook"
    )

if __name__ == "__main__":
    main()
