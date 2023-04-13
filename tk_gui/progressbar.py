from tkinter import *
from tkinter.ttk import Progressbar
from time import sleep

from base_tk.base import Window


win = Window(400, 500)

pb = Progressbar(win,
                 orient=HORIZONTAL,
                 mode='determinate', # будет заполняться с лева направо
                 length=200) # размер прогресс бара
pb.pack()
# pb.configure(maximum=3) # максимальное значение прогресс бара
# pb.configure(value=1) # заполняется на 20%

pb1 = Progressbar(win,
                 orient=HORIZONTAL,
                 mode='determinate', # будет заполняться с лева направо
                 length=200) # размер прогресс бара
pb1.pack()
# В прогресс баре есть встроенные команды stop и start можно использовать при нажатии кнопок например:
Button(win, text='Старт прогресс бар', command=pb1.start).pack()
Button(win, text='Стоп прогресс бар', command=pb1.stop).pack()

# заполнение прогресс бара в цикле
for i in range(101):
    pb.configure(value=i)
    pb.update() # вызываем обязательно иначе не прорисует
    sleep(0.05)

win.run()
