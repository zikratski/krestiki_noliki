import config # в конфиге хранится токен и прочая инфа в будущем
import telebot # библиотека для телеграм-бота

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
