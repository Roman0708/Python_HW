# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

y = int(input("Введите номер четверти: "))

if (y == 1):
    print("x(0:inf), y(0:inf)")
elif (y == 2):
    print("x(-inf:0), y(0:inf)")
elif (y == 3):
    print("x(-inf:0, y(-inf:0)")
elif (y == 4):
    print("x(0:inf), y(-inf:0)")
else:
    print("Неправильный номер четверти")