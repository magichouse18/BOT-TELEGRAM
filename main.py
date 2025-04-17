from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler, Updater

TOKEN = "inserisci_il_tuo_token_qui"

# Costanti per i tasti
SHOP, WEED, HASH, EDIBILI, REGOLAMENTO, PAGAMENTI, CONTATTI = range(7)
GREENPOISON, CALIUSA = range(7, 9)

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop 🛍️", callback_data=str(SHOP))],
        [InlineKeyboardButton("💰 Pagamenti 💰", callback_data=str(PAGAMENTI))],
        [InlineKeyboardButton("👤 Contattami 👤", callback_data=str(CONTATTI))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Benvenuti nel nostro Bot Ufficiale. Il Bot viene costantemente aggiornato con i prodotti disponibili. Per qualsiasi informazione o ordini contattare: @theitalianfactory_official 📲",
        reply_markup=reply_markup,
    )

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = int(query.data)

    if data == SHOP:
        keyboard = [
            [InlineKeyboardButton("🍁 WEED 🍁", callback_data=str(WEED))],
            [InlineKeyboardButton("🍫 HASH 🍫", callback_data=str(HASH))],
            [InlineKeyboardButton("🍬 EDIBILI 🍬", callback_data=str(EDIBILI))],
            [InlineKeyboardButton("📖 REGOLAMENTO 📖", callback_data=str(REGOLAMENTO))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data="/start")],
        ]
        query.edit_message_text("Seleziona il servizio per ricevere maggiori informazioni.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == WEED:
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA 🇺🇸", callback_data=str(CALIUSA))],
            [InlineKeyboardButton("🌴 GREEN POISON 🌴", callback_data=str(GREENPOISON))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))],
        ]
        query.edit_message_text("La nostra selezione delle migliori erbe disponibili al momento:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == GREENPOISON:
        query.message.delete()
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=open("green_poison.jpg", "rb"),
            caption=(
                """🌴 GREEN POISON (✅)
🏡 INDOOR

💰PREZZO:
10g👉90€
15g👉125€
20g👉160€
30g👉225€
50g👉375€
100g👉675€
200g👉1300€
500g👉3125€

ℹ️Coltivata in serra, cime belle piene. NO SEMI, cime compatte sia tozze sia lunghe"""
            ),
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]
            ),
        )

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()