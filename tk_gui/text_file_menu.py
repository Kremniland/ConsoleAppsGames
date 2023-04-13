from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()


def open_file():
    # В file_path будет путь и имя файла который надо открыть
    file_path = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert(END, f'Надо открыть файл: {file_path}\n Содержимое файла:\n')
        text_fild.insert(END, open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    f.write(text)
    f.close()


def change_theme(theme):
    text_fild['bg'] = view_colors[theme]['text_bg']
    text_fild['fg'] = view_colors[theme]['text_fg']
    text_fild['insertbackground'] = view_colors[theme]['cursor']
    text_fild['selectbackground'] = view_colors[theme]['select_bg']


def change_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']


root = Tk()
root.title('Текстовый редактор')
root.geometry('600x700')

# Menu ======================================
main_menu = Menu(root)

# Файл
file_menu = Menu(main_menu,
                 tearoff=0  # уберем пунктирную линию при нажатии на
                 # которую открывает меню в отдельном окне
                 )
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()  # нарисуем линию отделяющую кнопку Закрыть
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

# Вид - с подменю
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)

view_menu_sub.add_command(label='Темная', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)

font_menu_sub.add_command(label='Aria', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_fonts('CSMS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('TNR'))
view_menu.add_cascade(label='Шрифт', menu=font_menu_sub)

root.config(menu=view_menu)

# Добавление списков меню
main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)
root.config(menu=main_menu)
# =========================================

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

# словари для смены темы и шрифтов ======================================================
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
    }
}

fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'CSMS': {
        'font': ('Comic Sans MS', 14, 'bold')
    },
    'TNR': {
        'font': ('Times New Roman', 14, 'bold')
    }
}
# ==========================================================================
text_fild = Text(f_text, bg='black', fg='lime', padx=10, pady=10,
                 wrap=WORD,  # перенос текста на новую строку по окончании слова
                 insertbackground='brown',  # цвет курсора
                 selectbackground='#8D917A',  # цвет выделяемого текста
                 spacing3=10,  # делает отступ между абзацами
                 width=30,  # ширина в символах
                 font='Arial 14 bold')
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

# добавляем скролл бар
scroll = Scrollbar(f_text, command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

root.mainloop()
