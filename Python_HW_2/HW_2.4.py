# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input("Введите N: "))

def index_mult(number: int):
    number_list = []
    for i in range(-number, number + 1):
        number_list.append(i)
    # print(number_list)

    index_list = []
    j = any
   
    while j != " ":
        j = (input("\nДля окончания ввода введите пробел\nВведите индекс: "))
        
        try: 
            int(j) in range(0, len(number_list)-1)
            index_list.append(int(j))
            print(index_list) # Хотел оставить закомментированной эту проверку, но так более юзер-френдли выглядит :)

        except ValueError:
            if j == " ":
                # pass 
                print("Конец ввода") # также оставил вместо pass, понятнее выглядит)
                # print("Index_list = ",index_list)
            else:
                print("Неверный индекс")

    answer = 1
    for i in range(0, len(index_list)):
        # print(number_list[index_list[i]])
        answer *= number_list[index_list[i]]
    print("\n",answer)

index_mult(n)