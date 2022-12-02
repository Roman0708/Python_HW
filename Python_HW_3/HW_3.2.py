# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def sum_of_couple(num_list: list):
    i = 0
    result_list = []
    while (len(num_list) - 1)/2 - i >= 0:
        result_list.append(num_list[i] * num_list[len(num_list) - 1 - i])
        i += 1
    print(result_list)

sum_of_couple([2, 3, 4, 5, 6])

