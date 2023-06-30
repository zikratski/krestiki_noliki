import numpy as np
import telebot

import algo
import play, graphic
from telebot import types

# Определяем переменные, ответственные за режим игры, её сложность и размер поля
# Первоначальное значение None, т.к. пользователь ничего не выбрал
mode = None
difficult = None
field = None
symbol_person = None
symbol_ai = None
graphics_mode = "standart"


# Токена для телеграмма
bot = telebot.TeleBot('6064467428:AAF8R7L7dLDJQ_3OqoJSxwWZYE_IeVmxfKQ')
# КНОПКИ В БОТЕ

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Начать игру")
    btn2 = types.KeyboardButton("Задать вопрос")
    btn3 = types.KeyboardButton("Авторы проекта")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text= f"Привет! Я тестовый бот для тебя, {message.from_user.first_name}!", reply_markup=markup)
    photo = open('C:/Users/Kirill/Desktop/XsOs.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['text'])
def func(message):
    global mode
    global difficult
    global field
    global symbol_person
    global symbol_ai
    global graphics_mode
    if (message.text == "Начать игру"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

#Выбор режима игры и сохранение в переменную mode
        bot_mode = types.KeyboardButton("c ботом")
        people_mode = types.KeyboardButton("c другом(одно устройство)")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bot_mode, people_mode, back)
        bot.send_message(message.chat.id, text='Выберите режим игры: ', reply_markup=markup)

# Если пользователь выбрал 'с ботом', то далее выбирает сложность игры(лёгкий, анриал)
# Доступен выбор возврата к предыдущему выбору и к выходу в главное меню
    elif message.text == "c ботом":
        mode = "c ботом"
        bot.send_message(message.chat.id, "Вы будете играть <i>с ботом</i>", parse_mode='HTML')
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton("Лёгкий")
        b2 = types.KeyboardButton("Анриал(бот унижает)")
        back = types.KeyboardButton("Вернуться к выбору режима")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(b1, b2, back, back_to_menu)
        bot.send_message(message.chat.id, text="Выберите сложность бота: ", reply_markup=kb)

# Если выбрана кнопка Вернуться к выбору режима
    elif (message.text == "Вернуться к выбору режима"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot_mode = types.KeyboardButton("c ботом")
        people_mode = types.KeyboardButton("c другом(одно устройство)")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bot_mode, people_mode, back)
        bot.send_message(message.chat.id, text='Выберите режим игры: ', reply_markup=markup)

# Если пользователь выбрал режим Лёгкий
    elif (message.text == "Лёгкий"):
        difficult = "Лёгкий"
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back = types.KeyboardButton("Вернуться к выбору сложности")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(button1, button2, back, back_to_menu)
        bot.send_message(message.chat.id, text="Выберите размер игрового поля: ", reply_markup=keyboard)


    elif (message.text == "Вернуться к выбору сложности"):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton("Лёгкий")
        b2 = types.KeyboardButton("Анриал(бот унижает)")
        back = types.KeyboardButton("Вернуться к выбору режима")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(b1, b2, back, back_to_menu)
        bot.send_message(message.chat.id, text="Выберите сложность бота: ", reply_markup=kb)

# Если пользователь выбрал 3x3
    elif (message.text == "3x3"):
        field = "3x3"
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Крестики")
        btn2 = types.KeyboardButton("Нолики")
        btn3 = types.KeyboardButton("Дамблдор")
        btn4 = types.KeyboardButton("Северус Снегг")
        kb.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Выберите за кого хотите играть: ", reply_markup=kb)

# Выбор фигуры, за которую будет играть пользователь и ИИ

    elif (message.text == "Крестики"):
        symbol_person = 1
        symbol_ai = 2
        msg = bot.send_message(message.chat.id, text="Вы - Крестики\nБот - Нолики")
        bot.register_next_step_handler(msg, play_bot)
    elif (message.text == "Нолики"):
        symbol_person = 2
        symbol_ai = 1
        msg = bot.send_message(message.chat.id, text="Вы - Нолики\nБот - Крестики")
        bot.register_next_step_handler(msg, play_bot)
    elif (message.text == "Дамблдор"):
        symbol_person = 1
        symbol_ai = 2
        graphics_mode = "HP"
        msg = bot.send_message(message.chat.id, text="Вы - Дамблдор\nБот - Северус Снегг")
        bot.register_next_step_handler(msg, play_bot)
    elif (message.text) == "Северус Снегг":
        symbol_person = 2
        symbol_ai = 1
        graphics_mode = "HP"
        msg = bot.send_message(message.chat.id, text="Вы - Северус Снегг\nБот - Дамблдор")
        bot.register_next_step_handler(msg, play_bot)



    elif (message.text == "Авторы проекта" or message.text == "/authors"):
        bot.send_message(message.chat.id, text="Этот бот был создан Кириллом, Лерой, Антоном и Ильей ")


    elif (message.text == "Задать вопрос" or message.text == "/question"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "Бот для игры в крестики-нолики!!!!")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Я почти готов играть с тобой 🚀")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("Начать игру")
        button2 = types.KeyboardButton("Задать вопрос")
        button3 = types.KeyboardButton("Авторы проекта")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


#Функция для игры в крестики-нолики(in future)

def play_bot(mode, difficult, field, symbol_person, symbol_ai, graphics_mode):
    algo.check_tie()
    matr = np.zeros_like(np.eye(int(field[0])))
    while True:
    # кидает картинку в чат используя graphic.graph(matr)
    #pers_move =  принимает координаты пользователя
    pers_move = None
    matr[pers_move[0]][pers_move[1]] = symbol_person
    #рисует картинку
    ai_move = play.comp_move(matr,level=difficult,ai=symbol_ai,pers=symbol_person)
    matr[ai_move[0]][ai_move[1]] = symbol_ai
    # рисует картинку
    else:
        pass


if __name__ == "__main__":
    # бесконечная работа бота

    bot.infinity_polling()



