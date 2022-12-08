# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

# import os.path

# print(os.path.abspath("HW_4.5.py"))

from pathlib import Path
import os

# print(os.path.realpath(__file__))
# print(os.getcwd())

home = Path.home()
path_absolute = Path(os.path.realpath(__file__))
# print(home)
print(path_absolute.parent)

input_1 = Path(path_absolute.parent,input("Введите название первого файла: "))
# path_1 = Path("Python_HW_4",input_1)
# print(input_1)
input_2 = Path(path_absolute.parent,input("Введите название второго файла: "))
# path_2 = Path("Python_HW_4",input_2)
# print(input_2)

os.chdir(path_absolute.parent)

with open(input_1,'r') as frst_file:
    global frst_pl 
    frst_pl = frst_file.read()

with open(input_2,'r') as scnd_file:
    global scnd_pl 
    scnd_pl = scnd_file.read()

def string_to_pl_list(input_string):
    pl_lst = input_string[:-4].split(" + ")
    return(pl_lst)

# frst_pl_lst = frst_pl[:-4].split(" + ")

frst_pl_list = string_to_pl_list(frst_pl)
scnd_pl_list = string_to_pl_list(scnd_pl)

print(frst_pl_list)
print(scnd_pl_list)

def string_to_parts(input_pl_lst):
    out_dict = dict()
    for i in range(len(input_pl_lst)):
        if input_pl_lst[i].find('(**') != -1:
            help_list = input_pl_lst[i].split("*")
            out_dict.update({int(input_pl_lst[i][-2]):int(help_list[0])})
        else:
            out_dict.update({0:int(input_pl_lst[i])})
            # print(out_dict)
    return(out_dict)

frst_dict = string_to_parts(frst_pl_list)
scnd_dict = string_to_parts(scnd_pl_list)

print(frst_dict)
print(scnd_dict)

print(len(scnd_dict))
# print(frst_pl,scnd_pl)

