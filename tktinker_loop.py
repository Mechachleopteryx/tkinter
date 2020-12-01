import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Asad')

# creat label
labels = ['Name : ','Age : ', 'Email : ','Mobile : ','Country : ' ]

for i in range(len(labels)):
    curnt_label = 'label' + str(i)
    curnt_label = ttk.Label(window, width=10, text=labels[i])
    curnt_label.grid(row=i,column=0, sticky=tkinter.W, padx=30,pady=30)

# creat rntry box

user_info = {
    'Name': tkinter.StringVar(),
    'Age': tkinter.StringVar(),
    'Email': tkinter.StringVar(),
    'Mobile': tkinter.StringVar(),
    'Country': tkinter.StringVar()
}
counter=0
for i in user_info:
    curnt_entrybox = 'entry' + i
    curnt_entrybox = ttk.Entry(window, width=16, textvariable=user_info[i])
    curnt_entrybox.grid(row=counter,column=1, padx=20, pady=20)
    counter +=1
import csv
import os
from csv import DictWriter

def  submit():
    Name = user_info['Name'].get()
    Age = user_info['Age'].get()
    Email = user_info['Email'].get()
    Mobile = user_info['Mobile'].get()
    Country = user_info['Country'].get()
    print(user_info['Name'].get())
    print(user_info.get('Age').get())
    print(user_info.get('Email').get())
    print(user_info['Mobile'].get())
    print(user_info['Country'].get())


    with open('file2.csv', 'a') as f:
        write_dict = DictWriter(f, fieldnames=['Full Name','Age:','Email......','Mobile Number','Country'])
        if os.stat('file2.csv').st_size==0:
            write_dict.writeheader()

        write_dict.writerow({
            'Full Name': Name,
            'Age:': Age,
            'Email......':Email,
            'Mobile Number': Mobile,
            'Country': Country
        })

        curnt_entrybox.delete(0,tkinter.END)






submit_button = ttk.Button(window, text='Submit', command=submit)
submit_button.grid(row=6,columnspan=2)











window.mainloop()