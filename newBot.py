import telebot
from telebot.types import Message

TOKEN = '962102849:AAHmDtPsD8xJrf_6lC0HmfUTpzmz4i9hLuY'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text', 'document', 'audio'])
#Анотация. что это именно класс Message,
# для возможности автодополнения функций этого класса
# можно также делать со стрингами и т.п.
#в целом можно и строчки туда закинуть пока месэдж не кинул)
def upper (message  : Message):
    pass

bot.polling()