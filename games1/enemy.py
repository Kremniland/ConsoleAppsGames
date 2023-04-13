import random


class Goblin:
    def __init__(self):
        self.level = random.randint(1,10)
        self.hp = random.randint(100,300)
        self.patack = random.randint(100,300)

    def damage(self):
        '''расчет урона'''
        damage = random.randint(self.patack // 2, self.patack)
        return damage
