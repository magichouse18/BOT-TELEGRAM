
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

# === CONFIG ===
TOKEN = "INSERISCI_IL_TUO_TOKEN"
WEED = "weed"
GREENPOISON = "green_poison"
CALIUSA = "cali_usa"
SHOP = "shop"

# === HANDLER PRINCIPALE ===
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🌿 WEED 🌿", callback_data=WEED)],
    ]
    update.message.reply_text("Benvenuto! Seleziona una categoria:", reply_markup=InlineKeyboardMarkup(keyboard))

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = query.data

    if data == WEED:
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA 🇺🇸", callback_data=CALIUSA)],
            [InlineKeyboardButton("🌴 GREEN POISON 🌴", callback_data=GREENPOISON)],
            [InlineKeyboardButton("⬅️ Indietro", callback_data="start")]
        ]
        query.edit_message_text("La nostra selezione delle migliori erbe disponibili al momento:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == GREENPOISON:
        query.message.delete()
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=open("green_poison.jpg", "rb"),
            caption="🌴 GREEN POISON (✅)
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
        )
        context.bot.send_message(
            chat_id=query.message.chat_id,
            text="La nostra selezione delle migliori erbe disponibili al momento:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🇺🇸 CALI USA 🇺🇸", callback_data=CALIUSA)],
                [InlineKeyboardButton("🌴 GREEN POISON 🌴", callback_data=GREENPOISON)],
                [InlineKeyboardButton("⬅️ Indietro", callback_data=WEED)]
            ])
        )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
