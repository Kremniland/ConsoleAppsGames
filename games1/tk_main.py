import random
from tkinter import *
from tkinter import ttk
from loguru import logger

from hero import Hero
from action import action_goblin_tk

hero = Hero()


class GameWindow(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('My Game')
        # self.geometry('300x300')
        self['bg'] = 'green'
        self.pad_conf = {'padx': (30, 30), 'pady': 10}
        self.font_conf = ('Arial', 12, 'bold')
        self.put_frames()

    def put_frames(self):
        self.hero_info = HeroInfo(self)
        self.hero_info.grid(row=0, column=0, sticky='nswe')

        self.action_info = ActionInfo(self)
        self.action_info.grid(row=1, column=0, sticky='nswe')


class HeroInfo(Frame):
    def __init__(self, parent):
        super().__init__(parent, width=350, height=150)

        # self['bg'] = self.master['bg']
        self.put_widgets()

    def put_widgets(self):
        global hero
        self.hero_level_text = ttk.Label(self, text=f'Ваш уровень:', font=self.master.font_conf)
        self.hero_level_value = ttk.Label(self, text=hero.get_level(), font=self.master.font_conf)
        self.hero_exp_text = ttk.Label(self, text=f'Ваше exp:', font=self.master.font_conf)
        self.hero_exp_value = ttk.Label(self, text=hero.exp, font=self.master.font_conf)
        self.hero_hp_text = ttk.Label(self, text=f'Ваше здоровье:', font=self.master.font_conf)
        self.hero_hp_value = ttk.Label(self, text=hero.hp, font=self.master.font_conf)
        self.hero_patack_text = ttk.Label(self, text=f'Ваша физ. атака:', font=self.master.font_conf)
        self.hero_patack_value = ttk.Label(self, text=hero.patack, font=self.master.font_conf)

        self.hero_level_text.grid(row=0, column=0, sticky='w', cnf=self.master.pad_conf)
        self.hero_level_value.grid(row=0, column=1, sticky='e', cnf=self.master.pad_conf)
        self.hero_exp_text.grid(row=1, column=0, sticky='w', cnf=self.master.pad_conf)
        self.hero_exp_value.grid(row=1, column=1, sticky='e', cnf=self.master.pad_conf)
        self.hero_hp_text.grid(row=2, column=0, sticky='w', cnf=self.master.pad_conf)
        self.hero_hp_value.grid(row=2, column=1, sticky='e', cnf=self.master.pad_conf)
        self.hero_patack_text.grid(row=3, column=0, sticky='w', cnf=self.master.pad_conf)
        self.hero_patack_value.grid(row=3, column=1, sticky='e', cnf=self.master.pad_conf)


class ActionInfo(Frame):
    def __init__(self, parent):
        super().__init__(parent, width=300, height=150)

        self['bg'] = 'red'
        self.view = parent
        self.get_action()

    def get_action(self):
        action_list = ['goblin', 'empty']
        action = random.choice(action_list)
        match action:
            case 'goblin':
                self.widgets_goblin()
            case 'empty':
                self.widgets_empty()

    def widgets_goblin(self):
        self.label_goblin = Label(self, text='Вы встретили гоблина!', bg='red', font=self.master.font_conf)
        self.label_goblin.place(relx=0.2, rely=0.2)
        self.btn_atack = ttk.Button(self, text='Атакуем?', command=self.open_batle_win)
        self.btn_atack.place(relx=0.1, rely=0.8)
        self.btn_run = ttk.Button(self, text='Убегаем?', command=self.view.put_frames)
        self.btn_run.place(relx=0.7, rely=0.8)

    def open_batle_win(self):
        BatleWin()

    def widgets_empty(self):
        hero.regen_hp()
        self.btn_game = ttk.Button(self, text='Продолжить игру?', command=self.view.put_frames)
        self.btn_game.place(relx=0.1, rely=0.8)
        self.btn_stop_game = ttk.Button(self, text='Выйти из игры?', command=self.view.destroy)
        self.btn_stop_game.place(relx=0.6, rely=0.8)

class BatleWin(Toplevel):
    def __init__(self):
        super().__init__(win)
        self.init_batle_win()

    def init_batle_win(self):
        self.title('Битва!')
        self.batle_list = action_goblin_tk(hero)
        for info in self.batle_list:
            Label(self, text=info, font=win.font_conf).pack()
        self.btn_stop_game = ttk.Button(self, text='Закрыть?', command=self.close)
        self.btn_stop_game.pack()
        self.grab_set()
        self.focus_set()

    def close(self):
        if self.batle_list[-1] == 'Вы погибли!':
            win.destroy()
        elif self.batle_list[-1] == 'Победа!':
            win.put_frames()
            self.destroy()

if __name__ == '__main__':
    win = GameWindow()
    win.mainloop()
