from tkinter import *
import time
import random

tk = Tk()
tk.title('Арканоид')
tk.resizable(False, False)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=500, height=400,
                bd=0, highlightthickness=0  # чтобы не было рамок вокруг холста
                )
canvas.pack()
tk.update()


class Board:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.board_width = 150
        self.id = canvas.create_rectangle(0, 0, self.board_width, 15, fill=color)
        self.canvas_height = self.canvas.winfo_height()  # высота нашего холста
        self.canvas_width = self.canvas.winfo_width()  # ширина нашего холста
        self.x = 0
        self.speed_x = 5
        # координаты верхнего левого угла доски
        self.xx = self.canvas_width / 2 - self.board_width / 2
        self.yy = self.canvas_height - 40
        self.canvas.move(self.id, self.xx, self.yy)  # перемещаем доску в наши координаты

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

    def move_left(self, event):
        if self.xx + (-1) * self.speed_x >= 0:
            self.x = (-1) * self.speed_x
            self.xx = self.xx + self.x
            self.draw()

    def move_right(self, event):
        if self.xx + self.speed_x <= self.canvas_width - self.board_width:
            self.x = self.speed_x
            self.xx = self.xx + self.x
            self.draw()


class Ball:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(5, 5, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 200)
        start = [-3, -2, -1, 1, 2, 3]  # список рандомных скоростей
        random.shuffle(start)  # перемешиваем список скоростей
        self.x = start[0]
        self.y = start[1]
        self.canvas_height = self.canvas.winfo_height()  # высота нашего холста
        self.canvas_width = self.canvas.winfo_width()  # ширина нашего холста

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)  # считываем координаты объекта
        # print(pos)
        # print(pos[0], pos[1],  # верхний левый угол фигуры
        #       pos[2], pos[3])  # нижний правый угол фигуры
        if pos[1] <= 0:
            # self.y = 1
            self.y = self.y * (-1)  # меняем направление и сохраняем скорость
        if pos[3] >= self.canvas_height:
            # self.y = -1
            self.y = self.y * (-1)  # меняем направление и сохраняем скорость

        if pos[0] <= 0:
            # self.x = 1
            self.x = self.x * (-1)  # меняем направление и сохраняем скорость
        if pos[2] >= self.canvas_width:
            # self.x = -1
            self.x = self.x * (-1)  # меняем направление и сохраняем скорость


ball = Ball(canvas, 'red')
board = Board(canvas, 'blue')
canvas.bind_all("<KeyPress-Left>", board.move_left)
canvas.bind_all("<KeyPress-Right>", board.move_right)
# canvas.bind_all("<KeyPress-Up>", board.move_up)
# canvas.bind_all("<KeyPress-Down>", board.move_down)

while True:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)

# tk.mainloop()
