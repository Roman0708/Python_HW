# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной идексах.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных идексах элементы 3 и 9, ответ: 12

def sum_odd_index(num_list: list):
    # result_list = []
    result = 0
    for i in range(0,len(num_list) - 1):
        if i % 2 != 0:
            # result_list.append(num_list[i])
            result += num_list[i]
    print(result)
        
sum_odd_index([2, 3, 5, 9, 3])