# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input("Введите число: "))

result = 0

result_list = [(1 + 1/i)**i for i in range(1, n + 1)]
for i in range(len(result_list)): result += result_list[i]

print(result)

