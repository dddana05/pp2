import telebot
from telebot import types

bot = telebot.TeleBot("6262892158:AAFWSiJYbbuBPEm21YTDfeZRLzfJzQfXYFc")

my_list= {
 'contacts':['mam', 'dad', 'sis'] ,
 'schedule':['monday', 'tuesday', 'wednesday', 'thrusday', 'friday'] ,
 'groups':['skz', 'enhypen', 'svt']
}

def markup(my_list):
 mak1=types.ReplyKeyboardMarkup()
 for i in my_list:
  mark=types.KeyboardButton(i)
  mak1.add(mark)
 return mak1


markup2 = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('Понедельник')
itembtnv = types.KeyboardButton('Вторник')
itembtnc = types.KeyboardButton('Среда')

markup2.add(itembtna, itembtnv , itembtnc)

   

@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.send_message(message.from_user.id,"Hi, what do you need?", reply_markup=markup(my_list))

@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.reply_to(message, "Howdy, how are you doing?")




@bot.message_handler(func=lambda message: True)
def echo_all(message):
 bot.reply_to(message, message.text)

print("Bot started")
bot.infinity_polling()