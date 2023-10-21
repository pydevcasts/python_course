import telebot

bot = telebot.TeleBot("6610039769:AAGVs_OTo8jGU4XNIWQTxCWd1O59T9jacrA")

@bot.message_handler(commands=["start"])
def send_welcom(message):
    bot.send_message(message.chat.id, "hi")
while True:
    try:

        bot.polling()
    except Exception as e:
        print("erorrr....", e)
    continue