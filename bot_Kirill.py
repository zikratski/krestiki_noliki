import telebot
from telebot import types
import configure
#
#
# # Токена для телеграмма
bot = telebot.TeleBot(configure.token)
#
# # @bot.message_handler(commands=['start','end'])
# # def say_hello_or_bye(message):
# #     if message.start == 'start':
# #         bot.send_message(message.chat.id, 'Привет, друг, давай поиграем в крестики-нолики!')
# #     elif message.end == 'end':
# #         bot.send_message(message.chat.id, 'Прощай, друг, надеюсь, что ты вернёшься')
#
# keyboard_list = types.ReplyKeyboardMarkup()
# keyboard_list.row('Привет', 'Пока')
#
# #
# @bot.message_handler(commands=['start'])
# def say_hello(message):
#     bot.send_message(message.chat.id, 'Привет, друг, давай поиграем в крестики-нолики!', reply_markup=keyboard_list)
#
# @bot.message_handler(commands=['end'])
# def say_bye(message):
#     bot.send_message(message.chat.id, 'Прощай, друг, надеюсь, что ты вернёшься')
#
#
#
#
#
@bot.message_handler(content_types=['text'])
# # def echo(message):
# #     bot.send_message(message.chat.id, text=f'{message.text}')
def send_text(message):
    while True:
        if message.isdigit():
            bot.send_message(message.chat.id, f'Наше число, умноженное на 2: {message.text*2}')
        else:
            bot.send_message(message.chat.id, text=f'{message.text}')
#
#
if __name__ == "__main__":
    bot.infinity_polling()

