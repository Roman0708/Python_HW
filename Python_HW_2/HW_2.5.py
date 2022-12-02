# Реализуйте алгоритм перемешивания списка.

import time

random_list1 = [1,2,3,4,5,6,7,8,9]
# random_list2 = []
# random_list3 = [1,2,3,4]
# random_list5 = [0,1,2,3,4,5,6,7,8,9]

# Пересортировщик основан на определении размера списка
def desorter (input_list: list):
    index_list = []
    for i in range(0, len(input_list)):
        random = random_number(len(input_list) - 1)
        if (i not in index_list or random not in index_list) and i != random: # Условие для повышения изменяемости списка
            help = input_list[i]
            input_list[i] = input_list[random]
            input_list[random] = help
            index_list.append(i)
            index_list.append(random)
            # print(input_list)
    print(input_list)


# Определяет позицию в списке, с которой будет менять текущую
# Эта функция вытекла из last_check_digit для масштабирования рандомайзера
def random_number(limit): 

    if (limit % 10 == 0 and limit > 0) or (limit // 10 == 0): # check that 
        random = last_digit_check(limit)
        return(random)        

    else: 
        return(random_number(limit//10)*10 + random_number(limit%10))


# Сам рандомайзер, написанный в первую очередь. Работает с помощью библиотеки time на миллисекундах
def last_digit_check(digit):
    if digit == 0:
        return(0)
    else:
        while True: # limit's last digit check
            time_to_string = str(time.time())
            # print(time_to_string)
            string1 = time_to_string.split(".")
            # print(string1)
            random_number = int(string1[1][len(string1) - 3])
            if digit >= random_number:
                return(random_number)
            else:
                False


# desorter(random_list5)






# Это я уже игрался как ребенок с собственным рандомайзером :)
# Рандомайзер написал для автоматического определения предела вводимого списка

# n = int(input("Введите предел рандома: "))
# a = random_number(n)
# print(a)