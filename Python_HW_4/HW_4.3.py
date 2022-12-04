# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

input_list = [1, 1, 2, 3, 4, 4, 4]

help_set = set(input_list)
result_set = set(input_list)
help_lst = input_list.copy()

for i in range(0,len(input_list) - 1):
    if input_list[i] in help_set:
        #print(help_lst[i])
        help_set.remove(input_list[i])
        help_lst.remove(input_list[i])
        
help_set = set(help_lst)
# print(result_set)
# print(help_set)
result_set.difference_update(help_set)
result_lst = list(result_set)

print(result_lst)
