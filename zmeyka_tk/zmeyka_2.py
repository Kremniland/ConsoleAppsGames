'''
Движение при нажатии клавиш и отрисовка
стирание хвоста змеи если длинна превышает размер змеи
'''
from tkinter import *
import random

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
# Список с элементами нашей змейки
snake_list = []
# Размер змейки
snake_size = 3

root = Tk()
root.title('Zmeyka')
root.resizable(False, False)
root.wm_attributes('-topmost', 1)  # поверх всех окон
canvas = Canvas(root, width=win_width, height=win_height, bd=0, highlightthickness=0)
canvas.pack()
root.update()


def snake_paint_item(canvas, x, y):
    '''прорисовка итема змейки итем состоит из 2 квадратов'''
    global snake_list
    # присваиваем элементам змеи id для того чтобы удалить их из списка когда размер
    # списка больше длинны змеи
    id1 = canvas.create_rectangle(x * snake_item, y * snake_item,
                            x * snake_item + snake_item, y * snake_item + snake_item,
                            fill=snake_color_1)  # окантовка snake_item
    id2 = canvas.create_rectangle(x * snake_item + 2, y * snake_item + 2,
                            x * snake_item + snake_item - 2, y * snake_item + snake_item - 2,
                            fill=snake_color_2)  # внутренний квадратик snake_item
    # сохраняем в список с итемами змеи координаты итема и его id1 id2
    snake_list.append([x, y, id1, id2])
    print(snake_list)


def check_can_we_delete_snake_item():
    '''проверяем можемли мы удалить итем змеи'''
    if len(snake_list) >= snake_size:
        # удаляем первый элемент в списке итемов змеи и помещаем его во временную переменную
        temp_item = snake_list.pop(0)
        print(temp_item)
        # стираем элемент с экрана по id1 id2 - т к итем состоит из 2 квадратов
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])


def snake_move(event):
    '''движение змейки при нажатии клавиш'''
    print(event)
    global snake_x, snake_y, snake_x_nav, snake_y_nav
    if event.keysym == 'Up':
        snake_x_nav = 0
        snake_y_nav = -1
        check_can_we_delete_snake_item()
    elif event.keysym == 'Down':
        snake_x_nav = 0
        snake_y_nav = 1
        check_can_we_delete_snake_item()
    elif event.keysym == 'Left':
        snake_x_nav = -1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    elif event.keysym == 'Right':
        snake_x_nav = 1
        snake_y_nav = 0
        check_can_we_delete_snake_item()
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    snake_paint_item(canvas, snake_x, snake_y)


snake_paint_item(canvas, snake_x, snake_y)

canvas.bind_all('<KeyPress-Left>', snake_move)
canvas.bind_all('<KeyPress-Right>', snake_move)
canvas.bind_all('<KeyPress-Up>', snake_move)
canvas.bind_all('<KeyPress-Down>', snake_move)

root.mainloop()
