#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# ⋀ - and ⋁ - or ¬ - not

a = bool(input("Введите a"))  # Пока не знаю как сделать ввод нескольких переменных одного вида менее громоздким способом
b = bool(input("Введите b"))
c = bool(input("Введите c"))

# if not(a or b or c) == (not a and not b and not c) : 
#     print(True)
# else: 
#     print(False)

print(not(a or b or c) == (not a and not b and not c))