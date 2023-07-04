import numpy as np
import telebot

import algo, algo2
import play
import graphic
from telebot import types

# Определяем переменные, ответственные за режим игры, её сложность и размер поля
# Первоначальное значение None, т.к. пользователь ничего не выбрал
mode = None
difficult = None
field = None
symbol_person = None
symbol_ai = None
graphics_mode = "standart"
dict_commands = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}
matr = np.array(list())
flag = True
flag2 = True


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
    #photo = open('C:/Users/Kirill/Desktop/XsOs.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['text'])
def choose_func(message):
    if (message.text == "Начать игру"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        #Выбор режима игры и сохранение в переменную mode
        bot_mode = types.KeyboardButton("c ботом")
        people_mode = types.KeyboardButton("c другом(одно устройство)")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bot_mode, people_mode, back)
        msg = bot.send_message(message.chat.id, text='Выберите режим игры: ', reply_markup=markup)
        bot.register_next_step_handler(msg, choose_gamemode)

    elif (message.text == "Авторы проекта" or message.text == "/authors"):
        bot.send_message(message.chat.id, text="Этот бот был создан Кириллом, Лерой, Антоном и Ильей ")

    elif (message.text == "Задать вопрос" or message.text == "/question"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        msg = bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
        bot.register_next_step_handler(msg, choose_question)

def return_menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Задать вопрос")
        btn3 = types.KeyboardButton("Авторы проекта")
        markup.add(btn1, btn2, btn3)
        msg = bot.send_message(message.chat.id, text= f"Привет! Я тестовый бот для тебя, {message.from_user.first_name}!", reply_markup=markup)
        bot.register_next_step_handler(msg, choose_func)

def choose_question(message):

    if (message.text == "Как меня зовут?"):
        msg = bot.send_message(message.chat.id, "Бот для игры в крестики-нолики!!!!")
        bot.register_next_step_handler(msg, choose_question)

    elif message.text == "Что я могу?":
        msg = bot.send_message(message.chat.id, text="Я почти готов играть с тобой 🚀")
        bot.register_next_step_handler(msg, choose_question)

    elif (message.text == "Вернуться в главное меню"):
        return_menu(message)

def choose_gamemode(message):
    global mode
    # Если пользователь выбрал 'с ботом', то далее выбирает сложность игры(лёгкий, анриал)
    # Доступен выбор возврата к предыдущему выбору и к выходу в главное меню
    if message.text == "c ботом":
        mode = "c ботом"
        bot.send_message(message.chat.id, "Вы будете играть <i>с ботом</i>", parse_mode='HTML')
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton("Лёгкий")
        b2 = types.KeyboardButton("Анриал(бот унижает)")
        back = types.KeyboardButton("Вернуться к выбору режима")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(b1, b2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите сложность бота: ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_difficulty)

    elif message.text == "c другом(одно устройство)":
        mode = "c другом"
        msg = bot.send_message(message.chat.id, "Вы будете играть <i>с другом</i>", parse_mode='HTML')
        bot.register_next_step_handler(msg, choose_field)

    elif (message.text == "Вернуться в главное меню"):
        return_menu(message)

def choose_difficulty(message):
    global difficult

# Если пользователь выбрал режим Лёгкий
    if (message.text == "Лёгкий"):
        difficult = "easy"
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back = types.KeyboardButton("Вернуться к выбору сложности")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(button1, button2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер игрового поля: ", reply_markup=keyboard)
        bot.register_next_step_handler(msg, choose_field)

    elif (message.text == "Анриал(бот унижает)"):
        difficult = "extreme"
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back = types.KeyboardButton("Вернуться к выбору сложности")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(button1, button2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер игрового поля: ", reply_markup=keyboard)
        bot.register_next_step_handler(msg, choose_field)

    elif (message.text == "Вернуться в главное меню"):
        return_menu(message)

    elif (message.text == "Вернуться к выбору режима"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot_mode = types.KeyboardButton("c ботом")
        people_mode = types.KeyboardButton("c другом(одно устройство)")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bot_mode, people_mode, back_to_menu)
        msg = bot.send_message(message.chat.id, text='Выберите режим игры: ', reply_markup=markup)
        bot.register_next_step_handler(msg, choose_gamemode)


# Если пользователь выбрал 3x3
def choose_field(message):
    if (message.text == "3x3"):
        global field
        global matr
        field = "3x3"
        matr = np.zeros_like(np.eye(int(field[0])))
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Крестики")
        btn2 = types.KeyboardButton("Нолики")
        btn3 = types.KeyboardButton("Дамблдор")
        btn4 = types.KeyboardButton("Северус Снегг")
        back = types.KeyboardButton("Вернуться к выбору поля")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(btn1, btn2, btn3, btn4, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите за кого хотите играть: ", reply_markup=keyboard)
        bot.register_next_step_handler(msg, choose_figure)

    elif (message.text == "Бесконечное(в разработке)"):
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back = types.KeyboardButton("Вернуться к выбору сложности")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(button1, button2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Услуга стоит 2,49$ ", reply_markup=keyboard)
        bot.register_next_step_handler(msg, choose_field)

    elif (message.text == "Вернуться к выбору сложности"):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton("Лёгкий")
        b2 = types.KeyboardButton("Анриал(бот унижает)")
        back = types.KeyboardButton("Вернуться к выбору режима")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(b1, b2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите сложность бота: ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_difficulty)

    elif (message.text == "Вернуться в главное меню"):
        return_menu(message)


# Выбор фигуры, за которую будет играть пользователь и ИИ
def choose_figure(message):
    global symbol_person
    global symbol_ai
    global graphics_mode
    global btns
    global flag

    if (message.text == "Крестики"):
        symbol_person = 1
        symbol_ai = 2
        bot.send_message(message.chat.id, text="Вы - Крестики\nБот - Нолики")

    elif (message.text == "Нолики"):
        symbol_person = 2
        symbol_ai = 1
        bot.send_message(message.chat.id, text="Вы - Нолики\nБот - Крестики")

    elif (message.text == "Дамблдор"):
        symbol_person = 1
        symbol_ai = 2
        graphics_mode = "HP"
        bot.send_message(message.chat.id, text="Вы - Дамблдор\nБот - Северус Снегг")

    elif (message.text) == "Северус Снегг":
        symbol_person = 2
        symbol_ai = 1
        graphics_mode = "HP"
        bot.send_message(message.chat.id, text="Вы - Северус Снегг\nБот - Дамблдор")

    elif message.text == "Вернуться к выбору поля":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back = types.KeyboardButton("Вернуться к выбору сложности")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(button1, button2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер игрового поля: ", reply_markup=keyboard)
        bot.register_next_step_handler(msg, choose_field)

    elif (message.text == "Вернуться в главное меню"):
        return_menu(message)

    flag = True
    while True:
        if flag == True:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                    types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                    types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
            markup.add(*btns)
            msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
            flag = False
            bot.register_next_step_handler(msg, start_game_person)

    #ЗДЕСЬ ДОЛЖЕН БЫТЬ ВЫХОД В МЕНЮ




def start_game_person(message):
    global matr
    global symbol_ai, symbol_person
    global dict_commands
    global difficult
    global flag, flag2
    state = matr[:]

    command = dict_commands[message.text]
    i = int(command[0])
    j = int(command[1])
    state[i][j] = symbol_person
    # ЗАПУСК ЛЕРИНОЙ ФУНКЦИИ ВМЕСТО СЛЕД СТРОКИ И ВЫВОД В ЧАТ ТЕКУЩЕЙ СИТУАЦИИ
    bot.send_message(message.chat.id, f"{str(state)}")

    if algo.check_lose(state, pers=symbol_person):
        msg = bot.send_message(message.chat.id, 'you have won')
        # ЗАПУСК ЛЕРИНОЙ ФУНКЦИИ ВЫВОД В ЧАТ ТЕКУЩЕЙ СИТУАЦИИ
        flag2 = False

    elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
        bot.send_message(message.chat.id, 'tie')
        # ЗАПУСК ЛЕРИНОЙ ФУНКЦИИ ВЫВОД В ЧАТ ТЕКУЩЕЙ СИТУАЦИИ
        flag2 = False

    if flag2:
        bot.send_message(message.chat.id, 'ход бота: ')
        start_game_ai(difficult,symbol_person,symbol_ai)
        # ЗАПУСК ЛЕРИНОЙ ФУНКЦИИ ВМЕСТО СЛЕД СТРОКИ И ВЫВОД В ЧАТ ТЕКУЩЕЙ СИТУАЦИИ
        bot.send_message(message.chat.id, f"{str(state)}")
        if algo.check_win(state, ai=symbol_ai):
            # ЗАПУСК ЛЕРИНОЙ ФУНКЦИИ ВЫВОД В ЧАТ ТЕКУЩЕЙ СИТУАЦИИ
            bot.send_message(message.chat.id, 'ai has won')
            flag2 = False
        elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
            bot.send_message(message.chat.id, 'tie')
            # ЗАПУСК ЛЕРИНОЙ ФУНКЦИИ ВЫВОД В ЧАТ ТЕКУЩЕЙ СИТУАЦИИ
            flag2 = False
        # ЗАПУСК ЛЕРИНОЙ ФУНКЦИИ ВЫВОД В ЧАТ ТЕКУЩЕЙ СИТУАЦИИ
    if flag2:
        flag = True


def start_game_ai(mode,symbol_person,symbol_ai):
    global matr
    state = matr[:]
    ij = algo2.best_move(state, mode=mode, pers=symbol_person, ai=symbol_ai)
    state[ij[0]][ij[1]] = symbol_ai

def check_game_situation(state,symbol_person,symbol_ai):
    ...
def show_and_replace_btn(message):
    global dict_commands
    if (message.text == button for button in dict_commands.keys()):
        btns[int(message.text) - 1] = types.KeyboardButton(" ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*btns)
        msg = bot.send_message(message.chat.id, f'Вы походили на клетку номер {message.text}', reply_markup=markup)
        #bot.register_next_step_handler(msg, start_game)
if __name__ == "__main__":
    # бесконечная работа бота

    bot.infinity_polling()


