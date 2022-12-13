# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint
import tkinter

window = tkinter.Tk()

window.config(bg='#4d4d4d')
window.title("Игра в конфеты с ботом")
window.geometry("350x400+100+100")
window.resizable(False,False)

player_score = 0
bot_score = 0
candy_left = 20
flag = True
x = 28
# функции

def bot_turn():
    global bot_score
    global candy_left
    global flag
    global x
    if candy_left < 28: x = candy_left
    result = randint(1,x+1)
    bot_score += result
    candy_left -= result
    bot_score_widget['text'] = str(f'Конфеты противника:\n{bot_score}')
    candy_left_widget['text'] = str(f'Осталось конфет:\n{candy_left}')
    prompt_label['text'] = str(f'Противник взял {result} конфет')
    flag=False
    check_game_over

def get_candy():
    global candy_left
    global x
    if candy_left < 28: x = candy_left
    try: 
        result = int(candy_entry.get())
    except ValueError:
        candy_entry.delete(0,"end")
        prompt_label['text'] = str("Неправильный формат числа")
    else:
        if result in range (1,x+1):
            candy_entry.delete(0,"end")
            answer_figure = int(result)
            global player_score
            global player_score_widget
            global flag
            player_score += answer_figure
            candy_left -= answer_figure
            candy_left_widget['text'] = str(f'Осталось конфет:\n{candy_left}')
            player_score_widget['text'] = str(f'Ваши конфеты:\n{player_score}')
            prompt_label['text'] = str(f'Вы взяли {answer_figure} конфет')
            flag = True
            check_game_over
            window.after(1500,bot_turn)
        else:
            candy_entry.delete(0,"end")
            prompt_label['text'] = str(f"Введите число от 1 до {x}")

def check_game_over():
    global candy_left
    if candy_left <= 0:
        window.destroy()
        game_over = tkinter.Tk()
        game_over.config(bg='#4d4d4d')
        game_over.title("Конец игры")
        game_over.geometry("200x150+200+200")
        game_over.resizable(False,False)
        if flag is True: result = "Игрок"
        else: result = "Бот"
        over_label = tkinter.Label(text=f'{result} победил')
        over_label.pack()
        game_over.mainloop()


# Виджеты

player_score_widget = tkinter.Label(window,text=f'Ваши конфеты:\n{player_score}',
                                    bg='green',font=('Arial',10,'bold'),
                                    relief=tkinter.RAISED,width=17)                                

bot_score_widget = tkinter.Label(window,text=f'Конфеты противника:\n{bot_score}',
                                    bg='red',font=('Arial',10,'bold'),
                                    relief=tkinter.RAISED,width=17)

candy_left_widget = tkinter.Label(window,text=f'Осталось конфет:\n{candy_left}',
                                    bg='white',font=('Arial',12,'bold'),
                                    relief=tkinter.RAISED,width=35)

invite_label = tkinter.Label(window,text='''Введите количество конфет, забираемых из кучи:''')                                   

candy_entry = tkinter.Entry(window)

entry_button = tkinter.Button(text='Ввести',command=get_candy)

prompt_label = tkinter.Label(text=f'Введите число от 1 до {x-1}')

# Первичная инициализация
candy_left_widget.grid(row=0,column=0,columnspan=2,sticky='we')
player_score_widget.grid(row=1,column=0,sticky='we')
bot_score_widget.grid(row=1,column=1,sticky='we')
invite_label.grid(row=2,column=0,columnspan=2,sticky='we')
candy_entry.grid(row=3,column=0,columnspan=2,sticky='we')
entry_button.grid(row=4,column=0,sticky='we')
prompt_label.grid(row=4,column=1,sticky='we')

window.mainloop()