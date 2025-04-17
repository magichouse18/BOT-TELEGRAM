import os
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"

MENU, SHOP, WEED, HASH, EDIBILI, REGOLAMENTO, FILTRATI, FROZEN, CALIUSA, GREENPOISON = range(10)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop 🛍️", callback_data=str(SHOP))],
        [InlineKeyboardButton("💰 Pagamenti 💰", callback_data="pagamenti")],
        [InlineKeyboardButton("🧍 Contattami 🧍", callback_data="contattami")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Benvenuti nel nostro Bot Ufficiale.\n"
        "Il Bot viene costantemente aggiornato con i prodotti disponibili.\n\n"
        "Per qualsiasi informazione o ordini contattare:\n"
        "@magichous8",
        reply_markup=reply_markup
    )

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    data = query.data

    if data == str(SHOP):
        keyboard = [
            [InlineKeyboardButton("🍁 WEED 🍁", callback_data=str(WEED)),
             InlineKeyboardButton("🍫 HASH 🍫", callback_data=str(HASH))],
            [InlineKeyboardButton("🍬 EDIBILI 🍬", callback_data=str(EDIBILI)),
             InlineKeyboardButton("📖 REGOLAMENTO 📖", callback_data=str(REGOLAMENTO))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]
        ]
        query.edit_message_text("Seleziona il servizio per ricevere maggiori informazioni:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(WEED):
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA 🇺🇸", callback_data=str(CALIUSA))],
            [InlineKeyboardButton("🌴 GREEN POISON 🌴", callback_data=str(GREENPOISON))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione delle migliori erbe disponibili al momento:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(CALIUSA):
        query.edit_message_text("Contattaci per conoscere i prodotti disponibili CALI USA.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]))

    elif data == str(GREENPOISON):
        with open("green_poison.jpeg", "rb") as photo:
            query.message.delete()
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=photo,
            caption="🌏🍫DUBAI CHOCOLATE 73u(✅)\n-FILTRATO 73u\n\n💰PREZZO:\n10g 👉 95€\n15g 👉 125€\n20g 👉 165€\n30g 👉 230€\n50g 👉 370€\n100g 👉 700€\n\nℹ️Profilo Aromatico/Fruttato con note tropicale di agrumi",,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]])
        )
                caption="🌴GREEN POISON (✅)\n🏡 INDOOR\n\n💰PREZZO:\n10g👉90€\n15g👉125€\n20g👉160€\n30g👉225€\n50g👉375€\n100g👉675€\n200g👉1300€\n500g👉3125€\n\nℹ️Coltivata in serra, cime belle piene. NO SEMI, cime compatte sia tozze sia lunghe"),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]])
            )

    elif data == str(HASH):
        keyboard = [
            [InlineKeyboardButton("🍫 FILTRATI 🍫", callback_data=str(FILTRATI))],
            [InlineKeyboardButton("❄️ FROZEN ❄️", callback_data=str(FROZEN))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione di hash per tutte le tipologie di smokers:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(FILTRATI):
        with open("dubai_chocolate.jpeg", "rb") as photo:
            query.message.delete()
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=photo,
            caption="🌏🍫DUBAI CHOCOLATE 73u(✅)\n-FILTRATO 73u\n\n💰PREZZO:\n10g 👉 95€\n15g 👉 125€\n20g 👉 165€\n30g 👉 230€\n50g 👉 370€\n100g 👉 700€\n\nℹ️Profilo Aromatico/Fruttato con note tropicale di agrumi",,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]])
        )
                caption="🌏🍫DUBAI CHOCOLATE 73u(✅)\n-FILTRATO 73u\n\n💰PREZZO:\n10g 👉 95€\n15g 👉 125€\n20g 👉 165€\n30g 👉 230€\n50g 👉 370€\n100g 👉 700€\n\nℹ️Profilo Aromatico/Fruttato con note tropicale di agrumi"),
                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]])
            )

    elif data == str(FROZEN):
        query.edit_message_text("Attualmente nessun prodotto disponibile nella categoria FROZEN.", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]]))

    elif data == str(EDIBILI):
        query.edit_message_text("VAPE PEN USA 🇺🇸", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]))

    elif data == str(REGOLAMENTO):
        keyboard = [
            [InlineKeyboardButton("📍 MEET UP 📍", callback_data="meetup")],
            [InlineKeyboardButton("🚗 DELIVERY 🚗", callback_data="delivery")],
            [InlineKeyboardButton("✈️ SHIP ✈️", callback_data="ship")],
            [InlineKeyboardButton("🪪 VERIFICA PRE ORDINE 🪪", callback_data="verifica")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("Leggere attentamente il regolamento sul servizio che desiderate. Prima di qualsiasi ordine vi verrà chiesta la Verifica.", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "pagamenti":
        query.edit_message_text("Accettiamo pagamenti in BTC, Postepay, PayPal e altri metodi su richiesta.")

    elif data == "contattami":
        query.edit_message_text("Per info o ordini: @magichous8")

    elif data == str(MENU):
        start(query, context)

def run_bot():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    Thread(target=run_flask).start()
    run_bot()
