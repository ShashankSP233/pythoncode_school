import tkinter as Thk


win = Thk.Tk()
win.geometry('800x1000')
win.config(bg='black')

name_label = Thk.Button(win,text='Name: ',bg='black',
                        fg='white',font='arial 20 bold',borderwidth=0)
name_label.grid(column=1,row=1)

gen_label = Thk.Button(win, text='gender: ', bg='black',
                       fg='white', font='arial 20 bold', borderwidth=0)
gen_label.grid(column=1, row=2)

race_label = Thk.Button(win, text='Race: ', bg='black',
                        fg='white', font='arial 20 bold', borderwidth=0)
race_label.grid(column=1,row=3)

class_label = Thk.Button(win, text='Class: ', bg='black',
                         fg='white', font='arial 20 bold', borderwidth=0)
class_label.grid(column=1,row=4)

alin_label = Thk.Button(win, text='Aligment: ', bg='black',
                        fg='white', font='arial 20 bold', borderwidth=0)
alin_label.grid(column=1,row=5)

name_txtbox = Thk.Entry(win, bg='black', fg='white',
                        font='arial 20 bold',borderwidth=1)
name_txtbox.grid(column=2,row=1)

gen_txtbox = Thk.Entry(win, bg='black', fg='white',
                        font='arial 20 bold',borderwidth=1)
gen_txtbox.grid(column=2,row=2)

race_txtbox = Thk.Entry(win, bg='black', fg='white',
                        font='arial 20 bold',borderwidth=1)
race_txtbox.grid(column=2,row=3)

class_txtbox = Thk.Entry(win, bg='black', fg='white',
                        font='arial 20 bold',borderwidth=1)
class_txtbox.grid(column=2,row=4)

alin_list= ['lawful good',
            'neutral good',
            'chaotic good',
            'lawful neutral',
            'true neutal',
            'chaotic neutal',
            'lawful evil',
            'neutal evil',
            'chaotic evil']

alin_data=Thk.StringVar()
alin_data.set('select')

alin_txtbox = Thk.OptionMenu(win,alin_data,*alin_list)
alin_txtbox.config(bg='black', fg='white',font='arial 20 bold',borderwidth=0,highlightbackground='black')
alin_txtbox.grid(column=2,row=5)

def get_data():
    # data_lis=[]
    name_value = name_txtbox.get()
    gen_value = gen_txtbox.get()
    race_value = race_txtbox.get()
    class_value = class_txtbox.get()
    alin_value = alin_data.get()
    data_list=[name_value,gen_value,race_value,class_value,alin_value]
    print (data_list)

sub_button = Thk.Button(win,text='submit',command=get_data,bg='black',fg='white',font='roman 20 bold')
sub_button.grid(column=3,row=6)
win.mainloop()