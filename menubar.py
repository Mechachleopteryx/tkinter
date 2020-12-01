import tkinter
from tkinter import ttk
window = tkinter.Tk()
window.title('Menu Bar')

def func():
    print('function called')

menu_bar = tkinter.Menu(window)

file_menu = tkinter.Menu(menu_bar)
file_menu.add_command(label='New File', command=func)
file_menu.add_command(label='Open File', command=func)

menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = tkinter.Menu(menu_bar)
edit_menu.add_command(label='Undo', command=func)
edit_menu.add_command(label='Redo', command=func)

menu_bar.add_cascade(label='Edit', menu=menu_bar)




window.config(menu=menu_bar)
window.mainloop()
