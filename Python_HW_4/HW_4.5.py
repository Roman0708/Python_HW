# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

# import os.path

# print(os.path.abspath("HW_4.5.py"))

from pathlib import Path
import os

home = Path.home()
path_absolute = Path(os.path.realpath(__file__))            

input_1 = Path(path_absolute.parent,input("Введите название первого файла: "))
input_2 = Path(path_absolute.parent,input("Введите название второго файла: "))

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
        if input_pl_lst[i].find('(**') != -1:                               # Проверяем, что элемент последовательности не последний
            help_list = input_pl_lst[i].split("*")                          # Разделяем многочлен на список коэффициентов и
            out_dict.update({int(input_pl_lst[i][-2]):int(help_list[0])})   # Добавление в словарь ключа (степени) и элемента (коэффициента). Программа работает только при степени <=9
        else:
            out_dict.update({0:int(input_pl_lst[i])})
            # print(out_dict)
    return(out_dict)

frst_dict = string_to_parts(frst_pl_list)
scnd_dict = string_to_parts(scnd_pl_list)

print(frst_dict)
print(scnd_dict)

def dict_sum(dict_1,dict_2):
    result_dict = {}
    for i in range(max(len(dict_1),len(dict_2))):                   # Определяем длину самого большого словаря
        result_dict.update({i:dict_1.get(i,0)+dict_2.get(i,0)})     # Добавляем в результирующий словарь сумму элементов с одинаковыми ключами (одно значение если ключ уникален для всех словарей)
    return(result_dict)

result_dict = dict_sum(frst_dict,scnd_dict)
print(result_dict)

result_string = ""
for i in range(len(result_dict)):
    result_string += str(f"{result_dict[(len(result_dict)-1)-i]}*(x**{(len(result_dict)-1)-i}) + ")
if result_string[-5] == "0":
    result_string = result_string[:-10]
else:
    result_string = result_string[:-3]
result_string += " = 0"

# print(result_string)

output = Path(path_absolute.parent,"output.md")

with open(output,'w') as output:
    output.write(result_string)