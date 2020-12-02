# we are creating messageboxes Error, Warning, info.
import tkinter
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.title('message Box in tkinter')

frame_label = ttk.LabelFrame(window, text='Input Your Information')
frame_label.grid(row=0,column=0)

name_label=ttk.Label(frame_label, text='Enter Your Name : ', font=('helvatica',14,'bold'))
name_label.grid(row=0,column=0,padx=30,pady=10, sticky=tkinter.W)
name_var= tkinter.StringVar()
entry_name=ttk.Entry(frame_label, width=20, textvariable=name_var)
entry_name.grid(row=1,column=0,padx=30,sticky=tkinter.W)


age_label = ttk.Label(frame_label, text='Enter Your Age : ',font=('halvatica',14,'bold'))
age_label.grid(row=0,column=1,padx=30,pady=10)
age_var=tkinter.StringVar()
entry_age=ttk.Entry(frame_label, width=3, textvariable=age_var)
entry_age.grid(row=1,column=1,padx=30)

def submit():
    name = name_var.get()
    age = age_var.get()
    if name==''or age=='' :
        messagebox.showerror('Error','Please Enter your name and age both')
    else:
        try:
            age=int(age)
        except ValueError:
            messagebox.showerror('Error','Age should be integer')
        else:
            if age<18:
                messagebox.showwarning('Warning','You are under 18 years')
            print((f'your name is {name} and you are {age} years old.'))


submit_label=ttk.Button(frame_label, text='Submit',command=submit)
submit_label.grid(row=2,column=0,padx=30,pady=20)


window.mainloop()