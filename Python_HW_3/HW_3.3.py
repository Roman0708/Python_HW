# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

# Преобразование сделал строковым во избежание округлений и прочих прелестей языка
def frac_part(number: float):
    helper = str(number)
    h_list = helper.split(".")
    result = "0." + h_list[1]
    return(result)

# def diff_btw_maxmin(num_list):
#     result = 0
#     for i in range(0, len(num_list) - 1):
#         if float(num_list[i]) > result:
#             result = num_list[i]
#     print(result)

def result_list(num_list: list):
    res_list = []
    for i in range(0, len(num_list)):
        j = frac_part(num_list[i])
        res_list.append(float(j))
    return(res_list)

lst1 = result_list([1.1, 1.2, 3.1, 10.01])
answer = (max(lst1) - min(lst1))

print(answer)