import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Main Menu')

def func():
    print('function called ')
menubar = tkinter.Menu(window)
menubar.add_command(label='Save', command=func)
menubar.add_command(label='Copy', command=func)
menubar.add_command(label='Save', command=func)





window.config(menu=menubar)
window.mainloop()
