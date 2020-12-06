import tkinter
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os

win=tkinter.Tk()
win.title('Vpad text editor')
win.geometry('1200x800')

#######################   main menu  #############################
menu1= tkinter.Menu()

###### File menu ##############

new_icon = tkinter.PhotoImage(file='icons2/new.png')
open_icon= tkinter.PhotoImage(file='icons2/open.png')
save_icon=tkinter.PhotoImage(file='icons2/save.png')
save_as_icon=tkinter.PhotoImage(file='icons2/save_as.png')
exit_icon=tkinter.PhotoImage(file='icons2/exit.png')


file=tkinter.Menu(menu1, tearoff=False)

#####################  Edit Menu #####################

copy_icon = tkinter.PhotoImage(file='icons2/copy.png')
paste_icon = tkinter.PhotoImage(file='icons2/paste.png')
cut_icon = tkinter.PhotoImage(file='icons2/cut.png')
clear_all_icon = tkinter.PhotoImage(file='icons2/clear_all.png')
find_icon = tkinter.PhotoImage(file='icons2/find.png')

edit=tkinter.Menu(menu1, tearoff=False)



                ################ View Menu  ###############
tool_bar_icon = tkinter.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tkinter.PhotoImage(file='icons2/status_bar.png')


view=tkinter.Menu(menu1, tearoff=False)





      ################# Color Menu ####################

light_icon = tkinter.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tkinter.PhotoImage(file='icons2/light_plus.png')
dark_icon = tkinter.PhotoImage(file='icons2/dark.png')
red_icon = tkinter.PhotoImage(file='icons2/red.png')
monokai_icon = tkinter.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tkinter.PhotoImage(file='icons2/night_blue.png')

color=tkinter.Menu(menu1, tearoff=False)

color_var = tkinter.StringVar


################################  View ##########################





########---------------------------->>>>>>>>>>>>>>--------------------<<<<<<<<<<<<<<<<



menu1.add_cascade(label='File',menu=file)
menu1.add_cascade(label='Edit',menu=edit)
menu1.add_cascade(label='View',menu=view)
menu1.add_cascade(label='Color',menu=color)


########################### end main menu  ############################


##################### Tool Bar  ####################    ###################

tool_bar = ttk.Label(win)
tool_bar.pack(side=tkinter.TOP,fill=tkinter.X)

########## Font Box #######

font_tuple = tkinter.font.families()
font_var = tkinter.StringVar()
font_box = ttk.Combobox(tool_bar, width=30,textvariable=font_var, stat='readonly')
font_box['value']=font_tuple
font_box.current(font_tuple.index('Standard Symbols PS'))
font_box.grid(row=0,column=0,padx=5)


############ Font size ##########

font_size = tkinter.IntVar()
font_size_box = ttk.Combobox(tool_bar, width=14,textvariable= font_size,stat='readonly')
font_size_box['value'] = tuple(range(8,81,2))
font_size_box.current(3)
font_size_box.grid(row=0,column=1,padx=5)

############# Butons
#### bold button
bold_icon=tkinter.PhotoImage(file='icons2/bold.png')
bold_button = ttk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0,column=2,padx=5)

##########italic button
italic_icon=tkinter.PhotoImage(file='icons2/italic.png')
italic_button = ttk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0,column=3,padx=5)

########## under line button
under_line_icon = tkinter.PhotoImage(file='icons2/underline.png')
underline_button = ttk.Button(tool_bar, image=under_line_icon)
underline_button.grid(row=0,column=4,padx=5)

#########################   Font Color button  ############
fontcolor_icon = tkinter.PhotoImage(file='icons2/font_color.png')
fontcolor_button = ttk.Button(tool_bar, image=fontcolor_icon)
fontcolor_button.grid(row=0,column=5,padx=5)

###### Align buttons left, center, right.###########
align_left_icon = tkinter.PhotoImage(file='icons2/align_left.png')
alignleft_button = ttk.Button(tool_bar, image=align_left_icon)
alignleft_button.grid(row=0,column=6, padx=5)

align_center_icon=tkinter.PhotoImage(file='icons2/align_center.png')
aligncenter_button = ttk.Button(tool_bar, image=align_center_icon)
aligncenter_button.grid(row=0,column=7,padx=5)

align_right_icon = tkinter.PhotoImage(file='icons2/align_right.png')
alignright_button = ttk.Button(tool_bar, image=align_right_icon)
alignright_button.grid(row=0,column=8,padx=5)


############ End Button #############

#################################################### END  Tool Bar    ############################

###############################  Text editor ########################

text_editor = tkinter.Text(win)
text_editor.config(wrap='word', relief=tkinter.FLAT)

scrol_bar = tkinter.Scrollbar(win)
text_editor.focus_set()
scrol_bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text_editor.pack(fill=tkinter.BOTH, expand=True)
# scrol_bar.config(text_editor.yview)
text_editor.config(yscrollcommand=scrol_bar.set)

######################  End text editor  #################################
###############    sataus bar  ####################

status_bar = tkinter.Label(win, text = 'Status bar')
status_bar.pack(side=tkinter.BOTTOM, )

######################3  End status bar  #############################


################################ Main Menu Functionality ############################

########### File commands ###################


file.add_command(label=' New file ',image=new_icon,compound=tkinter.LEFT, accelerator='CTRL+N')
file.add_command(label=' Open ',image=open_icon,compound=tkinter.LEFT,accelerator='CTRL+O')
file.add_command(label=' Save ',image=save_icon,compound=tkinter.LEFT,accelerator='CTRL+S')
file.add_command(label=' Save As ',image=save_as_icon,compound=tkinter.LEFT,accelerator='CTRL+ALT+S')
file.add_command(label='Exit',image=exit_icon,compound=tkinter.LEFT,accelerator='CTRL+Q')



############### Edit Command #############################

edit.add_command(label='Copy',image=copy_icon,compound=tkinter.LEFT,accelerator='ctrl+c')
edit.add_command(label='Paste',image=paste_icon,compound=tkinter.LEFT,accelerator='ctrl+v')
edit.add_command(label='Cut',image=cut_icon,compound=tkinter.LEFT,accelerator='ctrl+x')
edit.add_command(label='Clear All',image=clear_all_icon,compound=tkinter.LEFT,accelerator='ctrl+alt+x')
edit.add_command(label='Find',image=find_icon,compound=tkinter.LEFT,accelerator='ctrl+f')

#################### View #######################

view.add_checkbutton(label='Tool Bar',image=tool_bar_icon,compound=tkinter.LEFT,)
view.add_checkbutton(label='Status Bar',image=status_bar_icon,compound=tkinter.LEFT)


################### Color  ##########################

color_icon = (light_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default': ('#000000','#ffffff'),
    'Light Plus': ('#474747','#e0e0e0'),
    'Dark': ('#c4c4c4','#2d2d2d'),
    'Red': ('#2d2d2d','#ffe8e8'),
    'Monokai' : ('#d3b774','#474747'),
    'Night Blue': ('#ededed','#6b9dc2')
}

count = 0
for i in color_dict:
    color.add_radiobutton(label=i,image=color_icon[count],variable=color_var, compound=tkinter.LEFT)
    count+=1



################  End main Menu Functionality ######################



win.config(menu=menu1)
win.mainloop()