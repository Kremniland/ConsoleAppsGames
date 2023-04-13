from tkinter import *

win = Tk()
win.title('Grid Place')
# win.geometry('300x300')
# win.minsize(200, 200) # минимальный размер
# win.maxsize(500, 400) # максимальный размер
# win.resizable(False, False)

frame_1 = Frame(win, width=150, height=150, bg='yellow')
frame_2 = Frame(win, width=150, height=150, bg='green')
frame_3 = Frame(win, width=300, height=150, bg='blue')

# вывод фреймов методом grid
# frame_1.grid(row=0, column=0,
#              sticky='ns') # прилепание к указанной границе
# frame_2.grid(row=0, column=1)
# frame_3.grid(row=1, column=0, columnspan=2, sticky='we')

# вывод методоми place через указание x, y
# frame_1.place(x=0, y=0)
# frame_2.place(x=150, y=0)
# frame_3.place(x=0, y=150)

# вывод методоми place через указание relx, rely
# frame_1.place(relx=0, rely=0)
# frame_2.place(relx=0.5, rely=0)
# frame_3.place(relx=0, rely=0.5)

# при растяжении окна фраймы будут примыкать к краям окна relheight, relwidth
frame_1.place(relx=0, rely=0, relheight=0.5, relwidth=0.5)
frame_2.place(relx=0.5, rely=0, relheight=0.5, relwidth=0.5)
frame_3.place(relx=0, rely=0.5, relheight=0.5, relwidth=1)

# также можно использовать anchor в методе place


win.mainloop()
