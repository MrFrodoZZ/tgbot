# -*- coding: utf-8 -*-
from telebot import TeleBot, types

from config import *
from db_interact import *


bot = TeleBot(token=token)


@bot.message_handler(commands=['start', 'profile', 'testcmd', 'menu', 'help'])
def base_commands(msg):
    user, text = msg.from_user.id, msg.text
    if text == '/start':
        if not check_user(user):
            new_user(user)
            bot.send_message(user, 'Добро пожаловать!\nПожалуйста, введите ваш ФИО')
            bot.register_next_step_handler(msg, process_one)
        else:
            bot.send_message(user, 'Вы уже зарегистрированы!')
    if text in ['/menu', '/help']:
        if check_user(user):
            bot.send_message(user, )


def process_one(msg):
    user, text = msg.from_user.id, msg.text
    if len(text.split()) == 3:
        insert_name(user, text)
        bot.send_message(user, 'Укажите вашу группу')
        bot.register_next_step_handler(msg, process_two)
    else:
        bot.reply_to(msg, 'Пожалуйста, укажитие фамилию, имя и отчество через пробелы')
        bot.register_next_step_handler(msg, process_one)


def process_two(msg):
    user, text = msg.from_user.id, msg.text
    bot.send_message(user, "Регистрация завершена.")


@bot.message_handler(func=lambda msg: True)
def any_text(msg):
    user = msg.from_user.id
    text = msg.text
    if text in ['.delprof', '.nullprof', '.botoff']:
        if user in admins:
            if text == '.delprof':
                delete_self(user)
                bot.reply_to(msg, 'DEBUG: Your profile was deleted successfully.')
            if text == '.botoff':
                bot.reply_to(msg, 'DEBUG: Bot is OFF.')
                bot.stop_bot()


bot.infinity_polling()
