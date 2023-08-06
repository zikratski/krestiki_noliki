import numpy as np
import telebot

import graphic
import algo
from telebot import types
# Остальная игровая логика
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
id1,id2 = None,None


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
    msg = bot.send_message(message.chat.id,
                     text= f"Привет! Я тестовый бот для тебя, {message.from_user.first_name}!", reply_markup=markup)
    #bot.register_next_step_handler(msg, choose_func)
    #photo = open('C:/Users/Kirill/Desktop/XsOs.jpg', 'rb')
    #bot.send_photo(message.chat.id, photo)

@bot.message_handler(content_types=['text'])
def choose_func(message):
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)
    elif (message.text == "Начать игру"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        #Выбор режима игры и сохранение в переменную mode
        if message.chat.type == "private":
            bot_mode = types.KeyboardButton("c ботом")
            people_mode = types.KeyboardButton("c другом(одно устройство)")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(bot_mode, people_mode, back)
            msg = bot.send_message(message.chat.id, text='Выберите режим игры\n\n<i>Чтобы играть с другом по сети, добавьте бота в общий чат: </i>', reply_markup=markup,parse_mode='HTML')
            bot.register_next_step_handler(msg, choose_gamemode)
        else:
            chat_mode = types.KeyboardButton("c другом(разные устройства)")
            back = types.KeyboardButton("Вернуться в главное меню")
            markup.add(chat_mode, back)
            msg = bot.send_message(message.chat.id, text='Выберите режим игры:\n\n<i>Чтобы играть с ботом или с другом на одном устройстве, запустилте бота https://t.me/XsAndOsBot в лс: </i>', reply_markup=markup,parse_mode='HTML')
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
    elif (message.text != "Начать игру") and (message.text != "Авторы проекта" and message.text != "/authors") and (message.text != "Задать вопрос" and  message.text != "/question") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
        msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
        bot.register_next_step_handler(msg, choose_func)


def ret_menu(message):
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)
    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Начать игру")
        btn2 = types.KeyboardButton("Задать вопрос")
        btn3 = types.KeyboardButton("Авторы проекта")
        markup.add(btn1, btn2, btn3)
        msg = bot.send_message(message.chat.id, text=f"Вы вернулись в главное меню", reply_markup=markup)
        bot.register_next_step_handler(msg, choose_func)
    elif (message.text != "/start") and (message.text != "Вы вернулись в главное меню") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
        pass

def choose_question(message):
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)

    elif (message.text == "Как меня зовут?"):
        msg = bot.send_message(message.chat.id, "Бот для игры в крестики-нолики!!!!")
        bot.register_next_step_handler(msg, choose_question)

    elif message.text == "Что я могу?":
        msg = bot.send_message(message.chat.id, text="Я почти готов играть с тобой 🚀")
        bot.register_next_step_handler(msg, choose_question)
    elif (message.text == "Вернуться в главное меню"):
        ret_menu(message)

    elif ((message.text != "Как меня зовут?") or (message.text != "Что я могу?") or (message.text != "Вернуться в главное меню")) and (message.text != "/start") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
        msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
        bot.register_next_step_handler(msg, choose_question)



def choose_gamemode(message):
    global mode
    global id1,id2
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)
    # Если пользователь выбрал 'с ботом', то далее выбирает сложность игры(лёгкий, анриал)
    elif message.text == "c ботом":
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
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(button1, button2, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер поля : ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_field)

    elif message.text == "c другом(разные устройства)":
        mode = "c чатом"
        id1,id2 = None, None
        bot.send_message(message.chat.id, "Играем в чате")
        chat_helper(message)

    elif message.text == "Вернуться в главное меню":
        ret_menu(message)

    elif (message.text != "c ботом" and message.text != "c другом(одно устройство)" and message.text != "c другом(разные устройства)" and message.text != "Вернуться в главное меню") and (message.text !="/start") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся") :
        msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
        bot.register_next_step_handler(msg, choose_gamemode)
    # Доступен выбор возврата к предыдущему выбору и к выходу в главное меню
def chat_helper(message):
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)
    global id1,id2
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button1 = types.KeyboardButton("Играю")
    kb.add(button1)
    msg = bot.send_message(message.chat.id, text="нажмите на <i>Играю</i> чтобы стать игроком : ", reply_markup=kb,parse_mode='HTML')
    bot.register_next_step_handler(msg, register_users)
def register_users(message):
    global id1, id2
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)

    elif message.text == 'Играю':
        if id1 and not id2:
            id2 = message.from_user.username
            bot.send_message(message.chat.id, f"Привет, @{id2}!")
        elif not id1 and not id2:
            id1 = message.from_user.username
            bot.send_message(message.chat.id, f"Привет, @{id1}!")


    if all((id1,id2)):
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(button1, button2, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер поля : ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_field)
    else:
        chat_helper(message)



def choose_difficulty(message):
    global difficult
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)

# Если выбрана кнопка Вернуться к выбору режима
    elif (message.text == "Вернуться к выбору режима"):
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

    elif ((message.text != "Вернуться в главное меню") or (message.text != "Вернуться к выбору режима") or (message.text != "Лёгкий") or (message.text != "Анриал(бот унижает)") or (message.text != "Рандом") or (message.text != "Вернуться к выбору сложности")) and (message.text != "/start") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
        msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
        bot.register_next_step_handler(msg, choose_difficulty)

# Если пользователь выбрал 3x3
def choose_field(message):
    global id1,id2, mode
    if mode != 'c чатом' or message.from_user.username == id1 or message.from_user.username == id2:
        if (message.text == "/start"):
            msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
            start(message)
        elif (message.text == "3x3"):
            global field
            global matr
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
            back_to_menu = types.KeyboardButton("Вернуться в главное меню")
            keyboard.add(button1, button2, back_to_menu)
            if mode == 'с ботом':
                back = types.KeyboardButton("Вернуться к выбору сложности")
                keyboard.add(back)
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

        elif (message.text != "3x3") and (message.text != "Бесконечное(в разработке)") and (message.text != "Вернуться к выбору сложности") and (message.text != "Вернуться в главное меню") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
            if mode == "c чатом":
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, choose_field)
            else:
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, choose_field)
    else:
        bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
        kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        button1 = types.KeyboardButton("3x3")
        button2 = types.KeyboardButton("Бесконечное(в разработке)")
        back_to_menu = types.KeyboardButton("Вернуться в главное меню")
        kb.add(button1, button2, back_to_menu)
        msg = bot.send_message(message.chat.id, text="Выберите размер поля : ", reply_markup=kb)
        bot.register_next_step_handler(msg, choose_field)



def choose_figure(message):
    global id1, id2, mode
    if message.from_user.username == id1 or message.from_user.username == id2 or mode != 'c чатом':
        if (message.text == "/start"):
            msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
            start(message)
        elif (message.text == "Вернуться в главное меню"):
            ret_menu(message)
        mess_id = message.from_user.username
        global symbol_person
        global symbol_ai
        global graphics_mode
        global btns
        btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
        global matr

        if (message.text == "Крестики"):
            symbol_person = 1
            symbol_ai = 2
            graphics_mode = 'standart'
            if mode == 'c ботом':
                bot.send_message(message.chat.id, text="Вы - Крестики\nБот - Нолики")
            elif mode == 'c другом':
                bot.send_message(message.chat.id, text="Игрок 1 - Крестики\nИгрок 2 - Нолики")
            elif mode == "c чатом":
                bot.send_message(message.chat.id, f"@{mess_id} - Крестики\n@{id2 if mess_id == id1 else id1} - Нолики")
            choose_mode(message)



        elif (message.text == "Нолики"):
            symbol_person = 2
            symbol_ai = 1
            graphics_mode = 'standart'
            if mode == 'c ботом':
                bot.send_message(message.chat.id, text="Вы - Нолики\nБот - Крестики")
            elif mode == 'c другом':
                bot.send_message(message.chat.id, text="Игрок 1 - Нолики\nИгрок 2 - Крестики")
            elif mode == "c чатом":
                bot.send_message(message.chat.id, f"@{mess_id} - Нолики\n@{id2 if mess_id == id1 else id1} - Крестики")
            choose_mode(message)

        elif (message.text == "Дамблдор"):
            symbol_person = 1
            symbol_ai = 2
            graphics_mode = "HP"
            if mode == "с ботом":
                bot.send_message(message.chat.id, text="Вы - Дамблдор\nБот - Северус Снегг")
            elif mode == "с другом":
                bot.send_message(message.chat.id, text="Person 1 - Дамблдор\nPerson 2 - Северус Снегг")
            elif mode == "c чатом":
                bot.send_message(message.chat.id, f"@{mess_id} - Дамблдори\n@{id2 if mess_id == id1 else id1} - Северус Снегг")
            choose_mode(message)

        elif (message.text == "Северус Снегг"):
            symbol_person = 2
            symbol_ai = 1
            graphics_mode = "HP"
            if mode == "с ботом":
                bot.send_message(message.chat.id, text="Вы - Северус Снегг\nБот - Дамблдор")
            elif mode == "с другом":
                bot.send_message(message.chat.id, text="Person 1 - Северус Снегг\nPerson 2 - Дамблдор")
            elif mode == "c чатом":
                bot.send_message(message.chat.id,
                                 f"@{mess_id} - Северус Снегг\n@{id2 if mess_id == id1 else id1} - Дамблдор")
            choose_mode(message)


        elif (message.text == "ManUnt"):
            symbol_person = 1
            symbol_ai = 2
            graphics_mode = "football"
            if mode == "с ботом":
                bot.send_message(message.chat.id, text="Вы - Лучший клуб в истории футбола\nБот - МанСити")
            elif mode == "с другом":
                bot.send_message(message.chat.id, text="Person 1 - Лучший клуб в истории футбола\nPerson 2 - МанСити")
            elif mode == "c чатом":
                bot.send_message(message.chat.id,
                                 f"@{mess_id} - Лучший клуб в истории футбола\n@{id2 if mess_id == id1 else id1} - МанСити")
            choose_mode(message)

        elif (message.text == "ManCity"):
            symbol_person = 2
            symbol_ai = 1
            graphics_mode = "football"
            if mode == "с ботом":
                bot.send_message(message.chat.id, text="Вы - МанСити\nБот - Лучший клуб в истории футбола")
            elif mode == "с другом":
                bot.send_message(message.chat.id, text="Person 1 - МанСити\nPerson 2 - Лучший клуб в истории футбола")
            elif mode == "c чатом":
                bot.send_message(message.chat.id,
                                 f"@{mess_id} - МанСити\n@{id2 if mess_id == id1 else id1} - Лучший клуб в истории футбола")
            choose_mode(message)

        elif ((message.text != "Вернуться в главное меню") or (message.text != "Крестики") or (message.text != "Нолики") or (message.text != "Дамблдор") or (message.text != "Северус Снегг") or (message.text != "ManUnt") or (message.text != "ManCity")) and (message.text != "/start") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
            if mode == "c чатом":
                #bot.send_message(message.chat.id, text="i am here")
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, choose_figure)
                #choose_figure(message)
            else:
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, choose_figure)

    else:
        bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
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

def choose_mode(message):
    global mode
    if mode == 'c ботом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("бот")
        btn2 = types.KeyboardButton("я")
        markup.add(btn1, btn2)
        msg = bot.send_message(message.chat.id, 'Кто ходит первый?: ', reply_markup=markup)
        bot.register_next_step_handler(msg, who_moves_first)
    elif mode == 'c другом':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(*btns)
        btn1 = types.KeyboardButton("получить статистику")
        markup.add(btn1)
        msg = bot.send_message(message.chat.id, 'Ходит игрок 1: ', reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_1)
    elif mode == "c чатом":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("я первый")
        markup.add(btn1)
        msg = bot.send_message(message.chat.id, f'Нажми <i>я первый</i>, чтобы походить первым: ', reply_markup=markup,
                               parse_mode='HTML')
        bot.register_next_step_handler(msg, who_moves_first_chat)
def who_moves_first_chat(message):
    global id1,id2, mode
    global btns
    btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                        types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                        types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
    global symbol_person
    global symbol_ai
    global graphics_mode
    global matr
    if message.from_user.username == id2 or message.from_user.username == id1 or mode != "c чатом":
        if message.text == "я первый":
            if message.from_user.username == id1:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                markup.add(*btns)
                btn1 = types.KeyboardButton("получить статистику")
                markup.add(btn1)
                msg = bot.send_message(message.chat.id, f'Ходит: @{id1}', reply_markup=markup)
                bot.register_next_step_handler(msg, move_person_1)
            elif message.from_user.username == id2:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                markup.add(*btns)
                btn1 = types.KeyboardButton("получить статистику")
                markup.add(btn1)
                msg = bot.send_message(message.chat.id, f'Ходит: @{id2}', reply_markup=markup)
                bot.register_next_step_handler(msg, move_person_2)
            else:
                bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("я первый")
                markup.add(btn1)
                msg = bot.send_message(message.chat.id, f'Нажми <i>я первый</i>, чтобы походить первым: ', reply_markup=markup, parse_mode='HTML')
                bot.register_next_step_handler(msg, who_moves_first_chat)
        elif message.text != 'я первый' and (message.text != "/start") and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
            if mode == "c чатом":
                #bot.send_message(message.chat.id, text="i am here")
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, who_moves_first_chat)
                #who_moves_first_chat(message)
            else:
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, who_moves_first_chat)
    else:
        bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("я первый")
        markup.add(btn1)
        msg = bot.send_message(message.chat.id, f'Нажми <i>я первый</i>, чтобы походить первым: ', reply_markup=markup,
                               parse_mode='HTML')
        bot.register_next_step_handler(msg, who_moves_first_chat)

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
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)

    elif (message.text) == "я":
        msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
        bot.register_next_step_handler(msg, move_person)
    elif (message.text) == "бот":
        first_ai_move(message,mode,symbol_person,symbol_ai)
    elif (message.text != "/start") and (message.text != "я") and (message.text) != "бот":
        msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
        bot.register_next_step_handler(msg, who_moves_first)


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
    if (message.text == "/start"):
        msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
        start(message)
    elif message.text == 'получить статистику':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("моя победа")
        btn2 = types.KeyboardButton("победа бота")
        btn3 = types.KeyboardButton("ничья")
        markup.add(btn1,btn2,btn3)
        msg = bot.send_message(message.chat.id, 'чью статистику показывать', reply_markup=markup)
        bot.register_next_step_handler(msg, stats_show)
    else:
        try:
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
                    msg = bot.send_message(message.chat.id, 'Вы выиграли.\nПоздравляем!',reply_markup=markup)
                    bot.register_next_step_handler(msg, ret_menu_call)

                elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    btn1 = types.KeyboardButton("Вернуться в главное меню")
                    back = types.KeyboardButton("Сыграть еще раз")
                    markup.add(btn1, back)
                    msg = bot.send_message(message.chat.id, 'Ничья', reply_markup=markup)
                    bot.register_next_step_handler(msg, ret_menu_call)

                else:
                    bot.send_message(message.chat.id, 'Ход бота: ', reply_markup=markup)
                    start_game_ai(message,difficult,symbol_person,symbol_ai)
        except KeyError:
            msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
            bot.register_next_step_handler(msg, move_person)

def stats_show(message):
    global id1,id2,mode
    if message.from_user.username == id2 or message.from_user.username == id1 or mode != "c чатом":
        global matr, symbol_person, symbol_ai
        global move_choose
        state = matr[:]
        stats = algo.get_stats(message, state,
                                move='person' if move_choose == 'you' or move_choose == 'person 1' else 'ai',
                                pers=symbol_person, ai=symbol_ai)
        if (message.text == "/start"):
            msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
            start(message)

        elif message.text == 'моя победа' or message.text == 'победа игрока 1' or message.text == f"победа {id1}" :
            bot.send_message(message.chat.id, f'шанс выиграть: {stats[1]}%')
            stats_show_helper(message)
        elif message.text == 'победа бота' or message.text == 'победа игрока 2'or message.text == f"победа {id2}" :
            bot.send_message(message.chat.id, f'шанс выиграть: {stats[0]}%')
            stats_show_helper(message)
        elif message.text == 'ничья':
            bot.send_message(message.chat.id, f'шанс ничьи: {stats[2]}%')
            stats_show_helper(message)


        elif (message.text != 'моя победа' and message.text != 'победа игрока 1' and message.text != f"победа {id1}" and message.text != 'победа бота' and message.text != 'победа игрока 2'and message.text != f"победа {id2}" and message.text != 'ничья') and message.text != '/start' and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
            if mode == "c чатом":
                #bot.send_message(message.chat.id, text="i am here")
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, stats_show)
                #stats_show(message)
            else:
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, stats_show)
    else:
        bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("победа игрока 1" if mode != 'c чатом' else f"победа {id1}")
        btn2 = types.KeyboardButton("победа игрока 2" if mode != 'c чатом' else f"победа {id2}")
        btn3 = types.KeyboardButton("ничья")
        markup.add(btn1, btn2, btn3)
        msg = bot.send_message(message.chat.id, 'чью статистику показывать', reply_markup=markup)
        bot.register_next_step_handler(msg, stats_show)


def stats_show_helper(message):
    global move_choose
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add(*btns)
    btn1 = types.KeyboardButton("получить статистику")
    markup.add(btn1)
    if move_choose == 'you':
        msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
        bot.register_next_step_handler(msg, move_person)
    elif move_choose == 'person 1':
        msg = bot.send_message(message.chat.id, 'Ходит игрок 1: ' if mode != 'c чатом' else f"Ходит @{id1}",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_1)
    elif move_choose == 'person 2':
        msg = bot.send_message(message.chat.id, 'Ходит игрок 2: ' if mode != 'c чатом' else f"Ходит @{id2}",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_2)
def start_game_ai(message,mode,symbol_person,symbol_ai):
    global matr
    global graphics_mode
    state = matr[:]
    ij = algo.best_move(state, mode=mode, pers=symbol_person, ai=symbol_ai)
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
        msg = bot.send_message(message.chat.id, 'Бот выиграл.\n :(', reply_markup=markup)
        bot.register_next_step_handler(msg, ret_menu_call)


    elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Вернуться в главное меню")
        back = types.KeyboardButton("Сыграть еще раз")
        markup.add(btn1, back)
        msg = bot.send_message(message.chat.id, 'Ничья', reply_markup=markup)
        bot.register_next_step_handler(msg, ret_menu_call)
    else:
        msg = bot.send_message(message.chat.id, 'Ваш ход: ', reply_markup=markup)
        bot.register_next_step_handler(msg, move_person)

def ret_menu_call(message):
    global id1, id2, mode
    if message.from_user.username == id1 or message.from_user.username == id2 or mode != "c чатом":
        if (message.text == "/start"):
            msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
            start(message)
        elif (message.text == 'Вернуться в главное меню'):
            ret_menu(message)
        elif (message.text == 'Сыграть еще раз'):
            global symbol_person
            global symbol_ai
            global graphics_mode
            global btns
            global matr
            matr = np.zeros_like(np.eye(3))
            if mode == 'c ботом':
                btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                        types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                        types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("бот")
                btn2 = types.KeyboardButton("я")
                markup.add(btn1, btn2)
                msg = bot.send_message(message.chat.id, 'Кто ходит первый?: ', reply_markup=markup)

                bot.register_next_step_handler(msg, who_moves_first)
            elif mode == 'c другом':
                btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                        types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                        types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                markup.add(*btns)
                btn1 = types.KeyboardButton("получить статистику")
                markup.add(btn1)
                msg = bot.send_message(message.chat.id, 'Ходит игрок 1: ', reply_markup=markup)
                bot.register_next_step_handler(msg, move_person_1)
            elif mode == "c чатом":
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                btn1 = types.KeyboardButton("я первый")
                markup.add(btn1)
                msg = bot.send_message(message.chat.id, f'Нажми <i>я первый</i>, чтобы походить первым: ',
                                       reply_markup=markup,parse_mode='HTML')
                bot.register_next_step_handler(msg, who_moves_first_chat)
        elif (message.text != 'Вернуться в главное меню') and (message.text != 'Сыграть еще раз') and (message.text != '"/start"') and (message.text != "Я не знаю данной команды!\nВыберите из имеющихся"):
            if mode == "c чатом":
                #bot.send_message(message.chat.id, text="i am here")
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, ret_menu_call)
                #ret_menu_call(message)
            else:
                msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                bot.register_next_step_handler(msg, ret_menu_call)
    else:
        bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton("Вернуться в главное меню")
        back = types.KeyboardButton("Сыграть еще раз")
        markup.add(btn1, back)
        msg = bot.send_message(message.chat.id, "что дальше?", reply_markup=markup)
        bot.register_next_step_handler(msg, ret_menu_call)


def move_person_1(message):
    global id1, id2
    global symbol_ai, symbol_person
    global dict_commands
    global difficult
    global matr
    global graphics_mode
    global btns
    global move_choose
    global mode
    if message.from_user.username == id1 or mode != "c чатом":
        move_choose = 'person 1'
        state = matr[:]
        if (message.text == "/start"):
            msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
            start(message)
        elif message.text == 'получить статистику':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("победа игрока 1" if mode != 'c чатом' else f"победа {id1}")
            btn2 = types.KeyboardButton("победа игрока 2" if mode != 'c чатом' else f"победа {id2}")
            btn3 = types.KeyboardButton("ничья")
            markup.add(btn1,btn2,btn3)
            msg = bot.send_message(message.chat.id, 'чью статистику показывать', reply_markup=markup)
            bot.register_next_step_handler(msg, stats_show)
        else:
            try:
                command = dict_commands[message.text]
                i = int(command[0])
                j = int(command[1])
                if state[i][j] != 0:
                    bot.send_message(message.chat.id, 'клетка уже занята!')
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    markup.add(*btns)
                    btn1 = types.KeyboardButton("получить статистику")
                    markup.add(btn1)
                    msg = bot.send_message(message.chat.id, 'Ходит игрок 1: 'if mode != 'c чатом' else f"Ходит @{id1}", reply_markup=markup)
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
                        msg = bot.send_message(message.chat.id, 'Игрок 1 победил' if mode != 'c чатом' else f"победил @{id1}", reply_markup=markup)
                        bot.register_next_step_handler(msg, ret_menu_call)

                    elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                        btn1 = types.KeyboardButton("Вернуться в главное меню")
                        back = types.KeyboardButton("Сыграть еще раз")
                        markup.add(btn1, back)
                        msg = bot.send_message(message.chat.id, 'ничья', reply_markup=markup)
                        bot.register_next_step_handler(msg, ret_menu_call)

                    else:
                        msg = bot.send_message(message.chat.id, f"Ходит @{id2}" if mode == 'c чатом' else 'Ходит игрок 2', reply_markup=markup)
                        #bot.send_message(message.chat.id,f"mode: {mode}")
                        bot.register_next_step_handler(msg, move_person_2)
            except KeyError:
                if mode == "c чатом":
                    #bot.send_message(message.chat.id, text="i am here")
                    msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                    bot.register_next_step_handler(msg, move_person_1)
                    #move_person_1(message)
                else:
                    msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                    bot.register_next_step_handler(msg, move_person_1)
    else:
        if message.from_user.username == id2:
            bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ ТВОЙ ХОД, КЛОУН!!! ")
        else:
            bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(*btns)
        btn1 = types.KeyboardButton("получить статистику")
        markup.add(btn1)
        msg = bot.send_message(message.chat.id, f"Ходит @{id1}", reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_1)

def move_person_2(message):
    global id1,id2
    global matr
    global symbol_ai, symbol_person
    global dict_commands
    global difficult
    global graphics_mode
    global btns
    global move_choose
    global mode
    if message.from_user.username == id2 or mode != "c чатом":
        move_choose = 'person 2'
        state = matr[:]
        if (message.text == "/start"):
            msg = bot.send_message(message.chat.id, "<i>---перезапускаю бот---</i>", parse_mode='HTML')
            start(message)
        elif message.text == 'получить статистику':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            btn1 = types.KeyboardButton("победа игрока 1" if mode != 'c чатом' else f"победа {id1}")
            btn2 = types.KeyboardButton("победа игрока 2" if mode != 'c чатом' else f"победа {id2}")
            btn3 = types.KeyboardButton("ничья")
            markup.add(btn1,btn2,btn3)
            msg = bot.send_message(message.chat.id, 'чью статистику показывать', reply_markup=markup)
            bot.register_next_step_handler(msg, stats_show)
        else:
            try:
                command = dict_commands[message.text]
                i = int(command[0])
                j = int(command[1])
                if state[i][j] != 0:
                    bot.send_message(message.chat.id, 'клетка уже занята!')
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                    markup.add(*btns)
                    btn1 = types.KeyboardButton("получить статистику")
                    markup.add(btn1)
                    msg = bot.send_message(message.chat.id, 'Ходит игрок 2: ' if mode != 'c чатом' else f"Ходит  @{id2}", reply_markup=markup)
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
                        msg = bot.send_message(message.chat.id, 'Игрок 2 победил' if mode != 'c чатом' else f"победил @{id2}", reply_markup=markup)
                        bot.register_next_step_handler(msg, ret_menu_call)

                    elif algo.check_tie(state, ai=symbol_ai, pers=symbol_person):
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
                        btn1 = types.KeyboardButton("Вернуться в главное меню")
                        back = types.KeyboardButton("Сыграть еще раз")
                        markup.add(btn1, back)
                        msg = bot.send_message(message.chat.id, 'Ничья', reply_markup=markup)
                        bot.register_next_step_handler(msg, ret_menu_call)

                    else:
                        msg = bot.send_message(message.chat.id,  f"Ходит @{id1}" if mode == 'c чатом' else 'Ходит игрок 1', reply_markup=markup)
                        #bot.send_message(message.chat.id, f"mode: {mode}")
                        bot.register_next_step_handler(msg, move_person_1)
            except KeyError:
                if mode == "c чатом":
                    msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                    bot.register_next_step_handler(msg, move_person_2)
                    #move_person_2(message)
                else:
                    msg = bot.send_message(message.chat.id, text="Я не знаю данной команды!\nВыберите из имеющихся")
                    bot.register_next_step_handler(msg, move_person_2)

    else:
        if message.from_user.username == id1:
            bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ ТВОЙ ХОД, КЛОУН!!! ")
        else:
            bot.send_message(message.chat.id, f"@{message.from_user.username} НЕ МЕШАЙ ИГРАТЬ, КЛОУН!!! ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add(*btns)
        btn1 = types.KeyboardButton("получить статистику")
        markup.add(btn1)
        msg = bot.send_message(message.chat.id, f"Ходит @{id2}", reply_markup=markup)
        bot.register_next_step_handler(msg, move_person_2)

def clear_buttons(btn):
    global dict_commands
    if (btn == button for button in dict_commands.keys()):
        btns[int(btn) - 1] = types.KeyboardButton(" ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*btns)

if __name__ == "__main__":
    # бесконечная работа бота

    bot.infinity_polling()