
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from flask import Flask
from threading import Thread

# TOKEN del bot
TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"

# Chiavi dei menu
SHOP, WEED, GREENPOISON, FILTRATI, DUBAICHOC, EDIBILI, PAGAMENTI, CONTATTI, REGOLE = range(9)

# Logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Flask web server per Render
app = Flask('')

@app.route('/')
def home():
    return "Bot attivo!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop 🛍️", callback_data=str(SHOP))],
        [InlineKeyboardButton("💰 Pagamenti 💰", callback_data=str(PAGAMENTI))],
        [InlineKeyboardButton("👤 Contattami 👤", callback_data=str(CONTATTI))]
    ]
    update.message.reply_text(
        "Benvenuti nel nostro Bot Ufficiale.\nIl Bot viene costantemente aggiornato con i prodotti disponibili.\nPer qualsiasi informazione o ordini contattare: @theitalianfactory_official",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    data = int(query.data)

    if data == SHOP:
        keyboard = [
            [InlineKeyboardButton("🔥 WEED 🔥", callback_data=str(WEED))],
            [InlineKeyboardButton("🍫 HASH 🍫", callback_data=str(FILTRATI))],
            [InlineKeyboardButton("🍭 EDIBILI 🍭", callback_data=str(EDIBILI))],
            [InlineKeyboardButton("📋 REGOLAMENTO 📋", callback_data=str(REGOLE))],
        ]
        query.edit_message_text("Seleziona il tipo di prodotto:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == WEED:
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA", callback_data="cali")],
            [InlineKeyboardButton("🌴 GREEN POISON", callback_data=str(GREENPOISON))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione di erbe disponibili al momento:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == GREENPOISON:
        photo_url = "https://raw.githubusercontent.com/magichouse18/telegram-bot-magichous8/main/assets/greenpoison.jpeg"
        caption = "🌴GREEN POISON (✅)\n🏡 INDOOR\n\n💰PREZZO:\n10g👉90€\n15g👉125€\n20g👉160€\n30g👉225€\n50g👉375€\n100g👉675€\n200g👉1300€\n500g👉3125€\n\nℹ️Coltivata in serra, cime belle piene. NO SEMI, cime compatte sia tozze sia lunghe"
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]
        query.edit_message_media(
            media=InputMediaPhoto(media=photo_url, caption=caption),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == FILTRATI:
        photo_url = "https://raw.githubusercontent.com/magichouse18/telegram-bot-magichous8/main/assets/dubaichocolate.jpeg"
        caption = "🌏🍫DUBAI CHOCOLATE 73u(✅)\n-FILTRATO 73u\n\n💰PREZZO:\n10g 👉 95€\n15g 👉 125€\n20g 👉 165€\n30g 👉 230€\n50g 👉 370€\n100g 👉 700€\n\nℹ️Profilo Aromatico/Fruttato con note tropicale di agrumi"
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]
        query.edit_message_media(
            media=InputMediaPhoto(media=photo_url, caption=caption),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == EDIBILI:
        keyboard = [
            [InlineKeyboardButton("🇺🇸 VAPE PEN", callback_data="vape")],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("Seleziona il prodotto Edibile disponibile:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == PAGAMENTI:
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]
        query.edit_message_text("💳 Pagamenti disponibili:\n- Contanti\n- Criptovalute\n- Bonifico bancario", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == CONTATTI:
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]
        query.edit_message_text("Per info e ordini: @theitalianfactory_official", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == REGOLE:
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]]
        query.edit_message_text("Leggere attentamente il regolamento prima di ordinare. È necessaria la verifica.", reply_markup=InlineKeyboardMarkup(keyboard))

def main():
    keep_alive()
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
