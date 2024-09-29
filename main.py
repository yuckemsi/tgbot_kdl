import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot("7717870429:AAGrprdwzRsD_F3v4K6C_yLLTdghXoyEgco") 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")


bot.infinity_polling(none_stop=True)