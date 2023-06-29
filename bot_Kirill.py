import telebot
from telebot import types

# Токена для телеграмма
bot = telebot.TeleBot('6064467428:AAF8R7L7dLDJQ_3OqoJSxwWZYE_IeVmxfKQ')

# КНОПКИ В БОТЕ

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздороваться")
    btn2 = types.KeyboardButton("Задать вопрос")
    btn3 = types.KeyboardButton("Авторы проекта")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id,
                     text= f"Привет! Я тестовый бот для тебя, {message.from_user.first_name}!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Поздороваться" or message.text== "/hello"):
        bot.send_message(message.chat.id, text=f"Привет, {message.from_user.first_name}! Спасибо за то, что тестируешь меня!")
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
        bot.send_message(message.chat.id, text="Я пока что только умею отвечать на вопросы из заранее заданных категорий. Но в будущем, я научусь делать гораздо больше 🚀")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Поздороваться")
        button2 = types.KeyboardButton("Задать вопрос")
        button3 = types.KeyboardButton("Авторы проекта")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, message.text)

# def repeat(message):
#     bot.send_message(message.chat.id, message.text)
#
#
if __name__ == "__main__":
    # бесконечная работа бота

    bot.infinity_polling()
