import csv
import data_base as db
import os


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
    with open('DB.csv', 'r', newline='') as csvfile:
        fieldnames = ['last_name','first_name', 'phone_number']
        reader = csv.DictReader(csvfile,fieldnames=fieldnames, delimiter=";")
        count = 0
        for row in reader:
            if row['first_name'] == input_name and row['last_name'] == input_surname:
                count += 1
                print(f"{row['first_name']} {row['last_name']}, номер телефона: {row['phone_number']}")
        if count == 0:
            print("Контакт не найден")
        csvfile.close()
        print("---")


def delete_contact(input_name,input_surname):
    with open('DB.csv', 'r+', newline='') as csvfile:
        fieldnames = ['last_name','first_name', 'phone_number']
        reader = csv.DictReader(csvfile,fieldnames=fieldnames, delimiter=";")

        exist = False
        count = 1

        for row in reader:
            if row['first_name'] != input_name and row['last_name'] != input_surname:
                with open('newDB.csv', 'a', newline='') as newcsvfile:
                    writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames,delimiter=";")
                    writer.writerow(row)
                count += 1
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



def check_input(arg):
    while arg.isdigit() != True:
        print('\nВы ввели не число.')
        arg = input('Введите соответствующий пункт меню: ')
    return int(arg)