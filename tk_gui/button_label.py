from tkinter import *
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        root.destroy()


def click():
    print('Hello')


root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Мое приложение')
root.geometry('600x600')
root.resizable(width=False, height=False)
root.iconbitmap('img/free-icon-rocket-1356479.png')
root.config(bg='black')  # root['bg'] = 'RED'

btn = Button(root,
             text='Button',
             command=click,
             font=('Arial', 20, 'bold'),
             width=10, height=5,
             bg='lime',
             activebackground='red',
             activeforeground='yellow',
             fg='brown')
btn.pack()

label = Label(root,
              text='Label',
              font=('Comic Sans MS', 20, 'italic'),
              width=10, height=5,
              bg='lime',
              fg='black')
label.pack()

img = PhotoImage(file='../knb/img/free-icon-rocket-1356479.png')
l_logo = Label(root, image=img)
l_logo.place(x=150, y=200)

root.mainloop()
