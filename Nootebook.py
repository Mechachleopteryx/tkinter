# # creating Nootebook on Python tkinter
#
# import tkinter
# from tkinter import ttk
# window = tkinter.Tk()
# window.title('Nootebook')
# nootebook = ttk.Notebook(window)
# page1 = ttk.Frame(nootebook)
# page2 = ttk.Frame(nootebook)
# nootebook.add(page1, text='One')
# nootebook.add(page2, text='Two')
# #  i'm using pack instead of grid
# nootebook.pack(expand=True, fill='both')
#
# label1 = ttk.Label(page1, text='Enter your name : ')
# label1.grid(row=0,column=0)
# entryBox1 = ttk.Entry(page1, width=24)
# entryBox1.grid(row=0,column=1)
#
# label2 = ttk.Label(page2, text='Enter Your Full Name : ')
# label2.grid(row=0, column=0)
#
# entryBox2 = ttk.Entry(page2, width=24)
# entryBox2.grid(row=0,column=1)
#
#
#
#
#
#
#
# window.mainloop()