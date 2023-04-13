from tkinter import *


class ChildrenWindow:
    def __init__(self, parent, width, height, x=100, y=100, title='MyWindow', resizable=(False, False), icon=None):
        self.parent = parent
        self.parent.withdraw() # скрыть родительское окно
        self.root = Toplevel(self.parent)
        # при закрытии дочернего окна закроется родительское
        self.root.protocol("WM_DELETE_WINDOW", self.parent.destroy)
        # или так
        # self.root.protocol("WM_DELETE_WINDOW", lambda: self.parent.destroy())
        self.root.title(title)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)
        self.grab_focus()

    def grab_focus(self):
        '''захват фокуса и всех действий на дочернее окно'''
        self.root.grab_set()  # перехватывает все события
        self.root.focus_set()  # захватывает фокус
        self.root.wait_window()  # ждет когда будет уничтожен текущий объект не возобновляя работу


class Window(Tk):
    def __init__(self, width, height, x=100, y=100, title='MyWindow', resizable=(False, False), icon=None):
        Tk.__init__(self)
        self.wm_title(title)
        self.wm_geometry(f'{width}x{height}+{x}+{y}')
        self.wm_resizable(resizable[0], resizable[1])
        if icon:
            self.wm_iconbitmap(icon)

    def run(self):
        self.mainloop()

    def delete(self):
        self.destroy()

    def create_child(self, width=200, height=200, x=200, y=200, title='Children Window', resizable=(False, False), icon=None):
        '''создание дочернего окна'''
        ChildrenWindow(self, width, height, x, y, title, resizable, icon)


def child_win():
    second_win = win.create_child()
    Button(second_win, text='Закрой').pack()


if __name__ == '__main__':
    win = Window(width=400, height=500, title='Тест')
    # win.create_child(200, 200)
    label = Label(win,
                  text='Label',
                  font=('Comic Sans MS', 20, 'italic'),
                  width=10, height=5,
                  bg='lime',
                  fg='black')
    label.pack()
    btn = Button(win, text='Закрой', command=child_win)
    btn.pack()
    win.run()
