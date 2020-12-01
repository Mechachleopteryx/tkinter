import tkinter
from tkinter import  ttk
import os
import csv
from csv import DictWriter

window = tkinter.Tk()
window.title('Frame')

fram_label = ttk.LabelFrame(window, text='Frame')
fram_label.grid(row=0,column=0)

lebels = ['Name','Age','Country','Mobile','Email']

for i in range(len(lebels)):
    curent_lebel = 'lebel' + str(i)
    curent_lebel = ttk.Label(fram_label, width=16, text=lebels[i])
    curent_lebel.grid(row=i,column=0, padx=50,pady=20)

user_info={
    'name': tkinter.StringVar(),
    'age': tkinter.StringVar(),
    'country': tkinter.StringVar(),
    'mobile': tkinter.StringVar(),
    'email': tkinter.StringVar()
}

counter= 0
for i in user_info:
    curent_entrybox = 'entry' + i
    curent_entrybox = ttk.Entry(fram_label, width=20, textvariable=user_info[i])
    curent_entrybox.grid(row=counter,column=1, padx=50,pady=20)
    counter +=1

def submit():
    name = user_info['name'].get()
    age = user_info['age'].get()
    country = user_info['country'].get()
    mobile = user_info['mobile'].get()
    email = user_info['email'].get()
    print(f'your name is: {name} age is: {age} country is: {country} mobile number is: {mobile} email is: {email}')

    with open('info.csv','a')as f:
        dict_writer = DictWriter(f, fieldnames=['name','age','country','mobile','email'])
        if os.stat('info.csv').st_size==0:
            dict_writer.writeheader()

        dict_writer.writerow({
            'name':name,
            'age':age,
            'country':country,
            'mobile':mobile,
            'email':email
        })




fram2_label = ttk.LabelFrame(window, text='|___________<<<<Submit Your Info>>>>___________|')
fram2_label.grid(row=1,column=0,padx=50,pady=50)

submit_button = ttk.Button(fram2_label, text='Submit', command=submit)
submit_button.grid(row=0,columnspan=1, padx=50,pady=50)



window.mainloop()
