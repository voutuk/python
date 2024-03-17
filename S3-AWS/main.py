import boto3, random, telebot, os
from secrets import access_key, secret_key, key

bot = telebot.TeleBot(key)

def upload_file(file_name, bucket, usr_id=None):
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name="eu-north-1")
    rand_num = random.randint(0, 1000000)
    s3.upload_file(file_name, bucket, str(usr_id)+"|"+str(rand_num)+".jpg")
    return rand_num

@bot.message_handler(content_types=['document'])
def handle_docs_photo(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("new_file.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, upload_file("new_file.jpg", "voutuks", message.from_user.id))

@bot.message_handler(commands=['list'])
def list_command(message):
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name="eu-north-1")

    response = s3.list_objects_v2(Bucket="voutuks", Prefix=str(message.from_user.id))
    if 'Contents' in response:
        for obj in response['Contents']:
            bot.send_message(message.chat.id, obj['Key'])
    else:
        bot.send_message(message.chat.id, "No files")
    

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        file_key = str(message.chat.id) + "|" + message.text + ".jpg"
        s3.download_file("voutuks", file_key, "tmp.jpg")
        photo = open("tmp.jpg", 'rb')
        bot.send_photo(message.chat.id, photo)
        photo.close()
        os.remove("tmp.jpg")
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        bot.reply_to(message, error_message)
    
@bot.message_handler(commands=['delete'])
def handle_delete_command(message):
    if message.reply_to_message:
        print
        s3 = boto3.client('voutuks', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name="eu-north-1")
        
        s3.delete_object("voutuks", str(message.chat.id) + "|" + message.reply_to_message.text + ".jpg")

    else:
        bot.reply_to(message, "Потрібно вибрати повідомлення.")

bot.polling()
