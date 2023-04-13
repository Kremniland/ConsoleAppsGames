from tkinter import *
import random


root = Tk()
root.geometry('600x400')
root.title('Камень ножницы бумага')
root.resizable(width=False, height=False)
root.config(bg='black')


def whyknb():
    knb = ['камень', 'ножницы', 'бумага']
    value = random.choice(knb)
    labeltext.config(text=value)


labeltext = Label(root, text='', fg='white', font=('Comic Sans MS', 20, 'italic'), bg='black')
labeltext.place(x=240,y=200)

stone = Button(root,
               text='Камень',
               font=('Comic Sans MS', 20, 'italic'),
               bg='white',
               command=whyknb)
stone.place(x=50, y=300)

scissors = Button(root,
               text='Ножницы',
               font=('Comic Sans MS', 20, 'italic'),
               bg='white',
               command=whyknb)
scissors.place(x=230, y=300)

paper = Button(root,
               text='Бумага',
               font=('Comic Sans MS', 20, 'italic'),
               bg='white',
               command=whyknb)
paper.place(x=450, y=300)

root.mainloop()