from tkinter import *

root = Tk()
root.title('Pack')
root.geometry('600x400')
root.resizable(False, False)
root.config(bg='black')

l1 = Label(root, text='1', font='15', bg='yellow', width=8, height=4)
l1.place(x=100, y=100)  # отступы в пикселях

l2 = Label(root, text='2', font='15', bg='brown', padx=15, pady=15)
l2.place(relx=0.7, rely=0.7,  # отступы в %
         anchor=CENTER,
         width=100,  # размер в пикселях
         height=100,  # размер в пикселях
         )
l3 = Label(root, text='3', font='15', bg='blue', width=8, height=4)
l3.place(relwidth=0.5, relheight=0.5)  # размер lable в % относительно окна

root.mainloop()
