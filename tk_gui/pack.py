from tkinter import *

root = Tk()
root.title('Pack')
root.geometry('600x400')
root.resizable(False, False)
root.config(bg='black')

l1 = Label(root, text='1', font='15', bg='yellow', width=8, height=4).pack(side=LEFT)
l2 = Label(root, text='2', font='15', bg='brown', width=8, height=4).pack(side='left')
l3 = Label(root, text='3', font='15', bg='blue', width=8, height=4).pack(side=TOP)
l4 = Label(root, text='4', font='15', bg='pink', width=8, height=4).pack(side=BOTTOM)
l5 = Label(root, text='5', font='15', bg='pink', width=8, height=4)
l5.pack(side=LEFT, # RIGHT, TOP, BOTTOM, LEFT
        expand=1,  # 1 - в середине отведенного пространства, 0 - верх
        fill=X,  # растянуть X, Y, BOTH
        anchor=S  # SE, W, N, , E, S, NW, NE, SW - сместит в стороны света
        )

root.mainloop()
