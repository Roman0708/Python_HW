# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

import random
from pathlib import Path
import time

home = Path.home()

# print(home)
# print(hw)



k = int(input("Введите степень k: "))

result = []
answer = str()
for i in range(0, k + 1):
    result.append(random.randint(0,100))
    if result[i] == 0:
        pass
    elif i - k == 0:
        answer = answer + str(f"{random.randint(0,100)} + ")
    else:
        answer = answer + str(f"{random.randint(0,100)}*x(**{k - i}) + ")
answer = answer[:-2] + "= 0"
# print(answer)

now = time.strftime('%Y%m%d%H%M%S')

# file_name = str(f'"Python_HW_4","HW_4.4_output_{now}.md"')
# print(file_name)

hw = Path("Python_HW_4",f"HW_4.4_output_{now}.md")
# print(now)

with open(hw,'w') as result_out:
    result_out.write(answer)
