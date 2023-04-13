import random


class Hero:
    def __init__(self):
        self.exp = 0
        self.hp = 700
        self.max_hp = 1000 + 100 * self.get_level()
        self.mp = 1000 + 100 * self.get_level()
        self.patack = 100 + 10 * self.get_level()
        self.matack = 100 + 10 * self.get_level()
        self.equipment = [] # Список снаряжения

    def p_damage(self):
        '''расчет физ. урона'''
        damage = random.randint(self.patack // 2, self.patack)
        return damage

    def m_damage(self):
        '''расчет маг. урона'''
        damage = random.randint(self.matack // 2, self.matack)
        return damage

    def regen_hp(self):
        '''регенерация здоровья'''
        self.hp = self.max_hp if self.hp >= self.max_hp else self.hp + 10 * (self.get_level() + 1)

    def get_level(self):
        '''уровень персонажа'''
        return self.exp // 1000
