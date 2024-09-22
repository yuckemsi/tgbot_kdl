import telebot
import cfg

bot = telebot.TeleBot(cfg.TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "ПРИВ ЛОЛ")

@bot.message_handler(commands=['help'])
def send_help(message):
    img = open("C:/Users/yucke/Downloads/img.jpg", 'rb')
    bot.send_photo(message.chat.id, img, "фотка лол")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Информация о боте:')

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



bot.infinity_polling()