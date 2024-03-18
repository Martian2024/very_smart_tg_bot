import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from user import User
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

bot = telebot.TeleBot(open('token.txt').readline())

def setup_database():
    engine = create_engine('sqlite:///database.db')
    engine.connect()


@bot.message_handler(commands=['start'])
def start(message):
    user = User(message.chat.id)
    ACTIVE_CHATS.append(user)
    print(user.chat_id)


if __name__ == '__main__':
    ACTIVE_CHATS = []
    bot.infinity_polling()