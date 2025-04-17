
import os
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.utils.request import Request
import logging

TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"
bot = Bot(token=TOKEN) if "sent" not in locals() else None

app = Flask(__name__)

# Set webhook URL (Render specific)
WEBHOOK_URL = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/webhook"

# Dispatcher
dispatcher = Dispatcher(bot, None, workers=1)

# States
MENU, SHOP, WEED, HASH, EDIBILI, REGOLAMENTO, FILTRATI, FROZEN, CALIUSA, GREENPOISON = range(10)

@app.route("/")
def home():
    return "Bot attivo con webhook!"

@app.route('/webhook', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

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
            sent = 
            context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=photo,
                caption="""🌴GREEN POISON (✅)
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

ℹ️Coltivata in serra, cime belle piene. NO SEMI, cime compatte sia tozze sia lunghe""",
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
            sent = 
            context.bot.send_photo(
                chat_id=query.message.chat_id,
                photo=photo,
                caption="""🌏🍫DUBAI CHOCOLATE 73u(✅)
-FILTRATO 73u

💰PREZZO:
10g 👉 95€
15g 👉 125€
20g 👉 165€
30g 👉 230€
50g 👉 370€
100g 👉 700€

ℹ️Profilo Aromatico/Fruttato con note tropicale di agrumi""",
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
        query.edit_message_text(
        "Accettiamo pagamenti in BTC, Postepay, PayPal e altri metodi su richiesta.",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]])
    )

    elif data == "contattami":
        query.edit_message_text(
        "Per info o ordini: @magichous8",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]])
    )

    elif data == str(MENU):
        start(query, context)

# Handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button))

if __name__ == "__main__":
    bot.delete_webhook()
    bot.set_webhook(WEBHOOK_URL)
    app.run(host="0.0.0.0", port=10000)
