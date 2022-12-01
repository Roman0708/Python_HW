# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число: "))
  
def factorial (number: int):
    fctrl = 1
    for i in range(2, number + 2):
        print(fctrl, end=", ")
        fctrl = fctrl*i


        

   
    # if number == 1:
    #     return number
    # else:
    #     return number*factorial(number-1)

factorial(n)