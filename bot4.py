import telebot
from telebot import types

btns  = None
markup = None

bot = telebot.TeleBot('6112379025:AAF85X-PbXX1-CGlzijxow9sOU9F-JWP2DM') # Токен для телеграмма
buttons = [range(1,10)] # Список кнопок

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Играть с ботом")
    btn2 = types.KeyboardButton("Играть с другом")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text=f"Привет, {message.from_user.first_name}, выбери режим игры!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mode(message):
    global btns, markup
    if (message.text == "Играть с ботом"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
        markup.add(*btns)
        msg = bot.send_message(message.chat.id, 'Сделайте ход', reply_markup=markup)
        bot.register_next_step_handler(msg, game)
    elif (message.text == "Играть с другом"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btns = [types.KeyboardButton("1"), types.KeyboardButton("2"), types.KeyboardButton("3"),
                types.KeyboardButton("4"), types.KeyboardButton("5"), types.KeyboardButton("6"),
                types.KeyboardButton("7"), types.KeyboardButton("8"), types.KeyboardButton("9")]
        markup.add(*btns)
        msg = bot.send_message(message.chat.id, 'Сделайте ход', reply_markup=markup)
        bot.register_next_step_handler(msg, game)

def game(message):
    if (message.text == button for button in buttons):
        btns[int(message.text)-1] = types.KeyboardButton(" ")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(*btns)
        msg = bot.send_message(message.chat.id, f'Вы походили на клетку номер {message.text}', reply_markup=markup)
        bot.register_next_step_handler(msg, game)

if __name__ == "__main__":
    bot.infinity_polling()