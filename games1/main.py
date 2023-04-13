import random
import os
from tkinter import *
from colorama import init, Fore, Back, Style

from hero import Hero
from action import get_action
from base_tk.base import Window

init()  # для работы colorama


def clear():
    '''очистка консоли,  включить эмуляцию терминала в консоли вывода
    (делается это в Run|Edit Configurations)'''
    os.system('cls||clear')


def main():
    hero = Hero()
    end = 'д'
    win = Window(300, 300)

    while end not in 'Нн':
        print('Ваше уровень ', hero.get_level())
        print('Ваше exp ', hero.exp)
        text_color = Fore.RED if hero.hp < hero.max_hp * 0.4 else Style.RESET_ALL
        print(text_color + 'Ваше здоровье ', hero.hp, Style.RESET_ALL)
        # print('Ваша мана ', hero.mp)
        print('Ваше физ. атака ', hero.patack)
        # print('Ваше маг. атака ', hero.matack)
        action = get_action(hero)
        if action == 0:
            print('Вы проиграли!')
            break
        end = input('Продолжаем игру? (д/н) ')
        clear()


if __name__ == '__main__':
    main()

    # print(Fore.RED + 'зеленый текст')
    # print(Back.YELLOW + 'на желтом фоне')
    # print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
    # print('обычный текст')
