
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Callback data constants
MENU, WEED, GREENPOISON, CALIUSA, FILTRATI, DUBAI, EDIBILI, CONTATTI, PAGAMENTI, BACK = range(10)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔥 WEED 🔥", callback_data=str(WEED))],
        [InlineKeyboardButton("🍫 FILTRATI 🍫", callback_data=str(FILTRATI))],
        [InlineKeyboardButton("🍬 EDIBILI 🍬", callback_data=str(EDIBILI))],
        [InlineKeyboardButton("📞 CONTATTI 📞", callback_data=str(CONTATTI))],
        [InlineKeyboardButton("💳 PAGAMENTI 💳", callback_data=str(PAGAMENTI))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Benvenuto! Scegli una sezione dal menu:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = int(query.data)

    if data == MENU:
        return await start(query, context)

    elif data == WEED:
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA", callback_data=str(CALIUSA))],
            [InlineKeyboardButton("🌴 GREEN POISON", callback_data=str(GREENPOISON))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]
        ]
        await query.edit_message_text("Seleziona la categoria WEED:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == GREENPOISON:
        text = "🌴 GREEN POISON (✅)
🏡 INDOOR

💰 PREZZO:
10g 👉 90€
15g 👉 125€
20g 👉 160€
30g 👉 225€
50g 👉 375€
100g 👉 675€
200g 👉 1300€
500g 👉 3125€

ℹ️ Coltivata in serra, cime belle piene. NO SEMI, cime compatte sia tozze sia lunghe"
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]
        await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == CALIUSA:
        await query.edit_message_text("💨 CALI USA - in arrivo!", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]))

    elif data == FILTRATI:
        text = "🌏🍫DUBAI CHOCOLATE 73u(✅)
-FILTRATO 73u

💰PREZZO:
10g 👉 95€
15g 👉 125€
20g 👉 165€
30g 👉 230€
50g 👉 370€
100g 👉 700€

ℹ️ Profilo Aromatico/Fruttato con note tropicale di agrumi"
        keyboard = [[InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]]
        await query.edit_message_caption(caption=text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == EDIBILI:
        await query.edit_message_text("🍬 VAPE PEN disponibile", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]]))

    elif data == CONTATTI:
        await query.edit_message_text("Contattaci su Telegram: @yourtelegramlink", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]]))

    elif data == PAGAMENTI:
        await query.edit_message_text("Metodi di pagamento:
- PayPal
- Bitcoin
- Ricarica", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(MENU))]]))

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == "__main__":
    main()
