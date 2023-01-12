import telebot
from telebot import types
import func as f
import data_base as db



db.init_data_base()
bot = telebot.TeleBot("5911271467:AAGYlr2AFk1K-U4uSQPNdnp_JQY1oAVOo0c", parse_mode='MARKDOWN')


@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(
        message.chat.id, f'Я тебя не понимаю. Введи: /help.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'''Привет, *{message.from_user.first_name}!*\n
В любой непонятной ситуации введи\n
команду: /help\n
Чтобы вызвать главное меню введи: /main''')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'''/start - начать сначала (перезапустить бота)\n
/main - главное меню\n
/help - вызвать справку''')


command = ''
name_it = ''
surname_it = ''
number_it = ''

new_number_it = ''


@bot.message_handler(content_types=['text'])
def main(message):
    global command
    if message.text == '/main':
        bot.send_message(message.chat.id, (f'''Телефонный справочник\n
/1 - Добавить контакт\n
/2 - Найти контакт\n
/3 - Удалить контакт\n
/button - Редактировать контакт\n
Что вы хотите сделать?'''))
        db.init_data_base()
        

    elif message.text == '/1':
        command = '1'
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, get_name)


    elif message.text == '/2':
        command = '2'
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, get_name)


    elif message.text == '/3':
        command = '3'
        bot.send_message(message.chat.id, f'Введите имя')
        bot.register_next_step_handler(message, get_name)


    # elif message.text == '/4':
    #     command = '4'
    #     button('4')
        
    else:
        bot.send_message(message.chat.id, f'Неизвестная команда. Введи: /help.')


def get_name(message):
    global command
    global name_it
    name_it = str(message.text).capitalize()
    if command != 'edit':
        bot.send_message(message.chat.id, f'Введите фамилию')
        bot.register_next_step_handler(message, get_surname)
        
    

def get_surname(message):
    global command
    global surname_it
    surname_it = str(message.text).capitalize()
    if command == '1':
        bot.send_message(message.chat.id, f'Введите номер телефона')
        bot.register_next_step_handler(message, get_number)
    elif command == '2':
        result = f.search_contact(name_it,surname_it)
        bot.send_message(message.chat.id, f'{result[1]} {result[2]}, {result[3]}')
    elif command == '3':
        result = f.delete_contact(name_it,surname_it)
        if result is True:
            bot.send_message(message.chat.id, f'Контакт {name_it} {surname_it} удален')
            db.init_data_base()
        else:
            bot.send_message(message.chat.id, f'Контакт не найден')
    

def get_number(message):
    global command
    global number_it
    number_it = message.text
    if command == '1':
        f.database_manual_input(name_it,surname_it,number_it)
        bot.send_message(message.chat.id, f'Контакт {name_it} {surname_it} добавлен')
        db.init_data_base()


@bot.message_handler(commands=['button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_1 = types.KeyboardButton("Фамилия", callback_data='surname')
    btn_2 = types.KeyboardButton("Имя",callback_data='name')
    btn_3 = types.KeyboardButton("Номер телеофна",callback_data='number')
    markup.add(btn_1,btn_2,btn_3)

    bot.send_message(message.chat.id, f"""Что вы хотеите изменить?
1 - Фамилию
2 - Имя
3 - Номер телефона
4 - Закончить редактирование""", reply_markup=markup)


@bot.callback_query_handler(func= lambda call:True)
def edit_choice(call):
    global choice
    choice = ''
    if call.message:
        if call.data == 'surname':
            choice = "1"
            bot.send_message(call.message.chat.id, f'Введите фамилию')
        elif call.data == 'name':
            choice = "2"
            bot.send_message(call.message.chat.id, f'Введите имя')
        elif call.data == 'number':
            choice = "3"
            bot.send_message(call.message.chat.id, f'Введите номер телефона')

# @bot.message_handler(content_types=['text'])
# def edit_choice(message):
#     global choice
#     global new_data
#     choice = ""
#     new_data = ""
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn_1 = types.KeyboardButton("1")
#     btn_2 = types.KeyboardButton("2")
#     btn_3 = types.KeyboardButton("3")
#     markup.add(btn_1,btn_2,btn_3)
#     if(message.text == "1"):
#         choice = "1"
#         bot.send_message(message.chat.id, f'Введите фамилию')
#         new_data = get_surname
#     elif(message.text == "2"):
#         choice = "2"
#         bot.send_message(message.chat.id, f'Введите имя')
#         new_data = get_name
#     elif(message.text == "3"):
#         choice = "3"
#         bot.send_message(message.chat.id, f'Введите номер телефона')
#         new_data = get_number
#     else:
#         main
#         return()
#     f.edit_dict[choice] = new_data
#     result = f.search_contact(name_it,surname_it)
#     if result != "Контакт не найден":
#         f.delete_contact(name_it,surname_it)
#         f.database_manual_input
#     else:
#         bot.send_message(message.chat.id, f"Контакт не найден")


print('server start')
bot.infinity_polling()