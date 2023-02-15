import telebot

bot = telebot.TeleBot("6121717828:AAEdweid9pNEbbLCJZvGomf8HBW80RJvAxU")

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.send_message(message, "Howdy, how are you doing?")

 @bot.message_handler(commands=['help'])
 def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "привет" :
        bot.send_message(message.from_user.id, "привет,как дела")
    elif message.text == "хорошо" or message.text == "нормально" :
       bot.send_message(message.from_user.id, " у меня тоже")

  
print("bot started")
bot.infinity_polling()