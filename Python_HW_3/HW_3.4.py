# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input("Введите десятичное число: "))

def ten_to_two(num_10):
    answer = ""
    while num_10 > 0:
        answer = str(num_10 % 2) + answer
        num_10 = num_10 // 2
    return(int(answer))


a = ten_to_two(number)
print(a)