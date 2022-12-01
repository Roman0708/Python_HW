# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input("Введите число: "))

def sum_sequence(number: int):
    list = []
    answer = 0
    for i in range (1, number + 1):
        list.append((1 + 1/i)**i)
        answer += list[i - 1]
        # print(list[i-1])
    print("Сумма: ",answer)
    

sum_sequence(n)