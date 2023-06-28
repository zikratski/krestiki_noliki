import telebot
from telebot import types
import configure
#
#
# # Токена для телеграмма
bot = telebot.TeleBot(configure.token)

# КНОПКИ В БОТЕ

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    btn3 = types.KeyboardButton("Авторы")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text="Привет! Я тестовый бот для тебя, Кирилл".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо за тестинг меня!)")
    if (message.text == "Авторы"):
        bot.register_next_step_handler(message, author_question)
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "Бот для игры в крестики-нолики!!!!")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поиграть с тобой в крестики-нолики")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)


@bot.message_handler(commands=['authors'])
def author_question(message):
    bot.send_message(message.chat.id, 'Вы хотите узнать, кто создал бота?')
    bot.register_next_step_handler(message, author)

def author(message):
    if message.text == 'Да':
        bot.reply_to(message, 'Kirill, Lera, Anton, Ilya')
    elif message.text == 'Нет':
        bot.reply_to(message, 'Не хочешь - как хочешь.')
    else:
        bot.register_next_step_handler(message, author_question)



# @bot.message_handler(commands=['start'])
# def say_hello(message):
#     bot.send_message(message.chat.id, 'Привет, друг, давай поиграем в крестики-нолики!', reply_markup=keyboard_list)
#
# @bot.message_handler(commands=['end'])
# def say_bye(message):
#     bot.send_message(message.chat.id, 'Прощай, друг, надеюсь, что ты вернёшься')



# # def echo(message):
#     bot.send_message(message.chat.id, text=f'{message.text}')
@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, 'Введите ваше число/цифру, которую нужно умножить на 2:')
    bot.register_next_step_handler(message, multiply)

def multiply(message):
    try:
        number = int(message.text)
        bot.send_message(message.chat.id, f'Ваше число/цифра, умноженное на 2: {number*2}')
        send_text(message)
    except ValueError:
        bot.send_message(message.chat.id, 'Вы ввели не число. Попробуйте еще раз.')

        send_text(message)

#
#
if __name__ == "__main__":
    # бесконечная работа бота

    bot.infinity_polling()

