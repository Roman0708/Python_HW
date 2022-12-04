# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

natural_number = int(input("Введите натуральное число: "))

result_lst = []
for i in range(2,natural_number + 1):
    for j in result_lst:
        if i % j == 0:
            break
    else:
        result_lst.append(i)
print(result_lst)