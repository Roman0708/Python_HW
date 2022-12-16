# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

from pathlib import Path

# Функции

def get_string_func(file_name: str):
    hw = Path("Python_HW_5",f'{file_name}')
    with open(hw,'r') as result_out:
        input_data = result_out.read()
        return(input_data)

def create_output(file_name: str,text: str):
    output_path = Path("Python_HW_5",f'{file_name}')
    with open(output_path,'w') as result_out:
        result_out.writelines(text+'\nDone')
        return(result_out)

def zip_func(input_data: str):
    input_data += " "
    output_data = []
    counter = 1
    for i in range(1,len(input_data)):
        if input_data[i-1] == input_data[i]:
            counter += 1
        else:
            if counter < 2:
                output_data.append(input_data[i-1])
            else:
                output_data.append(f'{input_data[i-1]}{counter}')
            counter = 1
    result = ""
    for i in range(0,len(output_data)):
        result += str(output_data[i])
    return(result)

def unzip_func(input_data):
    result = ''
    counter = ''
    for i in range(0,len(input_data)):
        if (input_data[i]).isdigit():
            counter += input_data[i]
        else:
            if counter == '':
                counter = 1
            result += input_data[i] * int(counter)
            counter = ''
    return(result)

# Логика

file_name = str(input("Введите название файла для сжатия с расширением: "))                  # Поиск файла с данными для сжатия
initial_string = get_string_func(file_name)                                                           # Получения строки из начального файла
zipped_string = zip_func(initial_string)                                                     # Сжатие данных

create_output(file_name+"-zipped",zipped_string)                                             # Создание файла со сжатыми данными

unzipped_string = unzip_func(zipped_string)                                                  # Декомпрессия файла
create_output(file_name+"unzipped",unzipped_string)                                          # Создание файла с декомпрессированными данными

