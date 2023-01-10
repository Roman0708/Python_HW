import  func as f
from pathlib import Path
import csv


id=0
db_dict = {}

def init_data_base():

    global id
    with open('DB.csv', 'r', newline='') as csvfile:
        fieldnames = ['last_name','first_name', 'phone_number']
        reader = csv.DictReader(csvfile,fieldnames=fieldnames, delimiter=";")
        for row in reader:
            id += 1
            db_dict[id] = row['last_name'],row['first_name'],row['phone_number']
        csvfile.close()
    
# init_data_base()
# print(db_dict)
# # print(data_base)

