import numpy as np
import telebot

import graphic
import algo, algo2
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
btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
            types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
            types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
matr = np.array(list())
move_choose = None


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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        msg = bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
        bot.register_next_step_handler(msg, choose_question)

def ret_menu(message):
    if (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Задать вопрос")
        btn3 = types.KeyboardButton("Авторы проекта")
        markup.add(btn1, btn2, btn3)
        msg = bot.send_message(message.chat.id, text=f"Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, choose_func)

def choose_question(message):

    if (message.text == "Как меня зовут?"):
        msg = bot.send_message(message.chat.id, "Бот для игры в крестики-нолики!!!!")
        bot.register_next_step_handler(msg, choose_question)

    elif message.text == "Что я могу?":
        msg = bot.send_message(message.chat.id, text="Я почти готов играть с тобой 🚀")
        bot.register_next_step_handler(msg, choose_question)

    elif (message.text == "Вернуться в главное меню"):
        ret_menu(message)

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
        b3 = types.KeyboardButton("Рандом")
        back = types.KeyboardButton("Вернуться к выбору режима")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(b1, b2,b3, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите сложность бота: ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_difficulty)

    elif message.text == "c другом(одно устройство)":
        mode = "c другом"
        bot.send_message(message.chat.id, "Вы будете играть <i>с другом</i>", parse_mode='HTML')
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back = types.KeyboardButton("Вернуться к выбору сложности")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(button1, button2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер поля : ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_field)

    elif message.text == "Вернуться в главное меню":
        ret_menu(message)
def choose_difficulty_helper(message):
    pass
def choose_difficulty(message):
    global difficult
# Если выбрана кнопка Вернуться к выбору режима
    if (message.text == "Вернуться к выбору режима"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        bot_mode = types.KeyboardButton("c ботом")
        people_mode = types.KeyboardButton("c другом(одно устройство)")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(bot_mode, people_mode, back)
        msg = bot.send_message(message.chat.id, text='Выберите режим игры: ', reply_markup=markup)
        bot.register_next_step_handler(msg, choose_gamemode)

    elif (message.text == "Вернуться в главное меню"):
        ret_menu(message)

# Если пользователь выбрал режим Лёгкий
    elif (message.text == "Лёгкий"):
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

    elif (message.text == "Рандом"):
        difficult = "random"
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back = types.KeyboardButton("Вернуться к выбору сложности")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        keyboard.add(button1, button2, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер игрового поля: ", reply_markup=keyboard)
        bot.register_next_step_handler(msg, choose_field)

    elif (message.text == "Вернуться к выбору сложности"):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        b1 = types.KeyboardButton("Лёгкий")
        b2 = types.KeyboardButton("Анриал(бот унижает)")
        b3 = types.KeyboardButton("Рандом")
        back = types.KeyboardButton("Вернуться к выбору режима")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(b1, b2, b3, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите сложность бота: ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_difficulty)

# Если пользователь выбрал 3x3
def choose_field(message):
    if (message.text == "3x3"):
        global field
        global matr
        global mode
        field = "3x3"
        matr = np.zeros_like(np.eye(int(field[0])))
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Крестики")
        btn2 = types.KeyboardButton("Нолики")
        btn3 = types.KeyboardButton("Дамблдор")
        btn4 = types.KeyboardButton("Северус Снегг")
        btn5 = types.KeyboardButton("ManUnt")
        btn6 = types.KeyboardButton("ManCity")
        kb.add(btn1, btn2, btn3, btn4, btn5, btn6)
        msg = bot.send_message(message.chat.id, text="Выберите за кого хотите играть: ", reply_markup=kb)
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
        b3 = types.KeyboardButton("Рандом")
        back = types.KeyboardButton("Вернуться к выбору режима")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(b1, b2,b3, back, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите сложность бота: ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_difficulty)

    elif (message.text == "Вернуться в главное меню"):
        ret_menu(message)



# Выбор фигуры, за которую будет играть пользователь и ИИ
def choose_figure(message):
    if (message.text == "Вернуться в главное меню"):
        ret_menu(message)

    global symbol_person
    global symbol_ai
    global graphics_mode
    global btns
    global matr
    global mode
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton("бот")
    btn2 = types.KeyboardButton("я")
    markup.add(btn1,btn2)
    if (message.text == "Крестики"):
        symbol_person = 1
        symbol_ai = 2
        if mode == 'c ботом':
            bot.send_message(message.chat.id, text="Вы - Крестики\nБот - Нолики")
        elif mode == 'c другом':
            bot.send_message(message.chat.id, text="Person 1 - Крестики\nPerson 2 - Нолики")


    elif (message.text == "Нолики"):
        symbol_person = 2
        symbol_ai = 1
        if mode == 'c ботом':
            bot.send_message(message.chat.id, text="Вы - Нолики\nБот - Крестики")
        elif mode == 'c другом':
            bot.send_message(message.chat.id, text="Person 1 - Нолики\nPerson 2 - Крестики")

    elif (message.text == "Дамблдор"):
        symbol_person = 1
        symbol_ai = 2
        graphics_mode = "HP"
        if mode == "с ботом":
            bot.send_message(message.chat.id, text="Вы - Дамблдор\nБот - Северус Снегг")
        elif mode == "с другом":
            bot.send_message(message.chat.id, text="Person 1 - Дамблдор\nPerson 2 - Северус Снегг")
    elif (message.text == "Северус Снегг"):
        symbol_person = 2
        symbol_ai = 1
        graphics_mode = "HP"
        if mode == "с ботом":
            bot.send_message(message.chat.id, text="Вы - Северус Снегг\nБот - Дамблдор")
        elif mode == "с другом":
            bot.send_message(message.chat.id, text="Person 1 - Северус Снегг\nPerson 2 - Дамблдор")

    elif (message.text == "ManUnt"):
        symbol_person = 1
        symbol_ai = 2
        graphics_mode = "football"
        if mode == "с ботом":
            bot.send_message(message.chat.id, text="Вы - Лучший клуб в истории футбола\nБот - МанСити")
        elif mode == "с другом":
            bot.send_message(message.chat.id, text="Person 1 - Лучший клуб в истории футбола\nPerson 2 - МанСити")

    elif (message.text == "ManCity"):
        symbol_person = 2
        symbol_ai = 1
        graphics_mode = "football"
        if mode == "с ботом":
            bot.send_message(message.chat.id, text="Вы - МанСити\nБот - Лучший клуб в истории футбола")
        elif mode == "с другом":
            bot.send_message(message.chat.id, text="Person 1 - МанСити\nPerson 2 - Лучший клуб в истории футбола")


    if mode == 'c ботом':
        msg = bot.send_message(message.chat.id, 'Кто ходит первый?: ', reply_markup=markup)
        bot.register_next_step_handler(msg, who_moves_first)
    elif mode == 'c другом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(*btns)
        btn1 = types.KeyboardButton("получить статистику")
        markup.add(btn1)
        msg = bot.send_message(message.chat.id, 'Ходит человек 1: ', reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_1)

def who_moves_first(message):
    global btns
    global symbol_person
    global symbol_ai
    global graphics_mode
    global matr
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(*btns)
    btn1 = types.KeyboardButton("получить статистику")
    markup.add(btn1)
    if (message.text) == "я":
        msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
        bot.register_next_step_handler(msg, move_person)
    elif (message.text) == "бот":
        first_ai_move(message,mode,symbol_person,symbol_ai)

def first_ai_move(message,mode,symbol_person,symbol_ai):
    global matr
    global graphics_mode
    state = matr[:]
    ij = (0,0)
    state[ij[0]][ij[1]] = symbol_ai

    clear_buttons('1')
    graphic.graph(state, graphics_mode)
    photo = open('my_plot.png', 'rb')
    bot.send_photo(message.chat.id, photo)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(*btns)
    btn1 = types.KeyboardButton("получить статистику")
    markup.add(btn1)

    msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
    bot.register_next_step_handler(msg, move_person)

def move_person(message):
    global matr
    global symbol_ai, symbol_person
    global dict_commands
    global difficult
    global graphics_mode
    global btns
    global move_choose
    state = matr[:]
    move_choose = 'you'
    if message.text == 'получить статистику':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("моя победа")
        btn2 = types.KeyboardButton("победа бота")
        btn3 = types.KeyboardButton("ничья")
        markup.add(btn1,btn2,btn3)
        msg = bot.send_message(message.chat.id, 'чью статистику показывать', reply_markup=markup)
        bot.register_next_step_handler(msg, stats_show)
    else:
        command = dict_commands[message.text]
        i = int(command[0])
        j = int(command[1])
        if state[i][j] != 0:
            bot.send_message(message.chat.id, 'клетка уже занята!')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add(*btns)
            btn1 = types.KeyboardButton("получить статистику")
            markup.add(btn1)
            msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
            bot.register_next_step_handler(msg, move_person)
        else:
            state[i][j] = symbol_person
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            clear_buttons(message.text)
            graphic.graph(state, graphics_mode)
            photo = open('my_plot.png', 'rb')
            bot.send_photo(message.chat.id, photo)

            if algo.check_lose(state, pers=symbol_person):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("Вернуться в главное меню")
                back = types.KeyboardButton("Сыграть еще раз")
                markup.add(btn1, back)
                msg = bot.send_message(message.chat.id, 'you have won',reply_markup=markup)
                bot.register_next_step_handler(msg, ret_menu_call)

            elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("Вернуться в главное меню")
                back = types.KeyboardButton("Сыграть еще раз")
                markup.add(btn1, back)
                msg = bot.send_message(message.chat.id, 'tie', reply_markup=markup)
                bot.register_next_step_handler(msg, ret_menu_call)

            else:
                bot.send_message(message.chat.id, 'ход бота: ', reply_markup=markup)
                start_game_ai(message,difficult,symbol_person,symbol_ai)


def stats_show(message):
    global matr,symbol_person,symbol_ai
    global move_choose
    state = matr[:]
    stats = algo2.get_stats(message,state, move='person' if move_choose == 'you' or move_choose == 'person 1' else 'ai',pers=symbol_person,ai=symbol_ai)
    if message.text == 'моя победа' or message.text == 'победа person 1':
        bot.send_message(message.chat.id, f'шанс выиграть: {stats[1]}%')
    elif message.text == 'победа бота' or message.text == 'победа person 2':
        bot.send_message(message.chat.id, f'шанс выиграть: {stats[0]}%')
    elif message.text == 'ничья':
        bot.send_message(message.chat.id, f'шанс ничьи: {stats[2]}%')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(*btns)
    btn1 = types.KeyboardButton("получить статистику")
    markup.add(btn1)
    if move_choose == 'you':
        msg = bot.send_message(message.chat.id, 'Ваш ход: ',reply_markup=markup)
        bot.register_next_step_handler(msg, move_person)
    elif move_choose == 'person 1':
        msg = bot.send_message(message.chat.id, 'Ходит человек 1: ',reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_1)
    elif move_choose == 'person 2':
        msg = bot.send_message(message.chat.id, 'Ходит человек 2: ',reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_2)

def start_game_ai(message,mode,symbol_person,symbol_ai):
    global matr
    global graphics_mode
    state = matr[:]
    ij = algo2.best_move(state, mode=mode, pers=symbol_person, ai=symbol_ai)
    state[ij[0]][ij[1]] = symbol_ai
    clear_buttons(str([key for key in dict_commands if dict_commands[key] == ij][0]))
    graphic.graph(state, graphics_mode)
    photo = open('my_plot.png', 'rb')
    bot.send_photo(message.chat.id, photo)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(*btns)
    btn1 = types.KeyboardButton("получить статистику")
    markup.add(btn1)

    if algo.check_win(state, ai=symbol_ai):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Вернуться в главное меню")
        back = types.KeyboardButton("Сыграть еще раз")
        markup.add(btn1, back)
        msg = bot.send_message(message.chat.id, 'ai has won', reply_markup=markup)
        bot.register_next_step_handler(msg, ret_menu_call)


    elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Вернуться в главное меню")
        back = types.KeyboardButton("Сыграть еще раз")
        markup.add(btn1, back)
        msg = bot.send_message(message.chat.id, 'tie', reply_markup=markup)
        bot.register_next_step_handler(msg, ret_menu_call)
    else:
        msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
        bot.register_next_step_handler(msg, move_person)


def ret_menu_call(message):
    if (message.text == 'Вернуться в главное меню'):
        ret_menu(message)
    elif (message.text == 'Сыграть еще раз'):
        global symbol_person
        global symbol_ai
        global graphics_mode
        global btns
        global matr
        global mode
        matr = np.zeros_like(np.eye(3))
        if mode == 'c ботом':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("бот")
            btn2 = types.KeyboardButton("я")
            markup.add(btn1, btn2)
            msg = bot.send_message(message.chat.id, 'Кто ходит первый?: ', reply_markup=markup)
            btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                    types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                    types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
            bot.register_next_step_handler(msg, who_moves_first)
        elif mode == 'c другом':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add(*btns)
            btn1 = types.KeyboardButton("получить статистику")
            markup.add(btn1)
            msg = bot.send_message(message.chat.id, 'Ходит человек 1: ', reply_markup=markup)
            btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                    types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                    types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
            bot.register_next_step_handler(msg, move_person_1)

def move_person_1(message):
    global matr
    global symbol_ai, symbol_person
    global dict_commands
    global difficult
    global graphics_mode
    global btns
    global move_choose
    move_choose = 'person 1'
    state = matr[:]
    if message.text == 'получить статистику':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("победа person 1")
        btn2 = types.KeyboardButton("победа person 2")
        btn3 = types.KeyboardButton("ничья")
        markup.add(btn1,btn2,btn3)
        msg = bot.send_message(message.chat.id, 'чью статистику показывать', reply_markup=markup)
        bot.register_next_step_handler(msg, stats_show)
    else:
        command = dict_commands[message.text]
        i = int(command[0])
        j = int(command[1])
        if state[i][j] != 0:
            bot.send_message(message.chat.id, 'клетка уже занята!')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add(*btns)
            btn1 = types.KeyboardButton("получить статистику")
            markup.add(btn1)
            msg = bot.send_message(message.chat.id, 'Ходит человек 1: ', reply_markup=markup)
            bot.register_next_step_handler(msg, move_person_1)
        else:
            state[i][j] = symbol_person
            clear_buttons(message.text)
            graphic.graph(state, graphics_mode)
            photo = open('my_plot.png', 'rb')
            bot.send_photo(message.chat.id, photo)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add(*btns)
            btn1 = types.KeyboardButton("получить статистику")
            markup.add(btn1)

            if algo.check_lose(state, pers=symbol_person):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("Вернуться в главное меню")
                back = types.KeyboardButton("Сыграть еще раз")
                markup.add(btn1, back)
                msg = bot.send_message(message.chat.id, 'person 1 has won', reply_markup=markup)
                bot.register_next_step_handler(msg, ret_menu_call)

            elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("Вернуться в главное меню")
                back = types.KeyboardButton("Сыграть еще раз")
                markup.add(btn1, back)
                msg = bot.send_message(message.chat.id, 'tie', reply_markup=markup)
                bot.register_next_step_handler(msg, ret_menu_call)

            else:
                msg = bot.send_message(message.chat.id, 'Ходит человек 2: ', reply_markup=markup)
                bot.register_next_step_handler(msg, move_person_2)

def move_person_2(message):
    global matr
    global symbol_ai, symbol_person
    global dict_commands
    global difficult
    global graphics_mode
    global btns
    global move_choose
    move_choose = 'person 2'
    state = matr[:]
    if message.text == 'получить статистику':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("победа person 1")
        btn2 = types.KeyboardButton("победа person 2")
        btn3 = types.KeyboardButton("ничья")
        markup.add(btn1,btn2,btn3)
        msg = bot.send_message(message.chat.id, 'чью статистику показывать', reply_markup=markup)
        bot.register_next_step_handler(msg, stats_show)
    else:
        command = dict_commands[message.text]
        i = int(command[0])
        j = int(command[1])
        if state[i][j] != 0:
            bot.send_message(message.chat.id, 'клетка уже занята!')
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add(*btns)
            btn1 = types.KeyboardButton("получить статистику")
            markup.add(btn1)
            msg = bot.send_message(message.chat.id, 'Ходит человек 2: ', reply_markup=markup)
            bot.register_next_step_handler(msg, move_person_2)
        else:
            state[i][j] = symbol_ai
            clear_buttons(message.text)
            graphic.graph(state, graphics_mode)
            photo = open('my_plot.png', 'rb')
            bot.send_photo(message.chat.id, photo)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            markup.add(*btns)
            btn1 = types.KeyboardButton("получить статистику")
            markup.add(btn1)

            if algo.check_win(state, ai=symbol_ai):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("Вернуться в главное меню")
                back = types.KeyboardButton("Сыграть еще раз")
                markup.add(btn1, back)
                msg = bot.send_message(message.chat.id, 'person 2 has won', reply_markup=markup)
                bot.register_next_step_handler(msg, ret_menu_call)

            elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("Вернуться в главное меню")
                back = types.KeyboardButton("Сыграть еще раз")
                markup.add(btn1, back)
                msg = bot.send_message(message.chat.id, 'tie', reply_markup=markup)
                bot.register_next_step_handler(msg, ret_menu_call)

            else:
                msg = bot.send_message(message.chat.id, 'Ходит человек 1: ', reply_markup=markup)
                bot.register_next_step_handler(msg, move_person_1)

def clear_buttons(btn):
    global dict_commands
    if (btn == button for button in dict_commands.keys()):
        btns[int(btn) - 1] = types.KeyboardButton(" ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*btns)

if __name__ == "__main__":
    # бесконечная работа бота

    bot.infinity_polling()


