# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import tkinter

window = tkinter.Tk()

# Блок функций

def answer_check():
    
    try: 
        answer = int(enter_field.get())
    except ValueError:
        label_prompt_answer['text'] = str("Неправильный формат числа")
        label_prompt_answer.pack(fill='x',padx=20)       
    else:
        answer_figure = int(answer)
        if answer_figure == 20:
            label_prompt_answer['text'] = str("Верно")
            label_prompt_answer['fg'] = str("green")
            label_prompt_answer.pack(fill='x')
        else:
            label_prompt_answer['text'] = str("Неверно")
            label_prompt_answer['fg'] = str("red")
            label_prompt_answer.pack(fill='x')  
    enter_field.delete(0,"end")
    print(label_prompt_answer['text'])

# Главный экран

window.config(bg='#262424')
window.title("Задача про конфеты")
window.geometry("300x400+100+100")
window.resizable(False,False)

label_conditions = tkinter.Label(window,text='''На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28
конфет. Все конфеты оппонента достаются 
сделавшему последний ход.''',
bg='#262424',fg='white',font=('Arial',9,'bold'), anchor='w',
padx=10,pady=10)
label_conditions.pack(fill='x',padx=10,pady=10)

enter_field = tkinter.Entry()
enter_field.pack(padx=10,pady=10)

answer_button = tkinter.Button(text="Проверить",command=answer_check)
answer_button.pack(padx=10,pady=10)

label_prompt_answer = tkinter.Label(font=('Arial',10,'bold'),relief=tkinter.RAISED)

window.mainloop()


