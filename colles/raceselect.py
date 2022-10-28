import tkinter as Thk
import importlib.util


win = Thk.Tk()
win.geometry('800x1000')
win.config(bg='black')
win.rowconfigure(0,weight=1)
win.columnconfigure(0,weight=1)

frame1=Thk.Frame(win,bg="black")
frame2=Thk.Frame(win,bg="black")
frame3=Thk.Frame(win,bg="black")
for frame in [frame1,frame2,frame3]:
    frame.grid(row=0,column=0,sticky='nsew')

data_extract = []
possible_subraces=['coustom']



def nxt_cmd1():
    global subrace_var
    global race_file
    race_data = race_txtbox.get()
    data_extract.append(race_data)
    filename = race_data+'_RaceSheet.py'
    filepath = 'E:\\colles\\races\\'+filename
    race_file = importlib.util.spec_from_file_location(
        filename, filepath).loader.load_module()
    possible_subraces.extend(race_file.Subraces)
    subrace_var = Thk.StringVar()
    subrace_var.set('-')
    subrace_txtbox = Thk.OptionMenu(frame2, subrace_var, *possible_subraces)
    subrace_txtbox.config(text='Race: ', bg='black',
                          fg='white', font='arial 20 bold', borderwidth=0)
    subrace_txtbox.grid(column=2, row=3)
    frame2.tkraise()

def nxt_cmd2():
    global subrace_data
    subrace_data = subrace_var.get()
    compiled_info=race_file.give_info(subrace_data)
    frame3.tkraise()
    
    race_lable = Thk.Label(
        frame3, text=compiled_info["race"], bg='black', fg='white', font='arial 20 bold')
    race_lable.grid(row=1,column=2)
    
    subrace_lable = Thk.Label(
        frame3, text=compiled_info["subrace"], bg='black', fg='white', font='arial 20 bold')
    subrace_lable.grid(row=2,column=2)
    
    race_lable = Thk.Label(
        frame3, text=compiled_info["ability score"], bg='black', fg='white', font='arial 20 bold')
    race_lable.grid(row=3,column=2)
    
    race_lable = Thk.Label(
        frame3, text=compiled_info['speed'], bg='black', fg='white', font='arial 20 bold')
    race_lable.grid(row=4,column=2)
    
    race_lable = Thk.Label(
        frame3, text=compiled_info['darkvision'], bg='black', fg='white', font='arial 20 bold')
    race_lable.grid(row=5,column=2)
    
    race_lable = Thk.Label(
        frame3, text=compiled_info['language'], bg='black', fg='white', font='arial 20 bold')
    race_lable.grid(row=6,column=2)
    
    
    filesavedata=open('tempcharsavefile.txt','w')
    filesavedata.write( str(compiled_info))

    

race_label = Thk.Button(frame1, text='Race: ', bg='black',
                        fg='white', font='arial 20 bold', borderwidth=0)
race_label.grid(column=1, row=3)

race_txtbox = Thk.Entry(frame1, bg='black', fg='white',
                        font='arial 20 bold', borderwidth=1)
race_txtbox.grid(column=2, row=3)


    
but1 = Thk.Button(frame1,text='Next', command=nxt_cmd1)
but1.grid(column=3,row=4)

################page2###################

subrace_label = Thk.Button(frame2, text='Race: ', bg='black',
                        fg='white', font='arial 20 bold', borderwidth=0)
subrace_label.grid(column=1, row=3)

subrace_label.grid(column=1, row=3)
but2 = Thk.Button(frame2, text='Next', command=nxt_cmd2)
but2.grid(column=3, row=4)

race_lable = Thk.Label(
    frame3, text="race: ", bg='black', fg='white', font='arial 20 bold')
race_lable.grid(row=1, column=1)

subrace_lable = Thk.Label(
    frame3, text="subrace: ", bg='black', fg='white', font='arial 20 bold')
subrace_lable.grid(row=2, column=1)

race_lable = Thk.Label(
    frame3, text="ability score: ", bg='black', fg='white', font='arial 20 bold')
race_lable.grid(row=3, column=1)

race_lable = Thk.Label(
    frame3, text="speed: ", bg='black', fg='white', font='arial 20 bold')
race_lable.grid(row=4, column=1)

race_lable = Thk.Label(
    frame3, text="darkvision: ", bg='black', fg='white', font='arial 20 bold')
race_lable.grid(row=5, column=1)

race_lable = Thk.Label(
    frame3, text="language: ", bg='black', fg='white', font='arial 20 bold')
race_lable.grid(row=6, column=1)






frame1.tkraise()
def run():
    win.mainloop()

run()