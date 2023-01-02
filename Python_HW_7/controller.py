import func as f


def main_screen():
    while True:
        print("Телефонный справочник\n")
        print("1 - Добавить контакт\n")
        print("2 - Найти контакт\n")
        print("3 - Удалить контакт\n")
        print("9 - Выход\n")
        print("-"*10)
        input_command = f.check_input(input("Что вы хотите сделать?\n"))


        if input_command == 1:
            name = f.name()
            surname = f.surname()
            phone_number = f.phone_number()
            f.database_manual_input(name,surname,phone_number)
            main_screen()


        elif input_command == 2:
            name = f.name()
            surname = f.surname()
            f.search_contact(name,surname)
            input()
            main_screen()


        elif input_command == 9:
            quit()


