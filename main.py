from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "7829595925:AAFg1zi_RWGPbIEXRTazPuITJso7m36rhpQ"

# --- Costanti per i tasti ---
SHOP, PAGAMENTI, CONTATTI = range(3)
WEED, HASH, EDIBILI, REGOLAMENTO = range(4, 8)
CALI_USA, GREEN_POISON = range(8, 10)
FILTRATI, FROZEN = range(10, 12)
VAPE_PEN = 12

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("🛍️ Shop 🛍️", callback_data=str(SHOP))],
        [InlineKeyboardButton("💰 Pagamenti 💰", callback_data=str(PAGAMENTI))],
        [InlineKeyboardButton("👤 Contattami 👤", callback_data=str(CONTATTI))]
    ]
    update.message.reply_text(
        "Benvenuti nel nostro Bot Ufficiale.\n"
        "Il Bot viene costantemente aggiornato con i prodotti disponibili. "
        "Per qualsiasi informazione o ordini contattare: @theitalianfactory_official 📲",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    data = int(query.data)

    if data == SHOP:
        keyboard = [
            [InlineKeyboardButton("🍁 WEED 🍁", callback_data=str(WEED)),
             InlineKeyboardButton("🍫 HASH 🍫", callback_data=str(HASH))],
            [InlineKeyboardButton("🍭 EDIBILI 🍭", callback_data=str(EDIBILI)),
             InlineKeyboardButton("📖 REGOLAMENTO 📖", callback_data=str(REGOLAMENTO))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data="start")]
        ]
        query.edit_message_text("Seleziona il servizio per ricevere maggiori informazioni.",
                                reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == WEED:
        keyboard = [
            [InlineKeyboardButton("🇺🇸 CALI USA 🇺🇸", callback_data=str(CALI_USA))],
            [InlineKeyboardButton("🌴 GREEN POISON 🌴", callback_data=str(GREEN_POISON))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione delle migliori erbe disponibili al momento:",
                                reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == GREEN_POISON:
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=open("green_poison.jpeg", "rb"),
            caption=(
                "🌴 GREEN POISON (✅)\n🏡 INDOOR\n\n"
                "💰PREZZO:\n"
                "10g👉90€\n15g👉125€\n20g👉160€\n30g👉225€\n"
                "50g👉375€\n100g👉675€\n200g👉1300€\n500g👉3125€\n\n"
                "ℹ️ Coltivata in serra, cime belle piene. NO SEMI, cime compatte sia tozze sia lunghe."
            ),
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]])
        )

    elif data == CALI_USA:
        query.edit_message_text("🧪 Sezione in aggiornamento!",
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(WEED))]]))

    elif data == HASH:
        keyboard = [
            [InlineKeyboardButton("🍫 FILTRATI 🍫", callback_data=str(FILTRATI))],
            [InlineKeyboardButton("❄️ FROZEN ❄️", callback_data=str(FROZEN))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("La nostra selezione di hash per tutte le tipologie di smokers:",
                                reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == FILTRATI:
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=open("dubai_chocolate.jpeg", "rb"),
            caption=(
                "🌏🍫DUBAI CHOCOLATE 73u (✅)\n-FILTRATO 73u\n\n"
                "💰PREZZO:\n10g 👉 95€\n15g 👉 125€\n20g 👉 165€\n30g 👉 230€\n"
                "50g 👉 370€\n100g 👉 700€\n\n"
                "ℹ️Profilo Aromatico/Fruttato con note tropicale di agrumi"
            ),
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]])
        )

    elif data == FROZEN:
        query.edit_message_text("❄️ Sezione FROZEN al momento non disponibile ❄️",
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(HASH))]]))

    elif data == EDIBILI:
        keyboard = [
            [InlineKeyboardButton("VAPE PEN", callback_data=str(VAPE_PEN))],
            [InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]
        ]
        query.edit_message_text("Sezione edibili disponibile:",
                                reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == REGOLAMENTO:
        query.edit_message_text(
            "Leggere attentamente il regolamento sul servizio che desiderate. "
            "Prima di qualsiasi ordine vi verrà richiesta la Verifica.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(SHOP))]])
        )

    elif data == PAGAMENTI:
        query.edit_message_text("💳 Metodo di pagamento disponibile: solo criptovalute.",
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data="start")]]))

    elif data == CONTATTI:
        query.edit_message_text("Contattaci su Telegram: @theitalianfactory_official",
                                reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data="start")]]))

    elif data == VAPE_PEN:
        query.edit_message_text(
            "JEETER JUICE 1G THC PODS 🧪\n"
            "~ Slurricane\n~ Chemdog\n~ Banana Mango\n~ Lemon Drop\n\n"
            "1pz → 60€\n2pz → 100€\n5pz → 225€\n10pz → 400€\n50pz → 1750€\n100pz → 2700€\n\n"
            "Vere penne da Cali con QR e marchio originale. No fake homemade.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Indietro", callback_data=str(EDIBILI))]])
        )

    elif query.data == "start":
        start(update, context)

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
