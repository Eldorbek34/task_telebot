from telebot import Update, ForceReply
from telebot.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from datetime import datetime

# Start komandasi
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_html(
        rf'Assalomu alaykum {user.mention_html()}!',
        reply_markup=ForceReply(selective=True),
    )

# Help komandasi
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bu bot sizga yordam beradi. Mavjud buyruqlar:\n/start - Botni ishga tushirish\n/help - Yordam\n/info - Ma’lumot\n/caps <matn> - Matnni katta harflarga aylantirish\n/time - Hozirgi vaqtni ko‘rsatish')

# Info komandasi
def info_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bu bot Telegram API orqali ishlaydi va Python dasturlash tili yordamida yaratilgan.')

# Caps komandasi
def caps_command(update: Update, context: CallbackContext) -> None:
    text_caps = ' '.join(context.args).upper()
    update.message.reply_text(text_caps)

# Time komandasi
def time_command(update: Update, context: CallbackContext) -> None:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    update.message.reply_text(f"Hozirgi vaqt: {current_time}")

# Ekhomenlik funksiyasi
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Asosiy funksiya
def main() -> None:
    # Bot tokenini kiriting
    updater = Updater("YOUR_TOKEN_HERE")

    # Dispatcher va Handlerlar
    dispatcher = updater.dispatcher

    # /start komandasi uchun handler
    dispatcher.add_handler(CommandHandler("start", start))

    # /help komandasi uchun handler
    dispatcher.add_handler(CommandHandler("help", help_command))

    # /info komandasi uchun handler
    dispatcher.add_handler(CommandHandler("info", info_command))

    # /caps komandasi uchun handler
    dispatcher.add_handler(CommandHandler("caps", caps_command))

    # /time komandasi uchun handler
    dispatcher.add_handler(CommandHandler("time", time_command))

    # Matn xabarlari uchun handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Botni ishga tushirish
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
