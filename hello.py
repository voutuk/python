import telebot
import subprocess
import psutil
from secrets import token


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['exec'])
def execute_command(message):
    print (message.chat.id)
    if (message.chat.id == 650550237):
        try:
            result = subprocess.getoutput(message.text[6:])
            bot.reply_to(message, "Result:\n" + result)
        except Exception as e:
            bot.reply_to(message, "An error occurred:\n" + str(e))
    else:
         bot.send_message(message.chat.id, "!=")
    

@bot.message_handler(commands=['status'])
def status_command(message):
    print ("/status id: ", message.chat.id)
    tmp = ("Відсоток використання CPU: " + str(psutil.cpu_percent(interval=5.0)) + "%. ")
    status_id = bot.reply_to(message, tmp)
    while (True):
        bot.edit_message_text(chat_id=message.chat.id, message_id=status_id.message_id, text=("Відсоток використання CPU: " + str(psutil.cpu_percent(interval=5.0)) + "%. "))


@bot.message_handler(commands=['mas'])
def status_command(message):
    tmp = ["a", 2, 6]
    for i in tmp:
        bot.reply_to(message, i)

@bot.message_handler(commands=['spam'])
def status_command(message):
    abc = [1, 2, 3, 4, 5, 6]
    a = 0
    while(a < 5):
        bot.send_message(650550237, a)
        a+=1
    for i in abc:
        bot.send_message(650550237, i)

bot.polling()