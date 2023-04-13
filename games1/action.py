import random
from colorama import init, Style, Fore, Back

from enemy import Goblin
from hero import Hero

init()


def get_action(hero: Hero):
    '''определение рандомного события'''
    action_list = ['goblin', 'empty']
    action = random.choice(action_list)
    match action:
        case 'goblin':
            a = action_goblin(hero)
        case 'empty':
            hero.regen_hp()
            a = 3
    return a


def action_goblin(hero: Hero):
    '''бой с гоблином'''
    goblin = Goblin()
    exp = goblin.hp
    move = input('1 - атакуем, 2 - убегаем? ')
    if move == '1':
        while True:
            hero_damage = hero.p_damage()
            goblin_damage = goblin.damage()
            print(Fore.RED + f'Вы наносите гоблину {hero_damage} урона')
            goblin.hp -= hero_damage
            if goblin.hp <= 0:
                print('Победа!' + Style.RESET_ALL)
                hero.exp += exp
                return 1
            else:
                print(Fore.RED + f'Гоблин наносит вам {goblin_damage} урона')
                hero.hp -= goblin_damage
                if hero.hp <= 0:
                    print('Вы погибли!' + Style.RESET_ALL)
                    return 0
            hero.regen_hp()
    elif move == '2':
        print('Вы убежали!')
        hero.regen_hp()
        return 2

def action_goblin_tk(hero: Hero):
    '''бой с гоблином'''
    goblin = Goblin()
    exp = goblin.hp
    batle_info = []
    while True:
        hero_damage = hero.p_damage()
        goblin_damage = goblin.damage()

        batle_info.append(f'Вы наносите гоблину {hero_damage} урона')
        print(f'Вы наносите гоблину {hero_damage} урона')
        goblin.hp -= hero_damage
        if goblin.hp <= 0:
            batle_info.append('Победа!')
            print('Победа!')
            hero.exp += exp
            return batle_info
        else:
            batle_info.append(f'Гоблин наносит вам {goblin_damage} урона')
            print(f'Гоблин наносит вам {goblin_damage} урона')
            hero.hp -= goblin_damage
            if hero.hp <= 0:
                batle_info.append('Вы погибли!')
                print('Вы погибли!')
                return batle_info
        hero.regen_hp()


if __name__ == '__main__':
    pass
