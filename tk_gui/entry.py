from tkinter import *

root = Tk()
root.title('Entry')
root.geometry('600x400')
root.resizable(False, False)
root.config(bg='black')


def add():
    e.insert(END, 'Insert')


def delete():
    e.delete(0, END)


def get():
    label1.configure(text=e.get())  # label1['text'] = e.get()


e = Entry(root,
          # show='*'
          )
e.pack()

e.insert(0, 'Hello')
e.insert(END, ' world!')

btn1 = Button(root, font='Arial 15', text='insert', command=add)
btn1.pack()

btn2 = Button(root, font='Arial 15', text='delete', command=delete)
btn2.pack()

btn3 = Button(root, font='Arial 15', text='get', command=get)
btn3.pack()

label1 = Label(root, bg='black', fg='white', text='')
label1.pack()

root.mainloop()
