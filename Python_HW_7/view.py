from telegram import Update,ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import func as f


def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


def main_menu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    update.message.reply_text(f'''Телефонный справочник\n
/add_contact_command - Добавить контакт\n
/find_contact_command - Найти контакт\n
/delete_contact_command - Удалить контакт\n
/4 - Редактировать контакт\n
Что вы хотите сделать?''')


def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.text
    return(name.capitalize())


def get_surname(update: Update, context: ContextTypes.DEFAULT_TYPE):
    surname = update.message.text
    return(surname.capitalize())


def get_phone_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phone_number = update.message.text
    return(phone_number)


def add_contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    surname = get_surname()
    name = get_name()
    phone_number = get_phone_number()
    f.database_manual_input(name,surname,phone_number)
    update.message.reply_text(f'Контакт {surname} {name} добавлен')


def find_contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    surname = get_surname()
    name = get_name()
    result = f.search_contact(name,surname)
    update.message.reply_text(result.values())


def delete_contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    surname = get_surname()
    name = get_name()
    result = f.delete_contact(name,surname)
    if result is True:
        update.message.reply_text(f'Контакт {name} {surname} удален')
    else:
        update.message.reply_text(f'Контакт не найден')


# def edit_contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     surname = get_surname()
#     name = get_name()
#     result = f.search_contact
#     if result != "Контакт не найден":
#         lambda a:
#         btn_1 = InlineKeyboardButton("Имя",callback_data=get_name())
#         btn_2 = InlineKeyboardButton("Фамилия",callback_data=get_surname())
#         btn_3 = InlineKeyboardButton("Номер телефона",callback_data=get_phone_number())
#         choice_kb = InlineKeyboardMarkup.add(btn_1).add(btn_2).add(btn_3)
#         update.message.reply_text(f'Что нужно изменить?')
#         update.message.reply_markup = choice_kb
                
#         f.edit_dict[] = new_data
    
#         f.delete_contact(name,surname)
#         f.database_manual_input(edit_dict[1],edit_dict[2],edit_dict[3])
#         update.message.reply_text(f'')


app = ApplicationBuilder().token("5911271467:AAGYlr2AFk1K-U4uSQPNdnp_JQY1oAVOo0c").build()
print('bot started')
app.add_handler(CommandHandler("hello", hello))

app.run_polling()