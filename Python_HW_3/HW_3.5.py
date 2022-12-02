# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input("Введите число: "))

def fibonacci(num: int):
    result_list = [1,0,1]
    i = 0
    
    while i < num * 2 - 2:
        helper = result_list[i + 1] + result_list[i + 2]
        result_list.append(helper)
        if i % 4 == 0:
            result_list.insert(0, helper * (- 1))
        else:
            result_list.insert(0, helper)
        i += 2

    print(result_list)

fibonacci(number)