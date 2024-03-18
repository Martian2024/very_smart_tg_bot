import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from user import User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

bot = telebot.TeleBot(open('token.txt').readline())
engine = create_engine('sqlite:///database.db')
engine.connect()


@bot.message_handler(commands=['show_graphics'])
def main_menu(message):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Вернуться на главную", callback_data='main_menu')
    button2 = InlineKeyboardButton(text="<", callback_data='next_page')
    button3 = InlineKeyboardButton(text=">", callback_data='prev_page')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, text='Графики', reply_markup=keyboard)

@bot.message_handler(commands=['new_plot'])
def start_plotting(message):
    bot.register_next_step_handler(bot.send_message(message.chat.id, text='Отправьте файл с данными'), get_data)

def get_data(message):
    '''file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)'''

    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Тип графика 1", callback_data='plot_type_1')
    button2 = InlineKeyboardButton(text="Тип графика 2", callback_data='plot_type_2')
    button3 = InlineKeyboardButton(text="Тип графика 2", callback_data='plot_type_3')
    keyboard.add(button1, button2, button3)
    bot.send_message(message.chat.id, text='Выберите тип графика', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'plot_type_1')
def plot_type_1(call):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Сохранить график", callback_data='save_plot')
    button2 = InlineKeyboardButton(text="Скачать график", callback_data='download_plot')
    keyboard.add(button1, button2)
    bot.send_message(call.message.chat.id, text='Графики', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'plot_type_2')
def plot_type_2(call):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Сохранить график", callback_data='save_plot')
    button2 = InlineKeyboardButton(text="Скачать график", callback_data='download_plot')
    keyboard.add(button1, button2)
    bot.send_message(call.message.chat.id, text='Графики', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'plot_type_3')
def plot_type_3(call):
    keyboard = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Сохранить график", callback_data='save_plot')
    button2 = InlineKeyboardButton(text="Скачать график", callback_data='download_plot')
    keyboard.add(button1, button2)
    bot.send_message(call.message.chat.id, text='Графики', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'save_plot')
def save_plot(call):
    pass

@bot.callback_query_handler(func=lambda call: call.data == 'download_plot')
def plot_type_3(call):
    pass


if __name__ == '__main__':
    bot.infinity_polling()