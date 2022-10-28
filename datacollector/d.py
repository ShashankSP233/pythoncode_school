file1=open(r'datacollector\dataofurl.txt','r')
linset=file1.readlines()
#  print(linset)
# name=''
# get=''
# d=["['",", '"]
# for i in linset:
#     j=i.split(" _'",3)
#     print(j)
from tkinter import *
  
top = Tk()
Lb = Listbox(top)

for i in linset: 
                # j=i.strip('"[]')
                lis=i.split(" _",3)
                bis=[]
                d=lis[3]
                print(d)
                Lb.insert(1, )
Lb.pack()
top.mainloop()