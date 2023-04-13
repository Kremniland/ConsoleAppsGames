'''
Движение при нажатии клавиш и отрисовка
стирание хвоста змеи если длинна превышает размер змеи
создаем список с предметами на экране в рандомном месте, отрисоввываем
их и сохраняем в список id предметов и их координаты
добавляем ф-ию: змея съедает предмет
запускаем цикл для непрерывного движения змеи
проверка касания границ и самой себя
'''
from tkinter import *
import random
from loguru import logger
from time import sleep

# размеры игрового поля
win_width = 500
win_height = 500
# Размер итема предмета на канвасе
snake_item = 10
# колличество ячеек на экране игровом
virtual_game_x = win_width // snake_item
virtual_game_y = win_height // snake_item
# Цвета прорисовки итема змейки внутренний квадрат и внешний
snake_color_1 = 'red'
snake_color_2 = 'yellow'
# Начальные координаты змейки
snake_x = virtual_game_x // 2
snake_y = virtual_game_y // 2
# Смещение змеки при нажатии
snake_x_nav = 0
snake_y_nav = 0
# Список с элементами нашей змейки
snake_list = []
# Размер змейки
snake_size = 3
# Список предметов на экране
presents_list = []
# Кол-во предметов на экране
presents_size = 50
# цвета предметов
present_color1 = 'blue'
present_color2 = 'black'

Game_Running = True

root = Tk()
root.title('Zmeyka')
root.resizable(False, False)
root.wm_attributes('-topmost', 1)  # поверх всех окон
canvas = Canvas(root, width=win_width, height=win_height, bd=0, highlightthickness=0)
canvas.pack()
root.update()

for i in range(presents_size):
    # сохраняем рандомные координаты и id предметов в список предметов и отрисуем их
    x = random.randrange(virtual_game_x)
    y = random.randrange(virtual_game_y)
    id1 = canvas.create_oval(x * snake_item, y * snake_item,
                             x * snake_item + snake_item, y * snake_item + snake_item,
                             fill=snake_color_1)  # внешний овал
    id2 = canvas.create_oval(x * snake_item + 2, y * snake_item + 2,
                             x * snake_item + snake_item - 2, y * snake_item + snake_item - 2,
                             fill=snake_color_2)  # внутренний овал
    presents_list.append([x, y, id1, id2])

print(presents_list)


def snake_paint_item(canvas, x, y):
    '''прорисовка итема змейки'''
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


def check_can_we_delete_snake_item():
    '''проверяем можемли мы удалить итем змеи'''
    if len(snake_list) >= snake_size:
        # удаляем первый элемент в списке итемов змеи и помещаем его во временную переменную
        temp_item = snake_list.pop(0)
        # print(temp_item)
        # стираем элемент с экрана по id1 id2 - т к итем состоит из 2 квадратов
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])


def check_if_we_found_present():
    '''проверяем присутствуют ли координаты змеи в списке с координатами предметов'''
    global snake_size
    # проходим по списку с предметами и если x y предметов совпадают c snake_x snake_y
    # увеличиваем размер змеи и удаляем предмет
    for i in range(len(presents_list)):
        if presents_list[i][0] == snake_x and presents_list[i][1] == snake_y:
            # logger.info('Съел!')
            snake_size = snake_size + 1
            canvas.delete(presents_list[i][2])
            canvas.delete(presents_list[i][3])
            presents_list.pop(i)
            return
    logger.info(f'x = {snake_x}, y = {snake_y}')


def snake_move(event):
    '''движение змейки при нажатии клавиш'''
    # print(event)
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
    check_if_we_found_present()
    snake_paint_item(canvas, snake_x, snake_y)


snake_paint_item(canvas, snake_x, snake_y)

canvas.bind_all('<KeyPress-Left>', snake_move)
canvas.bind_all('<KeyPress-Right>', snake_move)
canvas.bind_all('<KeyPress-Up>', snake_move)
canvas.bind_all('<KeyPress-Down>', snake_move)


def game_over():
    global Game_Running
    Game_Running = False


def check_if_borders():
    '''проверка касания границ экрана'''
    global virtual_game_y, virtual_game_x, snake_y, snake_x
    if snake_x > virtual_game_x or snake_x < 0 or snake_y > virtual_game_y or snake_y < 0:
        game_over()


def check_we_touch_self(f_x, f_y):
    '''касание самой себя f_x, f_y - координаты следующего положения головы змеи'''
    global Game_Running
    if not (snake_x_nav == 0 and snake_y_nav == 0):  # если змея движется, а не стоит на месте
        for i in range(len(snake_list)):  # проходим по массиву с элементами змеи
            if snake_list[i][0] == f_x and snake_list[i][1] == f_y:
                print("found!!!")
                Game_Running = False


# запускаем цикл для движения змейки без нажатия на клавишу
while Game_Running:
    check_can_we_delete_snake_item()
    check_if_we_found_present()
    # для проверки касания себя отправляем координаты следующего положения головы змеи
    check_we_touch_self(snake_x + snake_x_nav, snake_y + snake_y_nav)
    snake_x = snake_x + snake_x_nav
    snake_y = snake_y + snake_y_nav
    check_if_borders()
    snake_paint_item(canvas, snake_x, snake_y)
    root.update_idletasks()
    root.update()
    sleep(0.1)


# Далее код для того чтобы при конце игры окно не закрывалось,
# просто привязываем события к пустой ф-ии
def fun_nothing(event):
    pass


canvas.bind_all("<KeyPress-Left>", fun_nothing)
canvas.bind_all("<KeyPress-Right>", fun_nothing)
canvas.bind_all("<KeyPress-Up>", fun_nothing)
canvas.bind_all("<KeyPress-Down>", fun_nothing)
root.mainloop()
# =================================================================
