from random import choice
import telebot
from telebot import types
from telebot.types import Message
import mysql.connector
from crontab import CronTab

conn = mysql.connector.connect(user="root", password="pass", host="127.0.0.1", database="vagina")
cursor = conn.cursor(buffered=True)


# message.from_user.id это тот от кого пришло данное сообщение
# нажми с зажатой q по тайпс и найди юзер и там все методы которые можно сохранять в бд))
bot = telebot.TeleBot('962102849:AAHmDtPsD8xJrf_6lC0HmfUTpzmz4i9hLuY')
name = ''
family = ''
age = 0
photoNumber = 1
smile = ['😉', '💋', '🙊', '😉', '😏', '😋', '😄', '😁', '😆', '😅', '😂']




# CALLBACK_BUTTON_LEFT:"hui"

#create klaviaturu
# def get_base_inline_keyboard():
#     keyboard = [
#         InlineKeyboardButton (TITLES[CALLBACK_BUTTON_LEFT]) ,callback_data=CALLBACK_BUTTON_LEFT),
#         InlineKeyboardButton(TITLES[CALLBACK_BUTTON_RIGHT]), callback_data = CALLBACK_BUTTON_LEFT)
#     ]
#     return InlineKeyboardButton(keyboard)




@bot.message_handler(content_types=['text', 'document', 'audio'])
# Анотация говорит. что это именно класс Message,
# для возможности автодополнения функций этого класса
# можно также делать со стрингами и т.п.
# в целом можно и строчки туда закинуть пока месэдж не кинул)
def get_text_messages(message: Message):

    if message.text == "Hello" or message.text == "hello" or message.text == "Привет" or message.text == "привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь? " + choice(smile))
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/reg - registration\n"
                                               "/rules -important information \n"
                                               "/sendMem - send mem for you\n"
                                               "or write hello " + smile[1] +
                         "\n/dealFinder - buy sneakers")
    elif message.text == "/reg":
        bot.send_message(message.from_user.id, "Какое ваше имя?")
                         # reply_markup=get_base_inline_keyboard)
        bot.register_next_step_handler(message, name)  # step - шаг
    elif message.text == "/sendMem":
        global photoNumber
        try:
            photo = open('мемы/1 (' + str(photoNumber) + ').png', 'rb')
        except FileNotFoundError:
            print("Не правильный формат (не png)")
        photoNumber += 1
        bot.send_photo(message.from_user.id, photo)
    elif message.text == "/rules":
        bot.forward_message(message.from_user.id, 431073306, 413)
    elif message.text == "/dealFinder":
        bot.register_next_step_handler(message, sellSneakers)
    elif message.text == "hui":
        bot.reply_to(message, message.text.upper())
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def name(message):
    global name  # видимо чтобы присвоить глобальному имени вписанное имя в чатике)
    name = message.text
    bot.send_message(message.from_user.id, "Введите вашу фамилию")
    bot.register_next_step_handler(message, family)


def family(message):
    global family
    family = message.text
    bot.send_message(message.from_user.id, "Введите ваш возраст")
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:  # проверяем что возраст изменился
        try:
            age = int(message.text)  # проверяем, что возраст введен корректно
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    bot.send_message(message.from_user.id, 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + family + '?')
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');  # кнопка «Да»
    keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no');
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + family + '?';
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


def sellSneakers(message):
    pass


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":  # call.data это callback_data, которую мы указали при объявлении кнопки
        ...  # код сохранения данных, или их обработки
        reg_new_user = (
            "INSERT INTO vagina(first_name, surname, age) values (%(first_name)s, %(second_name)s, %(age)s)")
        data_person = {
            'first_name': name,
            'second_name': family,
            'age': age,
        }
        cursor.execute(reg_new_user, data_person)
        conn.commit()
        # тут добавление в таблицу
        bot.send_message(call.message.chat.id, 'Запомню : )');
    elif call.data == "no":
        ...  # переспрашиваем

# эта хуита проводит просто опрос есть ли сообщение каждые 0 секунд
bot.polling(none_stop=True, interval=0)
