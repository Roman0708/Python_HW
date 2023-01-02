import  func as f
from pathlib import Path
import csv

db=[]
id=0
db_dict = {}

def init_data_base():
    global db
    global id
    with open('DB.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            db.append(row)
            id += 1
            db_dict[id]=db[id-1]
        csvfile.close()
    
init_data_base()
print(db)
# # print(data_base)

