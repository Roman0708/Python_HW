import  func as f
from pathlib import Path
import csv

def init_data_base():
    data_base = dict.fromkeys(['first_name','surname','phone_number'])
    with open('DB.csv', 'r', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name','phone_number']
            reader = csv.DictReader(csvfile,fieldnames=fieldnames, delimiter=";")
            # id = 1
            for row in reader:
                data_base["first_name"]=row['first_name']
                data_base['surname']=row['last_name']
                data_base['phone_number']=row['phone_number']
                # print(data_base)
                # data_base.items
            csvfile.close()


# print(data_base)