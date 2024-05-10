from tkinter import *

"""Параметры окна"""
root = Tk() #Главноне окно приложения
root.title('Body Mass Index') #Назавание на окоше
root.geometry('640x480') #Размеры окна приложения
root.resizable(width=False, height=False) #Отключаем возможность растягивать оно пилжения

"""Виджеты"""
"""Класс Lable-надписти на окошке"""
label_for_height = Label(
    text= 'Введите Ваш рост (м)',
    font=('Ubuntu', '18')
)
"""Класс Entry-ввод текста"""
entry_for_height = Entry(
    width=10,
    font=('Ubuntu', '30'),
    justify=CENTER
)

"""Класс Lable-надписи на окошке"""
label_for_weigth = Label(
    text= 'Введите Ваш вес (кг)',
    font=('Ubuntu', '18')
)
"""Класс Entry-ввод текста"""
entry_for_weigth = Entry(
    width=10,
    font=('Ubuntu', '30'),
    justify=CENTER
)


"""Создаем функцию высчисления ИМТ"""
def calculate():
    height = float(entry_for_height.get())
    weight = float(entry_for_weigth.get())
    bmi = round(weight / (height ** 2), 2)

    if bmi < 15.99:
        status = 'Выраженный дефицит массы тела.\n Необходимо обратиться к врачу.\n Хватит жевать траву!'
    elif bmi > 16 and bmi < 18.49:
        status = 'Дефицит массы тела.\n Стоит записаться в качалку'
    elif bmi > 18.5 and bmi < 24.99:
        status = 'Норма'
    elif bmi > 25 and bmi < 34.99:
        status = '1 степень ожирения.\n Стоит обратиться к врачу и сдать анализы.\n Но может ты просто на массе...'
    elif bmi > 35 and bmi < 39.99:
        status = '2 степень ожирения.\n Стоит обратиться к врачу и сдать анализы.\n Меньше жри!'
    else:
        status = '3 степень ожирения.\n Стоит обратиться к врачу и сдать анализы.\n Пора тебе перестать посещать холодильник ночью...'

    result_lable = Label(
        text= f'''
        Ваш ИМТ: {bmi} кг/м2
        Это {status}
        ''',
        font=('Ubuntu', '18')
    )
    result_lable.pack()


submit_button = Button(
    text='Рассчитать',
    font=('Ubuntu', '16'),
    command=calculate
)

"""Размещение виджетов"""
label_for_height.pack()
entry_for_height.pack()
label_for_weigth.pack()
entry_for_weigth.pack()
submit_button.pack()

if __name__ == '__main__':
    root.mainloop()

