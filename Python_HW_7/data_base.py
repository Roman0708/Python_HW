import  func as f
from pathlib import Path
import csv

data_base = dict.fromkeys(['first_name','surname','phone_number'])

def database_manual_input(name,surname,phone_number):
    with open('DB.csv', 'a', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name','phone_number']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=";")
        writer.writerow({'first_name': name, 'last_name': surname, 'phone_number': phone_number})

        # data_base.update({'first_name': name, 'surname': surname, 'phone_number': phone_number})
        # return({'first_name': name, 'surname': surname, 'phone_number': phone_number})

name = f.name()
surname = f.surname()
phone_number = f.phone_number()

database_manual_input(name,surname,phone_number)

print(data_base)


