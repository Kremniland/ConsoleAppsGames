'''
Движение при нажатии клавиш и отрисовка
'''
from tkinter import *

win_width = 500
win_height = 500
# Размер итема предмета на канвасе
snake_item = 10
# Цвета прорисовки итема змейки внутренний квадрат и внешний
snake_color_1 = 'red'
snake_color_2 = 'yellow'
# Начальные координаты змейки
snake_x = 24
snake_y = 24
# Смещение змеки при нажатии
snake_x_nav = 0
snake_y_nav = 0

root = Tk()
root.title('Zmeyka')
root.resizable(False, False)
root.wm_attributes('-topmost', 1)  # поверх всех окон
canvas = Canvas(root, width=win_width, height=win_height, bd=0, highlightthickness=0)
canvas.pack()
root.update()


def snake_paint_item(canvas, x, y):
    '''прорисовка итема змейки'''
    canvas.create_rectangle(x * snake_item, y * snake_item,
                            x * snake_item + snake_item, y * snake_item + snake_item,
                            fill=snake_color_1)  # окантовка snake_item
    canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2,
                            x * snake_item + snake_item - 2, y * snake_item + snake_item - 2,
                            fill=snake_color_2)  # внутренний квадратик snake_item


def snake_move(event):
    '''движение змейки при нажатии клавиш'''
    print(event)
    global snake_x, snake_y, snake_x_nav, snake_y_nav
    if event.keysym == 'Up':
        snake_x_nav = 0
        snake_y_nav = -1
    elif event.keysym == 'Down':
        snake_x_nav = 0
        snake_y_nav = 1
    elif event.keysym == 'Left':
        snake_x_nav = -1
        snake_y_nav = 0
    elif event.keysym == 'Right':
        snake_x_nav = 1
        snake_y_nav = 0
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)


snake_paint_item(canvas, snake_x, snake_y)

canvas.bind_all('<KeyPress-Left>', snake_move)
canvas.bind_all('<KeyPress-Right>', snake_move)
canvas.bind_all('<KeyPress-Up>', snake_move)
canvas.bind_all('<KeyPress-Down>', snake_move)

root.mainloop()
