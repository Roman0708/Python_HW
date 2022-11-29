# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

numb = input("Введите число: ")

i = numb.split(".")

complete_numb = int(i[0])
divided_numb = int(i[1])

sum = 0
while complete_numb != 0:
    sum = sum + complete_numb % 10
    complete_numb = complete_numb // 10
while divided_numb != 0:
    sum = sum + divided_numb % 10
    divided_numb = divided_numb // 10
print(sum)