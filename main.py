
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackQueryHandler
import os

TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"
bot = Bot(token=TOKEN)
app = Flask(__name__)

dispatcher = Dispatcher(bot=bot, update_queue=None, workers=0, use_context=True)

START, SHOP, WEED, HASH, EDIBILI, REGOLAMENTO, PAGAMENTI, CONTATTI, GREENPOISON, DUBAICHOC = range(10)

def start(update, context):
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop 🛍️", callback_data=str(SHOP))],
        [InlineKeyboardButton("💰 Pagamenti 💰", callback_data=str(PAGAMENTI))],
        [InlineKeyboardButton("🧍 Contattami 🧍", callback_data=str(CONTATTI))]
    ]
    update.message.reply_text(
        "Benvenuti nel nostro Bot Ufficiale. Il Bot viene costantemente aggiornato con i prodotti disponibili. Per qualsiasi informazione o ordini contattare: @theitalianfactory_official",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def button(update, context):
    query = update.callback_query
    data = int(query.data)
    keyboard = []
    text = ""

    if data == SHOP:
        keyboard = [
            [InlineKeyboardButton("🔥 WEED 🔥", callback_data=str(WEED))],
            [InlineKeyboardButton("🍫 HASH 🍫", callback_data=str(HASH))],
            [InlineKeyboardButton("🍭 EDIBILI 🍭", callback_data=str(EDIBILI))],
            [InlineKeyboardButton("📜 REGOLAMENTO 📜", callback_data=str(REGOLAMENTO))],
        ]
        text = "Seleziona il tipo di prodotto:"
    elif data == WEED:
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA", callback_data="cali")],
            [InlineKeyboardButton("🌴 GREEN POISON", callback_data=str(GREENPOISON))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        text = "La nostra selezione di erbe disponibili al momento:"
    elif data == GREENPOISON:
        text = "🌴GREEN POISON (✅)
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
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]
    elif data == HASH:
        keyboard = [
            [InlineKeyboardButton("🍫 FILTRATI 🍫", callback_data=str(DUBAICHOC))],
            [InlineKeyboardButton("❄️ FROZEN ❄️", callback_data="frozen")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        text = "La nostra selezione di hash per tutte le tipologie di smokers:"
    elif data == DUBAICHOC:
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
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]]
    elif data == EDIBILI:
        keyboard = [
            [InlineKeyboardButton("VAPE PEN", callback_data="vape")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        text = "Selezione disponibile:"
    elif data == REGOLAMENTO:
        text = "Leggere attentamente il regolamento sul servizio che desiderate. Prima di qualsiasi ordine vi verrà chiesta la Verifica."
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]
    elif data == PAGAMENTI:
        text = "Metodi di pagamento accettati:
- Paypal
- Bonifico
- Criptovalute"
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(START))]]
    elif data == CONTATTI:
        text = "Contatta il supporto su Telegram: @theitalianfactory_official"
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(START))]]

    query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(keyboard))

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK"

@app.route("/")
def index():
    return "Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
