from cProfile import label
import tkinter as thk

def web_url(rawurl):#just so no error occurs
    url_prime=rawurl.strip(' ')
    return url_prime


def col_data():                                                             #adding entry
    win2=thk.Toplevel(bg='#94da6a')
    win2.geometry('1900x1100')
    canv1=thk.Canvas(win2)
    canv1.pack(fill='both',expand=True)
    canv1.create_image(0,0,image=imgurl2,anchor='nw')
    lab1=thk.Label(win2,text='please enter url:',font=('calibri', 20, 'bold'),bg='#94f399',relief=thk.GROOVE)
    lab2=thk.Label(win2,text='please enter name:',font=('calibri', 20, 'bold'),bg='#94f399',relief=thk.GROOVE)
    lab3=thk.Label(win2,text='please enter date:',font=('calibri', 20, 'bold'),bg='#94f399',relief=thk.GROOVE)
    lab4=thk.Label(win2,text='please enter current watch status:',font=('calibri', 20, 'bold'),bg='#94f399',relief=thk.GROOVE)
    ent1=thk.Entry(win2,width=50)
    ent2=thk.Entry(win2,width=50)
    ent3=thk.Entry(win2,width=50)
    ent4=thk.Entry(win2,width=50)
    canvlb1=canv1.create_window(250,100,window=lab1)
    canvlb2=canv1.create_window(250,200,window=lab2)
    canvlb3=canv1.create_window(250,300,window=lab3)
    canvlb4=canv1.create_window(250,400,window=lab4)
    canve1=canv1.create_window(650,100,window=ent1)
    canve2=canv1.create_window(650,200,window=ent2)
    canve3=canv1.create_window(650,300,window=ent3)
    canve4=canv1.create_window(650,400,window=ent4)

    def data_wrt():  #it is the part that writes the data to the file
        raw_url=ent1.get()
        raw_name=ent2.get()
        raw_time=ent3.get()
        raw_stat=ent4.get()
        data_set=[raw_url+' _',raw_name+' _',raw_time+' _',raw_stat]  # every ething is sprated by ' _' so that even if name has a space they are easily seprated

        url_str=str(data_set)+'\n'# so that next data is in next line
        colfile= open(r'E:\py code\file hadleing.py\data collector\dataofurl.txt','a')
        colfile.write(url_str)
        print(web_url(url_str))
        ent1.delete(0,thk.END)
        ent2.delete(0,thk.END)
        ent3.delete(0,thk.END)
        ent4.delete(0,thk.END)

    butsub=thk.Button(win2,text='submit',command=data_wrt,font=('calibri', 20, 'bold'))
    canvbs=canv1.create_window(500,500,window=butsub)

    win2.mainloop()

def sow_data():#it is to shaw the data 
    win3=thk.Toplevel()
    win3.geometry('1000x1000')
    canv2=thk.Canvas(win3)
    canv2.pack(fill='both',expand=True)
    canv2.create_image(0,0,image=imgurl3,anchor='nw')

    lab1=thk.Label(win3,text='enter name:',height= 2, width=20,bg='black',fg='white')
    lab2=thk.Label(win3,text='what do you want:',height= 2, width=20,bg='black',fg='white')

    enq_name=thk.Entry(win3,text = 'enter name:',width=20)
    enq_get=thk.Entry(win3,text = 'what do you want',width=20)
      
    labdu=thk.Label(win3,text='your output:',height= 2, width=20,bg='black',fg='white')
    
    canv2.create_window(100,300,window=lab1)
    canv2.create_window(100,400,window=lab2)
    canv2.create_window(300,300,window=enq_name)
    canv2.create_window(300,400,window=enq_get)
    canv2.create_window(300,600,window=labdu)

    def but_nek():
        def data_ext(name,get1):
            file1=open(r'E:\py code\file hadleing.py\data collector\dataofurl.txt','r')
            linset=file1.readlines()
            get=''
            if get1 in ['url','website','site','address']:
                get='a_url'
            elif get1 in ['date','time','year','past']: 
                get='a_date'
            elif get1 in ['completion','episode','number','status']:
                get='a_stat'
            else:
                return 
            for i in linset: 

                j=i.strip('"[]')
                lis=j.split("_',")
                bis=[]
                for z in lis:
                    g=z.strip("'")
                    h=g.strip(" '")
                    i=h.strip()
                    bis+=i.split()
                if name in bis[1]:
                    if get == 'a_url':    
                        if name in bis[1]:
                            return (bis[0])
                        else:
                            return ('not found')
                    elif get == 'a_date':    
                        if name in bis[1]:
                            return (bis[2])
                        else:
                            return ('not found')
                    elif get == 'a_stat':    
                        if name in bis[1]:
                            return (bis[3])
                        else:
                            return ('not found')
                else:
                    pass

        dat=data_ext(enq_name.get(),enq_get.get())
        labdu.config(text='your output is :'+dat)
        enq_name.delete(0, thk.END)
        enq_get.delete(0, thk.END)
    butget=thk.Button(win3,text='submit',command=but_nek,bg='black',fg='white')
    canv2.create_window(400,800,window=butget)

top=thk.Tk( )
top.geometry('1500x800')

imgurl=thk.PhotoImage(file=r'E:\py code\file hadleing.py\data collector\526887.png')
imgurl2=thk.PhotoImage(file=r'E:\py code\file hadleing.py\data collector\cd2a50a274f3a54d5f9eeaa21c50555b.png')
imgurl3=thk.PhotoImage(file=r'E:\py code\file hadleing.py\data collector\watercolor-sugar-cotton-clouds-background_23-2149231326.png')

canv=thk.Canvas(top,width=1500,height=800)
canv.pack(fill='both',expand=True)
canv.create_image(0,0,image=imgurl,anchor='nw')


but1=thk.Button(top,text='add data',command=col_data,height= 2, width=20,bg='black',fg='white',font=('calibri', 20, 'bold', 'underline'))
but2=thk.Button(top,text='show info',command=sow_data,height= 2, width=20,bg='black',fg='white',font=('calibri', 20, 'bold', 'underline'))
but3=thk.Button(top,text='close',command=top.destroy,height= 2, width=20,bg='black',fg='white',font=('calibri', 20, 'bold', 'underline'))

can_but1=canv.create_window(100,100,anchor='nw',window=but1)
can_but1=canv.create_window(200,300,anchor='nw',window=but2)
can_but1=canv.create_window(300,500,anchor='nw',window=but3)

top.mainloop()

