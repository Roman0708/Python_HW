import func as f
import data_base as db


def main_screen():
    db.init_data_base()
    while True:
        print("Телефонный справочник\n")
        print("1 - Добавить контакт\n")
        print("2 - Найти контакт\n")
        print("3 - Удалить контакт\n")
        print("9 - Выход\n")
        print("-"*10)
        input_command = f.check_input(input("Что вы хотите сделать?\n"))


        if input_command == 1:
            surname = f.surname()
            name = f.name()
            phone_number = f.phone_number()
            f.database_manual_input(name,surname,phone_number)
            main_screen()


        elif input_command == 2:
            surname = f.surname()
            name = f.name()
            f.search_contact(name,surname)
            input()
            main_screen()

        
        elif input_command == 3:
            surname = f.surname()
            name = f.name()
            f.delete_contact(name,surname)
            input()
            main_screen()


        elif input_command == 9:
            quit()


