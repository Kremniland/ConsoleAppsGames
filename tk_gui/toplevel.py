from tkinter import *

root = Tk()
root.title('Toplevel')
root.geometry('500x500')


def open_win():
    win = Toplevel()
    win.geometry('200x200+100+100')
    win.grab_set() # не даст закрыть родительское окно пока открыто дочернее
    lb = Label(win, text='Toplevel', font='Aria 15 bold')
    lb.pack()
    # win.overrideredirect(True) # откроет окно без рамок
    win.after(3000, lambda: win.destroy()) # автоматически закроется через 3 сек


btn = Button(root, text='Открыть', padx=40, pady=5, command=open_win)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
