'''
Создано основное окно с таблицей, открытие дочернего окна с вводом данных
Создаем класс для работы с базой: создание базы, запись в базу данных из дочернего окна
Добавляем метод фрейма главного окна для записи в базу данных из дочернего окна,
обновляет сразу данные в таблице фрейма главного окна не закрывая дочернего
изменение записи в БД
'''
import tkinter as tk
from tkinter import ttk
import sqlite3
from loguru import logger


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db  # присваиваем объект класса DB созданный
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        btn_open_dialog = tk.Button(toolbar, text='Добавить позицию',
                                    command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='add.gif')
        btn_edit_dialog = tk.Button(toolbar, text='Редактировать',
                                     command=self.open_update_dialog,
                                     bg='#d7d8e0', bd=0, image=self.update_img,
                                     compound=tk.TOP) # отобразит название кнопки под иконкой
        btn_edit_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('ID', 'description', 'costs', 'total'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='Наименование')
        self.tree.heading('costs', text='Статья дохода\расхода')
        self.tree.heading('total', text='Сумма')

        self.tree.pack()

    def records(self, description, costs, total):
        '''записываем данные в db и обновляем их вывод'''
        self.db.insert_data(description, costs, total)
        self.view_records()

    def update_record(self, description, costs, total):
        self.db.c.execute('''UPDATE finance SET description=?, costs=?, total=? WHERE ID=?''', # знак ? ставим там где хотим использовать
                                    # значения, WHERE ID=? указываем ID которой записи изменить
                          (description, costs, total, self.tree.set(self.tree.selection()[0], '#1'))) # self.tree.set(self.tree.selection()[0], '#1') -
                                    # возвратит строку и из строки выберет 1 столбец, т.е. ID
        logger.info(self.tree.set(self.tree.selection()[0], '#1'))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        '''заполняем таблицу с данными'''
        self.db.c.execute('''SELECT * FROM finance''')
        # Очищаем данные из таблицы
        [self.tree.delete(i) for i in self.tree.get_children()]
        # Добавляем данные в таблицу
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()

        self.view = app  # присваиваем объект app - фрейм главного окна

    def init_child(self):
        self.title('Добавить доходы\расходы')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Наименование:')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Статья дохода\расхода:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Сумма:')
        label_sum.place(x=50, y=110)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=170)
        # при нажатии левой кнопки мыши на кнопку вызывается ф-ия фрейма главного окна
        # для записи данных из полей в базу данных
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                        self.combobox.get(),
                                                                        self.entry_money.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Редактирование записи')
        btn_edit = ttk.Button(self, text='Редактировать')
        btn_edit.place(x=205, y=170)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.entry_money.get(),
                                                                          self.entry_money.get()))
        self.btn_ok.destroy()


class DB:
    def __init__(self):
        '''если база не создана то создаем или открываем для работы с ней'''
        self.conn = sqlite3.connect('finance.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS finance (id integer primary key, description text, costs text, total real)''')
        self.conn.commit()

    def insert_data(self, description, costs, total):
        '''заносим данные в базу'''
        self.c.execute('''INSERT INTO finance(description, costs, total) VALUES (?, ?, ?)''',
                       (description, costs, total))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()

    db = DB()

    app = Main(root)
    app.pack()

    root.title("Household finance")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
