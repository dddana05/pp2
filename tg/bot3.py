import telebot 
 
bot = telebot.TeleBot("6130025056:AAHLQ2BMyCnSkmakY4uNXjAd_P3WxVeFUHU") 
 
@bot.message_handler(commands=['start', 'help']) 
def send_welcome(message): 
 bot.reply_to(message, "Howdy, how are you doing?") 
 
@bot.message_handler(func=lambda message: True) 
def echo_all(message): 
 if message.text =="hello": 
  bot.reply_to(message, "Hello, How are u?") 
 elif message.text =="Good" or message.text=="not bad": 
  bot.reply_to(message, "good, good") 
 bot.reply_to(message, message.text) 
 
 print("bot started")
bot.infinity_polling()