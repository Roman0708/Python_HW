# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_str = 'Я люблю Джавуабв абви Питон'

filtered_list = list(filter(lambda word: "абв" not in word, my_str.split(" "))) 

print(filtered_list)