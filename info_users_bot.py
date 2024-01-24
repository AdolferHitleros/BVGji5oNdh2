import telebot
from telebot import types

bot = telebot.TeleBot('6845662838:AAETW9l6DGusa3I4IL3WLBrOuTbIziaiqMs')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('База данных user_ip', callback_data='ip_give'))
    markup.add(types.InlineKeyboardButton('Узнать информацию по конкретному ip-адресу', callback_data='info_give'))

    bot.send_message(message.chat.id, 'Халло анд велкоме!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def ip_sender(callback):
    if callback.data == 'ip_give':
        with open('info_users.txt', 'r', encoding='utf-8') as f:
            bot.send_message(callback.message.chat.id, f'{f.read()}')
            print(f.read())

    if callback.data == 'info_give':
        pass

bot.polling(none_stop=True)