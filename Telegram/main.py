# 6525989663:AAHiR-VcibUolgmRfUDFHjm2dUm6q47z2FI
from telegram import Bot
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler,  CallbackContext
from telegram.ext import ConversationHandler

# توکن بات خود را وارد کنید
bot_token = '6525989663:AAHiR-VcibUolgmRfUDFHjm2dUm6q47z2FI'

# وضعیت مکالمه
START, GET_CHANNEL_ID, GET_MESSAGE, SEND_MESSAGE = range(4)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "سلام! خوش آمدید. برای شروع، لطفاً /send_message را ارسال کنید تا پیامی به اعضای کانال ارسال کنیم."
    )
    return START

def get_channel_id(update: Update, context: CallbackContext):
    update.message.reply_text("لطفاً آیدی کانال را وارد کنید:")
    return GET_CHANNEL_ID

def get_message(update: Update, context: CallbackContext):
    context.user_data['channel_id'] = update.message.text
    update.message.reply_text("لطفاً پیام خود را وارد کنید:")
    return GET_MESSAGE

def send_message(update: Update, context: CallbackContext):
    channel_id = context.user_data.get('channel_id')
    message = update.message.text

    # اتصال به بات
    bot = Bot(token=bot_token)

    try:
        # ارسال پیام به اعضای کانال
        bot.send_message(chat_id=channel_id, text=message)

        update.message.reply_text("پیام با موفقیت به اعضای کانال ارسال شد.")
    except Exception as e:
        update.message.reply_text('مشکل در ارسال پیام به اعضای کانال:', str(e))

    return ConversationHandler.END

def main():
    # اتصال به بات
    bot = Bot(token=bot_token)

    # ایجاد یک آپدیتر
    updater = Updater(bot=bot,update_queue=True)

    # ایجاد دستورات
    dp = updater
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("send_message", get_channel_id))
    # dp.add_handler(MessageHandler(Filters.text & ~Filters.command, get_message))
    # dp.add_handler(MessageHandler(Filters.text, send_message))

    # شروع گرفتن آپدیت‌ها
    updater.start_polling()

    # خاتمه دهی به برنامه در صورت دریافت Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
