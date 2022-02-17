import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Mirage")
    item2 = types.KeyboardButton("Dust2")
    item3 = types.KeyboardButton("Inferno")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nВыберите карту, чтобы продолжить."
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    g1 = open("ct.gif", 'rb')
    g2 = open("kitchen.gif", 'rb')
    g3 = open("short.gif", 'rb')
    g4 = open("stairs.gif", 'rb')
    g5 = open("window.gif", 'rb')
    g6 = open("city(long) (2).gif", 'rb')
    g7 = open("Ct(mid).gif", 'rb')
    g8 = open("Window B(tunnel).gif", 'rb')
    g9 = open("Ct Cross deep(long).gif", 'rb')
    g10 = open("Ct Cross close(long).gif", 'rb')
    g11 = open("xbox(t spawn).gif", 'rb')
    g12 = open("Arch(mid).gif", 'rb')
    g13 = open("Library(mid).gif", 'rb')
    g14 = open("Ct(banana).gif", 'rb')
    g15 = open("graveyard(banana).gif", 'rb')

    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Stairs(Pit)')
    item2 = types.KeyboardButton('City(Pit)')
    item3 = types.KeyboardButton('Window(T spawn)')
    item4 = types.KeyboardButton('Kitchen(B apps)')
    item5 = types.KeyboardButton('Short(B apps)')
    item6 = types.KeyboardButton('Go back')

    markup1.add(item1, item2, item3, item4, item5, item6)

    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1 = types.KeyboardButton('Deep City(Long)')
    i2 = types.KeyboardButton('Ct Cross (long)')
    i3 = types.KeyboardButton('City(Mid)')
    i4 = types.KeyboardButton('Window B(Tunnel)')
    i5 = types.KeyboardButton('Xbox(T spawn)')
    i6 = types.KeyboardButton('Go back')

    markup2.add(i1, i2, i3, i4, i5, i6)

    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    s1 = types.KeyboardButton('Arch(Mid)')
    s2 = types.KeyboardButton('Ct(Banana)')
    s3 = types.KeyboardButton('Graveyard(Banana)')
    s4 = types.KeyboardButton('Library(Mid)')
    s5 = types.KeyboardButton('')
    s6 = types.KeyboardButton('Go back')

    markup3.add(s1, s2, s3, s4, s5, s6)

    markup4 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    m1 = types.KeyboardButton('Mirage')
    m2 = types.KeyboardButton('Dust2')
    m3 = types.KeyboardButton('Inferno')

    markup4.add(m1, m2, m3)

    if message.chat.type == 'private':
        if message.text == 'Mirage':
            bot.send_message(message.chat.id, "Какую позицию хотите выбрать?", reply_markup=markup1)
        elif message.text == 'Stairs(Pit)':
            bot.send_video(message.chat.id, g4)
        elif message.text == 'City(Pit)':
            bot.send_video(message.chat.id, g1)
        elif message.text == 'Window(T spawn)':
            bot.send_video(message.chat.id, g5)
        elif message.text == 'Kitchen(B apps)':
            bot.send_video(message.chat.id, g2)
        elif message.text == 'Short(B apps)':
            bot.send_video(message.chat.id, g3)
        elif message.text == 'Dust2':
            bot.send_message(message.chat.id, "Какую позицию хотите выбрать?", reply_markup=markup2)
        elif message.text == 'Xbox(T spawn)':
            bot.send_video(message.chat.id, g11)
        elif message.text == 'Deep City(Long)':
            bot.send_video(message.chat.id, g6)
        elif message.text == 'Ct Cross (long)':
            bot.send_video(message.chat.id, g9)
            bot.send_video(message.chat.id, g10)
        elif message.text == 'City(Mid)':
            bot.send_video(message.chat.id, g7)
        elif message.text == 'Window B(Tunnel)':
            bot.send_video(message.chat.id, g8)
        elif message.text == 'Inferno':
            bot.send_message(message.chat.id, "Какую позицию хотите выбрать?", reply_markup=markup3)
        elif message.text == 'Graveyard(Banana)':
            bot.send_video(message.chat.id, g15)
        elif message.text == 'Arch(Mid)':
            bot.send_video(message.chat.id, g12)
        elif message.text == 'Ct(Banana)':
            bot.send_video(message.chat.id, g14)
        elif message.text == 'Library(Mid)':
            bot.send_video(message.chat.id, g13)
        elif message.text == 'Go back':
            bot.send_message(message.chat.id, "Какую карту хотите выбрать?", reply_markup=markup4)
        else:
            bot.send_message(message.chat.id, 'Извините, такой команды не существует')


bot.polling(none_stop=True)
