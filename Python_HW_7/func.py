import csv
import data_base as db
import os


fieldnames = {1:'last_name',2:'first_name',3:'phone_number'}
edit_dict = {}


def name():
    input_name = input("Введите имя: ")
    return(input_name.capitalize())


def surname():
    input_surname = input("Введите фамилию: ")
    return(input_surname.capitalize())


def phone_number():
    input_phone_number = int(input("Введите номер телефона: "))
    return(input_phone_number)


def database_manual_input(name,surname,phone_number):
    with open('DB.csv', 'a', newline='') as csvfile:
        fieldnames = ['last_name','first_name', 'phone_number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=";")
        writer.writerow({'first_name': name, 'last_name': surname, 'phone_number': phone_number})
        csvfile.close()
        print(f"Контакт {surname} {name} добавлен")


def search_contact(input_name,input_surname):
    global edit_dict
    with open('DB.csv', 'r', newline='') as csvfile:
        fieldnames = ['last_name','first_name', 'phone_number']
        reader = csv.DictReader(csvfile,fieldnames=fieldnames, delimiter=";")
        count = 0
        for row in reader:
            if row['first_name'] == input_name and row['last_name'] == input_surname:
                count += 1
                print(f"{row['last_name']} {row['first_name']}, номер телефона: {row['phone_number']}")
                edit_dict = {1:row['last_name'],2:row['first_name'],3:row['phone_number']}                  # для редактирования
                return(edit_dict)                                                                           # контактов
        if count == 0:
            print("Контакт не найден")
            return(False)
        csvfile.close()
        print("---")


def delete_contact(input_name,input_surname):
    with open('DB.csv', 'r+', newline='') as csvfile:
        fieldnames = ['last_name','first_name', 'phone_number']
        reader = csv.DictReader(csvfile,fieldnames=fieldnames, delimiter=";")

        exist = False

        for row in reader:
            if row['first_name'] != input_name and row['last_name'] != input_surname:
                with open('newDB.csv', 'a', newline='') as newcsvfile:
                    writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames,delimiter=";")
                    writer.writerow(row)
                newcsvfile.close()
            else:
                print(f'Контакт {input_name} {input_surname} удален')
                exist = True

        if exist == False:
            print("Контакт не найден")
        else:
            csvfile.close()
            scr_f, dst_f = 'newDB.csv','DB.csv'
            os.remove(dst_f)
            os.rename(scr_f,dst_f)

            
        csvfile.close()


def edit_choice():
    print("""Что вы хотеите изменить?
1 - Фамилию
2 - Имя
3 - Номер телефона
4 - Закончить редактирование""")
    choice = input()
    check_input(choice)
    while int(choice) < 0 and int(choice) > 5:
        choice = input('Введите соответствующий пункт меню: ')
    return int(choice)


def check_input(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)


def edit_contact(input_name,input_surname):
    global edit_dict
    if search_contact(input_name,input_surname) != False:
        data_type = edit_choice()
        if data_type == 1:
            new_data = surname()
        elif data_type == 2:
            new_data = name()
        elif data_type == 3:
            new_data = phone_number()
        else:
            return()
            
        edit_dict[data_type] = new_data
        # print(edit_dict[1])
        delete_contact(input_name,input_surname)
        database_manual_input(edit_dict[1],edit_dict[2],edit_dict[3])
        
    # else:
    #     print("Контакт не найден")


    
    # new_name = name()
    # delete_contact(name,surname)
    # database_manual_input(new_name,new_surname)