import telebot
import datetime
import random
import schedule
import time

bot = telebot.TeleBot()

type_clean = ['Уборка кухни', 'Уборка комнат', 'Уборка всей квартиры']

air_control = 'Проветрить квартиру'


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Ну привет')
    chat_id = message.chat.id
    save_chat_id(chat_id)
    send_text(chat_id)
    bot.stop_polling()


def CalculateTypeClean():
    chanse = random.randint(0, 100)
    if chanse <= 45:
        return type_clean[0]
    elif chanse <= 80:
        return type_clean[1]
    elif chanse > 80:
        return type_clean[2]


def send_text(chat_id):
    bot.send_message(chat_id, CalculateTypeClean())


def save_chat_id(chat_id):
    file = open('chatid.txt', 'w')
    file.write(str(chat_id))
    file.close()


def load_chat_id():
    file = open('chatid.txt', 'r')
    chat_id = file.read()
    file.close()
    return chat_id

def main():
    chat_id = load_chat_id()
    if not chat_id:
        bot.polling()
    else:
        send_text(chat_id)

main()