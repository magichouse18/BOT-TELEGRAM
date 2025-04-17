from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import os

TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"
bot = Bot(token=TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

START, SHOP, WEED, HASH, EDIBILI, REGOLAMENTO, PAGAMENTI, CONTATTI, GREENPOISON, DUBAI = range(10)

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop 🛍️", callback_data=str(SHOP))],
        [InlineKeyboardButton("💰 Pagamenti 💰", callback_data=str(PAGAMENTI))],
        [InlineKeyboardButton("🧑‍💻 Contattami 🧑‍💻", callback_data=str(CONTATTI))]
    ]
    update.message.reply_text(
        "Benvenuti nel nostro Bot Ufficiale. Il Bot viene costantemente aggiornato con i prodotti disponibili. Per qualsiasi informazione o ordini contattare: @theitalianfactory_official 📲",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def button(update, context):
    query = update.callback_query
    data = query.data
    query.answer()

    if data == str(SHOP):
        keyboard = [
            [InlineKeyboardButton("🌿 WEED 🌿", callback_data=str(WEED))],
            [InlineKeyboardButton("💎 HASH 💎", callback_data=str(HASH))],
            [InlineKeyboardButton("🍫 EDIBILI 🍫", callback_data=str(EDIBILI))],
            [InlineKeyboardButton("📄 REGOLAMENTO 📄", callback_data=str(REGOLAMENTO))],
        ]
        query.edit_message_text("Seleziona il reparto che ti interessa:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(WEED):
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA", callback_data="cali")],
            [InlineKeyboardButton("🌴 GREEN POISON", callback_data=str(GREENPOISON))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione di erbe disponibili al momento:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(GREENPOISON):
        text = "🌴 GREEN POISON (✅)
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

ℹ️Coltivata in serra, cime belle piene. NO SEMI, cime compatte sia tozze sia lunghe"
        context.bot.send_message(chat_id=query.message.chat_id, text=text)
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]
        context.bot.send_message(chat_id=query.message.chat_id, text="⬅️ Torna indietro:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(HASH):
        keyboard = [
            [InlineKeyboardButton("🍫 FILTRATI 🍫", callback_data=str(DUBAI))],
            [InlineKeyboardButton("❄️ FROZEN ❄️", callback_data="frozen")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione di hash per tutte le tipologie di smokers:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(DUBAI):
        text = "🌏🍫DUBAI CHOCOLATE 73u(✅)
-FILTRATO 73u

💰PREZZO:
10g 👉 95€
15g 👉 125€
20g 👉 165€
30g 👉 230€
50g 👉 370€
100g 👉 700€

ℹ️Profilo Aromatico/Fruttato con note tropicale di agrumi"
        context.bot.send_message(chat_id=query.message.chat_id, text=text)
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]]
        context.bot.send_message(chat_id=query.message.chat_id, text="⬅️ Torna indietro:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(EDIBILI):
        keyboard = [
            [InlineKeyboardButton("VAPE PEN", callback_data="vape")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("Prodotti Edibili disponibili:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(PAGAMENTI):
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(START))]]
        query.edit_message_text("Metodi di pagamento disponibili: ...", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == str(CONTATTI):
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(START))]]
        query.edit_message_text("Contattaci su Telegram: @theitalianfactory_official", reply_markup=InlineKeyboardMarkup(keyboard))

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/")
def home():
    return "Bot attivo!"

if __name__ == "__main__":
    bot.set_webhook("https://<YOUR_RENDER_URL>/" + TOKEN)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
