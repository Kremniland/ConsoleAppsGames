from tkinter import *
from googletrans import Translator


def tran():
    text = txt1.get('1.0', END)  # считать из виджета Text: '1.0', END - указать обязательно!
    a = translator.translate(text, dest='en')
    print(a.text)
    txt2.delete('1.0', END)
    txt2.insert('1.0', a.text)


root = Tk()
root.title('Translate')
root.geometry('500x400')
root.resizable(False, False)

translator = Translator()

lb = Label(root, text='Переводчик')
lb.place(relx=0.5, y=10, anchor=CENTER)

txt1 = Text(root, width=35, height=5, font='Arial 12 bold')
txt1.place(relx=0.5, y=80, anchor=CENTER)

btn = Button(root, text='Перевести', command=tran)
btn.place(relx=0.5, y=160, anchor=CENTER)

txt2 = Text(root, width=35, height=5, font='Arial 12 bold')
txt2.place(relx=0.5, y=240, anchor=CENTER)

root.mainloop()
