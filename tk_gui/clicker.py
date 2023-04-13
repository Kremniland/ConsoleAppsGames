from tkinter import *

root = Tk()
root.title('Кликер')
root.geometry('200x200')
root.resizable(False, False)

count = 0


def clicked():
    global count
    count += 1
    click.configure(text=count)


click = Label(root, text='0', font='Aria 35')
click.pack()

btn = Button(root, text='Кликер', padx='20', pady='20', command=clicked)
btn.pack()

root.mainloop()
